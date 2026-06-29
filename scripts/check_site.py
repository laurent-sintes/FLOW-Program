from __future__ import annotations

import argparse
import html
import json
import re
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - explicit runtime diagnostic
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
AGENTS = ROOT / "AGENTS.md"
INSTRUCTIONS = DOCS / "administration" / "instructions-codex.md"
IMAGE_REGISTRY = DOCS / "administration" / "referentiel-schemas.md"
MKDOCS = ROOT / "mkdocs.yml"
GITIGNORE = ROOT / ".gitignore"
GITATTRIBUTES = ROOT / ".gitattributes"
GITHUB_PAGES_WORKFLOW = ROOT / ".github" / "workflows" / "github-pages.yml"
READING_METRICS_SCRIPT = ROOT / "scripts" / "update_reading_metrics.py"
READING_METRICS = DOCS / "referentiel" / "page-metrics.json"
ROLE_REGISTRY = DOCS / "administration" / "referentiel-roles.md"
CARD_START = "<!-- FLOW-READING-CARD:START -->"
CARD_END = "<!-- FLOW-READING-CARD:END -->"
AUDIENCE_RE = re.compile(
    r"<span>\s*Public cible\s*</span>\s*<strong>(.*?)</strong>",
    re.IGNORECASE | re.DOTALL,
)
MARKDOWN_SVG_RE = re.compile(r"!\[[^\]]*]\(([^)\s]+\.svg)(?:\s+\"[^\"]*\")?\)")
EXTERNAL_LINK_SCHEMES = {"http", "https"}
EXTERNAL_LINK_USER_AGENT = "FLOW-Program link checker (+https://github.com/laurent-sintes/FLOW-Program)"


@dataclass
class Finding:
    level: str
    code: str
    message: str
    path: Path | None = None


@dataclass
class ExternalLinkResult:
    status: int | None
    final_url: str | None
    error: str | None = None


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value for name, value in attrs if value is not None}

        if tag == "a" and values.get("href"):
            self.links.append(values["href"])

        if values.get("id"):
            self.ids.add(values["id"])

        if values.get("name"):
            self.ids.add(values["name"])


class Checks:
    def __init__(self) -> None:
        self.findings: list[Finding] = []
        self.ok: list[str] = []

    def add(self, level: str, code: str, message: str, path: Path | None = None) -> None:
        self.findings.append(Finding(level, code, message, path))

    def error(self, code: str, message: str, path: Path | None = None) -> None:
        self.add("ERROR", code, message, path)

    def warn(self, code: str, message: str, path: Path | None = None) -> None:
        self.add("WARN", code, message, path)

    def pass_check(self, message: str) -> None:
        self.ok.append(message)

    @property
    def errors(self) -> list[Finding]:
        return [finding for finding in self.findings if finding.level == "ERROR"]

    @property
    def warnings(self) -> list[Finding]:
        return [finding for finding in self.findings if finding.level == "WARN"]


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def docs_markdown_pages() -> list[Path]:
    return sorted(path for path in DOCS.rglob("*.md") if path.is_file())


def resolve_markdown_asset(markdown_path: Path, href: str) -> Path | None:
    parsed = urllib.parse.urlsplit(href.strip())
    if parsed.scheme or parsed.netloc:
        return None

    raw_path = urllib.parse.unquote(parsed.path)
    if not raw_path:
        return None

    return (markdown_path.parent / raw_path).resolve()


def collect_markdown_svg_references() -> dict[Path, set[Path]]:
    references: dict[Path, set[Path]] = {}

    for markdown_path in docs_markdown_pages():
        text = read_text(markdown_path)
        for match in MARKDOWN_SVG_RE.finditer(text):
            target = resolve_markdown_asset(markdown_path, match.group(1))
            if target is None:
                continue
            references.setdefault(target, set()).add(markdown_path)

    return references


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def load_mkdocs_config(checks: Checks) -> dict:
    if yaml is None:
        checks.error("PYTHON_DEP", "PyYAML is not available; run checks with the project environment.")
        return {}

    if not MKDOCS.exists():
        checks.error("MKDOCS_CONFIG", "mkdocs.yml is missing.", MKDOCS)
        return {}

    try:
        data = yaml.safe_load(read_text(MKDOCS)) or {}
    except Exception as exc:  # pragma: no cover - defensive diagnostic
        checks.error("MKDOCS_CONFIG", f"Cannot read mkdocs.yml: {exc}", MKDOCS)
        return {}

    if not isinstance(data, dict):
        checks.error("MKDOCS_CONFIG", "mkdocs.yml does not contain a YAML mapping.", MKDOCS)
        return {}

    return data


def collect_nav_pages(nav: object) -> set[str]:
    pages: set[str] = set()

    if isinstance(nav, str):
        if nav.endswith(".md"):
            pages.add(nav.replace("\\", "/"))
        return pages

    if isinstance(nav, list):
        for item in nav:
            pages.update(collect_nav_pages(item))
        return pages

    if isinstance(nav, dict):
        for value in nav.values():
            pages.update(collect_nav_pages(value))
        return pages

    return pages


def collect_nav_entries(nav: object) -> list[tuple[str | None, str]]:
    entries: list[tuple[str | None, str]] = []

    if isinstance(nav, str):
        if nav.endswith(".md"):
            entries.append((None, nav.replace("\\", "/")))
        return entries

    if isinstance(nav, list):
        for item in nav:
            entries.extend(collect_nav_entries(item))
        return entries

    if isinstance(nav, dict):
        for label, value in nav.items():
            if isinstance(value, str) and value.endswith(".md"):
                entries.append((str(label), value.replace("\\", "/")))
            else:
                entries.extend(collect_nav_entries(value))

    return entries


def comparable_title(value: str) -> str:
    value = value.replace("’", "'").replace("–", "—")
    value = re.sub(r"\s+", " ", value)
    return value.strip().casefold()


def extract_page_title(path: Path) -> str | None:
    text = read_text(path)

    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.IGNORECASE | re.DOTALL)
    if match:
        title = re.sub(r"<[^>]+>", "", match.group(1))
        return html.unescape(re.sub(r"\s+", " ", title).strip())

    return None


def check_nav_title_alignment(checks: Checks) -> None:
    config = load_mkdocs_config(checks)
    entries = collect_nav_entries(config.get("nav", []))
    mismatches = 0

    for label, page in entries:
        if label is None or page == "index.md":
            continue

        path = DOCS / page
        if not path.exists():
            continue

        title = extract_page_title(path)
        if title is None:
            checks.error("NAV_TITLE_MISSING", f"Page declared in mkdocs.yml has no H1 title: {page}", path)
            mismatches += 1
            continue

        if comparable_title(label) != comparable_title(title):
            checks.error(
                "NAV_TITLE_MISMATCH",
                f"Navigation label differs from page title for {page}: '{label}' != '{title}'",
                MKDOCS,
            )
            mismatches += 1

    if not mismatches:
        checks.pass_check("Explicit navigation labels match page titles.")


def check_nav_coverage(checks: Checks) -> None:
    config = load_mkdocs_config(checks)
    nav_pages = collect_nav_pages(config.get("nav", []))
    docs_pages = {
        path.relative_to(DOCS).as_posix()
        for path in DOCS.rglob("*.md")
        if path.is_file()
    }

    missing_files = sorted(page for page in nav_pages if not (DOCS / page).exists())
    unlisted_pages = sorted(docs_pages - nav_pages)

    for page in missing_files:
        checks.error("NAV_MISSING_FILE", f"Page declared in mkdocs.yml does not exist: {page}", MKDOCS)

    for page in unlisted_pages:
        checks.error("NAV_UNLISTED_PAGE", f"Markdown page is not declared in mkdocs.yml: {page}", DOCS / page)

    if not missing_files and not unlisted_pages:
        checks.pass_check("MkDocs navigation covers all Markdown pages.")


def check_generated_content_not_tracked(checks: Checks) -> None:
    tracked = run_git(["ls-files", "site", ".generated", ".venv", ".agents", "__pycache__"])

    if tracked.returncode != 0:
        checks.warn("GIT_LS_FILES", f"Cannot inspect tracked generated files: {tracked.stderr.strip()}")
        return

    tracked_files = [line for line in tracked.stdout.splitlines() if line.strip()]
    if tracked_files:
        checks.error(
            "GENERATED_TRACKED",
            "Generated/local paths are tracked by Git: " + ", ".join(tracked_files),
        )
    else:
        checks.pass_check("Generated/local paths are not tracked by Git.")

    expected_patterns = ["site/", ".generated/", ".venv/", ".agents/"]
    if not GITIGNORE.exists():
        checks.error("GITIGNORE", ".gitignore is missing.", GITIGNORE)
        return

    gitignore = {line.strip() for line in read_text(GITIGNORE).splitlines()}
    for pattern in expected_patterns:
        if pattern not in gitignore:
            checks.error("GITIGNORE_PATTERN", f"Missing .gitignore pattern: {pattern}", GITIGNORE)

    if all(pattern in gitignore for pattern in expected_patterns):
        checks.pass_check(".gitignore protects generated/local paths.")


def check_repository_line_endings(checks: Checks) -> None:
    if not GITATTRIBUTES.exists():
        checks.error("GITATTRIBUTES", ".gitattributes is missing.", GITATTRIBUTES)
        return

    text = read_text(GITATTRIBUTES)
    required_patterns = ["* text=auto eol=lf"]
    missing = [pattern for pattern in required_patterns if pattern not in text]

    for pattern in missing:
        checks.error("GITATTRIBUTES_PATTERN", f"Missing .gitattributes pattern: {pattern}", GITATTRIBUTES)

    if not missing:
        checks.pass_check(".gitattributes stabilizes repository line endings.")


def parse_html(path: Path) -> LinkParser:
    parser = LinkParser()
    parser.feed(read_text(path))
    return parser


def should_skip_href(href: str) -> bool:
    href = href.strip()
    if not href:
        return True

    if href.startswith("//"):
        return True

    parsed = urllib.parse.urlsplit(href)
    return parsed.scheme in {"http", "https", "mailto", "tel", "javascript", "data"}


def normalize_external_href(href: str) -> str | None:
    value = href.strip()
    if not value:
        return None

    if value.startswith("//"):
        value = f"https:{value}"

    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme not in EXTERNAL_LINK_SCHEMES or not parsed.netloc:
        return None

    path = urllib.parse.quote(parsed.path or "/", safe="/%:@")
    query = urllib.parse.quote(parsed.query, safe="=&?/:;%+,.@")
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, query, ""))


def request_external_url(url: str, method: str, timeout: float) -> ExternalLinkResult:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": EXTERNAL_LINK_USER_AGENT,
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"

    request = urllib.request.Request(url, headers=headers, method=method)

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if method == "GET":
                response.read(1)
            return ExternalLinkResult(response.getcode(), response.geturl())
    except urllib.error.HTTPError as exc:
        return ExternalLinkResult(exc.code, exc.geturl(), str(exc))
    except (urllib.error.URLError, TimeoutError, socket.timeout, OSError, ValueError) as exc:
        return ExternalLinkResult(None, None, str(exc))


def check_external_url(url: str, timeout: float) -> ExternalLinkResult:
    head_result = request_external_url(url, "HEAD", timeout)
    if head_result.status is not None and head_result.status not in {403, 405, 406, 429, 501}:
        return head_result

    get_result = request_external_url(url, "GET", timeout)
    if get_result.status is not None:
        return get_result

    if head_result.status is not None:
        return head_result

    return get_result


def collect_external_site_links() -> dict[str, set[Path]]:
    links: dict[str, set[Path]] = {}

    for html_file in sorted(SITE.rglob("*.html")):
        page = parse_html(html_file)
        for href in page.links:
            url = normalize_external_href(href)
            if url is None:
                continue
            links.setdefault(url, set()).add(html_file)

    return links


def normalize_site_target(source: Path, href: str) -> tuple[Path, str]:
    parsed = urllib.parse.urlsplit(href)
    path_part = urllib.parse.unquote(parsed.path)
    fragment = urllib.parse.unquote(parsed.fragment)

    if path_part == "/FLOW-Program":
        path_part = "/"
    elif path_part.startswith("/FLOW-Program/"):
        path_part = path_part.removeprefix("/FLOW-Program")

    if not path_part:
        target = source
    elif path_part.startswith("/"):
        target = SITE / path_part.lstrip("/")
    else:
        target = source.parent / path_part

    if path_part.endswith("/") or target.is_dir():
        target = target / "index.html"
    elif not target.suffix:
        index_target = target / "index.html"
        html_target = target.with_suffix(".html")
        if index_target.exists():
            target = index_target
        elif html_target.exists():
            target = html_target

    return target.resolve(), fragment


def is_inside_site(path: Path) -> bool:
    try:
        path.resolve().relative_to(SITE.resolve())
        return True
    except ValueError:
        return False


def check_built_site_links(checks: Checks) -> None:
    if not SITE.exists():
        checks.error("SITE_MISSING", "site/ does not exist. Run the MkDocs build first.", SITE)
        return

    html_files = sorted(SITE.rglob("*.html"))
    if not html_files:
        checks.error("SITE_EMPTY", "No HTML files found in site/.", SITE)
        return

    parsed_pages: dict[Path, LinkParser] = {}
    for html_file in html_files:
        parsed_pages[html_file.resolve()] = parse_html(html_file)

    broken_links = 0
    broken_anchors = 0
    checked_links = 0
    seen: set[tuple[Path, str]] = set()

    for html_file, page in parsed_pages.items():
        for href in page.links:
            if should_skip_href(href):
                continue

            key = (html_file, href)
            if key in seen:
                continue
            seen.add(key)

            target, fragment = normalize_site_target(html_file, href)
            checked_links += 1

            if not is_inside_site(target):
                checks.error("HTML_LINK_OUTSIDE_SITE", f"Internal link points outside site/: {href}", html_file)
                broken_links += 1
                continue

            if not target.exists():
                checks.error("HTML_LINK_MISSING", f"Internal link target is missing: {href}", html_file)
                broken_links += 1
                continue

            if target.suffix.lower() == ".html" and fragment:
                target_page = parsed_pages.get(target)
                if target_page is None:
                    target_page = parse_html(target)
                    parsed_pages[target] = target_page

                if fragment not in target_page.ids:
                    checks.error("HTML_ANCHOR_MISSING", f"Anchor is missing: {href}", html_file)
                    broken_anchors += 1

    if not broken_links and not broken_anchors:
        checks.pass_check(f"Built site internal links and anchors are valid ({checked_links} checked).")


def check_multilingual_site(checks: Checks) -> None:
    expected_pages = [
        SITE / "index.html",
        SITE / "fr" / "index.html",
        SITE / "en" / "index.html",
    ]

    for page in expected_pages:
        if not page.exists():
            checks.error("I18N_SITE_PAGE", f"Multilingual site page is missing: {rel(page)}", page)

    english_pages = sorted((SITE / "en").rglob("*.html")) if (SITE / "en").exists() else []
    if english_pages:
        sample_text = "\n".join(read_text(page) for page in english_pages[:5])
        if "English version in progress" not in sample_text:
            checks.error("I18N_EN_NOTICE", "English generated site does not include the translation notice.", SITE / "en")
    elif (SITE / "en").exists():
        checks.error("I18N_EN_EMPTY", "English generated site has no HTML pages.", SITE / "en")

    if not any(finding.code.startswith("I18N_") for finding in checks.errors):
        checks.pass_check("Multilingual site structure is generated for fr and en.")


def check_external_links(checks: Checks, timeout: float, strict: bool) -> None:
    if not SITE.exists():
        checks.error("SITE_MISSING", "site/ does not exist. Run the MkDocs build first.", SITE)
        return

    external_links = collect_external_site_links()
    if not external_links:
        checks.pass_check("No external links found in built site.")
        return

    checked = 0
    issues = 0

    for url, source_pages in sorted(external_links.items()):
        source_page = sorted(source_pages)[0]
        result = check_external_url(url, timeout)
        checked += 1

        if result.status is not None and 200 <= result.status < 400:
            continue

        issues += 1
        source_count = len(source_pages)
        source_detail = f"first seen in {rel(source_page)}"
        if source_count > 1:
            source_detail += f", {source_count} pages total"

        if result.status is None:
            checks.warn(
                "EXTERNAL_LINK_UNREACHABLE",
                f"External link could not be reached: {url} ({result.error}; {source_detail})",
                source_page,
            )
            continue

        message = f"External link returned HTTP {result.status}: {url} ({source_detail})"
        if strict and result.status not in {401, 403, 429}:
            checks.error("EXTERNAL_LINK_STATUS", message, source_page)
        else:
            checks.warn("EXTERNAL_LINK_STATUS", message, source_page)

    if not issues:
        checks.pass_check(f"External links are reachable ({checked} checked).")


def check_agents_publication_sync(checks: Checks) -> None:
    if not AGENTS.exists():
        checks.error("AGENTS_MISSING", "AGENTS.md is missing.", AGENTS)
        return

    if not INSTRUCTIONS.exists():
        checks.error("INSTRUCTIONS_MISSING", "Published Codex instructions page is missing.", INSTRUCTIONS)
        return

    agents = read_text(AGENTS).casefold()
    instructions = read_text(INSTRUCTIONS).casefold()

    required_phrases = [
        "administrer et construire le site",
        "structure du site et impacts",
        "concepts flow",
        "scripts\\build-docs.ps1",
        "scripts\\build_multilang.py",
        "scripts\\check-site.ps1",
        "scripts\\doctor.ps1",
        "scripts\\update-reading-metrics.ps1",
        ".gitattributes",
        "multilingue-traduction.md",
        "guide-contribution-contenu.md",
        "modele-mental-connaissances.md",
        "environnement-codex-windows.md",
        "referentiel-roles.md",
        "referentiel-schemas.md",
    ]

    for phrase in required_phrases:
        if phrase.casefold() not in agents:
            checks.error("AGENTS_SYNC", f"AGENTS.md does not mention: {phrase}", AGENTS)
        if phrase.casefold() not in instructions:
            checks.error("INSTRUCTIONS_SYNC", f"Published instructions do not mention: {phrase}", INSTRUCTIONS)

    if "docs/administration/instructions-codex.md" not in agents:
        checks.error("AGENTS_PUBLIC_PAGE", "AGENTS.md does not point to the published instructions page.", AGENTS)

    if "agents.md" not in instructions:
        checks.error("INSTRUCTIONS_AGENTS_REF", "Published instructions do not reference AGENTS.md.", INSTRUCTIONS)

    if not any(finding.code.startswith("AGENTS") or finding.code.startswith("INSTRUCTIONS") for finding in checks.errors):
        checks.pass_check("AGENTS.md and the published Codex instructions are synchronized on key rules.")


def check_ci_workflow(checks: Checks) -> None:
    if not GITHUB_PAGES_WORKFLOW.exists():
        checks.error("CI_WORKFLOW", "GitHub Pages workflow is missing.", GITHUB_PAGES_WORKFLOW)
        return

    text = read_text(GITHUB_PAGES_WORKFLOW)
    required_fragments = [
        "cache: \"pip\"",
        "pip install -r requirements.txt",
        "python scripts/build_multilang.py",
        "python scripts/check_site.py --external-links",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in text]

    for fragment in missing:
        checks.error("CI_WORKFLOW_RULE", f"GitHub Pages workflow is missing: {fragment}", GITHUB_PAGES_WORKFLOW)

    if not missing:
        checks.pass_check("GitHub Pages workflow builds the multilingual site and runs external-link checks.")


def check_section_indexes(checks: Checks) -> None:
    faq_index = DOCS / "faq" / "index.md"
    faq_dir = DOCS / "faq"
    if not faq_index.exists():
        checks.error("FAQ_INDEX", "FAQ index is missing.", faq_index)
    else:
        faq_text = read_text(faq_index)
        faq_child_pages = sorted(
            path for path in faq_dir.glob("*.md")
            if path.is_file() and path.name != "index.md"
        )

        for page in faq_child_pages:
            if page.name not in faq_text:
                checks.error("FAQ_INDEX_LINK", f"FAQ index does not link to FAQ page: {page.name}.", faq_index)

        if all(page.name in faq_text for page in faq_child_pages):
            checks.pass_check("FAQ index links to FAQ child pages.")

    methode_index = DOCS / "methode" / "index.md"
    if not methode_index.exists():
        checks.error("METHODE_INDEX", "Methodology index is missing.", methode_index)
    else:
        index_text = read_text(methode_index)
        expected = ["processus-de-cadrage.md"]

        for page in expected:
            if page not in index_text:
                checks.error("METHODE_INDEX_LINK", f"Methodology index does not link to {page}.", methode_index)

        forbidden = ["environnement-codex-windows.md", "instructions-codex.md"]
        for page in forbidden:
            if page in index_text:
                checks.error("METHODE_INDEX_SCOPE", f"Methodology index should not link to administration page: {page}.", methode_index)

        if all(page in index_text for page in expected) and not any(page in index_text for page in forbidden):
            checks.pass_check("Methodology index stays focused on project methodology.")

    admin_index = DOCS / "administration" / "index.md"
    if not admin_index.exists():
        checks.error("ADMIN_INDEX", "Administration index is missing.", admin_index)
        return

    admin_text = read_text(admin_index)
    expected_admin = [
        "guide-contribution-contenu.md",
        "modele-mental-connaissances.md",
        "referentiel-roles.md",
        "referentiel-schemas.md",
        "multilingue-traduction.md",
        "environnement-codex-windows.md",
        "instructions-codex.md",
    ]

    for page in expected_admin:
        if page not in admin_text:
            checks.error("ADMIN_INDEX_LINK", f"Administration index does not link to {page}.", admin_index)

    if all(page in admin_text for page in expected_admin):
        checks.pass_check("Administration index links to expected operational pages.")


def parse_role_registry(checks: Checks) -> set[str]:
    if not ROLE_REGISTRY.exists():
        checks.error("ROLE_REGISTRY_MISSING", "Role registry page is missing.", ROLE_REGISTRY)
        return set()

    roles: set[str] = set()
    seen: dict[str, str] = {}
    for line in read_text(ROLE_REGISTRY).splitlines():
        if not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue

        role = cells[0]
        if role.casefold() == "rôle" or re.fullmatch(r":?-+:?", role):
            continue

        if "," in role:
            checks.error("ROLE_REGISTRY_SEPARATOR", f"Role label cannot contain a comma: {role}", ROLE_REGISTRY)
            continue

        key = role.casefold()
        if key in seen:
            checks.error("ROLE_REGISTRY_DUPLICATE", f"Duplicate role label: {role}", ROLE_REGISTRY)
            continue

        seen[key] = role
        roles.add(role)

    if not roles:
        checks.error("ROLE_REGISTRY_EMPTY", "Role registry does not contain any role.", ROLE_REGISTRY)

    return roles


def split_audience_roles(audience: str) -> list[str]:
    return [role.strip() for role in audience.split(",") if role.strip()]


def extract_reading_card_audience(path: Path, checks: Checks) -> str | None:
    text = read_text(path)
    start_count = text.count(CARD_START)
    end_count = text.count(CARD_END)

    if start_count != 1 or end_count != 1:
        checks.error(
            "READING_CARD_COUNT",
            f"Expected exactly one reading card, found {start_count} start marker(s) and {end_count} end marker(s).",
            path,
        )
        return None

    block = text.split(CARD_START, 1)[1].split(CARD_END, 1)[0]
    match = AUDIENCE_RE.search(block)
    if not match:
        checks.error("READING_CARD_AUDIENCE", "Reading card does not expose a Public cible field.", path)
        return None

    return re.sub(r"\s+", " ", match.group(1)).strip()


def validate_audience_roles(path: Path, audience: str, roles: set[str], checks: Checks) -> bool:
    audience_roles = split_audience_roles(audience)
    if not audience_roles:
        checks.error("READING_ROLE_EMPTY", "Reading card audience is empty.", path)
        return False

    valid = True
    if len(audience_roles) > 3:
        checks.error("READING_ROLE_TOO_MANY", f"Reading card uses more than three roles: {audience}", path)
        valid = False

    unknown = [role for role in audience_roles if role not in roles]
    if unknown:
        checks.error(
            "READING_ROLE_UNKNOWN",
            f"Reading card uses role(s) outside the registry: {', '.join(unknown)}",
            path,
        )
        valid = False

    return valid


def load_metric_audiences(checks: Checks, roles: set[str]) -> dict[str, str]:
    if not READING_METRICS.exists():
        checks.error("READING_METRICS_FILE", "Reading metrics JSON is missing.", READING_METRICS)
        return {}

    try:
        data = json.loads(read_text(READING_METRICS))
    except json.JSONDecodeError as exc:
        checks.error("READING_METRICS_JSON", f"Cannot parse reading metrics JSON: {exc}", READING_METRICS)
        return {}

    expected_registry = ROLE_REGISTRY.relative_to(DOCS).as_posix()
    if data.get("role_registry") != expected_registry:
        checks.error(
            "READING_METRICS_ROLE_REGISTRY",
            f"Reading metrics should reference {expected_registry}.",
            READING_METRICS,
        )

    pages = data.get("pages")
    if not isinstance(pages, list):
        checks.error("READING_METRICS_PAGES", "Reading metrics JSON does not expose a pages list.", READING_METRICS)
        return {}

    audiences: dict[str, str] = {}
    for page in pages:
        if not isinstance(page, dict):
            checks.error("READING_METRICS_PAGE", "Reading metrics page entry is not an object.", READING_METRICS)
            continue

        page_path = page.get("path")
        audience = page.get("target_audience")
        if not isinstance(page_path, str) or not isinstance(audience, str):
            checks.error("READING_METRICS_AUDIENCE", "Reading metrics page entry misses path or target_audience.", READING_METRICS)
            continue

        validate_audience_roles(DOCS / page_path, audience, roles, checks)
        audiences[page_path] = audience

    return audiences


def check_reading_role_registry(checks: Checks) -> None:
    before = len(checks.errors)
    roles = parse_role_registry(checks)
    if not roles:
        return

    metric_audiences = load_metric_audiences(checks, roles)
    for path in docs_markdown_pages():
        audience = extract_reading_card_audience(path, checks)
        if audience is None:
            continue

        validate_audience_roles(path, audience, roles, checks)

        page_key = path.relative_to(DOCS).as_posix()
        metric_audience = metric_audiences.get(page_key)
        if metric_audience is not None and metric_audience != audience:
            checks.error(
                "READING_CARD_METRICS_MISMATCH",
                f"Reading card audience differs from page metrics: {audience} != {metric_audience}",
                path,
            )

    if len(checks.errors) == before:
        checks.pass_check("Reading card audiences use the role registry.")


def check_reading_metrics(checks: Checks) -> None:
    if not READING_METRICS_SCRIPT.exists():
        checks.error("READING_METRICS_SCRIPT", "Reading metrics script is missing.", READING_METRICS_SCRIPT)
        return

    result = subprocess.run(
        [sys.executable, str(READING_METRICS_SCRIPT), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        details = (result.stdout + result.stderr).strip()
        checks.error("READING_METRICS_STALE", details or "Reading metrics are stale.", READING_METRICS_SCRIPT)
    else:
        checks.pass_check("Reading cards and repository statistics are up to date.")


def all_markdown_text() -> str:
    parts = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".venv" in path.parts or "site" in path.parts or ".git" in path.parts:
            continue
        parts.append(read_text(path))
    return "\n".join(parts).casefold()


def check_flow_guardrails(checks: Checks) -> None:
    content = all_markdown_text()

    required_phrases = [
        "converger sans nécessairement uniformiser",
        "bon niveau de commun",
        "plateforme demand",
        "colonne vertébrale opérationnelle",
        "données en transit",
        "contrats de données",
    ]

    for phrase in required_phrases:
        if phrase.casefold() not in content:
            checks.warn("FLOW_PHRASE_MISSING", f"Expected FLOW phrase not found: {phrase}")

    forbidden_patterns = [
        r"\bflow\s+est\s+un\s+oms\b",
        r"\bflow\s+est\s+un\s+erp\b",
        r"\bflow\s+remplace\s+l['’]erp\b",
        r"\bflow\s+remplace\s+l['’]oms\b",
    ]

    md_files = [
        path
        for path in sorted(ROOT.rglob("*.md"))
        if ".venv" not in path.parts and "site" not in path.parts and ".git" not in path.parts
    ]

    for path in md_files:
        text = read_text(path).casefold()
        for pattern in forbidden_patterns:
            if re.search(pattern, text):
                checks.error("FLOW_FORBIDDEN_FORMULATION", f"Forbidden FLOW formulation matched: {pattern}", path)

    if not any(finding.code == "FLOW_FORBIDDEN_FORMULATION" for finding in checks.errors):
        checks.pass_check("No forbidden FLOW positioning formulations found.")


def check_glossary_core_concepts(checks: Checks) -> None:
    glossary = DOCS / "glossaire.md"
    concepts = DOCS / "vision" / "concepts-cles.md"

    if not glossary.exists():
        checks.error("GLOSSARY_MISSING", "Glossary is missing.", glossary)
        return

    if not concepts.exists():
        checks.error("CONCEPTS_MISSING", "Concepts page is missing.", concepts)
        return

    glossary_text = read_text(glossary).casefold()
    concepts_text = read_text(concepts).casefold()

    required = [
        "bon niveau de commun",
        "demande / demand",
        "case",
        "plateforme demand",
        "fulfillment network",
        "agreement",
        "source de référence / projection",
        "stock unifié",
        "vues 360",
    ]

    for concept in required:
        if concept.casefold() not in glossary_text:
            checks.error("GLOSSARY_CONCEPT", f"Core concept missing from glossary: {concept}", glossary)
        if concept.casefold() not in concepts_text:
            checks.warn("CONCEPT_PAGE_CONCEPT", f"Core concept missing from concepts page: {concept}", concepts)

    if not any(finding.code == "GLOSSARY_CONCEPT" for finding in checks.errors):
        checks.pass_check("Glossary contains the expected core FLOW concepts.")


def check_svg_assets(checks: Checks) -> None:
    svg_files = sorted(DOCS.rglob("*.svg"))
    invalid = 0

    for path in svg_files:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            checks.error("SVG_XML", f"SVG is not valid XML: {exc}", path)
            invalid += 1

    if not invalid:
        checks.pass_check(f"SVG assets are valid XML ({len(svg_files)} checked).")


def check_image_registry(checks: Checks) -> None:
    if not IMAGE_REGISTRY.exists():
        checks.error("IMAGE_REGISTRY_MISSING", "Image dependency registry is missing.", IMAGE_REGISTRY)
        return

    registry_text = read_text(IMAGE_REGISTRY)
    svg_files = sorted(DOCS.rglob("*.svg"))
    references = collect_markdown_svg_references()
    missing_entries = 0
    missing_usages = 0

    for svg_file in svg_files:
        if svg_file.name not in registry_text:
            checks.error("IMAGE_REGISTRY_ENTRY", f"SVG is missing from image registry: {svg_file.name}", IMAGE_REGISTRY)
            missing_entries += 1

    for svg_file, pages in sorted(references.items(), key=lambda item: item[0].name):
        if svg_file.name not in registry_text:
            checks.error("IMAGE_REGISTRY_REFERENCE", f"Referenced SVG is missing from image registry: {svg_file.name}", IMAGE_REGISTRY)
            missing_entries += 1

        for page in sorted(pages):
            page_ref = rel(page)
            if page_ref not in registry_text:
                checks.error(
                    "IMAGE_REGISTRY_USAGE",
                    f"Image registry does not mention page using {svg_file.name}: {page_ref}",
                    IMAGE_REGISTRY,
                )
                missing_usages += 1

    if not missing_entries and not missing_usages:
        checks.pass_check(f"Image dependency registry covers SVG assets and usages ({len(svg_files)} SVG files).")


def print_report(checks: Checks) -> None:
    print("FLOW site checks")
    print("================")

    for message in checks.ok:
        print(f"[OK] {message}")

    for finding in checks.findings:
        location = f" ({rel(finding.path)})" if finding.path else ""
        print(f"[{finding.level}] {finding.code}: {finding.message}{location}")

    print()
    print(f"Summary: {len(checks.errors)} error(s), {len(checks.warnings)} warning(s)")


def run_checks(check_external: bool = False, external_timeout: float = 8.0, strict_external: bool = False) -> Checks:
    checks = Checks()
    check_nav_coverage(checks)
    check_nav_title_alignment(checks)
    check_generated_content_not_tracked(checks)
    check_repository_line_endings(checks)
    check_built_site_links(checks)
    check_multilingual_site(checks)
    if check_external:
        check_external_links(checks, external_timeout, strict_external)
    check_agents_publication_sync(checks)
    check_ci_workflow(checks)
    check_section_indexes(checks)
    check_reading_role_registry(checks)
    check_reading_metrics(checks)
    check_flow_guardrails(checks)
    check_glossary_core_concepts(checks)
    check_svg_assets(checks)
    check_image_registry(checks)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Run FLOW documentation consistency checks.")
    parser.add_argument(
        "--external-links",
        action="store_true",
        help="Also check external HTTP(S) links from the built site. This requires network access.",
    )
    parser.add_argument(
        "--external-timeout",
        type=float,
        default=8.0,
        help="Timeout in seconds for each external link request.",
    )
    parser.add_argument(
        "--strict-external-links",
        action="store_true",
        help="Turn confirmed external HTTP failures into errors. Network failures remain warnings.",
    )
    args = parser.parse_args()

    checks = run_checks(
        check_external=args.external_links or args.strict_external_links,
        external_timeout=args.external_timeout,
        strict_external=args.strict_external_links,
    )
    print_report(checks)

    return 1 if checks.errors else 0


if __name__ == "__main__":
    sys.exit(main())
