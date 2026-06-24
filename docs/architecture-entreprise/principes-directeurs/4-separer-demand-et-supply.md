# Principe 4 — Séparer Demand et Supply

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

---

## Principe

> Les demandes et les ressources évoluent indépendamment.
>
> FLOW distingue le domaine des engagements du domaine des ressources.

---

## Ce que ce principe ne signifie pas

FLOW ne cherche pas à opposer les métiers commerciaux aux métiers logistiques.

FLOW ne cherche pas à créer de nouveaux silos.

FLOW cherche à distinguer deux responsabilités fondamentalement différentes :

* décider ce qui doit être réalisé ;
* déterminer ce qui peut être réalisé.

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

## Demand : le domaine des engagements

Demand représente les intentions de l'entreprise.

Demand s'intéresse à :

* ce qui est demandé ;
* ce qui est promis ;
* ce qui est attendu ;
* ce qui est engagé.

Demand ne représente pas un référentiel.

Demand représente un système de pilotage des engagements.

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
* une gestion des engagements.

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

Demand les utilise pour prendre des décisions.

---

## La décision relie Demand et Supply

Demand et Supply ne sont pas indépendants.

Ils collaborent en permanence.

Une demande interroge les ressources disponibles.

Les ressources influencent les décisions.

```text
Demande
        ↓
Décision
        ↓
Ressource affectée
```

La décision constitue le point de rencontre entre les deux domaines.

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

La décision émerge progressivement de cette interaction.

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

FLOW identifie aujourd'hui deux domaines majeurs :

```text
Demand
    ↓
Décider

Supply
    ↓
Exécuter
```

Les produits qui composeront ces domaines restent à préciser.

---

## Conséquences pour FLOW

Cette séparation conduit naturellement à distinguer :

* les systèmes qui gèrent des engagements ;
* les systèmes qui gèrent des ressources ;
* les mécanismes qui prennent des décisions.

Elle favorise :

* la fédération des capacités ;
* l'explicitation des règles ;
* la réutilisation des ressources ;
* l'amélioration des arbitrages.

---

## À retenir

Demand gère les engagements.

Supply gère les ressources.

Les ressources sont limitées.

Les demandes sont concurrentes.

Les décisions permettent de relier les deux.

FLOW construit sa plateforme autour de cette distinction fondamentale.
