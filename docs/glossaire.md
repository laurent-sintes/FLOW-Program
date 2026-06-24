# Glossaire FLOW

Ce glossaire établit le langage commun du programme. Les définitions sont volontairement orientées métier et architecture ; elles évolueront avec le référentiel.

## A

### Accord / Agreement

Objet qui porte les termes d’un engagement entre des parties. Il aide à expliquer les différences entre les contextes Achat, B2B et B2C, sans les réduire à une application ou à un processus.

### ADR — Architecture Decision Record

Document qui formalise une décision d’architecture : son contexte, les options considérées, la décision retenue et ses conséquences.

### Allocation

Décision de réserver, prioriser ou affecter une ressource à une demande, selon des règles métier explicites.

### API First

Principe selon lequel les capacités sont conçues pour être consommées au travers d’interfaces contractuelles et réutilisables, plutôt que seulement par une expérience donnée.

## C

### Capacité

Ce que l’entreprise doit durablement être capable de faire pour assumer une responsabilité. Une capacité peut être mise en œuvre par plusieurs produits, équipes ou solutions.

### Case

Objet métier central qui représente une demande dans la durée. Il conserve son intention, son contexte, ses engagements, les décisions qui le font progresser, les événements, les actions, les ressources et les documents associés.

### Case Management

Approche d’orchestration adaptée aux demandes qui traversent plusieurs domaines, décisions et étapes d’exécution, sans imposer un déroulé unique à l’avance. Le Case en constitue l’unité de pilotage.

### CEP — Complex Event Processing

Traitement d’événements permettant de détecter des situations ou des motifs significatifs à partir de plusieurs événements.

### Cohérence opérationnelle

Propriété selon laquelle les acteurs disposent d’informations suffisamment alignées pour prendre et exécuter des décisions fiables. Elle ne suppose pas nécessairement un temps réel absolu.

## D

### DataHub

Dispositif de partage et de mise à disposition de données ou de projections, au service de la cohérence opérationnelle entre domaines.

### Donnée de référence / donnée partagée

Donnée nécessaire à plusieurs décisions ou domaines, dont la responsabilité est attribuée, la qualité gouvernée, la définition vérifiée et la disponibilité assurée. Elle ne suppose pas une base de données unique ni une catégorie héritée d’un ERP.

### Décision

Choix explicite qui fait progresser le traitement d’un Case. Une décision s’appuie sur des faits, des données et des règles de comportement ; elle produit un résultat traçable, susceptible de créer un engagement, de mobiliser une ressource ou de déclencher une action.

### Demande / Demand

Expression d’un besoin ou d’une intention à traiter. La demande constitue un objet de pilotage plus stable qu’un processus ou qu’une application et peut être représentée par un Case.

### Document

Pièce opérationnelle ou financière associée à un Case, telle qu’une facture, un bon de livraison, un bon de retour, un avoir, un contrat ou une preuve de remise. Un document peut être généré, reçu, validé ou référencé au cours du traitement.

### Domaine

Espace cohérent de responsabilités métier durables. Les domaines sont découverts à partir des problèmes de l’entreprise ; ils ne se déduisent pas mécaniquement de l’organisation existante.

## E

### Engagement

Promesse ou obligation envers une partie prenante, qui peut porter sur une disponibilité, une livraison, un service, un prix ou une autre condition commerciale.

### Événement

Signal publié lorsqu’un fait ou un état métier a changé, afin d’informer d’autres domaines ou consommateurs. Un événement ne décrit pas toute la réalité métier : il annonce qu’une évolution significative s’est produite.

### Experience Agnostic

Principe selon lequel FLOW expose des capacités réutilisables sans imposer les interfaces, parcours ou outils d’engagement qui les consomment.

## F

### Fonctionnalité

Comportement concret offert par un produit ou une solution. Une fonctionnalité contribue à une capacité, sans définir à elle seule la responsabilité métier.

### Fait

Réalité métier observée à un instant donné, utilisée pour instruire une décision ou comprendre l’état d’un Case : stock disponible, contrat actif, capacité restante, document reçu ou statut d’une demande.

## I

### Insight

Constat, hypothèse, apprentissage ou conviction issu des observations du programme. Un insight peut nourrir la vision, un principe directeur ou une décision, mais il n’est pas encore une règle stable.

### Inventory Visibility

Capacité de rendre visibles les ressources de stock et leur contexte d’usage, à l’échelle pertinente de l’entreprise.

## P

### Plateforme d’entreprise

Ensemble de capacités partagées, gouvernées et réutilisables, conçu pour servir plusieurs domaines, marques, canaux et business models.

### Principe directeur

Règle durable qui oriente les choix de conception et permet d’évaluer leur cohérence avec l’ambition de FLOW.

### Produit

Périmètre de gouvernance autonome par lequel une ou plusieurs capacités sont exposées, opérées et font l’objet d’une évolution continue au contact de leurs consommateurs, clients ou utilisateurs.

### Projection de données

Vue de données construite pour un usage ou une décision donnée, sans prétendre remplacer la responsabilité du domaine source.

## R

### Responsabilité

Mission durable que l’entreprise doit assumer. Une responsabilité constitue l’ancrage entre un domaine et les capacités nécessaires pour l’exercer.

### Règle

Expression d’un comportement métier attendu : la manière dont l’entreprise doit réagir, décider ou agir dans une situation donnée. Une règle peut rendre une décision automatiquement, encadrer une décision humaine, déclencher une action, calculer une priorité ou interdire une action.

## S

### Solution

Assemblage concret de produits, fonctionnalités, API, événements, interfaces et traitements destiné à répondre à un besoin dans un contexte donné.

### Supply

Domaine qui porte les responsabilités relatives à la disponibilité, à la mobilisation, à l’allocation et à l’exécution des ressources.

## T

### Tenant

Notion de gouvernance qui représente une unité à laquelle s’appliquent des règles, données ou droits distincts : marque, enseigne, pays ou autre périmètre pertinent.
