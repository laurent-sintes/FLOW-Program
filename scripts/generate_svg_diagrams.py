from __future__ import annotations

import argparse
import html
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "assets" / "images"


GENERATED_DIAGRAMS = {
    "architecture-cible-flow-overview.svg": IMAGES / "architecture-cible-flow-overview.svg",
    "architecture-cible-flow-ecosysteme-brd.svg": IMAGES / "architecture-cible-flow-ecosysteme-brd.svg",
    "architecture-cible-flow-ecosysteme-gbm.svg": IMAGES / "architecture-cible-flow-ecosysteme-gbm.svg",
    "chronologie-engagement-supply-flow.svg": IMAGES / "chronologie-engagement-supply-flow.svg",
    "c-log-oms-workflow-nominal.svg": IMAGES / "c-log-oms-workflow-nominal.svg",
    "c-log-oms-workflow-crossdock.svg": IMAGES / "c-log-oms-workflow-crossdock.svg",
    "c-log-oms-workflow-equilibrage-stock.svg": IMAGES / "c-log-oms-workflow-equilibrage-stock.svg",
    "flux-produits-fonctionnalites-flow.svg": IMAGES / "flux-produits-fonctionnalites-flow.svg",
    "methodologie-flow-overview.svg": IMAGES / "methodologie-flow-overview.svg",
    "modele-demand-notions-flow.svg": IMAGES / "modele-demand-notions-flow.svg",
    "modele-mental-connaissances-flow.svg": IMAGES / "modele-mental-connaissances-flow.svg",
    "panorama-brd-ecosystem.svg": IMAGES / "panorama-brd-ecosystem.svg",
    "panorama-gbm-ecosystem.svg": IMAGES / "panorama-gbm-ecosystem.svg",
    "pattern-api-conversationnelle.svg": IMAGES / "pattern-api-conversationnelle.svg",
    "pattern-case-centric-orchestration.svg": IMAGES / "pattern-case-centric-orchestration.svg",
    "pattern-cqrs-projections.svg": IMAGES / "pattern-cqrs-projections.svg",
    "pattern-event-driven-architecture.svg": IMAGES / "pattern-event-driven-architecture.svg",
    "pattern-event-sourcing-ledger.svg": IMAGES / "pattern-event-sourcing-ledger.svg",
    "pattern-externalisation-decisions.svg": IMAGES / "pattern-externalisation-decisions.svg",
    "pattern-operational-datahub.svg": IMAGES / "pattern-operational-datahub.svg",
    "pattern-plateforme-ouverte-gouvernee.svg": IMAGES / "pattern-plateforme-ouverte-gouvernee.svg",
    "positionnement-flow-4-domaines.svg": IMAGES / "positionnement-flow-4-domaines.svg",
    "produit-socle-case-management.svg": IMAGES / "produit-socle-case-management.svg",
    "produit-stock-unifie.svg": IMAGES / "produit-stock-unifie.svg",
}


def escape(text: str) -> str:
    return html.escape(text, quote=False)


def estimated_text_width(text: str, font_size: int, bold: bool = False) -> float:
    """Approximate browser text width for deterministic SVG layout decisions."""

    width_units = 0.0
    narrow = set("ijlrtfI.,:;!'|·")
    wide = set("mwMW@#%&Œœ")

    for char in text:
        if char.isspace():
            width_units += 0.32
        elif char in narrow:
            width_units += 0.28
        elif char in wide:
            width_units += 0.78
        elif char.isupper():
            width_units += 0.66
        elif char.isdigit():
            width_units += 0.55
        else:
            width_units += 0.54

    multiplier = 1.04 if bold else 1.0
    return width_units * font_size * multiplier


def split_long_word(word: str, max_width: int, font_size: int, bold: bool) -> list[str]:
    parts: list[str] = []
    current = ""

    for char in word:
        candidate = current + char
        if current and estimated_text_width(candidate, font_size, bold) > max_width:
            parts.append(current)
            current = char
        else:
            current = candidate

    if current:
        parts.append(current)

    return parts


def wrap_text(text: str, max_width: int, font_size: int, bold: bool = False) -> list[str]:
    lines: list[str] = []
    current = ""

    for word in text.split():
        candidates = [word]
        if estimated_text_width(word, font_size, bold) > max_width:
            candidates = split_long_word(word, max_width, font_size, bold)

        for candidate_word in candidates:
            candidate = candidate_word if not current else f"{current} {candidate_word}"
            if not current or estimated_text_width(candidate, font_size, bold) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = candidate_word

    if current:
        lines.append(current)

    return lines


def svg_start(width: int, height: int, title: str, desc: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{escape(title)}</title>',
        f'  <desc id="desc">{escape(desc)}</desc>',
        "  <defs>",
        "    <style>",
        "      .bg{fill:#f8fbfa}.panel{fill:#fff;stroke:#c7e4de;stroke-width:2}.panelSoft{fill:#eaf4f2;stroke:#236159;stroke-width:2}.accent{fill:#fff8f0;stroke:#e09238;stroke-width:2}.amber{fill:#fff8f0;stroke:#e09238;stroke-width:2}.green{fill:#eaf4f2;stroke:#236159;stroke-width:2}.blue{fill:#edf6fb;stroke:#7fb2d4;stroke-width:2}.purple{fill:#f4f0fb;stroke:#a98bd3;stroke-width:2}.grey{fill:#f4f6f8;stroke:#cbd5e1;stroke-width:2}.red{fill:#fff0ef;stroke:#d98b7d;stroke-width:2}.core{fill:#236159;stroke:#0b3954;stroke-width:2}.dark{fill:#0b3954;stroke:#052437;stroke-width:2}.title{font:700 28px Aptos,Calibri,Segoe UI,sans-serif;fill:#236159}.subtitle{font:600 16px Aptos,Calibri,Segoe UI,sans-serif;fill:#5b6b78}.h{font:700 18px Aptos,Calibri,Segoe UI,sans-serif;fill:#0b3954}.hWhite{font:700 18px Aptos,Calibri,Segoe UI,sans-serif;fill:#fff}.txt{font:500 15px Aptos,Calibri,Segoe UI,sans-serif;fill:#1e293b}.small{font:500 13px Aptos,Calibri,Segoe UI,sans-serif;fill:#5b6b78}.smallWhite{font:500 13px Aptos,Calibri,Segoe UI,sans-serif;fill:#eaf4f2}.pill{fill:#eaf4f2;stroke:#c7e4de;stroke-width:1.5}.pillAccent{fill:#fff8f0;stroke:#e09238;stroke-width:1.5}.pillText{font:700 12px Aptos,Calibri,Segoe UI,sans-serif;fill:#0b3954}.pillAccentText{font:700 12px Aptos,Calibri,Segoe UI,sans-serif;fill:#8a4f0f}.arrow{stroke:#236159;stroke-width:2.5;fill:none;marker-end:url(#arrow)}.arrowAccent{stroke:#e09238;stroke-width:2.5;fill:none;marker-end:url(#arrowAccent)}.arrowSoft{stroke:#8aa7a1;stroke-width:2;fill:none;stroke-dasharray:6 6;marker-end:url(#arrow)}.dash{stroke-dasharray:6 6}.label{font:700 12px Aptos,Calibri,Segoe UI,sans-serif;fill:#236159}.labelAccent{font:700 12px Aptos,Calibri,Segoe UI,sans-serif;fill:#8a4f0f}.num{font:800 20px Aptos,Calibri,Segoe UI,sans-serif;fill:#e09238}",
        "    </style>",
        '    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#236159"/></marker>',
        '    <marker id="arrowAccent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e09238"/></marker>',
        "  </defs>",
        "",
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}" rx="24"/>',
    ]


def text_element(css_class: str, x: int, y: int, text: str, anchor: str | None = None) -> str:
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    return f'  <text class="{css_class}" x="{x}" y="{y}"{anchor_attr}>{escape(text)}</text>'


def text_lines(
    lines: list[str],
    css_class: str,
    x: int,
    first_y: int,
    line_height: int,
    anchor: str | None = None,
) -> list[str]:
    return [
        text_element(css_class, x, first_y + index * line_height, line, anchor)
        for index, line in enumerate(lines)
    ]


def wrapped_text(
    text: str,
    css_class: str,
    x: int,
    y: int,
    width: int,
    font_size: int,
    line_height: int,
    bold: bool = False,
    anchor: str | None = None,
) -> list[str]:
    return text_lines(wrap_text(text, width, font_size, bold), css_class, x, y, line_height, anchor)


def rect(css_class: str, x: int, y: int, width: int, height: int, rx: int = 18) -> str:
    return f'  <rect class="{css_class}" x="{x}" y="{y}" width="{width}" height="{height}" rx="{rx}"/>'


def circle(css_class: str, x: int, y: int, radius: int) -> str:
    return f'  <circle class="{css_class}" cx="{x}" cy="{y}" r="{radius}"/>'


def badge_width(label: str, minimum: int, font_size: int = 12) -> int:
    return max(minimum, int(estimated_text_width(label, font_size, bold=True) + 48))


def centered_text_x(rect_x: int, rect_width: int, label: str, font_size: int = 12) -> int:
    label_width = estimated_text_width(label, font_size, bold=True)
    return int(rect_x + ((rect_width - label_width) / 2))


@dataclass
class ProductCard:
    x: int
    y: int
    width: int
    badge: str
    badge_width: int
    title: str
    body: str
    title_lines: list[str] = field(default_factory=list)
    body_lines: list[str] = field(default_factory=list)

    def prepare(self) -> None:
        text_width = self.width - 96
        self.title_lines = wrap_text(self.title, text_width, 18, bold=True)
        self.body_lines = wrap_text(self.body, text_width, 15)

    def required_height(self) -> int:
        title_line_height = 22
        body_line_height = 24
        title_baseline = 86
        body_baseline = title_baseline + ((len(self.title_lines) - 1) * title_line_height) + 30
        last_body_baseline = body_baseline + ((len(self.body_lines) - 1) * body_line_height)
        return max(168, last_body_baseline + 28)


@dataclass
class Card:
    x: int
    y: int
    width: int
    title: str
    body: list[str]
    css_class: str = "panel"
    min_height: int = 120
    title_class: str = "h"
    body_class: str = "small"
    padding: int = 24

    def title_lines(self) -> list[str]:
        return wrap_text(self.title, self.width - (self.padding * 2), 18, bold=True)

    def body_lines(self) -> list[str]:
        lines: list[str] = []
        for item in self.body:
            lines.extend(wrap_text(item, self.width - (self.padding * 2), 13))
        return lines

    def required_height(self) -> int:
        return max(self.min_height, self.padding + len(self.title_lines()) * 24 + 10 + len(self.body_lines()) * 20 + self.padding)


def render_product_card(card: ProductCard, height: int) -> list[str]:
    card.prepare()
    title_y = card.y + 86
    title_line_height = 22
    body_y = title_y + ((len(card.title_lines) - 1) * title_line_height) + 30
    actual_badge_width = badge_width(card.badge, card.badge_width)
    actual_badge_x = card.x + 30

    lines = [
        rect("panel", card.x, card.y, card.width, height),
        f'  <rect class="pill" x="{actual_badge_x}" y="{card.y + 24}" width="{actual_badge_width}" height="28" rx="14"/>',
        text_element("pillText", centered_text_x(actual_badge_x, actual_badge_width, card.badge), card.y + 43, card.badge),
    ]
    lines.extend(text_lines(card.title_lines, "h", card.x + 30, title_y, title_line_height))
    lines.extend(text_lines(card.body_lines, "txt", card.x + 30, body_y, 24))
    return lines


def render_card(card: Card, height: int | None = None) -> list[str]:
    actual_height = height or card.required_height()
    title_lines = card.title_lines()
    body_lines = card.body_lines()
    title_y = card.y + card.padding + 16
    body_y = title_y + len(title_lines) * 24 + 8
    lines = [rect(card.css_class, card.x, card.y, card.width, actual_height)]
    lines.extend(text_lines(title_lines, card.title_class, card.x + card.padding, title_y, 24))
    lines.extend(text_lines(body_lines, card.body_class, card.x + card.padding, body_y, 20))
    return lines


def render_chip(x: int, y: int, label: str, css_class: str = "pill", min_width: int = 95) -> list[str]:
    width = badge_width(label, min_width, font_size=12)
    return [
        f'  <rect class="{css_class}" x="{x}" y="{y}" width="{width}" height="30" rx="15"/>',
        text_element("pillText", centered_text_x(x, width, label), y + 20, label),
    ]


def arrow(path: str, css_class: str = "arrow") -> str:
    return f'  <path class="{css_class}" d="{path}"/>'


def connector(points: list[tuple[int, int]], css_class: str = "arrow") -> str:
    if not points:
        raise ValueError("connector requires at least one point")

    commands = [f"M{points[0][0]} {points[0][1]}"]
    commands.extend(f"L{x} {y}" for x, y in points[1:])
    return arrow(" ".join(commands), css_class)


def render_step_box(x: int, y: int, width: int, height: int, label: str) -> list[str]:
    lines = [
        f'  <rect class="panel" x="{x}" y="{y}" width="{width}" height="{height}" rx="8"/>',
    ]
    wrapped = wrap_text(label, width - 24, 13, bold=True)
    line_height = 17
    first_y = int(y + (height / 2) - (((len(wrapped) - 1) * line_height) / 2) + 5)
    lines.extend(text_lines(wrapped, "small", int(x + width / 2), first_y, line_height, anchor="middle"))
    return lines


def render_workflow_lane(label: str, css_class: str, y: int, height: int, width: int) -> list[str]:
    return [
        f'  <rect class="{css_class}" x="52" y="{y}" width="{width - 104}" height="{height}" rx="8"/>',
        text_element("h", 72, y + 34, label),
    ]


def render_workflow_title(title: str, subtitle: str, width: int) -> list[str]:
    return [
        text_element("title", 52, 58, title),
        text_element("subtitle", 52, 86, subtitle),
        f'  <line x1="52" y1="104" x2="{width - 52}" y2="104" stroke="#e09238" stroke-width="2"/>',
    ]


def render_overview_svg() -> str:
    product_cards = [
        ProductCard(
            x=82,
            y=420,
            width=340,
            badge="PROJECTION",
            badge_width=100,
            title="Product Agreement Catalog",
            body="Projection produit / agreements pour décider vite, sans couplage PLM ou PIM.",
        ),
        ProductCard(
            x=470,
            y=420,
            width=340,
            badge="PROJECTION",
            badge_width=100,
            title="Vues 360",
            body="Contextes client, fournisseur, Case et signaux transverses pour décider et expliquer.",
        ),
        ProductCard(
            x=858,
            y=420,
            width=340,
            badge="SERVICE SUPPLY",
            badge_width=142,
            title="Supply Service Registry",
            body="APIs, SLA, engagements de service et contraintes Supply mobilisables.",
        ),
    ]

    for card in product_cards:
        card.prepare()

    product_row_height = max(card.required_height() for card in product_cards)
    message_y = 420 + product_row_height + 50
    message_height = 86
    panel_height = (message_y + message_height + 36) - 122
    canvas_height = 122 + panel_height + 64

    svg_lines = svg_start(
        1280,
        canvas_height,
        "Overview de la plateforme FLOW",
        "Cartographie claire des six produits à instruire de la plateforme FLOW, avec Case Management au cœur, services partagés et projections opérationnelles.",
    )

    svg_lines.extend(
        [
            text_element("title", 52, 58, "Overview de la plateforme FLOW"),
            text_element("subtitle", 52, 86, "Une plateforme Demand centrée sur les Cases, enrichie par des services partagés et projections opérationnelles."),
            "",
            rect("panel", 48, 122, 1184, panel_height, 24),
            text_element("h", 82, 160, "Produits fonctionnels à instruire"),
            text_element("small", 82, 184, "Lecture cible : FLOW porte le cœur Demand + Fulfillment et raccorde Engagement, Supply et les domaines spécialisés."),
            "",
            rect("core", 424, 210, 432, 164, 28),
            text_element("hWhite", 502, 250, "Plateforme de Case Management"),
            text_element("smallWhite", 470, 278, "Socle PaaS : Cases, règles, paramétrage"),
            text_element("smallWhite", 492, 302, "promesses, documents et événements métier."),
            '  <rect class="pillAccent" x="520" y="326" width="240" height="30" rx="15"/>',
            text_element("pillAccentText", 542, 346, "CŒUR DEMAND + FULFILLMENT"),
            "",
            rect("panelSoft", 82, 220, 270, 132),
            text_element("h", 112, 256, "Stock Unifié"),
            text_element("txt", 112, 286, "Inventory Visibility,"),
            text_element("txt", 112, 310, "réservations, allocations"),
            text_element("txt", 112, 334, "et commandes d'exécution."),
            "",
            rect("panelSoft", 928, 220, 270, 132),
            text_element("h", 958, 256, "Réseau d'Exécution"),
            text_element("txt", 958, 286, "Configuration des nœuds"),
            text_element("txt", 958, 310, "Supply, capacités, services"),
            text_element("txt", 958, 334, "et contraintes mobilisables."),
            "",
            arrow("M352 286 C382 286 390 286 420 286"),
            text_element("label", 366, 270, "facts"),
            arrow("M856 286 C888 286 894 286 924 286"),
            text_element("label", 872, 270, "ressources"),
            "",
        ]
    )

    for card in product_cards:
        svg_lines.extend(render_product_card(card, product_row_height))
        svg_lines.append("")

    svg_lines.extend(
        [
            arrow("M640 374 C640 402 640 402 640 414", "arrowAccent dash"),
            text_element("labelAccent", 560, 406, "contextes et projections"),
            "",
            rect("panelSoft", 82, message_y, 1116, message_height),
            text_element("h", 112, message_y + 30, "Message clé"),
            text_element("small", 112, message_y + 56, "FLOW n'est pas un ERP bis : c'est une plateforme Demand composée de produits fonctionnels gouvernés."),
            text_element("small", 112, message_y + 78, "Elle expose des capacités communes sans absorber Engagement, Supply ni les domaines spécialisés."),
            "</svg>",
        ]
    )
    return "\n".join(svg_lines) + "\n"


def render_architecture_brd_svg() -> str:
    lines = svg_start(
        1500,
        920,
        "FLOW dans l'écosystème BRD",
        "Schéma de positionnement cible de FLOW dans l'écosystème applicatif BRD.",
    )
    lines.extend(
        [
            text_element("title", 750, 70, "FLOW dans l'écosystème BRD", "middle"),
            text_element("subtitle", 750, 100, "FLOW porte Demand et Fulfillment ; les domaines spécialisés restent autour, raccordés par contrats.", "middle"),
            rect("panel", 42, 132, 1416, 730, 24),
            "",
            rect("core", 500, 238, 500, 342, 30),
            text_element("hWhite", 750, 292, "Plateforme FLOW", "middle"),
            text_element("smallWhite", 750, 322, "Demand · Case Management · cohérence transverse", "middle"),
        ]
    )

    chip_positions = [
        (555, 365, "Case Management"),
        (765, 365, "Stock unifié"),
        (555, 420, "Réseau d'exécution"),
        (765, 420, "Supply Services"),
        (555, 475, "Product Agreement"),
        (765, 475, "Vues 360"),
    ]
    for x, y, label in chip_positions:
        lines.extend(render_chip(x, y, label, min_width=175))
    lines.extend(wrapped_text("Instruction, promesse, allocation, orchestration et événements.", "smallWhite", 750, 545, 390, 13, 19, anchor="middle"))

    cards = [
        Card(78, 165, 270, "Engagement / canaux", ["Intention, commerce, retail et publication.", "Canaux digitaux : Salesforce Commerce Cloud, Elastic, CMS / Web Platform.", "Retail : Cegid Y2, back-office store, stock magasin."], "blue", 190),
        Card(78, 405, 270, "Produit / offre / planning", ["PLM Centric, PIM, DAM.", "Assortiments, contenus, prix.", "Planning : BPC / EPM, Optimate / APS."], "purple", 210),
        Card(1152, 170, 270, "Supply", ["Logistique et entrepôts : Maersk 4PL, C-Logistics, Bleckmann UK, WMS.", "Transport / douanes : TMS Connex, statuts et événements."], "green", 220),
        Card(1152, 442, 270, "Finance", ["SAP FI/CO, comptabilité, contrôle, fiscalité et écritures financières.", "Domaine séparé de Demand, Fulfillment et Supply."], "red", 170),
        Card(500, 655, 500, "Sourcing / fournisseurs", ["SNC, Fast, Vendor, Purchase Request, Planned Request.", "Contributeurs du contexte amont, sans être nécessairement absorbés par FLOW."], "grey", 145),
    ]
    for card in cards:
        lines.extend(render_card(card))
        lines.append("")

    lines.extend(
        [
            arrow("M348 260 C410 260 432 308 500 336", "arrowSoft"),
            arrow("M348 500 C420 486 438 454 500 432", "arrowSoft"),
            arrow("M1000 350 C1060 312 1095 274 1152 260", "arrow"),
            arrow("M1000 458 C1068 490 1095 520 1152 535", "arrow"),
            arrow("M750 580 L750 655", "arrowAccent"),
            rect("panelSoft", 142, 828, 1216, 58, 16),
        ]
    )
    lines.extend(wrapped_text("SAP et NewStore ne sont pas représentés comme satellites : ils sont dans la trajectoire de retrait / remplacement, avec découpage par responsabilité.", "small", 750, 858, 1100, 13, 18, anchor="middle"))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_methodology_svg() -> str:
    steps = [
        ("0", "Comprendre", ["Panorama", "irritants", "tensions"], "blue"),
        ("1", "Vision", ["Ambition", "problème", "cible narrative"], "purple"),
        ("2", "Principes", ["Règles", "arbitrages", "garde-fous"], "purple"),
        ("3", "Urbaniser", ["Domaines", "responsabilités", "frontières"], "green"),
        ("4", "Capacités", ["Savoir-faire", "durables", "consommateurs"], "green"),
        ("5", "Produits", ["Gouvernance", "owners", "backlog"], "green"),
        ("6", "Solutions", ["Fonctionnalités", "interfaces", "exigences"], "dark"),
    ]
    width = 1500
    height = 900
    lines = svg_start(
        width,
        height,
        "Processus de cadrage FLOW",
        "Vue d'ensemble des étapes du cadrage FLOW, de l'existant à l'arbitrage Build / Buy.",
    )
    lines.extend(
        [
            text_element("title", 750, 70, "Processus de cadrage FLOW", "middle"),
            text_element("subtitle", 750, 100, "Transformer les observations terrain en architecture cible, produits, solutions et trajectoire avant delivery.", "middle"),
            rect("panel", 42, 128, 1416, 730, 24),
            rect("panelSoft", 92, 160, 1316, 78, 18),
            text_element("h", 750, 192, "Chaque étape produit un livrable qui devient l'entrée de l'étape suivante", "middle"),
        ]
    )
    lines.extend(wrapped_text("Existant → Vision → Principes → Urbanisme → Capacités → Produits → Options de solution → Build / Buy", "small", 750, 218, 1180, 13, 18, anchor="middle"))

    card_width = 176
    gap = 22
    x0 = 68
    card_y = 286
    card_height = 168
    for index, (num, title, body, style) in enumerate(steps):
        x = x0 + index * (card_width + gap)
        cls = "dark" if style == "dark" else style
        lines.append(rect(cls, x, card_y, card_width, card_height, 18))
        number_class = "hWhite" if style == "dark" else "num"
        title_class = "hWhite" if style == "dark" else "h"
        body_class = "smallWhite" if style == "dark" else "small"
        lines.append(text_element(number_class, x + 24, card_y + 36, num))
        lines.extend(wrapped_text(title, title_class, x + 24, card_y + 68, card_width - 48, 18, 22, bold=True))
        body_y = card_y + 104
        for item in body:
            lines.extend(wrapped_text(item, body_class, x + 24, body_y, card_width - 48, 13, 18))
            body_y += 20
        if index < len(steps) - 1:
            lines.append(arrow(f"M{x + card_width + 5} {card_y + 88} L{x + card_width + gap - 8} {card_y + 88}", "arrowAccent"))

    solution_x = x0 + (len(steps) - 1) * (card_width + gap)
    solution_center_x = solution_x + card_width // 2
    decision_x = 570
    decision_y = 540
    decision_width = 360
    decision_height = 120
    decision_center_x = decision_x + decision_width // 2
    lines.append(arrow(f"M{solution_center_x} {card_y + card_height + 8} C{solution_center_x} 510 {decision_center_x} 500 {decision_center_x} {decision_y - 10}", "arrowAccent"))
    lines.append(rect("dark", decision_x, decision_y, decision_width, decision_height, 18))
    lines.append(text_element("hWhite", decision_x + 24, decision_y + 34, "7  Arbitrer Build / Buy"))
    lines.extend(wrapped_text("Acheter, construire ou hybrider selon la couverture, les risques, les coûts complets et la gouvernance attendue.", "smallWhite", decision_x + 24, decision_y + 66, decision_width - 48, 13, 18))

    buy_x = 130
    build_x = 800
    branch_y = 724
    branch_width = 570
    branch_height = 98
    lines.append(arrow(f"M{decision_center_x - 70} {decision_y + decision_height + 8} C600 690 430 694 {buy_x + branch_width // 2} {branch_y - 8}", "arrowAccent"))
    lines.append(arrow(f"M{decision_center_x + 70} {decision_y + decision_height + 8} C900 690 1060 694 {build_x + branch_width // 2} {branch_y - 8}", "arrow"))

    lines.append(rect("accent", buy_x, branch_y, branch_width, branch_height, 18))
    lines.append(text_element("h", buy_x + 24, branch_y + 33, "Trajectoire Buy"))
    lines.extend(wrapped_text("RFI pour explorer le marché → RFP pour comparer les réponses → RFQ pour chiffrer et contractualiser.", "small", buy_x + 24, branch_y + 62, branch_width - 48, 13, 18))

    lines.append(rect("green", build_x, branch_y, branch_width, branch_height, 18))
    lines.append(text_element("h", build_x + 24, branch_y + 33, "Trajectoire Build"))
    lines.extend(wrapped_text("Préparer la plateforme de développement : environnements, CI/CD, standards, données de test et backlog.", "small", build_x + 24, branch_y + 62, branch_width - 48, 13, 18))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_panorama_brd_svg() -> str:
    lines = svg_start(
        1280,
        820,
        "Synthèse de l'écosystème applicatif BRD",
        "Schéma synthétique des blocs applicatifs BRD et de leurs responsabilités à qualifier pour FLOW.",
    )
    lines.extend(
        [
            text_element("title", 64, 58, "Écosystème applicatif BRD — lecture synthétique"),
            text_element("subtitle", 64, 86, "FLOW remplace SAP et NewStore : la question est de clarifier les responsabilités qui restent, sortent ou deviennent des capacités FLOW."),
        ]
    )
    cards = [
        Card(64, 125, 260, "Sourcing", ["Collaboration fournisseur.", "SNC · Fast."], "green", 120),
        Card(64, 290, 260, "PLM / Planning", ["Produit, planification, prévisions.", "PLM · BPC · Optimate."], "purple", 150),
        Card(64, 500, 260, "Sustainability", ["DTT.", "Sujet transverse à relier aux exigences de données."], "amber", 120),
        Card(382, 220, 270, "Achat / Stock", ["SAP porte le cœur transactionnel actuel : achats, commandes, finance, billing.", "Stock entrepôt."], "green", 205),
        Card(480, 540, 350, "NewStore / OMS", ["Commandes, promesse, allocation et réservation.", "Point clé si NewStore disparaît du paysage cible."], "green", 155),
        Card(735, 125, 270, "E-commerce & B2B", ["Salesforce, Elastic, CMS / Web Platform.", "Canaux et exposition digitale."], "amber", 170),
        Card(735, 340, 270, "Retail / Stores", ["Cegid Y2.", "Back-office stores et stock magasin."], "amber", 145),
        Card(1040, 210, 190, "WMS", ["KTN BE, C-Logistics, Bleckmann UK, FMS FR.", "Exécution logistique."], "grey", 210),
        Card(1040, 470, 190, "Douanes", ["Connex.", "Statuts, documents et événements."], "grey", 120),
    ]
    for card in cards:
        lines.extend(render_card(card))
        lines.append("")
    lines.extend(
        [
            arrow("M324 190 C355 205 365 258 382 306", "arrowSoft"),
            arrow("M324 365 C350 360 362 344 382 330", "arrowSoft"),
            arrow("M652 310 C690 262 708 228 735 210", "arrow"),
            arrow("M652 360 C695 398 708 412 735 420", "arrow"),
            arrow("M550 425 C560 475 585 515 620 540", "arrowAccent"),
            arrow("M830 618 C920 568 980 420 1040 325", "arrow"),
            arrow("M830 650 C920 636 980 548 1040 528", "arrow"),
            rect("panelSoft", 64, 735, 1158, 52, 14),
        ]
    )
    lines.extend(wrapped_text("Lecture FLOW : SAP et NewStore sont dans le périmètre de remplacement initial, mais l'écosystème montre des responsabilités distribuées à qualifier avant de décider ce qui entre réellement dans FLOW.", "small", 84, 765, 1110, 13, 18))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_panorama_gbm_svg() -> str:
    lines = svg_start(
        1400,
        940,
        "Synthèse de l'écosystème applicatif GBM",
        "Vue synthétique du paysage GBM et des responsabilités transverses candidates FLOW.",
    )
    lines.extend(
        [
            text_element("title", 52, 58, "Panorama applicatif GBM — synthèse FLOW"),
            text_element("subtitle", 52, 86, "Un SI historiquement retail, ouvert au e-commerce puis au B2B, avec des responsabilités transverses candidates à FLOW."),
            rect("blue", 50, 125, 1300, 150, 22),
            text_element("h", 75, 160, "Expériences, canaux et engagement client"),
        ]
    )
    for x, y, label in [
        (78, 190, "SFCC"),
        (245, 190, "Mirakl"),
        (412, 190, "Outils magasins"),
        (610, 190, "Marketplace"),
        (805, 190, "Elastic"),
        (960, 190, "Zoho"),
        (1115, 190, "Import / saisie commandes B2B"),
    ]:
        lines.extend(render_chip(x, y, label, "pill", 115))

    cards = [
        Card(50, 315, 825, "Orchestration transverse et cycle de vie", ["UR : cycle de vie B2C, retours, litiges.", "Socloz : omnicanal, stock, promesse.", "OMS C-LOG : fulfillment, scoring, crossdock.", "EAI C-LOG : échanges, transformations et statuts."], "amber", 220),
        Card(50, 580, 825, "Socle retail historique et stock", ["StoreLand par marque, StoreLand Fournitures mutualisé.", "Stocks magasins, dépôts B2C, dépôts canal.", "Module Négoce, moteur réassort, stock virtuel."], "green", 240),
        Card(910, 315, 440, "B2B / wholesale et engagement commercial", ["Zoho CRM, Elastic, Négoce, Product Live.", "Assortiment, achats, catalogue et pilotage commercial."], "purple", 220),
        Card(910, 580, 440, "Exécution, fournisseurs et systèmes spécialisés", ["CBS, dépôts, transport, finance.", "Achats fournisseur, packing list, documents et écritures."], "grey", 240),
    ]
    for card in cards:
        lines.extend(render_card(card))
        lines.append("")

    lines.extend(
        [
            arrow("M210 220 C210 270 220 292 245 315", "arrowSoft"),
            arrow("M510 220 C510 270 490 292 462 315", "arrowSoft"),
            arrow("M1030 220 C1040 270 1070 292 1115 315", "arrowAccent"),
            arrow("M462 535 C462 560 462 565 462 580", "arrow"),
            arrow("M690 535 C760 574 832 618 910 650", "arrow"),
            arrow("M1115 535 C1080 580 1060 602 1030 650", "arrowSoft"),
            rect("core", 370, 850, 660, 54, 18),
        ]
    )
    lines.extend(wrapped_text("Responsabilités candidates FLOW : Demand, Order Lifecycle, Inventory Visibility, Promise, Allocation, Exceptions.", "smallWhite", 700, 882, 590, 13, 18, anchor="middle"))
    lines.append(rect("panelSoft", 1065, 850, 285, 54, 14))
    lines.extend(wrapped_text("Les expériences restent autonomes ; les responsabilités transverses doivent être réconciliées.", "small", 1088, 874, 238, 13, 17))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_api_svg() -> str:
    lines = svg_start(
        1280,
        640,
        "Pattern API conversationnelle",
        "Une API conversationnelle maintient un dialogue corrélé entre un consommateur, un Case et des systèmes contributeurs.",
    )
    lines.extend(
        [
            text_element("title", 54, 58, "API conversationnelle"),
            text_element("subtitle", 54, 84, "Une interaction longue n'est pas un appel unique : c'est un dialogue corrélé, observable et pilotable."),
            rect("panel", 70, 205, 260, 160, 20),
            text_element("h", 108, 250, "Consommateur"),
        ]
    )
    lines.extend(wrapped_text("Canal, domaine ou partenaire. Initie, suit et complète la demande.", "txt", 108, 282, 190, 15, 22))
    lines.extend(
        [
            rect("core", 500, 175, 280, 220, 28),
            text_element("hWhite", 640, 230, "Conversation", "middle"),
        ]
    )
    for y, item in [(265, "correlation id"), (292, "état du dialogue"), (319, "messages / événements"), (346, "timeouts / relances")]:
        lines.extend(wrapped_text(item, "smallWhite", 555, y, 190, 13, 19))

    for card in [
        Card(955, 118, 250, "Case FLOW", ["Porte la demande et son contexte durable."], "panel", 112),
        Card(955, 286, 250, "Services FLOW", ["Stock, rules, network et autres capacités interrogées."], "panel", 112),
        Card(955, 454, 250, "Systèmes tiers", ["WMS, POS, paiement et événements retour."], "panel", 112),
    ]:
        lines.extend(render_card(card))
        lines.append("")

    lines.extend(
        [
            arrow("M330 255 C390 235 430 235 500 250"),
            text_element("small", 352, 228, "request / command"),
            arrow("M500 318 C430 356 392 360 330 330", "arrowAccent dash"),
            text_element("small", 350, 386, "status / callback"),
            arrow("M780 235 C850 205 890 176 955 176"),
            text_element("small", 820, 190, "pilote"),
            arrow("M780 306 C850 326 890 344 955 344"),
            text_element("small", 820, 336, "interroge / réserve"),
            arrow("M955 510 C860 526 805 438 740 395", "arrowAccent dash"),
        ]
    )
    lines.extend(wrapped_text("événements retour", "small", 845, 528, 170, 13, 18, anchor="middle"))
    lines.extend(
        [
            rect("accent", 420, 480, 440, 82, 18),
            text_element("h", 475, 513, "Contrat conversationnel"),
        ]
    )
    lines.extend(wrapped_text("États, messages, SLA, erreurs, reprise et audit.", "txt", 470, 540, 340, 15, 22))
    lines.append(arrow("M640 395 L640 480", "arrowAccent"))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_operational_datahub_svg() -> str:
    lines = svg_start(
        1280,
        640,
        "Pattern Operational DataHub",
        "Transformer des faits distribués en vérité opérationnelle fraîche, gouvernée et consommable.",
    )
    lines.extend(
        [
            text_element("title", 54, 58, "Operational DataHub"),
            text_element("subtitle", 54, 84, "Transformer des faits distribués en vérité opérationnelle fraîche, gouvernée et consommable."),
        ]
    )
    source = Card(70, 150, 235, "Sources", ["POS", "WMS", "C-LOG", "SAP / NewStore", "Partenaires"], "panel", 310)
    usage = Card(975, 150, 235, "Usages", ["API métier", "Décisions", "Vues 360", "Audit", "Monitoring"], "panel", 310)
    lines.extend(render_card(source))
    lines.extend(render_card(usage))
    lines.extend(
        [
            rect("core", 430, 132, 420, 350, 28),
            text_element("hWhite", 640, 178, "Operational DataHub", "middle"),
        ]
    )
    inner_cards = [
        Card(480, 220, 145, "Ledger", ["historique"], "accent", 74),
        Card(655, 220, 145, "Qualité", ["fraîcheur"], "accent", 74),
        Card(480, 335, 145, "Projection", ["lecture"], "accent", 74),
        Card(655, 335, 145, "Confiance", ["source"], "accent", 74),
    ]
    for card in inner_cards:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M305 305 L430 305"),
            text_element("small", 328, 287, "événements / faits"),
            arrow("M850 305 L975 305", "arrowAccent"),
            text_element("small", 872, 287, "produits de données"),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def render_product_case_management_svg() -> str:
    lines = svg_start(
        1280,
        780,
        "Schéma produit — Socle Case Management",
        "Le Case comme unité autonome de décision métier et d'orchestration.",
    )
    lines.extend(
        [
            text_element("title", 52, 58, "Socle Case Management"),
            text_element("subtitle", 52, 86, "Le Case porte la demande, le contexte, les décisions métier et l'histoire ; le workflow n'est qu'un composant d'exécution."),
        ]
    )
    left = Card(50, 130, 270, "Canaux & domaines", ["Engagement client", "SAV / retours", "Achats / fournisseur", "Back-office métier", "Command / Request"], "panel", 220)
    right = Card(960, 130, 270, "Systèmes d'exécution", ["Stock Unifié", "Réseau d'Exécution", "Paiement / finance", "WMS / POS / partenaires", "API / Events"], "panel", 220)
    lines.extend(render_card(left))
    lines.extend(render_card(right))
    lines.extend(
        [
            rect("panelSoft", 430, 118, 420, 260, 24),
            text_element("h", 640, 156, "Case", "middle"),
        ]
    )
    lines.extend(wrapped_text("Unité autonome de décision métier et d'orchestration.", "small", 640, 184, 330, 13, 18, anchor="middle"))
    for x, y, label in [
        (465, 215, "Request"),
        (590, 215, "Goal"),
        (710, 215, "Intent"),
        (465, 260, "State"),
        (590, 260, "Docs"),
        (710, 260, "Views 360"),
    ]:
        lines.extend(render_chip(x, y, label, min_width=105))
    lines.extend(
        [
            rect("accent", 500, 320, 280, 44, 18),
            text_element("h", 640, 349, "Event log + décisions métier", "middle"),
            arrow("M320 240 C365 240 382 240 430 240"),
            text_element("label", 340, 224, "crée / agit"),
            arrow("M850 240 C895 240 915 240 960 240"),
            text_element("label", 872, 224, "délègue"),
            arrow("M960 304 C905 398 770 422 680 380", "arrowAccent"),
            text_element("label", 855, 410, "événements d'exécution", "middle"),
            rect("accent", 392, 414, 496, 54, 16),
        ]
    )
    lines.extend(wrapped_text("Le processus émerge des décisions métier prises sur le Case.", "h", 640, 447, 420, 18, 22, bold=True, anchor="middle"))
    lines.append(arrow("M640 414 C640 394 640 394 640 378", "arrowAccent dash"))

    lines.extend(
        [
            rect("panel", 85, 505, 1110, 210, 22),
            text_element("h", 118, 540, "Boucle opérationnelle du Case"),
            text_element("small", 118, 566, "L'exécution de la demande influence la décision métier et adapte continuellement le plan d'exécution."),
        ]
    )
    loop = [
        ("1", "J'observe"),
        ("2", "Je comprends"),
        ("3", "Je décide"),
        ("4", "Je planifie"),
        ("5", "J'agis"),
        ("6", "J'apprends"),
    ]
    start_x = 145
    y = 620
    for index, (num, label) in enumerate(loop):
        cx = start_x + index * 190
        cls = "accent" if index % 2 == 0 else "panelSoft"
        lines.append(f'  <circle class="{cls}" cx="{cx}" cy="{y}" r="42"/>')
        lines.append(text_element("num", cx - 7, y + 7, num))
        lines.extend(wrapped_text(label, "h", cx, y + 76, 130, 18, 20, bold=True, anchor="middle"))
        if index < len(loop) - 1:
            lines.append(arrow(f"M{cx + 52} {y} L{cx + 138} {y}"))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_c_log_nominal_workflow_svg() -> str:
    width = 1500
    height = 820
    lines = svg_start(
        width,
        height,
        "OMS C-LOG - workflow nominal",
        "Workflow nominal entre ERP, OMS, WMS et TMS Aval pour une commande orchestrée par l'OMS C-LOG.",
    )
    lines.extend(render_workflow_title("OMS C-LOG - cas nominal", "Création de commande, orchestration, exécution WMS / TMS et remontée de mise à jour.", width))
    lanes = [
        ("ERP", "accent", 130, 105),
        ("OMS", "blue", 270, 115),
        ("WMS", "green", 430, 120),
        ("TMS Aval", "purple", 620, 120),
    ]
    for label, css_class, y, lane_height in lanes:
        lines.extend(render_workflow_lane(label, css_class, y, lane_height, width))

    steps = [
        (500, 152, 150, 54, "Création commande"),
        (980, 152, 150, 54, "Mise à jour commande"),
        (500, 304, 150, 58, "Orchestration"),
        (980, 304, 150, 58, "Mise à jour commande"),
        (250, 465, 150, 58, "Image de stock"),
        (500, 465, 150, 58, "Intégration commande"),
        (700, 465, 190, 58, "Picking packing expédition"),
        (980, 465, 150, 58, "Clôture commande"),
        (250, 655, 150, 58, "Plan de transport"),
        (700, 655, 190, 58, "Picking packing expédition"),
    ]
    for step in steps:
        lines.extend(render_step_box(*step))

    lines.extend(
        [
            connector([(575, 206), (575, 304)]),
            connector([(500, 333), (445, 333), (445, 494), (400, 494)]),
            connector([(400, 494), (500, 494)]),
            connector([(575, 362), (575, 465)]),
            connector([(650, 494), (700, 494)]),
            connector([(890, 494), (980, 494)]),
            connector([(1055, 465), (1055, 362)]),
            connector([(1055, 304), (1055, 206)]),
            connector([(400, 684), (700, 684)]),
            connector([(795, 655), (795, 523)]),
            connector([(400, 684), (445, 684), (445, 333), (500, 333)], "arrowSoft"),
            text_element("label", 452, 318, "stock + transport"),
            text_element("label", 810, 594, "coordination TMS / WMS"),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def render_c_log_crossdock_workflow_svg() -> str:
    width = 1700
    height = 930
    lines = svg_start(
        width,
        height,
        "OMS C-LOG - workflow crossdock",
        "Workflow crossdock avec commande maître, sous-commandes, réception XDO et coordination entre deux entrepôts.",
    )
    lines.extend(render_workflow_title("OMS C-LOG - crossdock", "Une commande à cheval entre deux entrepôts produit des sous-commandes et une consolidation d'exécution.", width))
    lanes = [
        ("ERP", "accent", 125, 105),
        ("OMS", "blue", 260, 115),
        ("WMS 1", "green", 415, 115),
        ("WMS 2", "green", 580, 115),
        ("TMS Aval", "purple", 760, 110),
    ]
    for label, css_class, y, lane_height in lanes:
        lines.extend(render_workflow_lane(label, css_class, y, lane_height, width))

    steps = [
        (110, 148, 150, 58, "Création commande"),
        (1480, 148, 150, 58, "Mise à jour commande"),
        (80, 292, 180, 62, "Orchestration"),
        (430, 292, 150, 62, "Mise à jour commande"),
        (610, 292, 150, 62, "Création réception XDO"),
        (945, 292, 150, 62, "Mise à jour commande"),
        (1125, 292, 160, 62, "Création commande globale"),
        (1480, 292, 150, 62, "Mise à jour commande"),
        (74, 448, 86, 62, "Image de stock"),
        (180, 448, 150, 62, "Intégration commande XDO"),
        (360, 448, 150, 62, "Picking packing expédition"),
        (540, 448, 150, 62, "Clôture commande XDO"),
        (610, 614, 160, 62, "Intégration réception XDO"),
        (790, 614, 150, 62, "Réception XDO"),
        (970, 614, 150, 62, "Clôture réception XDO"),
        (1125, 614, 160, 62, "Intégration commande globale"),
        (1305, 614, 160, 62, "Picking packing expédition"),
        (1480, 614, 150, 62, "Clôture commande"),
        (110, 786, 150, 58, "Plan de transport"),
        (1305, 786, 160, 58, "Picking packing expédition"),
    ]
    for step in steps:
        lines.extend(render_step_box(*step))

    lines.extend(
        [
            connector([(185, 206), (185, 292)]),
            connector([(160, 479), (180, 479)]),
            connector([(185, 354), (185, 448)]),
            connector([(330, 479), (360, 479)]),
            connector([(510, 479), (540, 479)]),
            connector([(615, 448), (615, 354), (505, 354)]),
            connector([(580, 323), (610, 323)]),
            connector([(685, 354), (685, 614)]),
            connector([(770, 645), (790, 645)]),
            connector([(940, 645), (970, 645)]),
            connector([(1045, 614), (1045, 354), (1020, 354)]),
            connector([(1095, 323), (1125, 323)]),
            connector([(1205, 354), (1205, 614)]),
            connector([(1285, 645), (1305, 645)]),
            connector([(1465, 645), (1480, 645)]),
            connector([(1555, 614), (1555, 354)]),
            connector([(1555, 292), (1555, 206)]),
            connector([(260, 815), (1305, 815)]),
            connector([(1385, 786), (1385, 676)]),
            connector([(260, 815), (150, 815), (150, 354), (80, 354)], "arrowSoft"),
            text_element("label", 274, 468, "commande XDO"),
            text_element("label", 802, 630, "réception XDO"),
            text_element("label", 1178, 602, "commande globale"),
            text_element("label", 1398, 735, "coordination TMS / WMS"),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def render_c_log_stock_balancing_workflow_svg() -> str:
    width = 1500
    height = 820
    lines = svg_start(
        width,
        height,
        "OMS C-LOG - workflow équilibrage de stock",
        "Workflow d'équilibrage de stock avec commande de transfert intersite, expédition, réception et clôture.",
    )
    lines.extend(render_workflow_title("OMS C-LOG - équilibrage de stock", "Transfert intersite pour rééquilibrer les stocks entre deux entrepôts.", width))
    lanes = [
        ("OMS", "blue", 125, 110),
        ("WMS 1", "green", 310, 115),
        ("WMS 2", "green", 490, 115),
        ("TMS Aval", "purple", 670, 110),
    ]
    for label, css_class, y, lane_height in lanes:
        lines.extend(render_workflow_lane(label, css_class, y, lane_height, width))

    steps = [
        (230, 150, 180, 62, "Création commande de transfert intersite"),
        (690, 150, 180, 62, "Mise à jour commande transfert intersite"),
        (910, 150, 170, 62, "Création réception transfert intersite"),
        (1310, 150, 150, 62, "Mise à jour commande"),
        (230, 342, 180, 62, "Intégration commande transfert intersite"),
        (460, 342, 180, 62, "Picking packing expédition"),
        (690, 342, 180, 62, "Clôture commande transfert intersite"),
        (910, 522, 170, 62, "Intégration réception transfert intersite"),
        (1130, 522, 150, 62, "Réception transfert intersite"),
        (1310, 522, 150, 62, "Clôture réception transfert intersite"),
        (230, 704, 150, 58, "Plan de transport"),
        (460, 704, 180, 58, "Picking packing expédition"),
    ]
    for step in steps:
        lines.extend(render_step_box(*step))

    lines.extend(
        [
            connector([(320, 212), (320, 342)]),
            connector([(410, 373), (460, 373)]),
            connector([(640, 373), (690, 373)]),
            connector([(780, 342), (780, 212)]),
            connector([(870, 181), (910, 181)]),
            connector([(995, 212), (995, 522)]),
            connector([(1080, 553), (1130, 553)]),
            connector([(1280, 553), (1310, 553)]),
            connector([(1385, 522), (1385, 212)]),
            connector([(380, 733), (460, 733)]),
            connector([(550, 704), (550, 404)]),
            text_element("label", 420, 358, "expédition intersite"),
            text_element("label", 1088, 538, "réception intersite"),
            text_element("label", 566, 640, "coordination transport"),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def render_architecture_gbm_svg() -> str:
    lines = svg_start(
        1500,
        920,
        "FLOW dans l'écosystème GBM",
        "Schéma de positionnement cible de FLOW dans l'écosystème applicatif GBM.",
    )
    lines.extend(
        [
            text_element("title", 750, 70, "FLOW dans l'écosystème GBM", "middle"),
            text_element("subtitle", 750, 100, "FLOW reprend les responsabilités transverses sans remplacer tous les systèmes satellites.", "middle"),
            rect("panel", 42, 132, 1416, 728, 24),
            rect("core", 496, 242, 508, 350, 30),
            text_element("hWhite", 750, 296, "Plateforme FLOW", "middle"),
            text_element("smallWhite", 750, 326, "Demand + Fulfillment à réunifier", "middle"),
        ]
    )
    for x, y, label in [
        (552, 370, "Case Management"),
        (770, 370, "Stock Unifié"),
        (552, 427, "Réseau d'Exécution"),
        (770, 427, "Supply Registry"),
        (552, 484, "Product Agreement"),
        (770, 484, "Vues 360"),
    ]:
        lines.extend(render_chip(x, y, label, min_width=178))
    lines.extend(wrapped_text("Case, stock, réseau, projections et contexte transverse.", "smallWhite", 750, 555, 390, 13, 18, anchor="middle"))

    cards = [
        Card(78, 166, 300, "Engagement / expériences", ["SFCC, Mirakl, Zoho, Elastic, outils magasins.", "Canaux, parcours, CRM, B2B / B2C, marketplace."], "blue", 190),
        Card(78, 420, 300, "Produit / offre / agreements", ["PLM, PIM / catalogue, pricing, assortiments.", "Contexte d'engagement consommé par FLOW."], "purple", 180),
        Card(1120, 160, 300, "Supply", ["C-LOG comme opérateur logistique.", "OMS C-LOG, WMS, TMS / Transware, dépôts et stores."], "green", 235),
        Card(1120, 455, 300, "Finance", ["SAP FI/CO, comptabilité, documents, écritures et contrôles.", "Domaine à raccorder sans l'absorber."], "red", 175),
        Card(492, 675, 516, "Applications retirées ou remplacées", ["StoreLand, Socloz et UR sont traités comme des responsabilités à reprendre, généraliser ou retirer dans la trajectoire cible.", "Le schéma est un positionnement, pas une cartographie de flux."], "grey", 150),
    ]
    for card in cards:
        lines.extend(render_card(card))
        lines.append("")

    lines.extend(
        [
            arrow("M378 260 C430 292 455 320 496 352", "arrowSoft"),
            arrow("M378 510 C430 498 455 478 496 456", "arrowSoft"),
            arrow("M1004 352 C1050 322 1080 285 1120 260", "arrow"),
            arrow("M1004 470 C1060 498 1088 525 1120 545", "arrow"),
            arrow("M750 592 L750 675", "arrowAccent"),
            rect("panelSoft", 142, 826, 1216, 60, 16),
        ]
    )
    lines.extend(wrapped_text("Lecture : FLOW porte la cohérence Demand + Fulfillment ; Engagement, Supply et Finance restent autonomes mais raccordés par contrats, événements et projections.", "small", 750, 858, 1100, 13, 18, anchor="middle"))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_positioning_domains_svg() -> str:
    lines = svg_start(
        1600,
        920,
        "Positionnement de FLOW",
        "FLOW porte le coeur Demand + Fulfillment ; Engagement et Supply sont adhérents et raccordés contractuellement.",
    )
    lines.extend(
        [
            text_element("title", 800, 68, "Positionnement de FLOW", "middle"),
            text_element("subtitle", 800, 98, "Engagement capte l'intention ; FLOW gouverne Demand + Fulfillment ; Supply exécute et remonte les faits.", "middle"),
            rect("panel", 58, 150, 330, 500, 24),
            rect("core", 430, 130, 740, 540, 30),
            rect("panel", 1212, 150, 330, 500, 24),
            text_element("labelAccent", 223, 190, "DOMAINE ADHÉRENT", "middle"),
            text_element("h", 223, 236, "Engagement", "middle"),
            text_element("hWhite", 800, 178, "COEUR FLOW", "middle"),
            text_element("labelAccent", 1377, 190, "DOMAINE ADHÉRENT", "middle"),
            text_element("h", 1377, 236, "Supply", "middle"),
        ]
    )
    engagement = ["Capte l'intention", "Porte les parcours", "Négocie le contexte", "Pilote l'expérience", "CRM · portails · marketplace", "B2B · B2C · SAV · négoce"]
    supply = ["Expose les ressources", "Publie les contraintes", "Exécute physiquement", "Retourne les événements", "stock · entrepôts · magasins", "transport · usines · fournisseurs"]
    lines.extend(text_lines(engagement[:4], "txt", 115, 300, 34))
    lines.extend(text_lines(engagement[4:], "small", 115, 478, 26))
    lines.extend(text_lines(supply[:4], "txt", 1268, 300, 34))
    lines.extend(text_lines(supply[4:], "small", 1268, 478, 26))

    for card in [
        Card(500, 250, 275, "Demand", ["Qualifie la demande.", "Porte le Case.", "Suit les statuts.", "Porte la promesse attendue.", "intention qualifiée · priorité · contexte"], "panelSoft", 295),
        Card(825, 250, 275, "Fulfillment", ["Arbitre la promesse.", "Choisit la trajectoire.", "Alloue et réserve.", "Ouvre les exceptions.", "sourcing · split · priorisation"], "accent", 295),
        Card(150, 725, 390, "Contrats d'entrée", ["APIs, événements, demandes, contexte et engagements utiles à la décision."], "blue", 105),
        Card(605, 725, 390, "Règle de périmètre", ["FLOW ne remplace pas Engagement ni Supply ; il gouverne la cohérence Demand + Fulfillment qui les relie."], "grey", 105),
        Card(1060, 725, 390, "Contrats Supply", ["Disponibilités, SLA, statuts, contraintes, confirmations et exceptions terrain."], "green", 105),
    ]:
        lines.extend(render_card(card))

    lines.extend(
        [
            arrow("M388 400 C420 400 450 397 500 397", "arrow"),
            arrow("M775 397 L825 397", "arrowAccent"),
            arrow("M1100 397 C1145 397 1175 400 1212 400", "arrow"),
            arrow("M800 545 L800 725", "arrowAccent"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_chronology_engagement_supply_svg() -> str:
    lines = svg_start(
        1600,
        1040,
        "Chronologie Engagement vers Supply",
        "La demande progresse avec les faits, événements, contraintes et retours d'exécution.",
    )
    lines.extend(
        [
            text_element("title", 800, 70, "Chronologie Engagement → FLOW → Supply", "middle"),
            text_element("subtitle", 800, 100, "Une demande n'est pas un aller simple : la décision se réévalue avec les faits et retours d'exécution.", "middle"),
            rect("blue", 70, 145, 310, 90, 20),
            rect("core", 430, 145, 740, 90, 20),
            rect("green", 1220, 145, 310, 90, 20),
            text_element("h", 225, 197, "Engagement", "middle"),
            text_element("hWhite", 800, 197, "FLOW : Demand + Fulfillment", "middle"),
            text_element("h", 1375, 197, "Supply", "middle"),
        ]
    )
    steps = [
        ("1", "Capte l'intention", ["parcours", "canal", "contexte"], "blue"),
        ("2", "Crée le Case", ["demande qualifiée", "statut initial"], "panelSoft"),
        ("3", "Enrichit", ["Agreement", "règles", "priorités"], "panelSoft"),
        ("4", "Décide", ["promesse tenable", "allocation", "sourcing"], "accent"),
        ("5", "Exécute", ["prépare", "transporte", "confirme"], "green"),
        ("6", "Remonte", ["faits", "statuts", "events"], "green"),
        ("7", "Actualise", ["Case", "promesse", "exception si besoin"], "panelSoft"),
        ("8", "Informe", ["promesse", "statut", "choix"], "blue"),
    ]
    for index, (num, title, body, css) in enumerate(steps):
        cx = 75 + index * 190
        lines.append(rect(css, cx, 315, 168, 215, 20))
        lines.append(circle("accent", cx + 34, 353, 24))
        lines.append(text_element("num", cx + 34, 361, num, "middle"))
        lines.extend(wrapped_text(title, "h", cx + 114, 360, 96, 18, 22, bold=True, anchor="middle"))
        lines.extend(text_lines(body, "small", cx + 24, 430, 22))
        if index < len(steps) - 1:
            lines.append(arrow(f"M{cx + 168} 423 L{cx + 190} 423", "arrow"))

    lines.extend(
        [
            rect("panelSoft", 130, 640, 350, 90, 18),
            rect("accent", 625, 640, 350, 90, 18),
            rect("panelSoft", 1120, 640, 350, 90, 18),
            text_element("h", 305, 680, "demande", "middle"),
            text_element("small", 305, 708, "intention qualifiée et suivie", "middle"),
            text_element("h", 800, 680, "plan d'exécution", "middle"),
            text_element("small", 800, 708, "sourcing, allocation, promesse", "middle"),
            text_element("h", 1295, 680, "retour d'information", "middle"),
            text_element("small", 1295, 708, "faits, statuts, exceptions", "middle"),
            arrow("M480 685 L625 685", "arrowAccent"),
            arrow("M975 685 L1120 685", "arrow"),
            arrow("M1295 730 C1295 850 305 850 305 730", "arrowSoft"),
            rect("panel", 225, 900, 1150, 70, 18),
        ]
    )
    lines.extend(wrapped_text("La promesse et le statut ne sont pas seulement calculés au départ : ils sont actualisés par les retours d'exécution et les exceptions observées.", "small", 800, 938, 1000, 13, 18, anchor="middle"))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_demand_notions_svg() -> str:
    lines = svg_start(
        1600,
        980,
        "Modèle mental des notions FLOW",
        "Schéma des notions Demand, fait, événement, décision, règle, promesse, Case et plan d'exécution.",
    )
    lines.extend(
        [
            text_element("title", 800, 70, "Modèle mental des notions FLOW", "middle"),
            text_element("subtitle", 800, 100, "Comprendre qui fait quoi dans le traitement d'une demande.", "middle"),
        ]
    )
    for card in [
        Card(70, 170, 290, "ENGAGEMENT", ["Intention", "parcours, canal", "contexte relationnel"], "blue", 170),
        Card(430, 160, 300, "DEMAND", ["Case", "demande qualifiée", "contexte et statut", "promesse attendue", "l'objet qui reste lisible"], "panelSoft", 250),
        Card(790, 150, 330, "FULFILLMENT", ["Décision", "applique les règles", "compare les contraintes", "arbitre la promesse", "explicable et traçable"], "accent", 255),
        Card(1230, 170, 300, "SUPPLY", ["Ressource", "stock, capacité", "SLA, contrainte", "Fait / event", "disponibilité, confirmation, exception terrain"], "green", 265),
        Card(430, 510, 300, "Contexte", ["Agreement, priorité", "client, canal, pays", "contraintes métier"], "panel", 155),
        Card(790, 510, 330, "Règle / policy", ["priorisation", "éligibilité", "fallback ou exception"], "amber", 155),
        Card(455, 760, 300, "Journal du Case", ["faits, événements, décisions, statuts"], "grey", 100),
        Card(845, 760, 300, "Projection consommable", ["vue statut, promesse, disponibilité"], "grey", 100),
    ]:
        lines.extend(render_card(card))
        lines.append("")
    lines.extend(
        [
            rect("core", 620, 690, 360, 70, 18),
            text_element("hWhite", 800, 730, "Promesse + plan", "middle"),
            text_element("smallWhite", 800, 752, "ce qui est décidé, expliqué et suivi", "middle"),
            arrow("M360 255 L430 255", "arrow"),
            arrow("M730 270 L790 270", "arrowAccent"),
            arrow("M1120 275 L1230 275", "arrow"),
            arrow("M1380 435 C1380 620 1000 660 980 690", "arrowSoft"),
            arrow("M945 405 L945 510", "arrowAccent"),
            arrow("M580 410 L580 510", "arrowSoft"),
            arrow("M800 760 L800 690", "arrowAccent"),
            arrow("M620 725 C555 725 560 760 605 760", "arrow"),
            arrow("M980 725 C1050 725 1045 760 995 760", "arrow"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_knowledge_model_svg() -> str:
    lines = svg_start(
        1600,
        980,
        "Modèle mental des connaissances FLOW",
        "Reconnaître une information, la ranger au bon endroit, puis mesurer ses impacts.",
    )
    lines.extend(
        [
            text_element("title", 800, 70, "Modèle mental des connaissances FLOW", "middle"),
            text_element("subtitle", 800, 100, "Reconnaître une information, la ranger au bon endroit, puis mesurer ses impacts dans le référentiel.", "middle"),
        ]
    )
    columns = [
        (70, "1. MATIÈRE ENTRANTE", "blue", [
            ("Réunion datée", ["atelier, transcript, notes", "contexte et périmètre"]),
            ("Faits observés", ["ce qui est dit ou confirmé", "sans sur-interprétation"]),
            ("Insights", ["ce que cela change", "dans la compréhension FLOW"]),
            ("Questions ouvertes", ["hypothèses, risques", "arbitrages à instruire"]),
            ("Questions fréquentes", ["malentendus", "objections terrain"]),
        ]),
        (560, "2. STRUCTURE DE CONNAISSANCE", "panelSoft", [
            ("Vision", ["pourquoi, ambition", "positionnement cible"]),
            ("Principes", ["règles durables", "de conception"]),
            ("Concepts / domaines", ["vocabulaire, glossaire", "frontières stables"]),
            ("Capacités / produits", ["ce qu'il faut savoir faire", "socles et services FLOW"]),
            ("Patterns", ["formes réutilisables", "de solution"]),
        ]),
        (1090, "3. IMPACTS ET GOUVERNANCE", "green", [
            ("FAQ", ["réponses courtes", "pages expertes"]),
            ("Hotspots", ["points sensibles", "à arbitrer"]),
            ("Architecture cible", ["produits, flux", "responsabilités"]),
            ("Transformation", ["changements", "d'usage et posture"]),
            ("Contrôles", ["cartouches, métriques", "liens, rôles, build"]),
        ]),
    ]
    for x, title, css, items in columns:
        lines.append(rect(css, x, 150, 440, 700, 24))
        lines.append(text_element("h", x + 220, 198, title, "middle"))
        y = 240
        for item_title, body in items:
            lines.extend(render_card(Card(x + 35, y, 370, item_title, body, "panel", 94)))
            y += 116
    lines.extend(
        [
            arrow("M510 500 L560 500", "arrow"),
            arrow("M1000 500 L1090 500", "arrow"),
            arrow("M1310 850 C1310 925 270 925 270 850", "arrowSoft"),
            text_element("label", 535, 480, "alimente", "middle"),
            text_element("label", 1045, 480, "structure", "middle"),
            text_element("label", 800, 912, "vérifie et maintient", "middle"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_functional_flows_svg() -> str:
    lines = svg_start(
        1320,
        780,
        "Flux fonctionnels FLOW",
        "Les flux traversent les produits et fonctionnalités FLOW, pas seulement les domaines.",
    )
    lines.extend(
        [
            text_element("title", 660, 58, "Flux fonctionnels FLOW", "middle"),
            text_element("subtitle", 660, 86, "Niveau architecture : les flux traversent les produits et fonctionnalités, pas seulement les domaines.", "middle"),
            rect("blue", 45, 140, 230, 470, 22),
            rect("core", 325, 115, 670, 520, 28),
            rect("green", 1045, 140, 230, 470, 22),
            text_element("h", 160, 185, "ENGAGEMENT", "middle"),
            text_element("hWhite", 660, 160, "COEUR FLOW : DEMAND + FULFILLMENT", "middle"),
            text_element("h", 1160, 185, "SUPPLY", "middle"),
        ]
    )
    lines.extend(text_lines(["Capte l'intention", "Canaux", "Portails", "CRM", "Négoce", "Interfaces partenaires", "API d'entrée"], "small", 92, 235, 32))
    lines.extend(text_lines(["Expose les ressources", "Stocks", "Capacités", "Services", "WMS, TMS, POS", "usines, fournisseurs", "transporteurs"], "small", 1090, 235, 32))
    for card in [
        Card(365, 205, 260, "Socle Case Management", ["Case, statut, journal", "documents, exception"], "panel", 112),
        Card(690, 205, 260, "Product Agreement Catalog", ["Produits, assortiments", "agreements, conditions"], "panel", 112),
        Card(365, 350, 260, "Vues 360", ["Contexte client, fournisseur", "Case et historique transverse"], "panel", 112),
        Card(690, 350, 260, "Règles et policies", ["Éligibilité, priorité", "fallback, arbitrage"], "accent", 112),
        Card(365, 495, 260, "Stock Unifié", ["Disponibilité, réservation", "allocation"], "panel", 112),
        Card(690, 495, 260, "Fulfillment Network", ["Noeuds, capacités", "contraintes, SLA"], "panel", 112),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            rect("amber", 430, 650, 460, 64, 18),
            text_element("h", 660, 675, "Pratique transverse : gouvernance des données en transit", "middle"),
            text_element("small", 660, 700, "Contrats de données, fraîcheur, qualité, supervision, réconciliation", "middle"),
            arrow("M275 375 L325 375", "arrow"),
            arrow("M995 375 L1045 375", "arrow"),
            arrow("M1045 535 C1010 585 935 620 890 660", "arrowSoft"),
            arrow("M325 535 C285 585 235 620 190 610", "arrowSoft"),
            text_element("label", 300, 355, "demande", "middle"),
            text_element("label", 1020, 355, "ressources", "middle"),
            text_element("labelAccent", 1015, 620, "retours d'exécution", "middle"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_product_stock_unifie_svg() -> str:
    lines = svg_start(
        1280,
        760,
        "Stock Unifié",
        "Un Operational DataHub qui transforme des mouvements distribués en disponibilité gouvernée et explicable.",
    )
    lines.extend(
        [
            text_element("title", 640, 58, "Stock Unifié", "middle"),
            text_element("subtitle", 640, 86, "Un Operational DataHub qui transforme des mouvements distribués en disponibilité gouvernée et explicable.", "middle"),
        ]
    )
    for card in [
        Card(60, 145, 260, "Sources opérationnelles", ["POS / magasins", "WMS / entrepôts", "C-LOG / partenaires", "SAP / NewStore", "Retours / inventaires"], "blue", 330),
        Card(405, 145, 470, "Operational DataHub Stock", ["ledger, projections, fraîcheur, confiance, réconciliation"], "core", 160, "hWhite", "smallWhite"),
        Card(960, 145, 260, "Consommateurs", ["Cases FLOW", "Engagement / canaux", "Supply / exécution", "Vues 360", "Finance / contrôle"], "green", 330),
        Card(430, 340, 175, "Ledger", ["mouvements", "auditables"], "panel", 105),
        Card(625, 340, 175, "Projections", ["disponible", "promettable"], "panel", 105),
        Card(430, 480, 175, "Décision", ["réserver", "allouer"], "accent", 105),
        Card(625, 480, 175, "Explain", ["source", "fraîcheur", "confiance"], "panel", 105),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M320 300 L405 300", "arrow"),
            arrow("M875 300 L960 300", "arrow"),
            arrow("M640 305 L640 340", "arrowAccent"),
            rect("panelSoft", 140, 645, 1000, 62, 18),
            text_element("h", 640, 672, "Capacités exposées : Availability · Reserve · Allocate · Release · Explain · Reconcile", "middle"),
            text_element("small", 640, 696, "Le Stock Unifié qualifie ce que l'entreprise peut promettre, à qui, pourquoi et avec quel niveau de confiance.", "middle"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_case_centric_orchestration_svg() -> str:
    lines = svg_start(1280, 620, "Case-centric orchestration", "Le Case porte la demande, le contexte, les décisions et l'histoire.")
    lines.extend(
        [
            text_element("title", 60, 58, "Case-centric orchestration"),
            text_element("subtitle", 60, 86, "Le Case porte la demande, le contexte, les décisions et l'histoire ; le plan s'adapte aux faits observés."),
            rect("core", 470, 210, 340, 180, 28),
            text_element("hWhite", 640, 270, "CASE", "middle"),
            text_element("smallWhite", 640, 302, "unité autonome de décision", "middle"),
            text_element("smallWhite", 640, 328, "et d'orchestration", "middle"),
        ]
    )
    for card in [
        Card(70, 155, 250, "Demande", ["Request · Goal · Intent"], "blue", 100),
        Card(70, 355, 250, "Événements", ["Ce qui s'est passé"], "green", 100),
        Card(930, 150, 270, "Policies / règles", ["guident la décision"], "accent", 100),
        Card(930, 315, 270, "Plan adaptable", ["tâches · attentes · exceptions"], "panel", 105),
        Card(500, 455, 280, "Exécution", ["API · Supply · finance · partenaires"], "grey", 100),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M320 205 L470 265", "arrow"),
            arrow("M320 405 L470 335", "arrow"),
            arrow("M930 200 L810 265", "arrowAccent"),
            arrow("M810 335 L930 365", "arrow"),
            arrow("M640 390 L640 455", "arrow"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_cqrs_projections_svg() -> str:
    lines = svg_start(1280, 620, "CQRS et projections", "Séparer ce qui modifie le système de ce qui est lu par les consommateurs.")
    lines.extend(
        [
            text_element("title", 60, 58, "CQRS et projections"),
            text_element("subtitle", 60, 86, "Séparer ce qui modifie le système de ce qui est lu par les consommateurs."),
        ]
    )
    for card in [
        Card(70, 170, 220, "Command", ["ReserveStock", "CreateCase"], "blue", 140),
        Card(360, 160, 250, "Write model", ["valide l'intention", "produit des événements"], "panelSoft", 160),
        Card(690, 180, 180, "Events", ["faits immuables"], "accent", 130),
        Card(940, 150, 260, "Read models", ["projections spécialisées"], "green", 145),
        Card(940, 370, 260, "Consommateurs", ["API · Vues 360 · UI"], "grey", 120),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M290 235 L360 235", "arrow"),
            arrow("M610 235 L690 235", "arrowAccent"),
            arrow("M870 235 L940 220", "arrow"),
            arrow("M1070 295 L1070 370", "arrow"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_event_driven_architecture_svg() -> str:
    lines = svg_start(1280, 620, "Event-Driven Architecture", "Les systèmes publient des faits métier ; les consommateurs réagissent sans dépendre de flux point à point.")
    lines.extend(
        [
            text_element("title", 60, 58, "Event-Driven Architecture"),
            text_element("subtitle", 60, 86, "Les systèmes publient des faits métier ; les consommateurs réagissent sans dépendre de flux point à point."),
            rect("core", 465, 215, 350, 170, 24),
            text_element("hWhite", 640, 270, "Event Backbone", "middle"),
            text_element("smallWhite", 640, 302, "topics · contrats · rejeu", "middle"),
            text_element("smallWhite", 640, 330, "observabilité · gouvernance", "middle"),
        ]
    )
    for card in [
        Card(70, 150, 230, "POS", ["StockSold"], "panel", 95),
        Card(70, 285, 230, "WMS", ["StockReceived"], "panel", 95),
        Card(70, 420, 230, "Case", ["CaseUpdated"], "panel", 95),
        Card(970, 125, 240, "Stock Unifié", ["projette la disponibilité"], "accent", 85),
        Card(970, 268, 240, "Vues 360", ["agrège la situation"], "accent", 85),
        Card(970, 411, 240, "Décision", ["déclenche règles / actions"], "accent", 85),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M300 198 C365 198 400 250 465 268", "arrow"),
            arrow("M300 333 C365 333 400 315 465 310", "arrow"),
            arrow("M300 468 C365 468 400 365 465 340", "arrow"),
            arrow("M815 270 C880 240 905 168 970 168", "arrowAccent"),
            arrow("M815 305 C880 305 905 310 970 310", "arrowAccent"),
            arrow("M815 340 C880 370 905 454 970 454", "arrowAccent"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_event_sourcing_ledger_svg() -> str:
    lines = svg_start(1280, 620, "Event Sourcing / Ledger", "Conserver l'histoire des événements pour reconstruire, auditer et expliquer l'état courant.")
    lines.extend(
        [
            text_element("title", 60, 58, "Event Sourcing / Ledger"),
            text_element("subtitle", 60, 86, "Conserver l'histoire des événements pour reconstruire, auditer et expliquer l'état courant."),
        ]
    )
    lines.extend(render_card(Card(70, 210, 220, "Action", ["ReserveStock"], "blue", 115)))
    lines.append(rect("core", 390, 145, 430, 330, 26))
    lines.append(text_element("hWhite", 605, 190, "Ledger immuable", "middle"))
    for index, event in enumerate(["+10  Received", "-1  Sold", "-1  Reserved", "+1  Returned"]):
        y = 235 + index * 58
        lines.append(rect("panel", 455, y, 300, 44, 10))
        lines.append(text_element("txt", 605, y + 28, event, "middle"))
    for card in [
        Card(930, 180, 240, "Projection", ["stock disponible"], "accent", 115),
        Card(930, 360, 240, "Audit", ["preuve / explication"], "grey", 115),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M290 268 L390 280", "arrow"),
            arrow("M820 280 L930 238", "arrowAccent"),
            arrow("M820 340 L930 418", "arrow"),
            rect("panelSoft", 240, 520, 800, 54, 16),
            text_element("small", 640, 553, "La vérité courante est reconstruite depuis l'historique.", "middle"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_externalisation_decisions_svg() -> str:
    lines = svg_start(1280, 620, "Externalisation des décisions métier", "Les variations métier sont gouvernées par des policies explicites.")
    lines.extend(
        [
            text_element("title", 60, 58, "Externalisation des décisions métier"),
            text_element("subtitle", 60, 86, "Les variations métier sont gouvernées par des policies et règles explicites, pas codées dans tous les processus."),
        ]
    )
    for card in [
        Card(70, 175, 260, "Contexte", ["Case", "Client", "Stock", "Canal", "SLA"], "blue", 235),
        Card(405, 210, 230, "Facts", ["situation exploitable"], "panelSoft", 125),
        Card(405, 390, 230, "Policies", ["règles / contraintes"], "accent", 125),
        Card(710, 250, 250, "Decision service", ["choix explicable"], "core", 150, "hWhite", "smallWhite"),
        Card(1030, 205, 200, "Action", ["réserver", "allouer", "annuler", "rembourser"], "green", 210),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M330 275 L405 275", "arrow"),
            arrow("M330 360 C360 410 375 430 405 452", "arrowAccent"),
            arrow("M635 275 L710 305", "arrow"),
            arrow("M635 452 C675 420 690 374 710 340", "arrowAccent"),
            arrow("M960 325 L1030 325", "arrow"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_pattern_open_governed_platform_svg() -> str:
    lines = svg_start(1280, 620, "Plateforme ouverte et gouvernée", "Centraliser le commun, ouvrir des capacités contrôlées aux domaines.")
    lines.extend(
        [
            text_element("title", 60, 58, "Plateforme ouverte et gouvernée"),
            text_element("subtitle", 60, 86, "Centraliser le commun, ouvrir des capacités contrôlées aux domaines, éviter le monolithe comme le foisonnement."),
            rect("core", 410, 145, 460, 250, 28),
            text_element("hWhite", 640, 205, "Plateforme FLOW", "middle"),
            text_element("smallWhite", 640, 238, "ressources communes gouvernées", "middle"),
            text_element("smallWhite", 640, 266, "contrats API / événements", "middle"),
            text_element("smallWhite", 640, 294, "standards d'extension", "middle"),
            text_element("smallWhite", 640, 322, "observabilité / sécurité", "middle"),
            text_element("smallWhite", 640, 350, "catalogue de capacités", "middle"),
        ]
    )
    for card in [
        Card(80, 155, 220, "B2C", ["expérience / apps"], "blue", 105),
        Card(80, 350, 220, "B2B", ["domaines consommateurs"], "blue", 105),
        Card(980, 250, 220, "Supply", ["exécution / partenaires"], "green", 115),
        Card(320, 465, 180, "Configurer", ["network · règles"], "accent", 95),
        Card(550, 465, 180, "Développer", ["types de Case"], "accent", 95),
        Card(780, 465, 180, "Consommer", ["API · events · vues"], "accent", 95),
    ]:
        lines.extend(render_card(card))
    lines.extend(
        [
            arrow("M300 207 L410 240", "arrow"),
            arrow("M300 402 L410 330", "arrow"),
            arrow("M870 290 L980 305", "arrow"),
            arrow("M640 395 L640 465", "arrowAccent"),
        ]
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_all() -> dict[str, str]:
    return {
        "architecture-cible-flow-overview.svg": render_overview_svg(),
        "architecture-cible-flow-ecosysteme-brd.svg": render_architecture_brd_svg(),
        "architecture-cible-flow-ecosysteme-gbm.svg": render_architecture_gbm_svg(),
        "chronologie-engagement-supply-flow.svg": render_chronology_engagement_supply_svg(),
        "c-log-oms-workflow-nominal.svg": render_c_log_nominal_workflow_svg(),
        "c-log-oms-workflow-crossdock.svg": render_c_log_crossdock_workflow_svg(),
        "c-log-oms-workflow-equilibrage-stock.svg": render_c_log_stock_balancing_workflow_svg(),
        "flux-produits-fonctionnalites-flow.svg": render_functional_flows_svg(),
        "methodologie-flow-overview.svg": render_methodology_svg(),
        "modele-demand-notions-flow.svg": render_demand_notions_svg(),
        "modele-mental-connaissances-flow.svg": render_knowledge_model_svg(),
        "panorama-brd-ecosystem.svg": render_panorama_brd_svg(),
        "panorama-gbm-ecosystem.svg": render_panorama_gbm_svg(),
        "pattern-api-conversationnelle.svg": render_pattern_api_svg(),
        "pattern-case-centric-orchestration.svg": render_pattern_case_centric_orchestration_svg(),
        "pattern-cqrs-projections.svg": render_pattern_cqrs_projections_svg(),
        "pattern-event-driven-architecture.svg": render_pattern_event_driven_architecture_svg(),
        "pattern-event-sourcing-ledger.svg": render_pattern_event_sourcing_ledger_svg(),
        "pattern-externalisation-decisions.svg": render_pattern_externalisation_decisions_svg(),
        "pattern-operational-datahub.svg": render_pattern_operational_datahub_svg(),
        "pattern-plateforme-ouverte-gouvernee.svg": render_pattern_open_governed_platform_svg(),
        "positionnement-flow-4-domaines.svg": render_positioning_domains_svg(),
        "produit-socle-case-management.svg": render_product_case_management_svg(),
        "produit-stock-unifie.svg": render_product_stock_unifie_svg(),
    }


def write_diagrams() -> None:
    rendered = render_all()
    declared = set(GENERATED_DIAGRAMS)
    missing_declarations = sorted(set(rendered) - declared)
    missing_renderers = sorted(declared - set(rendered))
    if missing_declarations or missing_renderers:
        raise SystemExit(
            "SVG generator registry mismatch: "
            f"missing declarations={missing_declarations}; missing renderers={missing_renderers}"
        )

    for name, content in rendered.items():
        GENERATED_DIAGRAMS[name].write_text(content, encoding="utf-8", newline="\n")


def check_diagrams() -> int:
    expected_by_name = render_all()
    declared = set(GENERATED_DIAGRAMS)
    missing_declarations = sorted(set(expected_by_name) - declared)
    missing_renderers = sorted(declared - set(expected_by_name))
    if missing_declarations or missing_renderers:
        print(
            "SVG generator registry mismatch: "
            f"missing declarations={missing_declarations}; missing renderers={missing_renderers}"
        )
        return 1

    stale: list[str] = []

    for name, expected in expected_by_name.items():
        path = GENERATED_DIAGRAMS[name]
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != expected:
            stale.append(str(path.relative_to(ROOT)))

    if stale:
        for path in stale:
            print(f"{path} is not up to date.")
        print("Run scripts\\generate-svg-diagrams.ps1.")
        return 1

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate FLOW SVG diagrams with deterministic text layout.")
    parser.add_argument("--check", action="store_true", help="Check generated SVG diagrams without writing them.")
    args = parser.parse_args()

    if args.check:
        return check_diagrams()

    write_diagrams()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
