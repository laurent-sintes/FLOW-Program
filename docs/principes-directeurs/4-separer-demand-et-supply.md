# Principe 4 — Articuler Demand, Fulfillment et Supply

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Sponsor</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>8 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Introduction

Les entreprises gèrent simultanément deux réalités fondamentalement différentes.

D'un côté, elles doivent traiter des demandes :

* commandes ;
* précommandes ;
* retours ;
* transferts ;
* réservations ;
* engagements clients ;
* engagements partenaires.

De l'autre, elles doivent gérer des ressources :

* stock ;
* capacité logistique ;
* capacité de transport ;
* capacité magasin ;
* capacité fournisseur ;
* capacité de production.

Ces deux préoccupations sont étroitement liées.

Elles ne sont pourtant pas de même nature.

FLOW considère que les demandes et les ressources doivent être pensées séparément.

Mais cette séparation ne suffit pas.

Entre ce qui est demandé et ce qui est disponible, il faut une capacité d'arbitrage : le <span class="flow-keyword">Fulfillment</span>.

Le Fulfillment transforme une demande qualifiée en trajectoire d'exécution, en arbitrant entre promesse, stock, priorités, contraintes Supply et règles métier.

---

## Principe

> Les demandes et les ressources évoluent indépendamment.
>
> FLOW distingue Demand, Fulfillment et Supply.
>
> Demand porte l'intention qualifiée, la priorité et la promesse à tenir.
>
> Fulfillment porte la décision opérationnelle.
>
> Supply porte les ressources, contraintes et capacités d'exécution.

---

## Ce que ce principe ne signifie pas

FLOW ne cherche pas à opposer les métiers commerciaux aux métiers logistiques.

FLOW ne cherche pas à créer de nouveaux silos.

FLOW cherche à distinguer trois responsabilités fondamentalement différentes :

* qualifier ce qui est demandé ou engagé ;
* arbitrer comment cette demande peut être servie ;
* exposer ce qui peut réellement être mobilisé.

---

## Ce que nous avons observé

### BRD

Les problématiques de :

* précommande ;
* allocation ;
* réallocation ;
* promesse de livraison ;

sont principalement pilotées par les engagements pris envers les clients.

Les décisions dépendent ensuite des ressources réellement disponibles.

---

### GBM

Les problématiques de :

* Ship From Store ;
* sourcing ;
* orchestration logistique ;
* visibilité de stock ;

montrent également que les demandes et les ressources évoluent selon des logiques différentes.

Une même demande peut être satisfaite de plusieurs façons.

Une même ressource peut servir plusieurs demandes concurrentes.

---

## Pourquoi cette distinction est-elle importante ?

Imaginons un monde où :

* le stock serait illimité ;
* le transport serait instantané ;
* les fournisseurs seraient toujours disponibles.

Dans ce monde :

```text
Une demande
        ↓
Une exécution
```

Il n'y aurait pratiquement aucune décision à prendre.

---

La réalité est différente.

Les ressources sont limitées.

Les ressources sont distribuées.

Les ressources évoluent constamment.

Les demandes sont concurrentes.

Les arbitrages deviennent nécessaires.

C'est précisément cette rareté qui justifie l'existence d'une couche de décision.

---

## Vue d'ensemble : Engagement, Demand, Fulfillment, Supply

Les notions ne décrivent pas des silos.

Elles décrivent des responsabilités complémentaires autour du cœur FLOW.

```text
Engagement
    parcours, canaux, interfaces, négociation, contexte relationnel
        ↓
Demand
    intention qualifiée, priorité, promesse à tenir
        ↓
Fulfillment
    arbitrage, promesse tenable, allocation, plan d'exécution
        ↓
Supply
    stock, sites, usines, fournisseurs, transport, capacités
```

Le cœur de FLOW est <span class="flow-keyword">Demand + Fulfillment</span>.

<span class="flow-keyword">Engagement</span> et <span class="flow-keyword">Supply</span> sont adhérents à FLOW : ils gardent leur autonomie, mais doivent exposer ou consommer les capacités, statuts, événements, règles et contrats de données nécessaires à la cohérence de bout en bout.

Le point clé est le suivant : le Fulfillment n'est pas seulement l'exécution logistique.

Dans FLOW, il représente la capacité de décision qui fait le lien entre une demande à servir et des ressources limitées, distribuées ou contraintes.

---

## Alignement avec les pratiques standard

La chaîne <span class="flow-keyword">Engagement / Demand / Fulfillment / Supply</span> est une formulation FLOW.

Ce n'est pas un standard académique cité tel quel dans toutes les écoles de commerce.

En revanche, il est aligné avec une évolution largement reconnue des pratiques Supply Chain, Operations et Case Management : sortir d'une lecture linéaire achat / vente / logistique pour distinguer la demande, les ressources, la planification intégrée, la décision et l'exécution des commandes ou services.

La solidité de la proposition vient précisément du croisement entre deux familles de connaissances :

- le <span class="flow-keyword">Case Management</span>, qui permet de traiter une demande comme un objet durable, contextualisé, évolutif et explicable ;
- les modèles Supply Chain, qui distinguent les processus de commande, planification, orchestration, fulfillment et mobilisation des ressources.

Trois références permettent d'appuyer cette lecture :

- [OMG — Case Management Model and Notation](https://www.omg.org/spec/CMMN/) : CMMN définit un méta-modèle et une notation pour modéliser et exprimer graphiquement des Cases. Cette référence soutient l'idée qu'une demande complexe ne doit pas être réduite à un workflow figé.
- [ASCM — SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) : SCOR DS distingue notamment les processus `Order`, `Plan`, `Source`, `Transform`, `Fulfill`, `Return` et `Orchestrate`. La séparation entre `Order`, `Plan` et `Fulfill` soutient l'idée qu'une demande, une capacité de planification / arbitrage et l'exécution ne doivent pas être confondues.
- [IBM — Integrated Business Planning](https://www.ibm.com/think/topics/integrated-business-planning) : l'IBP est présenté comme un cadre réunissant planification stratégique, opérationnelle et financière, avec collaboration entre sales, marketing, finance, supply chain, procurement et IT. Il confirme que la bonne maille n'est plus le silo applicatif, mais la décision transverse entre demande, ressources et contraintes.

La position FLOW est donc la suivante :

```text
Le vocabulaire exact est propre à FLOW.
L'évolution de fond est standard.
```

FLOW traduit cette évolution en un principe d'architecture : Engagement capte l'intention, Demand la qualifie et porte la promesse à tenir, Fulfillment porte l'arbitrage opérationnel, Supply porte les ressources mobilisables.

Le périmètre cœur de FLOW reste <span class="flow-keyword">Demand + Fulfillment</span>. Engagement et Supply sont des domaines adhérents : ils doivent être raccordés au cœur, sans être absorbés par lui.

---

## Engagement : le domaine adhérent des parcours

Engagement représente les espaces où l'intention naît, se formule, se négocie ou se contextualise.

Engagement peut prendre plusieurs formes :

* site e-commerce ;
* portail B2B ;
* CRM ;
* marketplace ;
* outil de négoce ;
* service client ;
* portail fournisseur ;
* application partenaire.

Engagement ne constitue pas le cœur de FLOW.

Il capte l'intention, porte les parcours, les interfaces et certaines règles locales de relation.

Il devient adhérent à FLOW lorsqu'il doit créer une demande, consulter une promesse, suivre un Case, recevoir des statuts ou contribuer des événements.

---

## Demand : le domaine de la demande et de la promesse

Demand représente les intentions qualifiées de l'entreprise.

Demand s'intéresse à :

* ce qui est demandé ;
* ce qui est promis ;
* ce qui est attendu ;
* ce qui doit rester explicable.

Demand ne représente pas un référentiel.

Demand représente un système de pilotage de la demande et de la promesse à tenir.

Demand doit répondre à des questions comme :

* Puis-je promettre ?
* Puis-je accepter cette commande ?
* Puis-je réallouer cette ressource ?
* Puis-je confirmer cette précommande ?

---

## Capacités typiques du domaine Demand

Le domaine Demand nécessite généralement :

* une gestion de cycle de vie ;
* une gestion des états ;
* une persistance de transactions longues ;
* un moteur de règles ;
* une gestion des événements ;
* une traçabilité des décisions ;
* une gestion des promesses.

L'objectif n'est pas de stocker des données.

L'objectif est de piloter des décisions.

---

## Supply : le domaine des ressources

Supply représente les moyens d'exécution de l'entreprise.

Supply s'intéresse à :

* ce qui existe ;
* ce qui est disponible ;
* ce qui est réservé ;
* ce qui peut être exécuté.

Supply doit maintenir une vision cohérente des ressources.

Supply doit répondre à des questions comme :

* Quel stock est disponible ?
* Quelle capacité de transport est disponible ?
* Quelle capacité fournisseur est disponible ?
* Quelle ressource peut être mobilisée ?

---

## Capacités typiques du domaine Supply

Le domaine Supply nécessite généralement :

* Inventory Visibility ;
* gestion des capacités ;
* visibilité fournisseur ;
* visibilité logistique ;
* projections ;
* disponibilité des ressources.

Supply produit des informations.

Fulfillment les utilise pour prendre des décisions au service de Demand.

---

## Fulfillment : la décision opérationnelle

Fulfillment représente la capacité qui transforme une demande qualifiée en trajectoire d'exécution.

Il s'intéresse à des questions comme :

* D'où servir cette demande ?
* Quel stock réserver ou allouer ?
* Quelle date peut être promise ?
* Faut-il splitter, substituer, reporter ou prioriser ?
* Quelle exception ouvrir si la promesse ne tient plus ?
* Quel plan d'exécution envoyer aux systèmes Supply ?

Fulfillment ne possède pas toute la Demand.

Il ne possède pas non plus toute la Supply.

Il arbitre entre les deux, à partir des règles métier, des priorités, des faits observés et des contraintes disponibles.

Il ne doit pas être confondu avec le <span class="flow-keyword">Fulfillment Network</span> : le réseau d'exécution décrit les lieux, partenaires, services et capacités mobilisables ; le Fulfillment décide comment les mobiliser pour satisfaire une demande.

---

## Fulfillment relie Demand et Supply

Demand, Fulfillment et Supply ne sont pas indépendants.

Ils collaborent en permanence.

Une demande interroge les ressources disponibles.

Les ressources influencent les décisions de Fulfillment.

```text
Demande
        ↓
Décision de Fulfillment
        ↓
Ressource affectée
```

La décision de Fulfillment constitue le point de rencontre entre Demand et Supply.

---

## Une relation conversationnelle

FLOW ne considère pas Demand et Supply comme deux systèmes échangeant simplement des données.

Une demande doit pouvoir dialoguer avec les ressources.

Par exemple :

```text
Peux-tu livrer demain ?
```

Supply répond :

```text
Non.
```

Demand peut alors reformuler :

```text
Et depuis un autre entrepôt ?
```

Supply répond :

```text
Oui.
```

La décision de Fulfillment émerge progressivement de cette interaction.

Cette logique est particulièrement visible dans :

* le sourcing ;
* l'orchestration logistique ;
* les allocations ;
* les précommandes ;
* les arbitrages de promesse.

---

## Inventory Visibility : une capacité partagée

Les ateliers ont montré que la visibilité de stock constitue une capacité d'entreprise.

Aujourd'hui :

* le stock magasin ;
* le stock entrepôt ;
* le stock omnicanal ;

sont souvent portés par des systèmes différents.

Les OMS omnicanaux fournissent parfois une vision consolidée.

Cependant cette vision est principalement utilisée pour prendre des décisions.

La visibilité de stock ne doit donc pas être considérée comme une simple fonctionnalité d'OMS.

Elle constitue une capacité transverse de la plateforme.

---

## Première hypothèse de structuration

FLOW identifie aujourd'hui trois responsabilités majeures :

```text
Demand
    ↓
Qualifier l'intention et la promesse à tenir

Fulfillment
    ↓
Arbitrer et construire la trajectoire d'exécution

Supply
    ↓
Exposer et mobiliser les ressources
```

Les produits qui composeront ces responsabilités restent à préciser.

---

## Conséquences pour FLOW

Cette séparation conduit naturellement à distinguer :

* les systèmes Engagement qui captent les intentions et portent les parcours ;
* les systèmes FLOW qui qualifient les demandes et arbitrent le Fulfillment ;
* les systèmes qui gèrent des ressources ;
* les mécanismes qui prennent les décisions de Fulfillment ;
* les contrats qui raccordent ces domaines sans les fusionner.

Elle favorise :

* la fédération des capacités ;
* l'explicitation des règles ;
* la réutilisation des ressources ;
* l'amélioration des arbitrages.

---

## À retenir

Engagement capte les intentions et porte les parcours.

Demand gère les demandes et les promesses à tenir.

Fulfillment arbitre la manière de les servir.

Supply gère les ressources.

Les ressources sont limitées.

Les demandes sont concurrentes.

Les décisions de Fulfillment permettent de relier les deux.

FLOW construit sa plateforme autour de cette distinction fondamentale.
