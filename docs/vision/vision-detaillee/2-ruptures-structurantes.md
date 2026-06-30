# Ruptures : déplacer le centre de gravité du SI

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsor, Direction, Architecte</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>4 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Comprendre la vision, les arbitrages et le vocabulaire cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

<div class="flow-conviction">
  <p>FLOW ne demande pas seulement de changer de plateforme.</p>
  <p>FLOW demande de changer le point de départ du raisonnement.</p>
</div>

FLOW ne propose pas seulement une nouvelle plateforme.

Il propose plusieurs ruptures de raisonnement nécessaires pour traiter la convergence du groupe.

## La Demande : l'objet métier central

<div class="flow-conviction">
  <p>On ne part plus du document.</p>
  <p>On part de la demande à satisfaire.</p>
</div>

Dans une approche ERP classique, le système est souvent organisé autour des documents : commande, livraison, facture, avoir, écritures comptables.

Dans une approche OMS classique, le système est souvent organisé autour de la commande, de la promesse, du sourcing ou de l'orchestration omnicanale.

Ces approches ne suffisent plus à traiter la convergence du groupe.

La question centrale n'est plus : comment gérer une commande ?

La question devient : quelle <span class="flow-keyword">demande</span> faut-il comprendre, décider, promettre, satisfaire et expliquer ?

FLOW déplace donc le <span class="flow-keyword">centre de gravité</span> du système d'information :

```text
Ancien centre de gravité
    ERP / documents / comptabilité
    OMS / commande / canal

Nouveau centre de gravité
    Demande / décision
    Satisfaction client-utilisateur
    Stock et réseau d'exécution
```

Ce déplacement est majeur.

Il signifie que l'on ne part plus d'abord de la facture, de la commande ou du module applicatif.

On part de la demande à comprendre, promettre, exécuter et expliquer.

## Engagement / Demand / Fulfillment / Supply : dépasser achat / vente

<div class="flow-conviction">
  <p>FLOW ne découpe pas le SI selon “j'achète” ou “je vends”.</p>
  <p>FLOW distingue ce qui capte l'intention, ce qui qualifie la demande, ce qui arbitre comment la servir, et ce qui permet d'exécuter.</p>
</div>

L'approche classique consiste souvent à découper le SI selon les organisations, les canaux ou les processus :

```text
Achat / Vente
B2B / B2C
Retail / Wholesale
Marque A / Marque B
ERP / OMS
```

FLOW propose une autre lecture.

Au lieu de partir de l'organisation existante, FLOW part des problèmes durables de l'entreprise.

Cette approche conduit à distinguer quatre responsabilités, dont deux constituent le cœur de FLOW :

```text
Engagement
    Les parcours, canaux, interfaces et négociations qui captent l'intention

Demand
    Les demandes à qualifier, instruire, promettre, suivre et expliquer

Fulfillment
    Les décisions de promesse tenable, allocation, sourcing, priorisation et trajectoire d'exécution

Supply
    Les ressources, lieux, partenaires et capacités d'exécution à mobiliser
```

Le cœur de FLOW est <span class="flow-keyword">Demand + Fulfillment</span>.

<span class="flow-keyword">Engagement</span> et <span class="flow-keyword">Supply</span> sont adhérents à FLOW : ils conservent leurs responsabilités propres, mais ils doivent exposer ou consommer les capacités, événements, statuts et contrats de données nécessaires à la cohérence de bout en bout.

La demande devient le point de départ du cœur FLOW.

Une commande client, une commande B2B, une demande SAV, un retour, une exception, une allocation, une promesse ou une demande fournisseur sont des formes différentes d'un même problème : comprendre une intention, prendre des décisions de Fulfillment, mobiliser des ressources et garantir une exécution fiable.

## La Demande : l'unité autonome de la décision et de l'orchestration

<div class="flow-conviction">
  <p>Une demande doit rester lisible de bout en bout.</p>
  <p>Même lorsqu'elle traverse plusieurs processus, applications et partenaires.</p>
</div>

FLOW part de la <span class="flow-keyword">demande</span>.

La demande devient l'unité métier qui permet de relier une intention, un contexte, des décisions, des ressources, des documents, des événements et une exécution.

```text
Demande
    ↓
Contexte et Agreement
    ↓
Règles et décisions
    ↓
Stock, promesse, allocation, réseau d'exécution
    ↓
Action, document, événement, exception
```

Cette lecture permet de dépasser la logique “une application = un processus”.

Elle donne une continuité métier lorsque la demande traverse plusieurs domaines, applications, organisations ou partenaires.

Dans l'architecture cible, cette demande pourra être portée par des objets de type <span class="flow-keyword">Case</span>, développés et opérés dans une plateforme de Case Management.

Mais au niveau de la vision, le concept central reste la demande : ce que l'entreprise doit comprendre, arbitrer, satisfaire et expliquer.

## Configuration du système : paramétrer et implémenter des capacités d'action

<div class="flow-conviction">
  <p>FLOW configure des capacités d'action.</p>
  <p>Il ne reconstruit pas un grand miroir administratif de l'entreprise.</p>
</div>

FLOW introduit aussi une rupture dans la manière de concevoir les informations de configuration.

Dans une approche ERP classique, la master data décrit souvent l'entreprise telle qu'elle est : clients, fournisseurs, articles, sites, magasins, entrepôts, organisations, stocks, conditions.

Dans FLOW, les objets de configuration ne sont pas conçus pour “représenter toute l'entreprise”.

Ils sont conçus pour résoudre des problèmes précis :

- Promettre une demande.
- Choisir un nœud d'exécution.
- Calculer un stock disponible.
- Appliquer une règle d'allocation.
- Prioriser un client.
- Déterminer un service possible.
- Expliquer une décision.

Autrement dit :

```text
ERP
    informations pour représenter l'entreprise

FLOW
    objets de configuration pour décider, promettre et exécuter
```

Cette rupture change la finalité même de l'information.

FLOW ne cherche pas à reconstruire une master data globale.

FLOW cherche à définir les objets nécessaires pour traiter les demandes de manière fiable, explicable et optimisable.

Cette rupture doit être comprise comme une évolution des pratiques MDM.

Il ne s'agit pas seulement de lister des objets maîtres ou d'accumuler des attributs dans une fiche globale.

Pour l'<span class="flow-keyword">information au repos</span>, FLOW doit qualifier les sources de référence, les projections, les vues et les responsabilités de gouvernance.

Pour l'<span class="flow-keyword">information en transit</span>, FLOW doit transformer les flux projet en contrats de données gouvernés : publication, consommation, fraîcheur, qualité, supervision, reprise et compatibilité dans la durée.

Cela exclut l'idée qu'une base de données applicative soit une ressource publique d'échange.

Une application doit protéger sa base et exposer des interfaces stables, versionnées et gouvernées.

---

← Page précédente : [Ambition](1-ambition.md) · → Page suivante : [Solution](3-plateforme-flow.md)
