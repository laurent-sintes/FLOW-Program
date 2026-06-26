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

Elle devient toutefois problématique lorsque les responsabilités structurantes de l'entreprise — demande, commande, stock, promesse, allocation, exécution, retour, exception — sont dispersées entre plusieurs systèmes qui doivent se synchroniser en permanence.

## Position exprimée par le CTO Beaumanoir

Le CTO de Beaumanoir a exprimé une conviction différente.

Selon lui, la séparation ERP / OMS constitue elle-même une partie du problème.

L'empilement de solutions spécialisées conduit souvent à :

- des synchronisations permanentes ;
- des redondances de données ;
- des responsabilités floues ;
- des arbitrages répartis ;
- une gouvernance complexe ;
- une difficulté à expliquer pourquoi une demande a été acceptée, refusée, partiellement servie ou réorientée.

## Deux visions

### Vision 1 — Best of Breed

ERP + OMS + WMS + TMS + PIM + PLM

Chaque solution est spécialisée.

Les intégrations deviennent le mécanisme principal de cohérence.

Dans cette vision, l'architecture doit constamment transférer des données entre des systèmes qui portent chacun une partie de la vérité opérationnelle.

### Vision 2 — Plateforme intégrée

FLOW Platform

- Agreement
- Demand
- Decision
- Inventory Visibility
- Supply
- Execution
- Case Management

Les responsabilités sont explicites mais réconciliées dans une plateforme cohérente.

L'intégration devient un mécanisme d'extension vers des expériences, des systèmes spécialisés ou des partenaires, plutôt qu'un mécanisme de survie entre ERP et OMS.

## Orientation FLOW

L'orientation de FLOW n'est pas de créer une nouvelle frontière entre ERP, OMS et engagement.

L'orientation est de réconcilier, dans une même plateforme Demand & Fulfillment, les responsabilités qui sont aujourd'hui réparties entre plusieurs systèmes :

- la demande ;
- la commande ;
- le cycle de vie ;
- la promesse ;
- l'allocation ;
- la visibilité stock ;
- les événements ;
- les exceptions ;
- les documents nécessaires au suivi d'un Case ;
- la vision 360 d'une demande ou d'un engagement.

La question n'est donc pas seulement :

> FLOW remplace-t-il un ERP ou un OMS ?

La question devient :

> Quelles responsabilités doivent être réunifiées dans FLOW pour éviter que la cohérence métier dépende de transferts permanents entre ERP, OMS et systèmes périphériques ?

## Conséquence pour FLOW

FLOW ne doit probablement pas être présenté comme le futur OMS du groupe.

FLOW n'est pas non plus le futur ERP.

FLOW est étudié comme une plateforme d'entreprise intégrée construite autour des responsabilités métier plutôt qu'autour des catégories historiques de logiciels.

Cette orientation n'empêche pas de conserver des systèmes spécialisés.

Elle impose en revanche de ne pas disperser les responsabilités centrales du Demand & Fulfillment entre plusieurs systèmes qui devraient ensuite se synchroniser pour reconstruire une vérité commune.

## Importance de cet insight

Cet insight explique en partie pourquoi la réflexion FLOW a progressivement évolué vers le modèle :

Party → Agreement → Demand → Decision → Execution

Il explique aussi pourquoi le Case Management devient structurant : le Case fournit une unité transverse capable de porter une demande longue, ses décisions, ses événements, ses documents, ses exceptions et ses effets sur plusieurs processus ou systèmes.

FLOW n'est donc pas un débat classique entre ERP, OMS, WMS ou TMS.

FLOW cherche à identifier le bon lieu de vérité et d'orchestration pour les responsabilités qui donnent leur cohérence à l'exécution métier.