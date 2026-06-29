from __future__ import annotations

import html
import os
import shutil
import subprocess
import sys
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


def write_root_landing() -> None:
    choices = "\n".join(
        f'<a class="language-card" href="{html.escape(code)}/">'
        f"<span>{html.escape(language['display_name'])}</span>"
        "</a>"
        for code, language in LANGUAGES.items()
    )
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
