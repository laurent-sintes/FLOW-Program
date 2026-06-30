# Référentiel des schémas

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Mainteneur, Contributeur, Codex</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>7 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page sert de dictionnaire d'impact pour les schémas SVG du référentiel FLOW.

Un schéma n'est pas seulement une illustration. Il porte souvent une partie du vocabulaire, du modèle mental ou de l'architecture cible. Lorsqu'un concept, un domaine, un produit ou une page source évolue, ce registre permet de savoir quels SVG relire ou régénérer.

## Règle de maintenance

- Tout fichier SVG dans `docs/assets/images/` doit avoir une ligne dans ce registre et être généré par `scripts/generate_svg_diagrams.py`.
- Les PNG d'atelier, captures ou images sources peuvent rester statiques lorsqu'ils documentent une source externe. Ils ne relèvent pas du générateur SVG.
- Toute page Markdown qui affiche un SVG doit être citée dans la colonne `Affiché dans`.
- La colonne `Dépendances à surveiller` indique les pages ou concepts qui peuvent rendre le schéma obsolète.
- Le contenu XML du SVG reste utile pour repérer du texte, mais il ne suffit pas à mesurer les impacts : certaines dépendances sont implicites ou conceptuelles.
- Les SVG doivent être modifiés depuis leur générateur, puis régénérés.
- Tous les SVG doivent rester agrandissables ou diminuables pour export Word / PowerPoint : `viewBox` obligatoire, `preserveAspectRatio="xMidYMid meet"`, contenu vectoriel, pas d'image bitmap embarquée, pas de `foreignObject`.
- Après ajout, renommage ou modification d'un SVG, relancer `.\scripts\check-site.ps1`.

Pour les schémas pilotés par script :

```powershell
.\scripts\generate-svg-diagrams.ps1
```

Cette commande reconstruit tous les SVG du référentiel avec un calcul déterministe des retours à la ligne et de la hauteur des blocs. Le contrôle `.\scripts\check-site.ps1` signale ensuite si un SVG n'est plus à jour ou si un nouveau SVG a été ajouté hors générateur.

Le générateur actuel ne dépend d'aucune librairie Python externe. Il utilise uniquement la bibliothèque standard Python (`argparse`, `dataclasses`, `html`, `pathlib`) afin de rester portable dans Codex, en local Windows et dans GitHub Actions.

Schémas actuellement pilotés par `scripts/generate_svg_diagrams.py` :

- `architecture-cible-flow-overview.svg`
- `architecture-cible-flow-ecosysteme-brd.svg`
- `architecture-cible-flow-ecosysteme-gbm.svg`
- `chronologie-engagement-supply-flow.svg`
- `c-log-oms-workflow-nominal.svg`
- `c-log-oms-workflow-crossdock.svg`
- `c-log-oms-workflow-equilibrage-stock.svg`
- `flux-produits-fonctionnalites-flow.svg`
- `methodologie-flow-overview.svg`
- `modele-demand-notions-flow.svg`
- `modele-mental-connaissances-flow.svg`
- `panorama-brd-ecosystem.svg`
- `panorama-gbm-ecosystem.svg`
- `pattern-api-conversationnelle.svg`
- `pattern-case-centric-orchestration.svg`
- `pattern-cqrs-projections.svg`
- `pattern-event-driven-architecture.svg`
- `pattern-event-sourcing-ledger.svg`
- `pattern-externalisation-decisions.svg`
- `pattern-operational-datahub.svg`
- `pattern-plateforme-ouverte-gouvernee.svg`
- `positionnement-flow-4-domaines.svg`
- `produit-socle-case-management.svg`
- `produit-stock-unifie.svg`

## Style visuel cible

Les schémas d'architecture et les fiches produits doivent rester cohérents avec les derniers SVG produits, notamment `produit-socle-case-management.svg` et `produit-stock-unifie.svg`.

Style à privilégier :

- fond général clair `#f8fbfa` avec coins arrondis ;
- panneaux blancs avec bordure vert pâle `#c7e4de` ;
- cœur ou capacité centrale en vert FLOW `#236159`, avec bordure `#0b3954` ;
- accent ocre `#e09238` sur les décisions, contrats, alertes ou éléments différenciants ;
- texte en Aptos, Calibri ou Segoe UI ;
- titres en vert FLOW, textes en gris bleu lisible ;
- éviter les grands fonds noirs ou bleu nuit pour les schémas d'architecture et de produits, sauf besoin ponctuel fortement justifié.

Les schémas plus anciens peuvent rester en l'état lorsqu'ils sont cohérents dans leur famille, mais toute modification substantielle doit tendre vers cette charte.

## Registre

| Schéma | Affiché dans | Dépendances à surveiller |
| --- | --- | --- |
| `architecture-cible-flow-ecosysteme-brd.svg` | `docs/architecture-cible/flow-dans-ecosysteme-brd.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; écosystème BRD, panorama BRD, frontières FLOW / SRM / PLM / SAP / CBS, hotspot fournisseur / usine / Agreement |
| `architecture-cible-flow-ecosysteme-gbm.svg` | `docs/architecture-cible/flow-dans-ecosysteme-gbm.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; écosystème GBM, panorama GBM, frontières FLOW / SAP / StoreLand / Socloz / NewStore / CBS |
| `architecture-cible-flow-overview.svg` | `docs/architecture-cible/overview-plateforme-flow.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; overview de la plateforme FLOW, six produits à instruire, domaines Engagement / Demand / Fulfillment / Supply, pratiques transverses de gouvernance des données |
| `c-log-oms-workflow-nominal.svg` | `docs/contexte/panorama-oms-c-log.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; atelier C-LOG du 30 juin 2026, cas nominal, ERP, OMS, WMS, TMS Aval, orchestration et mise à jour commande |
| `c-log-oms-workflow-crossdock.svg` | `docs/contexte/panorama-oms-c-log.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; atelier C-LOG du 30 juin 2026, OMS Crossroad, crossdock, commande maître, sous-commandes, WMS 1 / WMS 2, TMS Aval |
| `c-log-oms-workflow-equilibrage-stock.svg` | `docs/contexte/panorama-oms-c-log.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; atelier C-LOG du 30 juin 2026, stock optimal, transfert intersite, réception intersite, IRMA, Dataiku, WMS et TMS Aval |
| `chronologie-engagement-supply-flow.svg` | `docs/architecture-cible/overview-plateforme-flow.md`, `docs/vision/modele-fonctionnement-flow.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; chronologie Engagement vers FLOW vers Supply, promesse, décision, plan d'exécution, remontées d'information |
| `flux-produits-fonctionnalites-flow.svg` | `docs/architecture-cible/flux-fonctionnels-flow.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; produits FLOW, pratiques transverses, fonctionnalités, Case Management, Stock Unifié, Agreement, règles, événements, vues |
| `methodologie-flow-overview.svg` | `docs/methode/processus-de-cadrage.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; processus de cadrage, passage des observations aux choix de conception, arbitrage Build / Buy, trajectoires RFI / RFP / RFQ ou préparation de plateforme de développement |
| `modele-demand-notions-flow.svg` | `docs/vision/modele-fonctionnement-flow.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; notions Demand, fait, événement, décision, règle, promesse, Case, plan d'exécution |
| `modele-mental-connaissances-flow.svg` | `docs/administration/modele-mental-connaissances.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; source datée, fait observé, insight, vision, principe, concept, domaine, capacité, produit, pattern, hotspot, transformation, administration |
| `panorama-brd-ecosystem.svg` | `docs/contexte/panorama-brd.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; cartographie applicative BRD, PLM, PIM, SAP, SRM, CBS, modèle fournisseur / usine |
| `panorama-gbm-ecosystem.svg` | `docs/contexte/panorama-gbm.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; cartographie applicative GBM, SAP, StoreLand, Socloz, NewStore, CBS, B2B / B2C / retail |
| `pattern-api-conversationnelle.svg` | `docs/architecture-cible/patterns/api-conversationnelle.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Pattern API conversationnelle, demande progressive, contexte, décision, réponse et reprise de conversation |
| `pattern-case-centric-orchestration.svg` | `docs/architecture-cible/patterns/case-centric-orchestration.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Case Management, événement, tâche, décision, document, exception, historique |
| `pattern-cqrs-projections.svg` | `docs/architecture-cible/patterns/cqrs-et-projections.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; CQRS, modèle d'écriture, événements, projections, modèles de lecture, vues 360 |
| `pattern-event-driven-architecture.svg` | `docs/architecture-cible/patterns/event-driven-architecture.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Event-Driven Architecture, producteurs, événements, consommateurs, contrats d'événements |
| `pattern-event-sourcing-ledger.svg` | `docs/architecture-cible/patterns/event-sourcing-ledger.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Event Sourcing, ledger, faits, audit, relecture, projections |
| `pattern-externalisation-decisions.svg` | `docs/architecture-cible/patterns/externalisation-des-decisions.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; décisions métier, règles, policies, paramètres, moteur de règles |
| `pattern-operational-datahub.svg` | `docs/architecture-cible/patterns/operational-datahub.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Operational DataHub, ingestion, normalisation, disponibilité opérationnelle, distribution |
| `pattern-plateforme-ouverte-gouvernee.svg` | `docs/architecture-cible/patterns/plateforme-ouverte-gouvernee.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; plateforme ouverte, gouvernance, contrats, APIs, événements, extensions |
| `positionnement-flow-4-domaines.svg` | `docs/architecture-cible/overview-plateforme-flow.md`, `docs/vision/positionnement-flow.md`, `docs/vision/vision.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Engagement, Demand, Fulfillment, Supply, périmètre FLOW, domaines adhérents, promesse |
| `produit-socle-case-management.svg` | `docs/architecture-cible/produits/socle-case-management.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Socle Case Management, Case, statuts, décisions, événements, documents, exceptions |
| `produit-stock-unifie.svg` | `docs/architecture-cible/produits/stock-unifie.md` | SVG généré par `scripts/generate_svg_diagrams.py` ; Stock Unifié, disponibilité, réservation, ATP, mouvements, qualité et fraîcheur de stock |

## Comment décider de régénérer un SVG ?

Il faut relire ou régénérer un SVG lorsque :

- le nom d'un concept affiché dans le schéma change ;
- un concept structurant est ajouté dans une page dont le schéma dépend ;
- une frontière de domaine ou de produit change ;
- une page qui affiche le schéma change son raisonnement principal ;
- un lecteur pourrait tirer une conclusion fausse en lisant l'image sans relire tout l'article.

À l'inverse, il n'est pas nécessaire de régénérer tous les SVG à chaque ajout de contenu. Le registre sert justement à limiter la revue aux schémas réellement exposés au changement.
