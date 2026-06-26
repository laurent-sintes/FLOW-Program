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

## B

### B2B — Business to Business

Canal ou modèle commercial dans lequel l’entreprise vend à des clients professionnels, distributeurs, franchisés, agents ou partenaires commerciaux. Dans FLOW, le B2B ne doit pas être défini seulement comme un canal : certaines de ses responsabilités relèvent de l’engagement, d’autres de l’exécution ou du fulfillment.

### BRD — Boardriders

Périmètre issu de Boardriders dans le programme FLOW. Son SI est lu comme historiquement plus orienté B2B / wholesale, puis adapté au retail et à l’omnicanal.

## C

### Capacité

Ce que l’entreprise doit durablement être capable de faire pour assumer une responsabilité. Une capacité peut être mise en œuvre par plusieurs produits, équipes ou solutions.

### Case

Objet métier central qui représente une demande dans la durée. Il conserve son intention, son contexte, ses engagements, les décisions qui le font progresser, les événements, les actions, les ressources et les documents associés.

### Case Management

Approche d’orchestration adaptée aux demandes qui traversent plusieurs domaines, décisions et étapes d’exécution, sans imposer un déroulé unique à l’avance. Le Case en constitue l’unité de pilotage.

### CBS

SI composé de modules développés sur mesure en .NET, portant des processus support autour des commandes d’achat fournisseur, de la collaboration fournisseur, de la livraison amont, de la packing list et de la conformité documentaire. CBS est lu comme un domaine consommateur et contributeur de FLOW, tout en manipulant certaines responsabilités candidates à FLOW comme la commande, le cycle de vie, les statuts et la vision 360.

### CEP — Complex Event Processing

Traitement d’événements permettant de détecter des situations ou des motifs significatifs à partir de plusieurs événements.

### Cegid Y2

Système utilisé notamment pour le back-office retail et le stock magasin dans le paysage BRD. Son positionnement est structurant car il montre que le stock magasin n’est pas porté par SAP.

### C-LOG / EAI

Composant d’intégration et d’exécution logistique observé dans le paysage GBM. Il doit être analysé pour distinguer ce qui relève de l’intégration technique, de la logique métier, de l’exécution et du suivi d’événements.

### Cohérence opérationnelle

Propriété selon laquelle les acteurs disposent d’informations suffisamment alignées pour prendre et exécuter des décisions fiables. Elle ne suppose pas nécessairement un temps réel absolu.

### Commande d’achat

Commande passée auprès d’un fournisseur ou fabricant. Dans FLOW, la question est de savoir si elle doit être portée par FLOW, par l’ERP ou par un domaine spécialisé, selon son rôle dans l’exécution, la disponibilité future et le cycle de vie transverse.

### Commercial agreement

Accord commercial qui définit des conditions, prix, assortiment ou engagements entre parties. Il relève plutôt du domaine de l’engagement commercial, même si FLOW peut devoir en consommer le résultat pour exécuter une demande.

## D

### DataHub

Dispositif de partage et de mise à disposition de données ou de projections, au service de la cohérence opérationnelle entre domaines.

### Demand & Fulfillment

Ensemble des responsabilités qui permettent de recevoir une demande, de l’instruire, de décider si et comment elle peut être servie, puis d’en piloter l’exécution. Dans FLOW, ce périmètre réunit notamment demande, commande, stock, promesse, allocation, événements, exceptions, documents et cycle de vie.

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

### ERP — Enterprise Resource Planning

Socle applicatif de gestion transactionnelle, souvent utilisé pour les achats, ventes, stocks, finance ou référentiels. Dans FLOW, l’ERP doit être distingué des responsabilités d’orchestration transverse, de demande, de promesse et de cycle de vie, tout en restant articulé avec elles.

### Événement

Signal publié lorsqu’un fait ou un état métier a changé, afin d’informer d’autres domaines ou consommateurs. Un événement ne décrit pas toute la réalité métier : il annonce qu’une évolution significative s’est produite.

### Experience Agnostic

Principe selon lequel FLOW expose des capacités réutilisables sans imposer les interfaces, parcours ou outils d’engagement qui les consomment.

## F

### Fonctionnalité

Comportement concret offert par un produit ou une solution. Une fonctionnalité contribue à une capacité, sans définir à elle seule la responsabilité métier.

### Fait

Réalité métier observée à un instant donné, utilisée pour instruire une décision ou comprendre l’état d’un Case : stock disponible, contrat actif, capacité restante, document reçu ou statut d’une demande.

### Fulfillment

Ensemble des responsabilités permettant d’exécuter une demande ou une commande : disponibilité, promesse, allocation, préparation, livraison, retour, réintégration et suivi d’exécution.

## G

### GBM — Groupe Beaumanoir

Périmètre des marques historiques du Groupe Beaumanoir dans le programme FLOW. Son SI est lu comme historiquement retail, ouvert ensuite au e-commerce puis plus difficilement au B2B.

## I

### Insight

Constat, hypothèse, apprentissage ou conviction issu des observations du programme. Un insight peut nourrir la vision, un principe directeur ou une décision, mais il n’est pas encore une règle stable.

### Inventory Visibility

Capacité de rendre visibles les ressources de stock et leur contexte d’usage, à l’échelle pertinente de l’entreprise.

## M

### Module Négoce

Module StoreLand activé pour certaines marques premium. Il permet notamment de construire un assortiment, préparer un commercial agreement et passer des commandes d’achat. Son analyse conduit à découpler le design commercial, plutôt dans le domaine engagement, de la commande d’achat et de l’exécution, potentiellement candidates FLOW.

## O

### OMS — Order Management System

Système ou ensemble de responsabilités permettant de gérer le cycle de vie des commandes, leur orchestration, leurs statuts et parfois la promesse, la réservation ou l’exécution. Dans FLOW, il faut distinguer le rôle OMS d’un système existant et les responsabilités cibles de Demand / Order Lifecycle Orchestration.

## P

### Packing list

Document ou jeu d’informations publié par un fournisseur fabricant pour décrire les objets expédiés. Il contribue à la transparence transport, à l’identification des marchandises, aux obligations de taxes et à la conformité réglementaire du pays de réception.

### PIM — Product Information Management

Système de gestion et d’enrichissement des informations produit. Dans FLOW, le PIM est plutôt positionné dans le design de l’offre et de l’engagement ; FLOW peut consommer une projection produit d’exécution sans devenir un PIM.

### Plateforme d’entreprise

Ensemble de capacités partagées, gouvernées et réutilisables, conçu pour servir plusieurs domaines, marques, canaux et business models.

### PLM — Product Lifecycle Management

Système ou domaine portant la conception et le cycle de vie amont du produit. Il peut alimenter le PIM, le référentiel produit d’exécution ou d’autres systèmes contributeurs.

### Principe directeur

Règle durable qui oriente les choix de conception et permet d’évaluer leur cohérence avec l’ambition de FLOW.

### Produit

Périmètre de gouvernance autonome par lequel une ou plusieurs capacités sont exposées, opérées et font l’objet d’une évolution continue au contact de leurs consommateurs, clients ou utilisateurs.

### Produit d’exécution / Référentiel produit d’exécution

Projection produit plus statique, gouvernée et limitée aux données nécessaires au fulfillment. Elle permet à FLOW de promettre, allouer, orchestrer et exécuter sans absorber la responsabilité de conception ou d’enrichissement de l’offre.

### Projection de données

Vue de données construite pour un usage ou une décision donnée, sans prétendre remplacer la responsabilité du domaine source.

### Promesse

Engagement pris envers un client, un canal ou une partie prenante sur la capacité à servir une demande : disponibilité, quantité, délai, lieu, service ou autre condition d’exécution.

## R

### Réassort

Décision ou processus visant à réalimenter un magasin, dépôt, canal ou périmètre en stock. Le réassort doit être distingué de la visibilité de stock, de l’allocation, de la réservation et de la promesse.

### Responsabilité

Mission durable que l’entreprise doit assumer. Une responsabilité constitue l’ancrage entre un domaine et les capacités nécessaires pour l’exercer.

### Règle

Expression d’un comportement métier attendu : la manière dont l’entreprise doit réagir, décider ou agir dans une situation donnée. Une règle peut rendre une décision automatiquement, encadrer une décision humaine, déclencher une action, calculer une priorité ou interdire une action.

## S

### Socloz

Composant structurant du paysage GBM autour de l’e-commerce, de l’omnicanal, des stocks et des commandes. Son rôle cible doit être clarifié : OMS, orchestration, promesse, stock disponible, réservation ou intégration.

### Solution

Assemblage concret de produits, fonctionnalités, API, événements, interfaces et traitements destiné à répondre à un besoin dans un contexte donné.

### Stock confié

Stock détenu ou exploité dans un contexte où la propriété, la responsabilité commerciale ou la lecture métier peuvent varier selon les groupes. Les stocks confiés peuvent être lus comme B2B côté BRD et comme retail côté GBM, ce qui en fait un révélateur de divergence de modèle.

### StoreLand / STLD

Socle historique majeur du SI GBM, décliné en instances par marque. StoreLand porte des responsabilités retail, commandes, stocks et opérations associées. Il existe également un StoreLand Fournitures mutualisé pour certains besoins transverses magasins.

### Supply

Domaine qui porte les responsabilités relatives à la disponibilité, à la mobilisation, à l’allocation et à l’exécution des ressources.

## T

### Tenant

Notion de gouvernance qui représente une unité à laquelle s’appliquent des règles, données ou droits distincts : marque, enseigne, pays ou autre périmètre pertinent.

## U

### UR — United Retail

Composant sur mesure .NET / C# du paysage GBM, qui consolide les commandes B2C et leur cycle de vie dans un contexte StoreLand multi-instances. UR porte notamment des responsabilités de statuts, retours, remboursements, litiges, points fidélité et réintégration stock.

## W

### Wholesale

Modèle de vente à des clients professionnels ou distributeurs. Dans FLOW, Wholesale est proche du B2B, mais doit être analysé par responsabilités : engagement commercial, commandes, stock, promesse, exécution, retours et finance.
