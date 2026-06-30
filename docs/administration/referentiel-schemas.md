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
      <strong>4 min</strong>
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

- Tout fichier SVG dans `docs/assets/images/` doit avoir une ligne dans ce registre.
- Toute page Markdown qui affiche un SVG doit être citée dans la colonne `Affiché dans`.
- La colonne `Dépendances à surveiller` indique les pages ou concepts qui peuvent rendre le schéma obsolète.
- Le contenu XML du SVG reste utile pour repérer du texte, mais il ne suffit pas à mesurer les impacts : certaines dépendances sont implicites ou conceptuelles.
- Après ajout, renommage ou modification d'un SVG, relancer `.\scripts\check-site.ps1`.

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
| `architecture-cible-flow-ecosysteme-brd.svg` | `docs/architecture-cible/flow-dans-ecosysteme-brd.md` | Écosystème BRD, panorama BRD, frontières FLOW / SRM / PLM / SAP / CBS, hotspot fournisseur / usine / Agreement |
| `architecture-cible-flow-ecosysteme-gbm.svg` | `docs/architecture-cible/flow-dans-ecosysteme-gbm.md` | Écosystème GBM, panorama GBM, frontières FLOW / SAP / StoreLand / Socloz / NewStore / CBS |
| `architecture-cible-flow-overview.svg` | `docs/architecture-cible/overview-plateforme-flow.md` | Overview de la plateforme FLOW, sept produits candidats, domaines Engagement / Demand / Fulfillment / Supply, composants de gouvernance des données |
| `chronologie-engagement-supply-flow.svg` | `docs/architecture-cible/overview-plateforme-flow.md`, `docs/vision/modele-fonctionnement-flow.md` | Chronologie Engagement vers FLOW vers Supply, promesse, décision, plan d'exécution, remontées d'information |
| `flux-produits-fonctionnalites-flow.svg` | `docs/architecture-cible/flux-fonctionnels-flow.md` | Produits FLOW, fonctionnalités transverses, Case Management, Stock Unifié, Agreement, règles, événements, vues |
| `methodologie-flow-overview.svg` | `docs/methode/processus-de-cadrage.md` | Processus de cadrage, passage des observations aux choix de conception, livrables de méthode |
| `modele-demand-notions-flow.svg` | `docs/vision/modele-fonctionnement-flow.md` | Notions Demand, fait, événement, décision, règle, promesse, Case, plan d'exécution |
| `modele-mental-connaissances-flow.svg` | `docs/administration/modele-mental-connaissances.md` | Source datée, fait observé, insight, vision, principe, concept, domaine, capacité, produit, pattern, hotspot, transformation, administration |
| `panorama-brd-ecosystem.svg` | `docs/contexte/panorama-brd.md` | Cartographie applicative BRD, PLM, PIM, SAP, SRM, CBS, modèle fournisseur / usine |
| `panorama-gbm-ecosystem.svg` | `docs/contexte/panorama-gbm.md` | Cartographie applicative GBM, SAP, StoreLand, Socloz, NewStore, CBS, B2B / B2C / retail |
| `pattern-api-conversationnelle.svg` | `docs/architecture-cible/patterns/api-conversationnelle.md` | Pattern API conversationnelle, demande progressive, contexte, décision, réponse et reprise de conversation |
| `pattern-case-centric-orchestration.svg` | `docs/architecture-cible/patterns/case-centric-orchestration.md` | Case Management, événement, tâche, décision, document, exception, historique |
| `pattern-cqrs-projections.svg` | `docs/architecture-cible/patterns/cqrs-et-projections.md` | CQRS, modèle d'écriture, événements, projections, modèles de lecture, vues 360 |
| `pattern-event-driven-architecture.svg` | `docs/architecture-cible/patterns/event-driven-architecture.md` | Event-Driven Architecture, producteurs, événements, consommateurs, contrats d'événements |
| `pattern-event-sourcing-ledger.svg` | `docs/architecture-cible/patterns/event-sourcing-ledger.md` | Event Sourcing, ledger, faits, audit, relecture, projections |
| `pattern-externalisation-decisions.svg` | `docs/architecture-cible/patterns/externalisation-des-decisions.md` | Décisions métier, règles, policies, paramètres, moteur de règles |
| `pattern-operational-datahub.svg` | `docs/architecture-cible/patterns/operational-datahub.md` | Operational DataHub, ingestion, normalisation, disponibilité opérationnelle, distribution |
| `pattern-plateforme-ouverte-gouvernee.svg` | `docs/architecture-cible/patterns/plateforme-ouverte-gouvernee.md` | Plateforme ouverte, gouvernance, contrats, APIs, événements, extensions |
| `positionnement-flow-4-domaines.svg` | `docs/architecture-cible/overview-plateforme-flow.md`, `docs/vision/positionnement-flow.md`, `docs/vision/vision.md` | Engagement, Demand, Fulfillment, Supply, périmètre FLOW, domaines adhérents, promesse |
| `produit-socle-case-management.svg` | `docs/architecture-cible/produits/socle-case-management.md` | Socle Case Management, Case, statuts, décisions, événements, documents, exceptions |
| `produit-stock-unifie.svg` | `docs/architecture-cible/produits/stock-unifie.md` | Stock Unifié, disponibilité, réservation, ATP, mouvements, qualité et fraîcheur de stock |

## Comment décider de régénérer un SVG ?

Il faut relire ou régénérer un SVG lorsque :

- le nom d'un concept affiché dans le schéma change ;
- un concept structurant est ajouté dans une page dont le schéma dépend ;
- une frontière de domaine ou de produit change ;
- une page qui affiche le schéma change son raisonnement principal ;
- un lecteur pourrait tirer une conclusion fausse en lisant l'image sans relire tout l'article.

À l'inverse, il n'est pas nécessaire de régénérer tous les SVG à chaque ajout de contenu. Le registre sert justement à limiter la revue aux schémas réellement exposés au changement.
