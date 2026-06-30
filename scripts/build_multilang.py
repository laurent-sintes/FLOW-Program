from __future__ import annotations

import html
import hashlib
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit runtime diagnostic
    raise SystemExit("PyYAML is required to build the multilingual site.") from exc


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
GENERATED = ROOT / ".generated" / "i18n"
BASE_CONFIG = ROOT / "mkdocs.yml"
PUBLISHED_BASE_URL = "https://laurent-sintes.github.io/FLOW-Program"
PUBLISHED_BASE_PATH = "/FLOW-Program"
CACHE_BUST_EXTENSIONS = r"css|js|svg|png|jpe?g|webp|gif|ico|woff2?|ttf|otf"
CACHE_BUST_QUERY_PARAM = "v"
HTML_ASSET_RE = re.compile(
    rf'(?P<prefix>\b(?:href|src)=")'
    rf'(?P<url>[^"]+\.(?:{CACHE_BUST_EXTENSIONS})(?:\?[^"#]*)?(?:#[^"]*)?)'
    rf'(?P<suffix>")',
    re.IGNORECASE,
)
CSS_ASSET_RE = re.compile(
    rf"url\((?P<quote>['\"]?)(?P<url>[^)'\" ]+\.(?:{CACHE_BUST_EXTENSIONS})(?:\?[^)'\"]*)?(?:#[^)'\"]*)?)(?P=quote)\)",
    re.IGNORECASE,
)

LANGUAGES = {
    "fr": {
        "name": "Francais",
        "display_name": "Français",
        "theme_language": "fr",
        "site_name": "Programme FLOW",
        "docs_dir": DOCS,
        "notice": None,
    },
    "en": {
        "name": "English",
        "display_name": "English",
        "theme_language": "en",
        "site_name": "FLOW Program",
        "docs_dir": GENERATED / "en" / "docs",
        "notice": (
            '<div class="flow-translation-notice">'
            "<strong>English version in progress.</strong> "
            "This page is generated from the French reference source. "
            "Until the translation cache is configured, some content may remain in French."
            "</div>"
        ),
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_base_config() -> dict[str, Any]:
    data = yaml.safe_load(read_text(BASE_CONFIG)) or {}
    if not isinstance(data, dict):
        raise SystemExit("mkdocs.yml does not contain a YAML mapping.")
    return data


def copy_tree_with_markdown_transform(source: Path, target: Path, notice: str | None) -> None:
    if target.exists():
        shutil.rmtree(target)

    for path in source.rglob("*"):
        relative = path.relative_to(source)
        destination = target / relative

        if path.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        if path.suffix.lower() == ".md" and notice:
            write_text(destination, inject_translation_notice(read_text(path), notice))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)


def inject_translation_notice(text: str, notice: str) -> str:
    marker = "<!-- FLOW-READING-CARD:END -->"
    if marker in text:
        return text.replace(marker, f"{marker}\n\n{notice}", 1)

    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(index + 1, "")
            lines.insert(index + 2, notice)
            return "\n".join(lines) + "\n"

    return f"{notice}\n\n{text}"


def alternate_entries() -> list[dict[str, str]]:
    return [
        {
            "name": language["display_name"],
            "link": f"{PUBLISHED_BASE_URL}/{code}/",
            "lang": code,
        }
        for code, language in LANGUAGES.items()
    ]


def language_config(code: str, base_config: dict[str, Any]) -> dict[str, Any]:
    language = LANGUAGES[code]
    data = dict(base_config)
    data["site_name"] = language["site_name"]
    data["site_url"] = f"{PUBLISHED_BASE_URL}/{code}/"
    data["docs_dir"] = str(Path(language["docs_dir"]).resolve()).replace("\\", "/")
    data["site_dir"] = str((SITE / code).resolve()).replace("\\", "/")

    theme = dict(data.get("theme") or {})
    theme["language"] = language["theme_language"]
    data["theme"] = theme

    extra = dict(data.get("extra") or {})
    extra["alternate"] = alternate_entries()
    data["extra"] = extra

    return data


def write_language_config(code: str, base_config: dict[str, Any]) -> Path:
    config_path = GENERATED / code / "mkdocs.yml"
    config = language_config(code, base_config)
    write_text(config_path, yaml.safe_dump(config, allow_unicode=True, sort_keys=False))
    return config_path


def run_mkdocs(config_path: Path) -> None:
    env = os.environ.copy()
    env["NO_MKDOCS_2_WARNING"] = "true"
    process = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(config_path)],
        cwd=ROOT,
        env=env,
        check=False,
    )
    if process.returncode != 0:
        raise SystemExit(process.returncode)


def language_choices() -> str:
    return "\n".join(
        f'<a class="language-card" href="{html.escape(code)}/">'
        f"<span>{html.escape(language['display_name'])}</span>"
        "</a>"
        for code, language in LANGUAGES.items()
    )


def write_root_landing() -> None:
    choices = language_choices()
    page = f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0; url=fr/">
  <link rel="canonical" href="https://laurent-sintes.github.io/FLOW-Program/fr/">
  <script>
    window.location.replace("fr/" + window.location.search + window.location.hash);
  </script>
  <title>Programme FLOW</title>
  <style>
    body {{
      margin: 0;
      font-family: Aptos, Calibri, Arial, sans-serif;
      background: #f7fbfa;
      color: #173f3a;
      display: grid;
      min-height: 100vh;
      place-items: center;
    }}
    main {{
      width: min(680px, calc(100vw - 48px));
    }}
    h1 {{
      font-size: 2rem;
      margin: 0 0 0.75rem;
    }}
    p {{
      color: #58706b;
      line-height: 1.5;
    }}
    .language-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 24px;
    }}
    .language-card {{
      border: 1px solid #d7e5e2;
      background: #fff;
      border-radius: 8px;
      color: #173f3a;
      display: block;
      font-weight: 700;
      padding: 18px 20px;
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Programme FLOW</h1>
    <p>Redirection vers la version française. Sélectionnez une langue si la redirection automatique ne fonctionne pas.</p>
    <div class="language-grid">
      {choices}
    </div>
  </main>
</body>
</html>
"""
    write_text(SITE / "index.html", page)


def write_404_page() -> None:
    choices = "\n".join(
        f'<a class="language-card" href="{PUBLISHED_BASE_PATH}/{html.escape(code)}/">'
        f"<span>{html.escape(language['display_name'])}</span>"
        "</a>"
        for code, language in LANGUAGES.items()
    )
    page = f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>
    (function () {{
      var projectBase = "{PUBLISHED_BASE_PATH}";
      var languages = ["fr", "en"];
      var path = window.location.pathname.replace(/\\/+$/, "");

      function hasLanguagePrefix(value) {{
        return languages.some(function (language) {{
          var languagePath = projectBase + "/" + language;
          return value === languagePath || value.indexOf(languagePath + "/") === 0;
        }});
      }}

      if (window.location.pathname.indexOf(projectBase + "/") === 0 && !hasLanguagePrefix(path)) {{
        var rest = window.location.pathname.slice(projectBase.length);
        if (!rest || rest === "/") {{
          rest = "/";
        }}
        window.location.replace(projectBase + "/fr" + rest + window.location.search + window.location.hash);
      }}
    }}());
  </script>
  <title>Page introuvable - Programme FLOW</title>
  <style>
    body {{
      margin: 0;
      font-family: Aptos, Calibri, Arial, sans-serif;
      background: #f7fbfa;
      color: #173f3a;
      display: grid;
      min-height: 100vh;
      place-items: center;
    }}
    main {{
      width: min(680px, calc(100vw - 48px));
    }}
    h1 {{
      font-size: 2rem;
      margin: 0 0 0.75rem;
    }}
    p {{
      color: #58706b;
      line-height: 1.5;
    }}
    .language-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 24px;
    }}
    .language-card {{
      border: 1px solid #d7e5e2;
      background: #fff;
      border-radius: 8px;
      color: #173f3a;
      display: block;
      font-weight: 700;
      padding: 18px 20px;
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Page introuvable</h1>
    <p>Si vous avez utilisé un ancien lien sans préfixe de langue, redirection vers la version française en cours.</p>
    <p>Sinon, sélectionnez une langue pour revenir à l'accueil du programme FLOW.</p>
    <div class="language-grid">
      {choices}
    </div>
  </main>
</body>
</html>
"""
    write_text(SITE / "404.html", page)


def should_skip_asset_url(url: str) -> bool:
    value = url.strip().lower()
    if not value or value.startswith(("#", "//")):
        return True

    parsed = urllib.parse.urlsplit(value)
    return parsed.scheme in {"http", "https", "mailto", "tel", "javascript", "data"}


def split_asset_url(url: str) -> tuple[str, str]:
    parsed = urllib.parse.urlsplit(url)
    suffix = ""
    if parsed.fragment:
        suffix = f"#{parsed.fragment}"
    return parsed.path, suffix


def resolve_site_asset(source_file: Path, asset_path: str) -> Path | None:
    if not asset_path:
        return None

    decoded_path = urllib.parse.unquote(asset_path)
    if decoded_path == PUBLISHED_BASE_PATH:
        return SITE / "index.html"

    if decoded_path.startswith(f"{PUBLISHED_BASE_PATH}/"):
        candidate = SITE / decoded_path.removeprefix(f"{PUBLISHED_BASE_PATH}/")
    elif decoded_path.startswith("/"):
        candidate = SITE / decoded_path.lstrip("/")
    else:
        candidate = source_file.parent / decoded_path

    candidate = candidate.resolve()
    try:
        candidate.relative_to(SITE.resolve())
    except ValueError:
        return None

    if not candidate.is_file():
        return None

    return candidate


def versioned_asset_url(url: str, source_file: Path) -> str:
    if should_skip_asset_url(url):
        return url

    asset_path, suffix = split_asset_url(url)
    asset_file = resolve_site_asset(source_file, asset_path)
    if asset_file is None:
        return url

    digest = hashlib.sha256(asset_file.read_bytes()).hexdigest()[:12]
    return f"{asset_path}?{CACHE_BUST_QUERY_PARAM}={digest}{suffix}"


def cache_bust_css_file(path: Path) -> None:
    text = read_text(path)

    def replace(match: re.Match[str]) -> str:
        quote = match.group("quote") or ""
        url = versioned_asset_url(match.group("url"), path)
        return f"url({quote}{url}{quote})"

    updated = CSS_ASSET_RE.sub(replace, text)
    if updated != text:
        write_text(path, updated)


def cache_bust_html_file(path: Path) -> None:
    text = read_text(path)

    def replace(match: re.Match[str]) -> str:
        return f"{match.group('prefix')}{versioned_asset_url(match.group('url'), path)}{match.group('suffix')}"

    updated = HTML_ASSET_RE.sub(replace, text)
    if updated != text:
        write_text(path, updated)


def cache_bust_site_assets() -> None:
    for css_file in sorted(SITE.rglob("*.css")):
        cache_bust_css_file(css_file)

    for html_file in sorted(SITE.rglob("*.html")):
        cache_bust_html_file(html_file)


def main() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    if GENERATED.exists():
        shutil.rmtree(GENERATED)

    base_config = load_base_config()

    for code, language in LANGUAGES.items():
        if code != "fr":
            copy_tree_with_markdown_transform(DOCS, Path(language["docs_dir"]), language["notice"])

        config_path = write_language_config(code, base_config)
        run_mkdocs(config_path)

    write_root_landing()
    write_404_page()
    cache_bust_site_assets()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
