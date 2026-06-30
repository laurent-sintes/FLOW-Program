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
    "c-log-oms-workflow-nominal.svg": IMAGES / "c-log-oms-workflow-nominal.svg",
    "c-log-oms-workflow-crossdock.svg": IMAGES / "c-log-oms-workflow-crossdock.svg",
    "c-log-oms-workflow-equilibrage-stock.svg": IMAGES / "c-log-oms-workflow-equilibrage-stock.svg",
    "methodologie-flow-overview.svg": IMAGES / "methodologie-flow-overview.svg",
    "panorama-brd-ecosystem.svg": IMAGES / "panorama-brd-ecosystem.svg",
    "panorama-gbm-ecosystem.svg": IMAGES / "panorama-gbm-ecosystem.svg",
    "pattern-api-conversationnelle.svg": IMAGES / "pattern-api-conversationnelle.svg",
    "pattern-operational-datahub.svg": IMAGES / "pattern-operational-datahub.svg",
    "produit-socle-case-management.svg": IMAGES / "produit-socle-case-management.svg",
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
        "Cartographie claire des six produits candidats de la plateforme FLOW, avec Case Management au cœur, services partagés et projections opérationnelles.",
    )

    svg_lines.extend(
        [
            text_element("title", 52, 58, "Overview de la plateforme FLOW"),
            text_element("subtitle", 52, 86, "Une plateforme Demand centrée sur les Cases, enrichie par des services partagés et projections opérationnelles."),
            "",
            rect("panel", 48, 122, 1184, panel_height, 24),
            text_element("h", 82, 160, "Produits fonctionnels candidats"),
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
        ("0", "Comprendre", ["Panorama existant", "irritants", "tensions"], ["Faits qualifiés", "et insights"], "blue"),
        ("1", "Vision", ["Ambition commune", "problème à résoudre", "cible narrative"], ["Intention cible", "et promesse"], "purple"),
        ("2", "Principes", ["Règles de conception", "arbitrages", "garde-fous"], ["Critères de décision", "réutilisables"], "purple"),
        ("3", "Urbaniser", ["Domaines", "responsabilités", "frontières"], ["Carte des domaines", "et responsabilités"], "green"),
        ("4", "Capacités", ["Ce que l'entreprise", "doit savoir faire", "durablement"], ["Catalogue", "de capacités"], "green"),
        ("5-6", "Produits & solutions", ["Gouvernance", "fonctionnalités", "solutions"], ["Produits, backlog", "et solutions"], "dark"),
    ]
    width = 1500
    height = 800
    lines = svg_start(
        width,
        height,
        "Méthodologie Projet FLOW",
        "Vue d'ensemble des étapes de la méthodologie FLOW, de l'existant à la solution.",
    )
    lines.extend(
        [
            text_element("title", 750, 70, "Méthodologie Projet FLOW", "middle"),
            text_element("subtitle", 750, 100, "Transformer les observations terrain en architecture cible, produits et solutions.", "middle"),
            rect("panel", 42, 128, 1416, 610, 24),
            rect("panelSoft", 92, 160, 1316, 78, 18),
            text_element("h", 750, 192, "Chaque étape produit un livrable qui devient l'entrée de l'étape suivante", "middle"),
        ]
    )
    lines.extend(wrapped_text("Existant → Vision → Principes → Urbanisme → Capacités → Produits → Fonctionnalités → Solutions", "small", 750, 218, 1180, 13, 18, anchor="middle"))

    card_width = 190
    gap = 34
    x0 = 92
    card_y = 292
    card_height = 185
    for index, (num, title, body, output, style) in enumerate(steps):
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

        out_y = 532
        lines.append(text_element("label", x + card_width // 2, out_y, "Sortie", "middle"))
        for line_index, item in enumerate(output):
            lines.extend(wrapped_text(item, "small", x + card_width // 2, out_y + 26 + (line_index * 20), card_width - 18, 13, 18, anchor="middle"))

    lines.extend(
        [
            rect("panelSoft", 205, 645, 1090, 72, 18),
            text_element("h", 750, 675, "Chaîne logique cible", "middle"),
        ]
    )
    lines.extend(wrapped_text("Domaine → Responsabilité → Capacité → Produit → Fonctionnalités → Solutions", "small", 750, 700, 980, 13, 18, anchor="middle"))
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


def render_all() -> dict[str, str]:
    return {
        "architecture-cible-flow-overview.svg": render_overview_svg(),
        "architecture-cible-flow-ecosysteme-brd.svg": render_architecture_brd_svg(),
        "c-log-oms-workflow-nominal.svg": render_c_log_nominal_workflow_svg(),
        "c-log-oms-workflow-crossdock.svg": render_c_log_crossdock_workflow_svg(),
        "c-log-oms-workflow-equilibrage-stock.svg": render_c_log_stock_balancing_workflow_svg(),
        "methodologie-flow-overview.svg": render_methodology_svg(),
        "panorama-brd-ecosystem.svg": render_panorama_brd_svg(),
        "panorama-gbm-ecosystem.svg": render_panorama_gbm_svg(),
        "pattern-api-conversationnelle.svg": render_pattern_api_svg(),
        "pattern-operational-datahub.svg": render_pattern_operational_datahub_svg(),
        "produit-socle-case-management.svg": render_product_case_management_svg(),
    }


def write_diagrams() -> None:
    for name, content in render_all().items():
        GENERATED_DIAGRAMS[name].write_text(content, encoding="utf-8", newline="\n")


def check_diagrams() -> int:
    expected_by_name = render_all()
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
