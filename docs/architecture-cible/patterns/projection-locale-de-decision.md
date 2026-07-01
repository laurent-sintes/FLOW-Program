# Pattern — Projection locale de décision

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Développeur, Delivery</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Une décision critique ne doit pas dépendre, au moment du calcul, d'une chaîne d'appels synchrones vers des APIs externes dont FLOW ne maîtrise ni le SLA, ni la latence, ni les indisponibilités.

Le moteur de décision doit disposer localement des informations nécessaires à sa décision, sous forme de projections gouvernées, fraîches et adaptées au calcul.

Ce pattern est appelé ici <span class="flow-keyword">projection locale de décision</span>.

Il est une conséquence concrète du pattern [Self-contained System (SCS)](self-contained-system.md) : un produit autonome doit maîtriser localement les informations dont il a besoin pour tenir ses décisions critiques.

Il s'appuie sur plusieurs patterns reconnus : CQRS, Materialized View pattern / read models matérialisés, Event-Carried State Transfer et autonomie des services.

## Problème adressé

Une décision de fulfillment peut devoir répondre en quelques dizaines ou centaines de millisecondes.

Par exemple :

- promettre une date ;
- choisir une source d'exécution ;
- vérifier l'éligibilité d'un service ;
- prioriser une demande ;
- arbitrer une allocation ;
- scorer plusieurs plans d'exécution.

Si cette décision appelle en direct le PLM, le PIM, la SRM, un WMS, un TMS, Finance ou un service Supply externe, la robustesse de FLOW devient dépendante de la robustesse cumulée de tous ces appels.

Le problème n'est pas seulement technique.

Il devient fonctionnel : la promesse calculée par FLOW dépend d'informations dont la disponibilité, la fraîcheur et la performance ne sont plus maîtrisées par le domaine qui décide.

## Principe

> Pour une décision critique, FLOW ne doit pas interroger en temps réel tous les référentiels sources.
>
> FLOW doit consommer des projections locales de décision, construites à partir de sources de référence et maintenues par contrats de données.
>
> La projection locale optimise le calcul ; elle ne devient pas automatiquement source de référence.

Cette règle sépare deux chemins.

| Chemin | Objectif | SLA principal |
| --- | --- | --- |
| Chemin de synchronisation | Maintenir les projections de décision à partir des sources de référence. | Fraîcheur, complétude, réconciliation, reprise. |
| Chemin de décision | Calculer une décision métier à partir d'un contexte local maîtrisé. | Latence, disponibilité, explicabilité, traçabilité. |

## Application dans FLOW

Les produits FLOW concernés sont notamment :

- Socle Case Management, pour les règles, policies et décisions métier ;
- Stock Unifié, pour les disponibilités, réservations, allocations et mouvements ;
- Fulfillment Network Configuration, pour les nœuds, capacités, contraintes et SLA ;
- Product Agreement Catalog, pour les informations produit / article / agreement utiles au calcul ;
- Supply Service Registry, pour les services Supply consommables et leurs conditions d'appel.

Le moteur de décision ne doit pas appeler ces domaines comme une suite de dépendances synchrones au moment de décider.

Il doit travailler sur un modèle local :

```text
Sources de référence
    → contrats de données
    → événements / snapshots / APIs de publication
    → projections locales de décision
    → moteur de décision
    → décision traçable
```

## Ce que la projection locale doit maîtriser

Une projection locale de décision doit préciser :

- les sources de référence qui l'alimentent ;
- les contrats de données utilisés ;
- la granularité utile au calcul ;
- la fraîcheur attendue ;
- la politique de retard ou d'information manquante ;
- les règles de réconciliation ;
- la traçabilité des versions utilisées pour décider ;
- les consommateurs et décisions qu'elle supporte.

Sans ces éléments, la projection locale devient une copie opportuniste.

Avec ces éléments, elle devient un composant d'architecture maîtrisé.

## Ce que ce pattern ne dit pas

Ce pattern ne dit pas que FLOW doit recopier toute l'entreprise.

Il ne dit pas que toutes les informations doivent être localisées partout.

Il ne dit pas non plus que les sources de référence perdent leur responsabilité.

Il dit seulement que les décisions critiques doivent être autonomes sur leur chemin d'exécution.

La source de référence garde la maîtrise de l'information.

La projection locale garde la maîtrise du calcul.

## Anti-patterns

### API en cascade pendant la décision

Le moteur de décision appelle plusieurs APIs externes en direct pour calculer une promesse.

Chaque appel ajoute de la latence, un risque d'indisponibilité et une dépendance de SLA.

### Copie devenue maître par accident

Une projection, une vue, un export, un cache ou un agrégat devient l'endroit où l'on corrige l'information parce que la source de référence est trop lente ou trop éloignée.

La projection locale de décision reste alors optimisée pour le calcul, mais devient maître opérationnel sans que la responsabilité ait été explicitement transférée.

### Cache technique sans gouvernance

Un cache est ajouté pour accélérer, mais sans contrat de fraîcheur, traçabilité, règle de reprise ou responsabilité métier.

### Information trop fraîche mais décision instable

Le système cherche la fraîcheur maximale à tout prix, au lieu de définir la fraîcheur suffisante pour une décision fiable et explicable.

## Liens avec les autres patterns

| Pattern | Articulation |
| --- | --- |
| [Self-contained System (SCS)](self-contained-system.md) | La projection locale de décision donne au produit autonome les informations dont il a besoin sans dépendance synchrone cachée. |
| [CQRS et projections](cqrs-et-projections.md) | La projection locale de décision est un read model spécialisé pour décider, pas seulement pour consulter. |
| [Sources de référence, projections et vues](sources-reference-projections-vues.md) | La projection locale ne remplace pas la source de référence ; elle consomme des informations gouvernées. |
| [Event-Driven Architecture](event-driven-architecture.md) | Les événements permettent de maintenir les projections sans coupler le moteur de décision aux APIs sources. |
| [Externalisation des décisions métier](externalisation-des-decisions.md) | Les règles et contraintes ne sont efficaces que si les faits nécessaires sont disponibles localement. |
| [Operational DataHub](operational-datahub.md) | Le DataHub peut alimenter ou stabiliser certaines projections, mais la projection de décision reste optimisée pour un usage métier précis. |

## Références utiles

- [CQRS — Microservices.io](https://microservices.io/patterns/data/cqrs.html), pour le principe de read model matérialisé conçu pour une requête ou un groupe de requêtes.
- [Materialized View pattern — Microsoft Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view), pour le principe de vues préconstruites dans un format optimisé pour les lectures et la performance.
- [Database per Service — Microservices.io](https://microservices.io/patterns/data/database-per-service.html), pour la séparation des données par service et la nécessité de patterns comme CQRS pour les lectures multi-domaines.
- [Event-Carried State Transfer — Martin Fowler](https://martinfowler.com/articles/201701-event-driven.html#Event-CarriedStateTransfer), pour le principe de transmettre suffisamment d'état par événement afin que le consommateur n'ait plus besoin d'appeler la source pour travailler.

## À retenir

Pour FLOW, le découplage ne consiste pas seulement à éviter les appels point à point.

Il consiste à rendre le chemin de décision autonome, rapide et explicable, tout en gardant les sources de référence responsables de l'information.
