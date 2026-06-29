from __future__ import annotations

import argparse
import re
import subprocess
import sys
import urllib.parse
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
MKDOCS = ROOT / "mkdocs.yml"
GITIGNORE = ROOT / ".gitignore"
READING_METRICS_SCRIPT = ROOT / "scripts" / "update_reading_metrics.py"


@dataclass
class Finding:
    level: str
    code: str
    message: str
    path: Path | None = None


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
    tracked = run_git(["ls-files", "site", ".venv", ".agents", "__pycache__"])

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

    expected_patterns = ["site/", ".venv/", ".agents/"]
    if not GITIGNORE.exists():
        checks.error("GITIGNORE", ".gitignore is missing.", GITIGNORE)
        return

    gitignore = {line.strip() for line in read_text(GITIGNORE).splitlines()}
    for pattern in expected_patterns:
        if pattern not in gitignore:
            checks.error("GITIGNORE_PATTERN", f"Missing .gitignore pattern: {pattern}", GITIGNORE)

    if all(pattern in gitignore for pattern in expected_patterns):
        checks.pass_check(".gitignore protects generated/local paths.")


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


def normalize_site_target(source: Path, href: str) -> tuple[Path, str]:
    parsed = urllib.parse.urlsplit(href)
    path_part = urllib.parse.unquote(parsed.path)
    fragment = urllib.parse.unquote(parsed.fragment)

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
        "scripts\\check-site.ps1",
        "scripts\\update-reading-metrics.ps1",
        "environnement-codex-windows.md",
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


def check_section_indexes(checks: Checks) -> None:
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
        "environnement-codex-windows.md",
        "instructions-codex.md",
    ]

    for page in expected_admin:
        if page not in admin_text:
            checks.error("ADMIN_INDEX_LINK", f"Administration index does not link to {page}.", admin_index)

    if all(page in admin_text for page in expected_admin):
        checks.pass_check("Administration index links to expected operational pages.")


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


def run_checks() -> Checks:
    checks = Checks()
    check_nav_coverage(checks)
    check_generated_content_not_tracked(checks)
    check_built_site_links(checks)
    check_agents_publication_sync(checks)
    check_section_indexes(checks)
    check_reading_metrics(checks)
    check_flow_guardrails(checks)
    check_glossary_core_concepts(checks)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Run FLOW documentation consistency checks.")
    parser.parse_args()

    checks = run_checks()
    print_report(checks)

    return 1 if checks.errors else 0


if __name__ == "__main__":
    sys.exit(main())
