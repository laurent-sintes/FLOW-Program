# Architecture cible

Cette section décrit le positionnement cible de FLOW.

Elle ne part pas d'une solution à déployer.

Elle part d'une tension : le groupe doit créer du commun entre des patrimoines applicatifs, marques et business models différents, sans construire un nouveau monolithe qui rigidifierait l'entreprise.

La Vision explique cette ambition.

L'architecture cible décrit progressivement comment cette ambition peut se matérialiser :

- les responsabilités qui doivent devenir communes, gouvernées et transverses ;
- les patterns d'architecture qui structurent la plateforme ;
- les grands produits de la plateforme FLOW ;
- le positionnement de FLOW dans les écosystèmes existants ;
- l'urbanisme fonctionnel cible ;
- les responsabilités reprises par FLOW, conservées dans les systèmes existants ou exposées sous forme de projections.

## Pages disponibles

- [Overview de la plateforme FLOW](overview-plateforme-flow.md)
- [Patterns d'architecture](patterns/index.md)
- [Fiches produits FLOW](produits/index.md)
- [FLOW dans l’écosystème GBM](flow-dans-ecosysteme-gbm.md)
- [FLOW dans l’écosystème BRD](flow-dans-ecosysteme-brd.md)

## Patterns d'architecture

Les patterns donnent le vocabulaire commun de l'architecture cible.

Ils expliquent les choix réutilisables avant leur application dans les fiches produits.

- [Case-centric orchestration](patterns/case-centric-orchestration.md)
- [Event-Driven Architecture](patterns/event-driven-architecture.md)
- [API conversationnelle](patterns/api-conversationnelle.md)
- [CQRS et projections](patterns/cqrs-et-projections.md)
- [Operational DataHub](patterns/operational-datahub.md)
- [Event Sourcing / Ledger](patterns/event-sourcing-ledger.md)
- [Externalisation des décisions métier](patterns/externalisation-des-decisions.md)
- [Plateforme ouverte et gouvernée](patterns/plateforme-ouverte-gouvernee.md)

## Fiches produits initialisées

Les fiches produits donnent une première matière concrète aux PO / PM pour démarrer une réflexion de backlog.

Elles ne figent pas la solution, mais elles structurent les responsabilités, consommateurs, informations clés, interfaces et premiers epics.

- [Socle Case Management](produits/socle-case-management.md)
- [Stock Unifié](produits/stock-unifie.md)
- [Fulfillment Network Configuration](produits/fulfillment-network-configuration.md)
- [Product Agreement Catalog](produits/product-agreement-catalog.md)
- [Supply Service Registry](produits/supply-service-registry.md)
- [Vues 360](produits/vues-360.md)
- [Gouvernance des données en transit](produits/gouvernance-donnees-transit.md)

## Lecture actuelle

La cible n'est pas encore une architecture détaillée.

Elle pose une première carte de travail : FLOW est une réponse fédérée à la convergence, centrée sur Demand, les Cases, le stock unifié, le réseau d'exécution et les décisions métier qui relient la demande à l'exécution.

FLOW ne remplace pas l'ensemble du SI.

Il reprend les responsabilités transverses qui doivent être gouvernées durablement : demande, décision métier, stock disponible, réservations, réseau d'exécution, projections opérationnelles et contexte transverse.

Le reste du SI peut conserver ses spécialisations, à condition que ces spécialisations ne recréent pas des silos au cœur de la demande.
