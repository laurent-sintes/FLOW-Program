# Pattern — Self-contained System (SCS)

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

Un <span class="flow-keyword">Self-contained System</span> est une approche d'architecture qui découpe un grand système en systèmes plus petits, autonomes et collaborants.

L'idée importante pour FLOW est simple : un produit ou domaine qui porte une responsabilité critique doit maîtriser assez de logique, d'information, de configuration et d'exploitation pour remplir ses cas d'usage principaux sans dépendre en temps réel de la disponibilité d'autres systèmes.

Ce pattern complète directement la [projection locale de décision](projection-locale-de-decision.md).

- Le Self-contained System définit l'autonomie du périmètre.
- La projection locale de décision définit comment alimenter localement les informations nécessaires au calcul.

## Problème adressé

Les architectures de convergence échouent souvent lorsqu'elles remplacent un monolithe visible par un monolithe distribué.

Le symptôme est connu :

- une décision critique appelle plusieurs services en cascade ;
- la logique métier est répartie entre plusieurs applications sans propriétaire clair ;
- les données utiles au calcul sont ailleurs, dans des référentiels ou APIs non maîtrisés ;
- chaque incident externe peut bloquer le parcours principal ;
- les équipes ne savent plus qui est responsable de la promesse, de la décision ou de la qualité d'information.

FLOW doit éviter cette dérive.

La convergence ne doit pas créer une plateforme qui dépend de tout, tout le temps.

## Principe

> Un produit FLOW doit être conçu comme une unité autonome de responsabilité.
>
> Il peut collaborer avec d'autres systèmes, mais ses cas d'usage critiques ne doivent pas dépendre d'appels synchrones à des systèmes externes dans le chemin nominal.
>
> Lorsqu'il a besoin d'informations externes pour décider, il doit les consommer sous forme de contrats, événements, snapshots ou projections gouvernées.

Dans la version classique du pattern, un SCS inclut sa propre UI, sa logique métier et sa persistance.

Pour FLOW, il ne faut pas appliquer cette règle mécaniquement : certains produits de plateforme n'ont pas vocation à porter toute l'expérience utilisateur finale.

Le principe à retenir est plutôt :

```text
Responsabilité métier claire
    + logique et règles maîtrisées
    + informations nécessaires disponibles localement
    + contrats d'échange explicites
    + exploitation observable
    = produit autonome et remplaçable
```

## Impact sur le découpage en produits

Le pattern SCS a guidé le découpage initial de la plateforme FLOW en produits.

Un produit FLOW n'est donc pas seulement une brique fonctionnelle ou technique.

C'est une unité de responsabilité qui doit pouvoir porter :

- un périmètre métier compréhensible ;
- des règles, décisions ou configurations cohérentes ;
- les informations et projections nécessaires à ses usages critiques ;
- des contrats explicites avec les domaines contributeurs ou consommateurs ;
- une exploitation observable et réconciliable.

Cette lecture explique pourquoi FLOW est découpé en produits comme Case Management, Stock Unifié, Fulfillment Network Configuration, Product Agreement Catalog ou Supply Service Registry.

Chacun correspond à une responsabilité stable du modèle cible, plutôt qu'à une application existante, une couche technique ou un organigramme.

La gouvernance des données en transit reste volontairement une pratique transverse : elle soutient l'autonomie des produits, mais ne devient pas un produit fonctionnel autonome dans l'overview.

## Application dans FLOW

Le pattern est particulièrement utile pour penser les produits suivants :

| Produit FLOW | Lecture SCS |
| --- | --- |
| Socle Case Management | Autonome pour porter le Case, les statuts, les règles, les décisions et l'historique de la demande. |
| Stock Unifié | Autonome pour exposer disponibilité, réservation, allocation et faits stock, sans dépendre de la lecture directe des WMS ou POS au moment de décider. |
| Product Agreement Catalog | Autonome pour fournir les informations produit / agreement utiles au calcul FLOW, sans rappeler PLM, PIM ou pricing à chaque décision. |
| Fulfillment Network Configuration | Autonome pour décrire les nœuds, capacités, contraintes et conditions d'usage du réseau d'exécution. |
| Supply Service Registry | Autonome pour exposer les services Supply consommables, leurs SLA, contraintes et engagements opérationnels. |

Cette autonomie ne signifie pas que FLOW absorbe les responsabilités d'Engagement, Supply, Finance, PLM, PIM, WMS ou partenaires.

Elle signifie que FLOW ne doit pas dépendre de leur disponibilité synchrone pour tenir ses responsabilités critiques.

## Lien avec la projection locale de décision

Le Self-contained System est le principe d'architecture.

La projection locale de décision est l'un de ses mécanismes.

```text
Source responsable externe
    → contrat de données / événement / snapshot
    → projection locale de décision
    → produit FLOW autonome
    → décision rapide, traçable et explicable
```

Ce découplage accepte une tension normale : la projection locale peut être légèrement en retard sur la source.

Ce retard doit être gouverné explicitement : fraîcheur attendue, règles de reprise, réconciliation, traçabilité des versions et comportement en cas d'information manquante.

## Ce que ce pattern ne dit pas

Ce pattern ne dit pas que chaque produit FLOW doit devenir une application isolée.

Il ne dit pas que tout doit être recopié partout.

Il ne dit pas non plus que les produits FLOW ne doivent jamais appeler d'API externe.

Il dit que les appels externes ne doivent pas devenir une dépendance cachée dans le chemin critique d'une décision ou d'une promesse.

## Anti-patterns

### Monolithe distribué

Les composants sont séparés techniquement, mais chacun dépend en temps réel de plusieurs autres pour réaliser son cas d'usage principal.

### Shared database implicite

Plusieurs produits lisent directement les mêmes tables ou schémas internes au lieu de passer par des contrats d'échange stables.

### Responsabilité sans autonomie

Un produit est officiellement responsable d'une décision, mais ne maîtrise ni les informations nécessaires, ni les règles, ni le SLA des systèmes qu'il appelle.

### Autonomie sans gouvernance

Chaque produit devient autonome techniquement, mais les contrats, sources de référence, événements, projections et responsabilités ne sont pas gouvernés.

## Liens avec les autres patterns

| Pattern | Articulation |
| --- | --- |
| [Projection locale de décision](projection-locale-de-decision.md) | Mécanisme data permettant au produit autonome de décider sans appels synchrones critiques. |
| [Sources de référence, projections et vues](sources-reference-projections-vues.md) | L'autonomie ne doit pas transformer une projection en source de référence par accident. |
| [Event-Driven Architecture](event-driven-architecture.md) | Les événements permettent de maintenir l'autonomie sans multiplier les appels point à point. |
| [CQRS et projections](cqrs-et-projections.md) | Les modèles de lecture spécialisés soutiennent l'autonomie des usages de lecture et de décision. |
| [Plateforme ouverte et gouvernée](plateforme-ouverte-gouvernee.md) | Une plateforme peut être ouverte sans imposer un couplage fort entre tous les domaines. |

## Références utiles

- [Self-contained Systems — scs-architecture.org](https://scs-architecture.org/), pour les caractéristiques du pattern : autonomie, équipe responsable, données et logique propres, dépendances asynchrones autant que possible.
- [SCS vs. Microservices — scs-architecture.org](https://scs-architecture.org/vs-ms.html), pour distinguer SCS et microservices : moins d'unités, périmètre métier plus large, préférence pour l'autonomie et les dépendances asynchrones.
- [Case studies — scs-architecture.org](https://scs-architecture.org/case-studies.html), pour des exemples d'application du pattern sur des plateformes e-commerce, logistiques ou produit.

## À retenir

Pour FLOW, le Self-contained System apporte une règle d'architecture forte : le bon découpage n'est pas seulement fonctionnel.

Il doit aussi permettre à chaque produit critique de tenir sa responsabilité sans être bloqué par les indisponibilités, latences ou modèles internes des autres systèmes.
