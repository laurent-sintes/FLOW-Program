# Capacités d'intégration des systèmes réintégrés

## Pourquoi c'est un hotspot

FLOW ne vise pas à réécrire tout le SI.

La cible consiste plutôt à reconstruire une colonne vertébrale commune autour des demandes, décisions, statuts, événements, stock, promesses et capacités d'exécution.

Dans cette trajectoire, certains services existants peuvent être conservés et réintégrés autour de FLOW lorsqu'ils portent une valeur métier spécifique.

C'est le cas, par exemple :

- de CBS pour certains processus fournisseur spécialisés ;
- du SAV Client développé par Sarenza ;
- d'outils fournisseurs ;
- de systèmes logistiques spécialisés ;
- de domaines d'exécution ou de conformité.

Mais cette réintégration n'est possible que si ces systèmes disposent des capacités techniques minimales pour interagir avec FLOW.

Le sujet n'est donc pas seulement de décider si un outil reste ou sort.

Le sujet est aussi de savoir s'il peut être branché proprement sur la colonne vertébrale FLOW.

## Le risque

Un système existant peut porter une vraie valeur métier, mais être difficile à réintégrer s'il ne dispose pas de capacités d'intégration suffisantes.

Les risques sont alors :

- conserver un outil utile mais incapable de publier ses événements ;
- recréer des synchronisations fragiles ou batchées ;
- maintenir des statuts divergents entre FLOW et l'application spécialisée ;
- perdre la traçabilité du Case ;
- rendre les Vues 360 incomplètes ou trop peu fraîches ;
- empêcher FLOW d'expliquer une décision ou une exception ;
- créer une nouvelle dépendance point-à-point au lieu d'un contrat d'intégration gouverné.

Dans ce cas, la promesse “réintégrer sans tout réécrire” devient fragile.

## Capacités attendues

Un système réintégré autour de FLOW devrait disposer, selon son rôle, de capacités techniques telles que :

- APIs documentées et contractuelles ;
- publication d'événements métier ;
- consommation d'événements FLOW ;
- gestion d'identifiants de corrélation ;
- exposition de statuts et jalons d'avancement ;
- capacité à recevoir ou produire des documents ;
- mécanismes de reprise, réconciliation et rejeu ;
- exigences de fraîcheur explicites ;
- supervision et diagnostic des échanges ;
- versionnement des contrats d'interface.

Ces capacités ne sont pas toutes nécessaires pour tous les systèmes.

Elles doivent être évaluées selon la responsabilité portée par le système et la criticité de son interaction avec FLOW.

## Différence avec le hotspot Stock temps réel

Le hotspot [Stock temps réel](stock-temps-reel.md) traite un cas particulier : les systèmes qui observent ou provoquent des mouvements de stock doivent pouvoir publier ces mouvements avec une fraîcheur suffisante.

Ce hotspot-ci est plus général.

Il traite la capacité de tout système réintégré à interagir proprement avec FLOW : CBS, SAV Client Sarenza, outils fournisseurs, systèmes logistiques, Finance ou autres domaines spécialisés.

```text
Stock temps réel
    → focus sur les mouvements de stock
    → POS, WMS, logisticiens, magasins
    → exigence de fraîcheur pour promettre et allouer

Capacités d'intégration des systèmes réintégrés
    → focus sur la réintégration des services existants
    → APIs, événements, statuts, documents, corrélation
    → exigence d'urbanisme pour brancher les services sur FLOW
```

## Question d'architecture

La question centrale est donc :

> Quels prérequis techniques minimaux un service existant doit-il satisfaire pour être réintégré autour de FLOW sans fragiliser la colonne vertébrale commune ?

Cette question doit être instruite avant de décider qu'un service existant peut rester dans la cible.

Un service peut être métier-pertinent mais techniquement insuffisant.

Dans ce cas, il faudra arbitrer entre :

- le conserver tel quel avec une intégration limitée ;
- l'encapsuler derrière une façade API / événementielle ;
- le faire évoluer pour publier ou consommer les bons événements ;
- le remplacer si l'effort de réintégration est trop coûteux ;
- rapatrier certaines responsabilités dans FLOW si elles sont trop critiques pour rester dans un outil non intégrable.

## Ce que FLOW doit clarifier

| Sujet | Question à instruire |
| --- | --- |
| APIs | Le système expose-t-il des APIs stables, documentées et gouvernables ? |
| Événements | Le système peut-il publier les événements métier nécessaires à FLOW ? |
| Statuts | Les statuts peuvent-ils être corrélés avec les Cases et Vues 360 ? |
| Documents | Les documents produits ou consommés peuvent-ils être référencés ou attachés au Case ? |
| Fraîcheur | Quelle fraîcheur d'information est nécessaire selon l'usage métier ? |
| Réconciliation | Comment détecter, diagnostiquer et corriger les écarts entre systèmes ? |
| Trajectoire | Faut-il encapsuler, faire évoluer, remplacer ou rapatrier certaines responsabilités ? |

## À retenir

Réintégrer un outil existant n'est pas seulement une décision fonctionnelle.

C'est aussi une décision d'urbanisme et d'intégrabilité.

FLOW peut conserver des services spécialisés utiles, mais seulement s'ils peuvent être branchés sur la colonne vertébrale commune avec des contrats lisibles : APIs, événements, statuts, documents et mécanismes de réconciliation.

Sinon, on ne réintègre pas vraiment l'outil : on conserve un silo.