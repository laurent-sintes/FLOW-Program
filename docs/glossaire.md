# Glossaire FLOW

Ce glossaire établit le langage commun du programme. Les définitions sont volontairement orientées métier et architecture ; elles évolueront avec le référentiel.

## Index des concepts structurants

Cette section transforme progressivement le glossaire en point d'entrée vers les pages qui approfondissent les concepts clés. Elle reste volontairement limitée aux notions déjà stables dans le programme.

| Concept | Pages de référence |
| --- | --- |
| Accord / Agreement | [Concepts clés](vision/concepts-cles.md#agreement) · [Agreement comme pivot](insights/agreement-comme-pivot.md) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md#variation-metier-maitriser-sans-rigidifier) |
| Capacités d'intégration des systèmes réintégrés | [Concepts clés](vision/concepts-cles.md#capacites-dintegration-des-systemes-reintegres) · [Hotspot dédié](hotspots/capacites-integration-systemes-reintegres.md) · [Architecture cible](architecture-cible/overview-plateforme-flow.md#colonne-vertebrale-du-si) |
| Case | [Concepts clés](vision/concepts-cles.md#case) · [Principe 06](principes-directeurs/6-demande-objet-metier-central-orchestration.md) · [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md#la-demande-lunite-autonome-de-la-decision-et-de-lorchestration) |
| Colonne vertébrale opérationnelle | [Concepts clés](vision/concepts-cles.md#colonne-vertebrale-operationnelle) · [Vision synthétique](vision/vision-programme-flow.md#ce-que-porte-la-plateforme) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md#colonne-vertebrale-reintegrer-sans-tout-reecrire) |
| Contrat de données | [Concepts clés](vision/concepts-cles.md#contrat-de-donnees) · [Principe 08](principes-directeurs/8-gouverner-la-donnee-en-transit.md) · [Insight dédié](insights/gouverner-donnees-en-transit.md) |
| Convergence pilotée par niveaux | [Vision synthétique](vision/vision-programme-flow.md#ambition-converger-sans-uniformiser) · [Ambition](vision/vision-detaillee/1-ambition-et-contexte.md#opportunite-converger-sans-basculer-dans-un-modele-unique) · [Insight convergence](insights/convergence-federation-uniformisation.md) |
| Demande / Demand | [Concepts clés](vision/concepts-cles.md#demande--demand) · [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md) · [Principe 06](principes-directeurs/6-demande-objet-metier-central-orchestration.md) |
| Demand / Supply | [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md#demand--supply-depasser-achat--vente) · [Principe 04](principes-directeurs/4-separer-demand-et-supply.md) · [Architecture cible](architecture-cible/overview-plateforme-flow.md) |
| Donnée au repos | [Principe 07](principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) · [Concepts clés](vision/concepts-cles.md#source--projection) |
| Donnée en transit | [Principe 08](principes-directeurs/8-gouverner-la-donnee-en-transit.md) · [Insight dédié](insights/gouverner-donnees-en-transit.md) · [Architecture cible](architecture-cible/overview-plateforme-flow.md#donnees-en-transit--des-flux-projet-aux-contrats-gouvernes) |
| Hotspot | [Hotspots de la vision](vision/vision-detaillee/4-hotspots.md) · [Section Hotspots](hotspots/index.md) |
| Plateforme Demand | [Concepts clés](vision/concepts-cles.md#plateforme-demand) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md) · [Principe 02](principes-directeurs/2-flow-comme-plateforme-d-entreprise.md) |
| Réseau d'exécution / Fulfillment Network | [Concepts clés](vision/concepts-cles.md#fulfillment-network--reseau-dexecution) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md#fulfillment-network-decrire-ce-que-le-reseau-sait-faire) · [Architecture cible](architecture-cible/overview-plateforme-flow.md) |
| Source / Projection | [Concepts clés](vision/concepts-cles.md#source--projection) · [Principe 07](principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) |
| Stock Unifié | [Concepts clés](vision/concepts-cles.md#stock-unifie) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md#composants-structurants) · [Inventory Visibility](insights/inventory-visibility-capacite-d-entreprise.md) |
| Vues 360 | [Concepts clés](vision/concepts-cles.md#vues-360) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md#composants-structurants) |

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

### Capacités d'intégration des systèmes réintégrés

Ensemble des capacités techniques nécessaires pour brancher un service existant sur FLOW sans recréer un silo : APIs contractuelles, événements métier, statuts, documents, identifiants de corrélation, supervision, reprise et réconciliation.

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

### Colonne vertébrale opérationnelle

Responsabilités communes que FLOW porte pour faire fonctionner le SI comme un ensemble cohérent : demandes, décisions, statuts, événements, stock, promesses, allocations et orchestration transverse. La colonne vertébrale ne remplace pas tous les services spécialisés ; elle leur donne un point de cohérence commun.

### Command

Nature d’information représentant une intention adressée à un système ou domaine pour demander une action. Une command peut déclencher un traitement, être acceptée, refusée, mise en attente ou produire des événements.

### Commande d’achat

Commande passée auprès d’un fournisseur ou fabricant. Dans FLOW, la question est de savoir si elle doit être portée par FLOW, par l’ERP ou par un domaine spécialisé, selon son rôle dans l’exécution, la disponibilité future et le cycle de vie transverse.

### Commercial agreement

Accord commercial qui définit des conditions, prix, assortiment ou engagements entre parties. Il relève plutôt du domaine de l’engagement commercial, même si FLOW peut devoir en consommer le résultat pour exécuter une demande.

### Contrat de données

Engagement durable décrivant la manière dont une information est publiée, consommée, supervisée et réconciliée entre domaines ou applications. Il précise notamment la source, les consommateurs, le mode d'échange, la granularité, la fraîcheur attendue, la qualité attendue et les mécanismes de reprise.

### Convergence pilotée par niveaux

Approche selon laquelle la convergence ne signifie pas uniformiser partout. Selon la responsabilité concernée, FLOW peut centraliser, unifier, standardiser, fédérer ou différencier.

## D

### DataHub

Dispositif de partage et de mise à disposition de données ou de projections, au service de la cohérence opérationnelle entre domaines.

### Demi-flux

Intuition d'architecture qui sépare la publication d'une information de sa consommation. Le demi-flux permet de sortir d'une logique strictement point-à-point et prépare une gouvernance par contrats de données.

### Demand & Fulfillment

Ensemble des responsabilités qui permettent de recevoir une demande, de l’instruire, de décider si et comment elle peut être servie, puis d’en piloter l’exécution. Dans FLOW, ce périmètre réunit notamment demande, commande, stock, promesse, allocation, événements, exceptions, documents et cycle de vie.

### Donnée au repos

Information stockée, maintenue ou consultée dans un domaine, une application, une base, un référentiel ou une projection. Dans FLOW, la donnée au repos se qualifie d'abord par sa nature et par son statut dans le domaine : source ou projection.

### Donnée de référence / donnée partagée

Donnée nécessaire à plusieurs décisions ou domaines, dont la responsabilité est attribuée, la qualité gouvernée, la définition vérifiée et la disponibilité assurée. Elle ne suppose pas une base de données unique ni une catégorie héritée d’un ERP.

### Donnée en transit

Information qui circule entre domaines, applications ou plateformes. Dans FLOW, elle doit être gouvernée par contrat de données plutôt que traitée comme un simple flux technique opportuniste.

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

### Event / Événement

Nature d’information représentant un signal publié lorsqu’un fait ou un état métier significatif a changé. Un événement ne décrit pas toute la réalité métier : il annonce qu’une évolution significative s’est produite.

### Experience Agnostic

Principe selon lequel FLOW expose des capacités réutilisables sans imposer les interfaces, parcours ou outils d’engagement qui les consomment.

## F

### Fonctionnalité

Comportement concret offert par un produit ou une solution. Une fonctionnalité contribue à une capacité, sans définir à elle seule la responsabilité métier.

### Fact / Fait

Nature d’information représentant une réalité métier observée, reçue ou calculée à un instant donné. Un fact peut servir à constater, décider, promettre, allouer ou expliquer.

### Flux projet

Échange de données conçu pour répondre à un besoin local de projet, souvent entre une application source et une application cible. FLOW cherche à réduire cette logique lorsqu'elle produit de la tuyauterie opportuniste non gouvernée dans la durée.

### Fulfillment

Ensemble des responsabilités permettant d’exécuter une demande ou une commande : disponibilité, promesse, allocation, préparation, livraison, retour, réintégration et suivi d’exécution.

### Fulfillment Network

Voir [Réseau d'exécution](#reseau-dexecution).

## G

### GBM — Groupe Beaumanoir

Périmètre des marques historiques du Groupe Beaumanoir dans le programme FLOW. Son SI est lu comme historiquement retail, ouvert ensuite au e-commerce puis plus difficilement au B2B.

### Golden Source / source faisant foi

Source reconnue comme faisant autorité pour un usage, un consommateur, une décision ou un contexte donné. Dans un SI distribué, une information peut être disponible dans plusieurs sources : la Golden Source n’est donc pas absolue, elle est contextualisée par l’usage.

### Granularité d’échange

Dimension utile pour la conception d’interface, décrivant l’échelle d’un échange d’information. FLOW distinguera notamment les échanges unitaires, ciblés sur un objet ou une action, et les échanges de masse, portant sur un ensemble d’informations.

## H

### Hotspot

Sujet de tension métier ou architecture qui concentre des enjeux de convergence, de décision ou d’arbitrage. Un hotspot n’est pas nécessairement une capacité cible : c’est un point saillant à instruire.

## I

### Information

Donnée structurée suffisamment complète pour porter un sens métier. Si on la découpe davantage, on perd le sens utile pour le métier, la décision ou le système.

### Insight

Constat, hypothèse, apprentissage ou conviction issu des observations du programme. Un insight peut nourrir la vision, un principe directeur ou une décision, mais il n’est pas encore une règle stable.

### Inventory Visibility

Capacité de rendre visibles les ressources de stock et leur contexte d’usage, à l’échelle pertinente de l’entreprise.

## M

### Master Data

Notion historique issue de la distinction entre master file et transaction file, puis popularisée par les ERP comme SAP pour désigner des objets stables contextualisant les transactions. Dans FLOW, cette notion est jugée trop large : les informations doivent être qualifiées par nature et par statut source / projection plutôt que rangées dans une catégorie unique.

### Master Data Management

Discipline visant à mettre en qualité, gouverner, consolider, dédupliquer et diffuser des informations partagées afin d’assurer cohérence, fiabilité et réutilisation. Le MDM ne doit pas être confondu avec la catégorie ERP `Master Data`.

### Mode d’échange

Dimension utile pour la conception d’interface, décrivant comment une information circule entre domaines ou systèmes : event, query, command, synchronization ou stream. Elle ne doit pas être confondue avec la nature d’information utilisée en cartographie fonctionnelle.

### Module Négoce

Module StoreLand activé pour certaines marques premium. Il permet notamment de construire un assortiment, préparer un commercial agreement et passer des commandes d’achat. Son analyse conduit à découpler le design commercial, plutôt dans le domaine engagement, de la commande d’achat et de l’exécution, potentiellement candidates FLOW.

### Moteur de règles

Composant qui exécute des règles ou policies pour produire une décision, qualifier un traitement, appliquer une priorité ou adapter un comportement selon le contexte d’un Case.

## N

### Nature d’information

Catégorie qui induit un comportement commun pour les informations associées. Pour la cartographie fonctionnelle FLOW, les natures retenues sont : command, event, fact, policy, objet métier, document et nomenclature.

### Nomenclature

Nature d’information représentant un ensemble contrôlé de valeurs, codes ou classifications partagés. Une nomenclature stabilise le vocabulaire, les statuts, les catégories ou les classifications utilisées par plusieurs domaines.

## O

### Objet métier

Nature d’information représentant un objet portant une identité, un cycle de vie et la responsabilité de sa cohérence à chaque mise à jour. Un objet métier protège ses invariants et peut produire des événements.

### OMS — Order Management System

Système ou ensemble de responsabilités permettant de gérer le cycle de vie des commandes, leur orchestration, leurs statuts et parfois la promesse, la réservation ou l’exécution. Dans FLOW, il faut distinguer le rôle OMS d’un système existant et les responsabilités cibles de Demand / Order Lifecycle Orchestration.

### Orchestration

Coordination de plusieurs décisions, actions, événements, documents et systèmes autour d’une demande. Dans FLOW, l’orchestration est portée par les Cases et par les capacités qu’ils mobilisent.

## P

### Packing list

Document ou jeu d’informations publié par un fournisseur fabricant pour décrire les objets expédiés. Il contribue à la transparence transport, à l’identification des marchandises, aux obligations de taxes et à la conformité réglementaire du pays de réception.

### PIM — Product Information Management

Système de gestion et d’enrichissement des informations produit. Dans FLOW, le PIM est plutôt positionné dans le design de l’offre et de l’engagement ; FLOW peut consommer une projection produit d’exécution sans devenir un PIM.

### Plateforme Demand

Plateforme centrée sur la demande : elle instruit, décide, promet, orchestre, suit et explique des Cases transverses, en mobilisant les capacités partagées nécessaires au fulfillment.

### Plateforme d’entreprise

Ensemble de capacités partagées, gouvernées et réutilisables, conçu pour servir plusieurs domaines, marques, canaux et business models.

### PLM — Product Lifecycle Management

Système ou domaine portant la conception et le cycle de vie amont du produit. Il peut alimenter le PIM, le référentiel produit d’exécution ou d’autres systèmes contributeurs.

### Policy

Nature d’information représentant une règle, politique, paramètre ou contrainte qui influence une décision ou un comportement. Une policy peut encadrer une décision humaine, automatiser une décision, déclencher une action ou interdire un comportement.

### Principe directeur

Règle durable qui oriente les choix de conception et permet d’évaluer leur cohérence avec l’ambition de FLOW.

### Product Agreement Catalog

Projection d’exécution qui met à disposition les produits, assortiments, conditions commerciales et agreements nécessaires au traitement d’une demande. Il ne remplace pas nécessairement le PIM, le PLM ou les outils de design commercial.

### Produit

Périmètre de gouvernance autonome par lequel une ou plusieurs capacités sont exposées, opérées et font l’objet d’une évolution continue au contact de leurs consommateurs, clients ou utilisateurs.

### Produit d’exécution / Référentiel produit d’exécution

Projection produit plus statique, gouvernée et limitée aux données nécessaires au fulfillment. Elle permet à FLOW de promettre, allouer, orchestrer et exécuter sans absorber la responsabilité de conception ou d’enrichissement de l’offre.

### Projection

Statut d’une information dans un domaine lorsque ce domaine consomme une représentation issue d’une ou plusieurs sources, adaptée à son usage. Une vue, une copie, un cache, un index ou un snapshot sont des formes possibles de projection.

### Promesse

Engagement pris envers un client, un canal ou une partie prenante sur la capacité à servir une demande : disponibilité, quantité, délai, lieu, service ou autre condition d’exécution.

## R

### Réassort

Décision ou processus visant à réalimenter un magasin, dépôt, canal ou périmètre en stock. Le réassort doit être distingué de la visibilité de stock, de l’allocation, de la réservation et de la promesse.

### Réseau d’exécution

Ensemble des lieux, partenaires, services, capacités, contraintes et ressources mobilisables pour satisfaire une demande. Il couvre notamment les entrepôts, magasins, transporteurs, prestataires et capacités Supply.

### Responsabilité

Mission durable que l’entreprise doit assumer. Une responsabilité constitue l’ancrage entre un domaine et les capacités nécessaires pour l’exercer.

### Règle

Expression d’un comportement métier attendu : la manière dont l’entreprise doit réagir, décider ou agir dans une situation donnée. Dans la nomenclature d’information FLOW, une règle est généralement traitée comme une `Policy`.

## S

### SAV — Service après-vente

Ensemble des demandes de service, réclamations, litiges, retours, échanges ou remboursements liés à un client ou utilisateur. Dans FLOW, le SAV peut être lu comme une famille de demandes à instruire, suivre, décider, résoudre et expliquer.

### Socloz

Composant structurant du paysage GBM autour de l’e-commerce, de l’omnicanal, des stocks et des commandes. Son rôle cible doit être clarifié : OMS, orchestration, promesse, stock disponible, réservation ou intégration.

### Solution

Assemblage concret de produits, fonctionnalités, API, événements, interfaces et traitements destiné à répondre à un besoin dans un contexte donné.

### Source

Statut d’une information dans un domaine lorsque ce domaine crée et maintient l’information comme référence pour son périmètre ou son usage. Une information peut être source dans un domaine et projection dans un autre.

### Stock confié

Stock détenu ou exploité dans un contexte où la propriété, la responsabilité commerciale ou la lecture métier peuvent varier selon les groupes. Les stocks confiés peuvent être lus comme B2B côté BRD et comme retail côté GBM, ce qui en fait un révélateur de divergence de modèle.

### Stock Unifié

Capacité d'entreprise qui consolide et expose une vision opérationnelle du stock afin de promettre, réserver, allouer et optimiser le fulfillment selon un contexte business.

### StoreLand / STLD

Socle historique majeur du SI GBM, décliné en instances par marque. StoreLand porte des responsabilités retail, commandes, stocks et opérations associées. Il existe également un StoreLand Fournitures mutualisé pour certains besoins transverses magasins.

### Supply

Domaine qui porte les responsabilités relatives à la disponibilité, à la mobilisation, à l’allocation et à l’exécution des ressources.

### Supply Service Registry

Référentiel des services Supply consommables par FLOW : capacités disponibles, API, SLA, contraintes, périmètres, conditions d’appel et informations nécessaires pour mobiliser le réseau d’exécution.

## T

### Tenant

Notion de gouvernance qui représente une unité à laquelle s’appliquent des règles, données ou droits distincts : marque, enseigne, pays ou autre périmètre pertinent.

## U

### UR — United Retail

Composant sur mesure .NET / C# du paysage GBM, qui consolide les commandes B2C et leur cycle de vie dans un contexte StoreLand multi-instances. UR porte notamment des responsabilités de statuts, retours, remboursements, litiges, points fidélité et réintégration stock.

## V

### Vues 360

Projections agrégées autour d’un objet ou d’un acteur, par exemple client, fournisseur, commande ou Case. Elles donnent une lecture transverse en consultation, nourrie par des événements, faits, documents, statuts et décisions issus de plusieurs domaines.

## W

### Wholesale

Modèle de vente à des clients professionnels ou distributeurs. Dans FLOW, Wholesale est proche du B2B, mais doit être analysé par responsabilités : engagement commercial, commandes, stock, promesse, exécution, retours et finance.
