# Principe 3 — Les domaines avant les structures

## Introduction

Les systèmes d'information reflètent souvent l'histoire de l'entreprise.

Au fil du temps, les applications, les équipes et les processus se structurent autour :

* des marques ;
* des enseignes ;
* des directions ;
* des canaux ;
* des partenaires ;
* des produits du marché.

Cette organisation est légitime.

Cependant, elle ne constitue pas nécessairement le meilleur découpage pour construire une plateforme d'entreprise durable.

FLOW considère que les domaines métier sont plus stables que les organisations, les applications ou les processus.

---

## Principe

> Les domaines sont plus durables que les structures qui les portent.
>
> FLOW s'organise autour des domaines métier avant de s'organiser autour des structures existantes.

---

## Une nouvelle grille de lecture

L'entreprise est habituellement observée à travers :

* son organisation ;
* ses applications ;
* ses processus.

Ces représentations sont utiles.

Elles permettent de comprendre comment l'entreprise fonctionne aujourd'hui.

Mais elles ne permettent pas toujours de comprendre quelles responsabilités fondamentales l'entreprise devra continuer à assumer demain.

FLOW introduit une autre grille de lecture.

> L'entreprise doit apprendre à se regarder à travers ses domaines.

Les domaines permettent de révéler les responsabilités durables qui subsistent malgré les réorganisations, les changements de produits ou l'évolution des processus.

---

## Qu'est-ce qu'un domaine ?

Dans FLOW, un domaine ne représente pas une organisation.

Un domaine représente un espace problématique cohérent au sens du Domain-Driven Design.

Un domaine regroupe des problèmes qui doivent être compris et résolus ensemble.

Les domaines constituent le principal outil d'urbanisme de FLOW.

---

## Ce qu'un domaine n'est pas nécessairement

Un domaine n'est pas :

* une direction ;
* une équipe ;
* une marque ;
* une application ;
* un ERP ;
* un OMS ;
* un produit du marché ;
* un processus ;
* un parcours ;
* un flux métier.

Ces éléments peuvent révéler un domaine.

Ils ne le définissent pas.

---

## Ce qu'un domaine est

Un domaine est :

* un espace problématique cohérent ;
* un cadre de compréhension ;
* un outil d'urbanisme ;
* un moyen de délimiter les responsabilités ;
* une mission durable de l'entreprise.

Les domaines répondent à la question :

> Quelle responsabilité fondamentale l'entreprise doit-elle assumer durablement ?

---

## Pourquoi les domaines sont-ils importants ?

Les organisations évoluent constamment.

On observe régulièrement :

* des réorganisations ;
* des acquisitions ;
* des changements de périmètre ;
* des créations ou suppressions de marques ;
* des changements de partenaires.

Les domaines évoluent beaucoup plus lentement.

Ils représentent les grandes missions permanentes que l'entreprise doit assumer.

---

## Les domaines avant les applications

Une erreur fréquente consiste à confondre une responsabilité avec le produit qui l'implémente.

Par exemple :

```text
Facturation = SAP
Stock = WMS
Commande = OMS
Transport = TMS
```

Cette lecture est pratique mais trompeuse.

Les applications implémentent des responsabilités.

Elles ne définissent pas les domaines.

Une même responsabilité peut être portée successivement par plusieurs produits au cours de la vie de l'entreprise.

Les domaines doivent donc être identifiés indépendamment des solutions qui les implémentent aujourd'hui.

---

## Les domaines avant les processus

Une autre erreur fréquente consiste à utiliser les processus comme principal mécanisme de découpage.

Les processus sont utiles pour comprendre le fonctionnement opérationnel.

Ils deviennent insuffisants pour concevoir une architecture d'entreprise.

Un processus traverse généralement plusieurs domaines.

### Exemple : le processus de facturation

La facturation est souvent perçue comme une capacité unique ou comme une simple étape du processus Order-to-Cash.

Pourtant, lorsqu'on l'analyse sous l'angle des responsabilités, plusieurs domaines apparaissent.

```text
Demand
    └─ Décider qu'une facture doit être émise
       - état de la demande
       - contrat
       - client
       - canal
       - réglementation

Document Management
    └─ Produire la facture
       - template
       - format
       - variantes documentaires
       - diffusion

Finance
    └─ Comptabiliser l'événement économique
       - écritures comptables
       - TVA
       - contrôle de gestion
       - reporting financier
```

Selon le contexte, Supply peut également intervenir lorsque l'émission de la facture dépend d'un événement logistique.

Le processus est unique.

Les responsabilités sont multiples.

Le processus traverse les domaines.

Il ne définit pas les domaines.

---

## Domaines et processus

FLOW ne cherche pas à nier l'existence des processus.

Les processus restent indispensables pour :

* observer l'activité ;
* mesurer la performance ;
* analyser les irritants ;
* identifier les ruptures ;
* piloter l'amélioration continue.

Mais ils ne doivent pas dicter seuls le découpage de la plateforme.

> Les domaines expliquent pourquoi l'entreprise agit.
>
> Les processus décrivent comment les domaines collaborent.

Un processus peut changer.

Les responsabilités demeurent.

---

## Ce que nous avons observé

### GBM

Les ateliers sont souvent structurés autour :

* des marques ;
* des enseignes ;
* des applications historiques.

Pourtant, l'apparition de UR montre que certaines problématiques dépassent naturellement ces frontières.

### BRD

Les responsabilités liées :

* aux engagements ;
* aux décisions ;
* aux ressources ;
* à l'exécution ;

traversent SAP, NewStore, Maersk et les partenaires logistiques.

Aucune application ne porte naturellement ces problématiques dans leur intégralité.

---

## Les domaines doivent être découverts

Les métiers décrivent naturellement leurs besoins à travers leur organisation.

Un responsable logistique parlera :

* de transport ;
* d'entrepôt ;
* de picking ;
* de packing.

Un responsable retail parlera :

* de magasin ;
* de stock magasin ;
* de Ship From Store.

Un responsable wholesale parlera :

* de précommandes ;
* d'allocations ;
* de clients B2B.

Pourtant, derrière ces discours, on retrouve souvent les mêmes problématiques fondamentales :

* visibilité des ressources ;
* engagement ;
* décision ;
* exécution.

Les domaines ne sont pas directement observables.

Ils doivent être découverts.

Les interviews produisent des symptômes.

Les insights permettent de faire émerger les domaines.

---

## Domaines, produits, capacités et fonctionnalités

FLOW distingue plusieurs niveaux de conception.

```text
Domaine
    ↓
Produit
    ↓
Capacité
    ↓
Fonctionnalité
```

### Exemple

Domaine : Supply

Produit : Inventory Visibility

Capacité : maintenir une vision cohérente des ressources.

Fonctionnalités :

* consulter le stock ;
* réserver du stock ;
* calculer l'ATP.

Les fonctionnalités évoluent rapidement.

Les capacités évoluent plus lentement.

Les produits évoluent au rythme des besoins de l'entreprise.

Les domaines sont les éléments les plus durables.

---

## Première hypothèse de travail

FLOW identifie aujourd'hui une première structuration de domaines :

* Demand ;
* Supply.

Ces domaines seront détaillés dans les principes suivants.

Les produits qui les composent restent à découvrir et à préciser.

---

## Conséquences pour FLOW

FLOW ne cherche pas à reproduire :

* les organigrammes ;
* les applications historiques ;
* les processus existants ;
* les catégories de progiciels du marché.

FLOW cherche à identifier les espaces problématiques durables que l'entreprise devra continuer à maîtriser quelle que soit son organisation future.

---

## À retenir

Les organisations changent.

Les applications changent.

Les processus changent.

Les partenaires changent.

Les domaines demeurent.

FLOW urbanise l'entreprise autour des responsabilités durables plutôt qu'autour des structures temporaires qui les portent.
