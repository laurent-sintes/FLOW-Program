# Patterns d'architecture

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecture, product owners, delivery</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>S'orienter dans la section et identifier les pages utiles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette section décrit les patterns d'architecture qui structurent la plateforme FLOW.

Un pattern n'est pas une technologie.

C'est une manière récurrente d'organiser les responsabilités, les données, les décisions métier et les interactions entre composants.

<div class="flow-conviction">
  <p>Les patterns d'architecture donnent le vocabulaire commun.</p>
  <p>Les fiches produits expliquent comment ce vocabulaire s'applique concrètement dans FLOW.</p>
</div>

## Pourquoi cette section ?

Les fiches produits FLOW mobilisent plusieurs patterns transverses : Case Management, Event-Driven Architecture, CQRS, Operational DataHub, Event Sourcing, externalisation des décisions métier, API conversationnelle, plateforme ouverte et gouvernée.

Sans section dédiée, ces patterns seraient dispersés dans les fiches produit.

Cette section sert donc à :

- expliciter les patterns avant de les appliquer ;
- éviter que chaque fiche produit redéfinisse les mêmes concepts ;
- donner une base de discussion commune entre architecture, PO, PM, IT et métiers ;
- distinguer les choix d'architecture des choix technologiques ;
- relier les patterns aux produits FLOW.

## Patterns disponibles

| Pattern | Rôle dans FLOW | Produits principalement concernés |
| --- | --- | --- |
| [Case-centric orchestration](case-centric-orchestration.md) | Faire émerger le processus à partir de la demande, des faits et des décisions. | Socle Case Management |
| [Event-Driven Architecture](event-driven-architecture.md) | Faire circuler les faits opérationnels entre systèmes sans dépendre de flux projet point à point. | Case Management, Stock Unifié, données en transit |
| [API conversationnelle](api-conversationnelle.md) | Maintenir un dialogue corrélé, asynchrone et observable entre domaines, Cases et systèmes contributeurs. | Case Management, Stock Unifié, Supply Service Registry |
| [CQRS et projections](cqrs-et-projections.md) | Séparer actions, événements, modèles de lecture et projections métier. | Stock Unifié, Vues 360, Case Management |
| [Sources de référence, projections et vues](sources-reference-projections-vues.md) | Cartographier où une information est contrôlée par un processus, et distinguer source de référence, projection, vue et agrégat. | Case Management, Vues 360, Product Agreement Catalog, données en transit |
| [Operational DataHub](operational-datahub.md) | Construire une vérité opérationnelle fraîche, gouvernée et consommable. | Stock Unifié, Vues 360, données en transit |
| [Event Sourcing / Ledger](event-sourcing-ledger.md) | Historiser les événements ou mouvements pour reconstruire, auditer et expliquer. | Stock Unifié, Case Management |
| [Externalisation des décisions métier](externalisation-des-decisions.md) | Sortir règles, policies et variations métier des processus figés. | Case Management, Product Agreement Catalog, Stock Unifié |
| [Rôles, relations et policies](roles-relations-policies.md) | Éviter de figer dans le cœur des cardinalités qui relèvent de règles métier variables. | Product Agreement Catalog, Supply Service Registry, Vues 360 |
| [Plateforme ouverte et gouvernée](plateforme-ouverte-gouvernee.md) | Permettre à des domaines externes de configurer, développer et consommer sans recréer des silos. | Plateforme FLOW, tous produits |

## À retenir

Les patterns ne sont pas des dogmes.

Ils servent à sécuriser les choix structurants de FLOW : où placer la vérité, où placer la décision métier, où placer la lecture, où placer l'exécution, et comment éviter que la convergence ne recrée un grand monolithe.
