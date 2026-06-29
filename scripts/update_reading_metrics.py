from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
METRICS_PATH = DOCS / "referentiel" / "page-metrics.json"
STATS_PAGE = DOCS / "referentiel" / "statistiques.md"
ROLE_REGISTRY_PATH = DOCS / "administration" / "referentiel-roles.md"
READING_WORDS_PER_MINUTE = 220
PROFILE_VERSION = 3
SOURCE_LANGUAGE = "fr"
PUBLISHED_LANGUAGES = ["fr", "en"]
METRICS_SCOPE = "canonical_source"
LANGUAGE_METRICS_POLICY = (
    "Les métriques mesurent la source éditoriale française dans docs/. "
    "Les sorties publiées par langue ne sont pas additionnées."
)

CARD_START = "<!-- FLOW-READING-CARD:START -->"
CARD_END = "<!-- FLOW-READING-CARD:END -->"
GENERATED_START = "<!-- FLOW-GENERATED-STATS:START -->"
GENERATED_END = "<!-- FLOW-GENERATED-STATS:END -->"

STOPWORDS = {
    "afin",
    "ainsi",
    "alors",
    "apres",
    "assez",
    "aussi",
    "autour",
    "autre",
    "autres",
    "avec",
    "avoir",
    "besoin",
    "bien",
    "cette",
    "ceci",
    "cela",
    "celle",
    "celui",
    "ces",
    "cet",
    "cette",
    "chaque",
    "chez",
    "comme",
    "comment",
    "dans",
    "des",
    "donc",
    "dont",
    "doit",
    "doivent",
    "dune",
    "elle",
    "elles",
    "entre",
    "etre",
    "faire",
    "fait",
    "faut",
    "flow",
    "hors",
    "leur",
    "leurs",
    "mais",
    "meme",
    "moins",
    "n'est",
    "notamment",
    "nous",
    "peut",
    "peuvent",
    "plus",
    "pour",
    "pourquoi",
    "quand",
    "que",
    "quel",
    "quelle",
    "quelles",
    "quels",
    "sans",
    "selon",
    "sont",
    "sous",
    "sur",
    "tous",
    "tout",
    "toute",
    "toutes",
    "trop",
    "une",
    "vers",
    "via",
}


SECTION_PROFILES = {
    "vision": (
        "Sponsor, Direction, Architecte",
        "Comprendre la vision, les arbitrages et le vocabulaire cible",
    ),
    "architecture-cible": (
        "Architecte, Développeur, Delivery",
        "Relier les concepts FLOW aux produits, patterns et responsabilités cible",
    ),
    "principes-directeurs": (
        "Architecte, Métier, Sponsor",
        "Guider les décisions de conception et vérifier la cohérence des arbitrages",
    ),
    "hotspots": (
        "Sponsor, Architecte, Métier",
        "Préparer les arbitrages sur les points sensibles de convergence",
    ),
    "contexte": (
        "Architecte, Métier, Contributeur",
        "Comprendre le point de départ et les tensions observées",
    ),
    "insights": (
        "Architecte, Sponsor, Contributeur",
        "Retrouver la mémoire de raisonnement et les hypothèses stabilisées",
    ),
    "methode": (
        "PMO, Architecte, Contributeur",
        "Cadrer la démarche et passer des observations aux choix de conception",
    ),
    "administration": (
        "Mainteneur, Contributeur, Codex",
        "Maintenir le référentiel, l'environnement local et les contrôles",
    ),
    "transformation": (
        "Change Manager, Sponsor, Métier",
        "Préparer l'adoption et les changements de posture",
    ),
    "referentiel": (
        "Tous lecteurs, Contributeur, Mainteneur",
        "Piloter la lisibilité, les concepts et les repères quantitatifs",
    ),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def doc_rel(path: Path) -> str:
    return path.relative_to(DOCS).as_posix()


def strip_between(text: str, start: str, end: str) -> str:
    pattern = re.compile(rf"\n?{re.escape(start)}.*?{re.escape(end)}\n?", re.DOTALL)
    return pattern.sub("\n", text)


def strip_reading_card(text: str) -> str:
    return strip_between(text, CARD_START, CARD_END).strip() + "\n"


def strip_generated_stats(text: str) -> str:
    return strip_between(text, GENERATED_START, GENERATED_END).strip() + "\n"


def strip_generated_blocks(text: str) -> str:
    return strip_generated_stats(strip_reading_card(text))


def load_role_registry() -> set[str]:
    if not ROLE_REGISTRY_PATH.exists():
        raise RuntimeError(f"Référentiel des rôles introuvable : {rel(ROLE_REGISTRY_PATH)}")

    roles: set[str] = set()
    for line in read_text(ROLE_REGISTRY_PATH).splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        role = cells[0]
        if role in {"Rôle", "---"} or set(role) == {"-"}:
            continue
        roles.add(role)

    if not roles:
        raise RuntimeError(f"Aucun rôle trouvé dans {rel(ROLE_REGISTRY_PATH)}")

    return roles


def split_roles(audience: str) -> list[str]:
    return [role.strip() for role in audience.split(",") if role.strip()]


def validate_audience(audience: str, path: Path, role_registry: set[str]) -> None:
    roles = split_roles(audience)
    if not roles:
        raise RuntimeError(f"Aucun rôle défini pour {doc_rel(path)}")
    if len(roles) > 3:
        raise RuntimeError(f"Trop de rôles dans le cartouche de {doc_rel(path)} : {audience}")

    unknown = [role for role in roles if role not in role_registry]
    if unknown:
        allowed = ", ".join(sorted(role_registry))
        raise RuntimeError(
            f"Rôle non autorisé dans {doc_rel(path)} : {', '.join(unknown)}. "
            f"Rôles autorisés : {allowed}"
        )


def plain_text(markdown: str) -> str:
    text = strip_generated_blocks(markdown)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[#>*_|~\-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_word(word: str) -> str:
    word = word.lower().replace("’", " ").replace("'", " ")
    normalized = unicodedata.normalize("NFKD", word)
    return "".join(char for char in normalized if not unicodedata.combining(char)).strip()


def words(markdown: str) -> list[str]:
    text = plain_text(markdown)
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9][A-Za-zÀ-ÖØ-öø-ÿ0-9'’\-]*", text)


def term_counts(markdown: str) -> Counter[str]:
    result: Counter[str] = Counter()
    for word in words(markdown):
        normalized_phrase = normalize_word(word)
        for normalized in re.findall(r"[a-z0-9]+", normalized_phrase):
            if len(normalized) < 4:
                continue
            if normalized.isdigit():
                continue
            if normalized in STOPWORDS:
                continue
            result[normalized] += 1
    return result


def extract_title(markdown: str, fallback: str) -> str:
    md_match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    if md_match:
        return re.sub(r"<[^>]+>", "", md_match.group(1)).strip()

    html_match = re.search(r"<h1[^>]*>(.*?)</h1>", markdown, re.IGNORECASE | re.DOTALL)
    if html_match:
        return re.sub(r"<[^>]+>", "", html_match.group(1)).strip()

    return fallback


def section_for(path: Path) -> str:
    relative = path.relative_to(DOCS)
    if len(relative.parts) == 1:
        if relative.name == "glossaire.md":
            return "referentiel"
        return "accueil"
    return relative.parts[0]


def profile_for(path: Path, role_registry: set[str]) -> tuple[str, str]:
    relative = path.relative_to(DOCS)
    if relative.as_posix() == "index.md":
        profile = ("Tous lecteurs", "S'orienter dans le référentiel FLOW")
        validate_audience(profile[0], path, role_registry)
        return profile
    if relative.as_posix() == "glossaire.md":
        profile = ("Tous lecteurs, Contributeur", "Stabiliser le vocabulaire et retrouver les pages de référence")
        validate_audience(profile[0], path, role_registry)
        return profile
    section = section_for(path)
    if relative.name == "index.md" and section in SECTION_PROFILES:
        audience, _usage = SECTION_PROFILES[section]
        profile = (audience, "S'orienter dans la section et identifier les pages utiles")
        validate_audience(profile[0], path, role_registry)
        return profile
    profile = SECTION_PROFILES.get(
        section,
        ("Tous lecteurs", "Lire et maintenir le référentiel FLOW"),
    )
    validate_audience(profile[0], path, role_registry)
    return profile


def reading_minutes(word_count: int) -> int:
    return max(1, math.ceil(word_count / READING_WORDS_PER_MINUTE))


def format_minutes(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes} min"
    hours, rest = divmod(minutes, 60)
    if rest == 0:
        return f"{hours} h"
    return f"{hours} h {rest} min"


def content_hash(markdown: str) -> str:
    normalized = strip_generated_blocks(markdown)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def metric_for_page(
    path: Path,
    source: str,
    role_registry: set[str],
    cached: dict[str, Any] | None = None,
) -> dict[str, Any]:
    base = strip_generated_blocks(source)
    digest = content_hash(base)
    if cached and cached.get("content_hash") == digest and cached.get("profile_version") == PROFILE_VERSION:
        validate_audience(str(cached.get("target_audience", "")), path, role_registry)
        return cached

    word_count = len(words(base))
    terms = term_counts(base)
    audience, usage = profile_for(path, role_registry)
    return {
        "path": doc_rel(path),
        "language": SOURCE_LANGUAGE,
        "title": extract_title(base, path.stem.replace("-", " ").title()),
        "section": section_for(path),
        "target_audience": audience,
        "usage": usage,
        "profile_version": PROFILE_VERSION,
        "word_count": word_count,
        "reading_minutes": reading_minutes(word_count),
        "heading_count": len(re.findall(r"^#{1,6}\s+", base, flags=re.MULTILINE)),
        "link_count": len(re.findall(r"\[[^\]]+\]\([^)]+\)", base)),
        "content_hash": digest,
        "top_terms": dict(terms.most_common(30)),
    }


def reading_card(metric: dict[str, Any]) -> str:
    return "\n".join(
        [
            CARD_START,
            '<div class="flow-reading-card">',
            '  <div class="flow-reading-card__title">Repère de lecture</div>',
            '  <div class="flow-reading-card__grid">',
            "    <div>",
            "      <span>Public cible</span>",
            f"      <strong>{metric['target_audience']}</strong>",
            "    </div>",
            "    <div>",
            "      <span>Temps de lecture</span>",
            f"      <strong>{format_minutes(int(metric['reading_minutes']))}</strong>",
            "    </div>",
            "    <div>",
            "      <span>Usage</span>",
            f"      <strong>{metric['usage']}</strong>",
            "    </div>",
            "  </div>",
            "</div>",
            CARD_END,
        ]
    )


def insert_reading_card(path: Path, source: str, metric: dict[str, Any]) -> str:
    clean = strip_reading_card(source).strip() + "\n"
    card = reading_card(metric)

    h1_match = re.search(r"^#\s+.+?$", clean, flags=re.MULTILINE)
    if h1_match:
        insert_at = h1_match.end()
        head = clean[:insert_at].rstrip()
        tail = clean[insert_at:].lstrip("\n")
        return head + "\n\n" + card + "\n\n" + tail

    if doc_rel(path) == "index.md":
        hero_end = clean.find("</div>")
        if hero_end != -1:
            insert_at = hero_end + len("</div>")
            head = clean[:insert_at].rstrip()
            tail = clean[insert_at:].lstrip("\n")
            return head + "\n\n" + card + "\n\n" + tail

    return card + "\n\n" + clean.lstrip("\n")


def markdown_pages() -> list[Path]:
    return sorted(
        path
        for path in DOCS.rglob("*.md")
        if path != STATS_PAGE and path.is_file()
    )


def load_existing_metrics() -> dict[str, dict[str, Any]]:
    if not METRICS_PATH.exists():
        return {}
    try:
        data = json.loads(read_text(METRICS_PATH))
    except json.JSONDecodeError:
        return {}
    pages = data.get("pages", [])
    if not isinstance(pages, list):
        return {}
    return {
        page["path"]: page
        for page in pages
        if isinstance(page, dict) and isinstance(page.get("path"), str)
    }


def collect_metrics() -> list[dict[str, Any]]:
    cached = load_existing_metrics()
    role_registry = load_role_registry()
    metrics: list[dict[str, Any]] = []
    for path in markdown_pages():
        source = read_text(path)
        metrics.append(metric_for_page(path, source, role_registry, cached.get(doc_rel(path))))
    return sorted(metrics, key=lambda item: item["path"])


def write_page_metrics(metrics: list[dict[str, Any]]) -> None:
    write_text(METRICS_PATH, json.dumps(metrics_payload(metrics), ensure_ascii=False, indent=2) + "\n")


def metrics_payload(metrics: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "profile_version": PROFILE_VERSION,
        "metrics_scope": METRICS_SCOPE,
        "source_language": SOURCE_LANGUAGE,
        "published_languages": PUBLISHED_LANGUAGES,
        "language_metrics_policy": LANGUAGE_METRICS_POLICY,
        "reading_words_per_minute": READING_WORDS_PER_MINUTE,
        "role_registry": doc_rel(ROLE_REGISTRY_PATH),
        "source": "scripts/update_reading_metrics.py",
        "pages": metrics,
    }


def update_reading_cards(metrics: list[dict[str, Any]]) -> None:
    by_path = {metric["path"]: metric for metric in metrics}
    for path in markdown_pages():
        metric = by_path[doc_rel(path)]
        source = read_text(path)
        updated = insert_reading_card(path, source, metric)
        if updated != source:
            write_text(path, updated)


def count_glossary_concepts() -> int:
    glossary = DOCS / "glossaire.md"
    if not glossary.exists():
        return 0
    return len(re.findall(r"^###\s+", strip_generated_blocks(read_text(glossary)), flags=re.MULTILINE))


def count_pages(folder: str) -> int:
    path = DOCS / folder
    if not path.exists():
        return 0
    return len([item for item in path.glob("*.md") if item.name != "index.md"])


def aggregate_terms(metrics: list[dict[str, Any]]) -> Counter[str]:
    result: Counter[str] = Counter()
    for metric in metrics:
        result.update(metric.get("top_terms", {}))
    return result


def top_pages(metrics: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    return sorted(metrics, key=lambda item: item["word_count"], reverse=True)[:limit]


def section_summary(metrics: list[dict[str, Any]]) -> list[tuple[str, int, int, int]]:
    sections: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for metric in metrics:
        sections[metric["section"]].append(metric)

    rows = []
    for section, pages in sorted(sections.items()):
        rows.append(
            (
                section,
                len(pages),
                sum(page["word_count"] for page in pages),
                sum(page["reading_minutes"] for page in pages),
            )
        )
    return rows


def word_cloud_html(terms: Counter[str], limit: int = 45) -> str:
    if not terms:
        return "_Aucun terme disponible._"

    top = terms.most_common(limit)
    max_count = top[0][1]
    spans = []
    for term, count in top:
        weight = max(1, min(5, math.ceil((count / max_count) * 5)))
        spans.append(
            f'<span class="flow-word-cloud__term flow-word-cloud__term--{weight}" title="{count} occurrences">{term}</span>'
        )
    return '<div class="flow-word-cloud">\n' + "\n".join(spans) + "\n</div>"


def stats_page(metrics: list[dict[str, Any]]) -> str:
    total_words = sum(metric["word_count"] for metric in metrics)
    total_minutes = sum(metric["reading_minutes"] for metric in metrics)
    concepts = count_glossary_concepts()
    hotspots = count_pages("hotspots")
    products = count_pages("architecture-cible/produits")
    patterns = count_pages("architecture-cible/patterns")
    components = products + patterns
    terms = aggregate_terms(metrics)

    stats_metric = {
        "target_audience": "Sponsor, Architecte, Contributeur",
        "reading_minutes": 3,
        "usage": "Piloter la couverture documentaire et la charge de lecture",
    }
    validate_audience(stats_metric["target_audience"], STATS_PAGE, load_role_registry())

    lines = [
        "# Statistiques du référentiel",
        "",
        reading_card(stats_metric),
        "",
        GENERATED_START,
        "",
        "Cette page est générée par `scripts/update_reading_metrics.py` à partir du fichier `docs/referentiel/page-metrics.json`.",
        "",
        "## Périmètre linguistique",
        "",
        f"- Langue source des métriques : `{SOURCE_LANGUAGE}`.",
        "- Source mesurée : `docs/`, c'est-à-dire la base éditoriale française de référence.",
        f"- Langues publiées : {', '.join(f'`/{code}/`' for code in PUBLISHED_LANGUAGES)}.",
        "- Les sorties générées par langue ne sont pas additionnées afin d'éviter un double comptage artificiel.",
        "- Tant que la traduction anglaise est générée depuis le français, ses cartouches et durées de lecture reprennent les métriques de la source française.",
        "- Quand un cache de traduction anglais sera versionné, il faudra ajouter des métriques par langue plutôt que remplacer les métriques de référence.",
        "",
        "## Synthèse quantitative",
        "",
        "| Indicateur | Valeur |",
        "| --- | ---: |",
        f"| Pages suivies | {len(metrics)} |",
        f"| Nombre de mots | {total_words:,} |".replace(",", " "),
        f"| Temps de lecture complet | {format_minutes(total_minutes)} |",
        f"| Concepts du glossaire | {concepts} |",
        f"| Hotspots documentés | {hotspots} |",
        f"| Produits FLOW | {products} |",
        f"| Patterns d'architecture | {patterns} |",
        f"| Composants suivis, produits + patterns | {components} |",
        "",
        "## Répartition par section",
        "",
        "| Section | Pages | Mots | Lecture |",
        "| --- | ---: | ---: | ---: |",
    ]

    for section, page_count, words_count, minutes in section_summary(metrics):
        lines.append(f"| {section} | {page_count} | {words_count:,} | {format_minutes(minutes)} |".replace(",", " "))

    lines.extend(
        [
            "",
            "## Pages les plus longues",
            "",
            "| Page | Mots | Lecture |",
            "| --- | ---: | ---: |",
        ]
    )

    for metric in top_pages(metrics):
        title = metric["title"].replace("|", "\\|")
        lines.append(
            f"| [{title}](../{metric['path']}) | {metric['word_count']:,} | {format_minutes(metric['reading_minutes'])} |".replace(",", " ")
        )

    lines.extend(
        [
            "",
            "## Nuage de mots",
            "",
            word_cloud_html(terms),
            "",
            "## Fichier de comptage",
            "",
            "Le comptage unitaire par page est conservé dans `docs/referentiel/page-metrics.json`.",
            "",
            "Lorsqu'une page est modifiée, relancer :",
            "",
            "```powershell",
            ".\\scripts\\update-reading-metrics.ps1",
            "```",
            "",
            "Le contrôle `check-site` vérifie que les cartouches, les compteurs et cette page restent synchronisés.",
            "",
            GENERATED_END,
            "",
        ]
    )
    return "\n".join(lines)


def write_stats_page(metrics: list[dict[str, Any]]) -> None:
    write_text(STATS_PAGE, stats_page(metrics))


def current_expected_outputs() -> dict[Path, str]:
    metrics = collect_metrics()
    outputs: dict[Path, str] = {}
    by_path = {metric["path"]: metric for metric in metrics}
    for path in markdown_pages():
        outputs[path] = insert_reading_card(path, read_text(path), by_path[doc_rel(path)])

    outputs[METRICS_PATH] = json.dumps(metrics_payload(metrics), ensure_ascii=False, indent=2) + "\n"
    outputs[STATS_PAGE] = stats_page(metrics)
    return outputs


def run_update() -> None:
    metrics = collect_metrics()
    update_reading_cards(metrics)
    # Recompute after card insertion to keep hashes based on final source without generated cards.
    metrics = collect_metrics()
    write_page_metrics(metrics)
    write_stats_page(metrics)


def run_check() -> int:
    stale: list[str] = []
    outputs = current_expected_outputs()
    for path, expected in outputs.items():
        if not path.exists():
            stale.append(f"missing: {rel(path)}")
            continue
        actual = read_text(path)
        if actual != expected:
            stale.append(rel(path))

    if stale:
        print("Reading metrics are not up to date. Run scripts\\update-reading-metrics.ps1.")
        for item in stale[:30]:
            print(f"- {item}")
        if len(stale) > 30:
            print(f"- ... {len(stale) - 30} more")
        return 1

    print("Reading cards and repository statistics are up to date.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update FLOW reading cards and repository statistics.")
    parser.add_argument("--check", action="store_true", help="Only verify generated reading metrics.")
    args = parser.parse_args()

    if args.check:
        return run_check()

    run_update()
    return 0


if __name__ == "__main__":
    sys.exit(main())
