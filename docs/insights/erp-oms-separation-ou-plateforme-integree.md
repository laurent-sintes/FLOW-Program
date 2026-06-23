# ERP + OMS : séparation utile ou dette architecturale ?

## Contexte

La plupart des architectures retail modernes reposent sur une séparation entre :

- ERP ;
- OMS ;
- WMS ;
- TMS ;
- PIM ;
- PLM.

Cette approche est généralement considérée comme une bonne pratique permettant la spécialisation des solutions.

## Position exprimée par le CTO Beaumanoir

Le CTO de Beaumanoir a exprimé une conviction différente.

Selon lui, la séparation ERP / OMS constitue elle-même une partie du problème.

L'empilement de solutions spécialisées conduit souvent à :

- des synchronisations permanentes ;
- des redondances de données ;
- des responsabilités floues ;
- des arbitrages répartis ;
- une gouvernance complexe.

## Deux visions

### Vision 1 — Best of Breed

ERP + OMS + WMS + TMS + PIM + PLM

Chaque solution est spécialisée.

Les intégrations deviennent le mécanisme principal de cohérence.

### Vision 2 — Plateforme intégrée

FLOW Platform

- Agreement
- Demand
- Decision
- Execution
- Visibility

Les responsabilités sont explicites mais implémentées dans une plateforme cohérente.

L'intégration devient un mécanisme d'extension plutôt qu'un mécanisme de survie.

## Question ouverte

FLOW doit-il :

- assembler plusieurs produits spécialisés ;
- ou devenir progressivement une plateforme intégrée de gestion des engagements, des demandes, des décisions et des exécutions ?

Cette question reste ouverte.

## Conséquence pour FLOW

FLOW ne doit probablement pas être présenté comme le futur OMS du groupe.

FLOW n'est pas non plus le futur ERP.

FLOW pourrait devenir une plateforme d'entreprise intégrée construite autour des responsabilités métier plutôt qu'autour des catégories historiques de logiciels.

## Importance de cet insight

Cet insight explique en partie pourquoi la réflexion FLOW a progressivement évolué vers le modèle :

Party → Agreement → Demand → Decision → Execution

plutôt que vers un débat classique entre ERP, OMS, WMS ou TMS.