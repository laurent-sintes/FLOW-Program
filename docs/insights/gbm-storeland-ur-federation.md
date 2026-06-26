# GBM : StoreLand par marque, UR et besoin de fédération

## Contexte

Groupe Beaumanoir possède une histoire très retail, construite autour de marques et d'enseignes fortement différenciées.

Cette histoire s'est traduite dans le système d'information par une séparation forte des marques.

Historiquement, il existe une instance StoreLand par marque afin de conserver :

- les spécificités des marques ;
- les règles propres aux enseignes ;
- les modes de fonctionnement locaux ;
- les différences de business model.

Cette architecture a donc permis de préserver l'autonomie locale.

## Limite du modèle ségrégé

Avec le temps, ce modèle entièrement ségrégé a montré ses limites.

Certaines commandes, certains événements et certains cycles de vie ne peuvent plus être traités uniquement dans le périmètre d'une marque ou d'une instance StoreLand.

Le groupe a besoin de gérer :

- des cycles de vie de commandes transverses ;
- des parcours omnicanaux ;
- des règles partagées ;
- une vision groupe ;
- des capacités communes ;
- une gouvernance plus cohérente.

## Apparition de UR — United Retail

Pour répondre à ces besoins, GBM a dû ajouter un applicatif sur mesure appelé UR, pour United Retail.

UR consolide les commandes B2C et leur cycle de vie dans un contexte où StoreLand est fragmenté par marque.

Ce point est essentiel : UR n'est pas apparu par hasard.

UR est apparu parce qu'une architecture totalement ségrégée par marque ne suffisait plus à traiter certains besoins transverses du groupe.

UR porte notamment des responsabilités de statuts, retours, remboursements, litiges, points fidélité et réintégration stock.

## Insight FLOW

L'existence de UR démontre une tension fondamentale :

- les marques ont besoin de conserver leurs spécificités ;
- le groupe a besoin de mutualiser et gouverner certaines capacités.

Le problème n'est donc pas de choisir entre centralisation et autonomie.

Le problème est de définir quelles responsabilités doivent rester locales et quelles responsabilités doivent être fédérées, partagées ou centralisées.

UR est donc moins une simple application à remplacer qu'une trace architecturale d'un manque de transversalité dans le SI existant.

## Conséquence pour FLOW

FLOW doit permettre des business models variables, adaptés aux situations, sans recréer des silos applicatifs complets.

La plateforme doit donc être :

- moins silotée ;
- plus fédérée ;
- capable de mutualiser certaines capacités ;
- capable de préserver les spécificités utiles ;
- gouvernée à l'échelle du groupe lorsque les responsabilités deviennent transverses.

Dans une cible FLOW, les responsabilités aujourd'hui portées par UR doivent être évaluées comme candidates à une capacité transverse de type Demand / Order Lifecycle Orchestration.

## Concepts associés

Cet insight prépare directement plusieurs notions clés de FLOW :

- plateforme fédérale ;
- multi-tenant ;
- Shared Business Capabilities ;
- Agreement ;
- Demand Management ;
- Decision Services ;
- Case Management ;
- Order Lifecycle Orchestration.

## À retenir

UR est la preuve historique que certaines capacités ne peuvent pas rester enfermées dans des silos de marque.

FLOW doit capitaliser sur cet enseignement : préserver l'autonomie des marques, mais gouverner au niveau groupe les responsabilités qui deviennent transverses.