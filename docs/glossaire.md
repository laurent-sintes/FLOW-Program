# Glossaire FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Tous lecteurs, Contributeur</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>12 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Stabiliser le vocabulaire et retrouver les pages de référence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Ce glossaire établit le langage commun du programme FLOW.

Il sert aussi d'index vers les pages qui approfondissent les concepts structurants.

## Index des concepts structurants

| Concept | Pages de référence |
| --- | --- |
| Accord / Agreement | [Concepts clés](vision/concepts-cles.md#agreement) · [Agreement comme pivot](insights/agreement-comme-pivot.md) · [Product Agreement Catalog](architecture-cible/produits/product-agreement-catalog.md) |
| Arbitrage | [Concepts clés](vision/concepts-cles.md#arbitrage) · [Hotspots de la vision](vision/vision-detaillee/4-hotspots.md) |
| Case | [Concepts clés](vision/concepts-cles.md#case) · [Principe 06](principes-directeurs/6-demande-objet-metier-central-orchestration.md) · [Socle Case Management](architecture-cible/produits/socle-case-management.md) |
| Colonne vertébrale opérationnelle | [Concepts clés](vision/concepts-cles.md#colonne-vertebrale-operationnelle) · [Vision](vision/vision.md#ce-que-porte-la-plateforme) · [Architecture cible](architecture-cible/index.md) |
| Contrat de données | [Principe 08](principes-directeurs/8-gouverner-la-donnee-en-transit.md) · [Insight dédié](insights/gouverner-donnees-en-transit.md) · [Gouvernance des données en transit](architecture-cible/produits/gouvernance-donnees-transit.md) |
| Bon niveau de commun | [Vision](vision/vision.md#ambition-converger-sans-necessairement-uniformiser) · [Ambition détaillée](vision/vision-detaillee/1-ambition.md) · [Insight convergence](insights/convergence-federation-uniformisation.md) |
| Demande / Demand | [Concepts clés](vision/concepts-cles.md#demande-demand) · [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md) · [Socle Case Management](architecture-cible/produits/socle-case-management.md) |
| Engagement / Demand / Fulfillment / Supply | [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md#engagement-demand-fulfillment-supply-depasser-achat-vente) · [Principe 04](principes-directeurs/4-separer-demand-et-supply.md) · [Architecture cible](architecture-cible/overview-plateforme-flow.md) |
| Donnée au repos | [Principe 07](principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) |
| Donnée en transit | [Principe 08](principes-directeurs/8-gouverner-la-donnee-en-transit.md) · [Gouvernance des données en transit](architecture-cible/produits/gouvernance-donnees-transit.md) |
| Engagement | [Vision](vision/vision.md#ce-que-porte-la-plateforme) · [Ruptures](vision/vision-detaillee/2-ruptures-structurantes.md#engagement-demand-fulfillment-supply-depasser-achat-vente) · [Principe 04](principes-directeurs/4-separer-demand-et-supply.md) |
| Fulfillment Network / Réseau d'exécution | [Concepts clés](vision/concepts-cles.md#fulfillment-network-reseau-dexecution) · [Architecture cible](architecture-cible/overview-plateforme-flow.md) · [Fiche produit](architecture-cible/produits/fulfillment-network-configuration.md) |
| Hotspot | [Hotspots de la vision](vision/vision-detaillee/4-hotspots.md) · [Section Hotspots](hotspots/index.md) |
| Plateforme Demand | [Concepts clés](vision/concepts-cles.md#plateforme-demand) · [Solution FLOW](vision/vision-detaillee/3-plateforme-flow.md) · [Architecture cible](architecture-cible/index.md) |
| Product Agreement Catalog | [Fiche produit](architecture-cible/produits/product-agreement-catalog.md) · [Hotspot PLM / catalogue](hotspots/plm-catalogue-article-ean.md) |
| Source de référence / Projection | [Concepts clés](vision/concepts-cles.md#source-de-reference-projection) · [Principe 07](principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) · [Pattern dédié](architecture-cible/patterns/sources-reference-projections-vues.md) |
| Stock Unifié | [Concepts clés](vision/concepts-cles.md#stock-unifie) · [Fiche produit](architecture-cible/produits/stock-unifie.md) · [Inventory Visibility](insights/inventory-visibility-capacite-d-entreprise.md) |
| Supply Service Registry | [Fiche produit](architecture-cible/produits/supply-service-registry.md) |
| Vues 360 | [Concepts clés](vision/concepts-cles.md#vues-360) · [Fiche produit](architecture-cible/produits/vues-360.md) |

## A

### Accord / Agreement

Objet qui porte les termes d'un engagement entre des parties : conditions, prix, priorités, droits, contraintes ou règles de traitement.

Dans FLOW, l'Agreement permet de gérer des variations métier sans multiplier les processus ou les types de commande.

### Allocation

Décision de réserver, prioriser ou affecter une ressource à une demande selon des règles explicites.

### API

Interface contractuelle permettant à un consommateur d'appeler une capacité exposée par un produit ou un domaine.

### Arbitrage

Choix de programme, d'architecture ou de gouvernance qui doit être rendu explicite avant de stabiliser une cible, une frontière de responsabilité ou une trajectoire.

Un arbitrage ne doit pas être confondu avec une décision métier exécutée par FLOW dans le traitement d'un Case.

### Article / EAN / Product Variant

Granularité produit fine, souvent nécessaire pour vendre, promettre, réserver, allouer et exécuter.

Le hotspot PLM / catalogue pose la question de savoir si FLOW doit consommer une projection au niveau Article / EAN plutôt que dépendre directement de la structure PLM.

## B

### Bon niveau de commun

Principe selon lequel la convergence ne consiste pas à appliquer un modèle unique partout.

Selon la responsabilité, FLOW peut rendre une capacité commune, unifier, standardiser, fédérer ou différencier.

### B2B — Business to Business

Modèle dans lequel l'entreprise vend à des clients professionnels, distributeurs, franchisés, agents ou partenaires commerciaux.

### BRD — Boardriders

Périmètre issu de Boardriders dans le programme FLOW, historiquement plus orienté B2B / wholesale puis adapté au retail et à l'omnicanal.

## C

### Capacité

Ce que l'entreprise doit durablement être capable de faire pour assumer une responsabilité.

Une capacité peut être exposée par un produit, une application, une équipe ou un service.

### Capacités d'intégration des systèmes réintégrés

Capacités minimales nécessaires pour conserver un service existant autour de FLOW : APIs, événements, statuts, documents, identifiants de corrélation, supervision, reprise et réconciliation.

### Case

Objet métier qui représente une demande dans la durée.

Il conserve intention, contexte, décisions, événements, documents, ressources, actions et état courant.

### Case Management

Approche d'orchestration adaptée aux demandes longues, transverses ou variables, qui ne suivent pas toujours un processus linéaire fixé à l'avance.

### CBS

SI composé de modules .NET sur mesure autour des commandes d'achat fournisseur, de la collaboration fournisseur, de la livraison amont, de la packing list et de la conformité documentaire.

CBS est un domaine spécialisé consommateur et contributeur potentiel de FLOW.

### C-LOG

Acteur Supply / logistique du paysage GBM.

C-LOG ne doit pas être réduit à un EAI : il peut porter des responsabilités d'entrepôt, transport, stock, événements d'exécution et parfois décision de fulfillment.

### Colonne vertébrale opérationnelle

Responsabilités communes que FLOW porte pour faire fonctionner le SI comme un ensemble cohérent : demandes, décisions, statuts, événements, stock, promesses, allocations et orchestration transverse.

### Command

Nature d'information représentant une intention adressée à un système ou domaine pour demander une action.

### Contrat de données

Engagement durable décrivant comment une information est publiée, consommée, supervisée et réconciliée.

Il précise notamment source de référence, consommateurs, mode d'échange, granularité, fraîcheur, qualité et mécanismes de reprise.

## D

### Demi-flux

Intuition d'architecture qui sépare la publication d'une information de sa consommation.

Le demi-flux prépare une gouvernance par contrats de données.

### Demand / Demande

Expression d'un besoin ou d'une intention à traiter.

La demande constitue le point de départ de FLOW : comprendre, décider, promettre, satisfaire et expliquer.

Elle doit être distinguée du [Fulfillment](#fulfillment), qui décide comment la servir, et de [Supply](#supply), qui porte les ressources et contraintes mobilisables.

### Demand & Fulfillment

Ensemble des responsabilités permettant de recevoir une demande, l'instruire, décider si et comment elle peut être servie, puis piloter son exécution.

Dans cette expression, Demand porte l'intention qualifiée et la [promesse](#promesse) à tenir ; [Fulfillment](#fulfillment) porte l'arbitrage opérationnel entre cette demande et les capacités [Supply](#supply).

### Décision

Choix explicite qui fait progresser le traitement d'un Case.

Une décision s'appuie sur des faits, des données, des règles ou policies, et produit un résultat traçable.

Dans FLOW, une décision est une fonction métier du Case Management et ne doit pas être confondue avec un arbitrage de programme.

### Document

Pièce opérationnelle, commerciale, logistique ou financière associée à un Case : facture, bon de livraison, bon de retour, avoir, packing list, contrat ou preuve.

### Donnée au repos

Information stockée, maintenue ou consultée dans un domaine, une application, une base, un référentiel ou une projection.

### Donnée en transit

Information qui circule entre domaines, applications ou plateformes.

Dans FLOW, elle doit être gouvernée par contrat de données plutôt que traitée comme un simple flux technique opportuniste.

### Donnée de référence / donnée partagée

Information nécessaire à plusieurs usages ou domaines, dont la responsabilité, la qualité et la disponibilité sont gouvernées.

Elle ne suppose pas une base unique ni une catégorie ERP de type Master Data.

## E

### Engagement

Espace de relation qui capte l'intention et porte les parcours, interfaces, canaux, négociations ou interactions avec un client, partenaire, fournisseur ou collaborateur.

Dans FLOW, Engagement est adhérent au cœur [Demand & Fulfillment](#demand-fulfillment) : il peut créer une demande, consulter une promesse, suivre un Case ou publier des événements, mais il ne constitue pas le cœur de FLOW.

### ERP — Enterprise Resource Planning

Socle applicatif de gestion transactionnelle.

Dans FLOW, l'ERP est distingué des responsabilités de demande, de promesse, d'orchestration et de cycle de vie transverse.

### Event / Événement

Signal indiquant qu'un fait ou un état métier significatif a changé.

Un événement est publié pour être consommé par d'autres domaines ou projections.

## F

### Fact / Fait

Réalité métier observée, reçue ou calculée à un instant donné.

Un fait peut servir à constater, décider, promettre, allouer ou expliquer.

### Flux projet

Échange conçu pour répondre à un besoin local de projet, souvent sans gouvernance durable des producteurs, consommateurs, fraîcheur et qualité.

### Fulfillment

Capacité de décision opérationnelle qui transforme une [Demand / Demande](#demand-demande) qualifiée en trajectoire d'exécution.

Le Fulfillment arbitre entre promesse, stock, priorités, contraintes [Supply](#supply), règles métier et événements observés pour décider comment servir une demande.

Il ne se réduit pas à la logistique physique : préparation, livraison et retour sont des actes d'exécution, tandis que le Fulfillment porte aussi la décision de promettre, réserver, allouer, splitter, reporter, substituer ou ouvrir une exception.

### Fulfillment Network / Réseau d'exécution

Ensemble des lieux, partenaires, services, capacités, contraintes et ressources mobilisables pour satisfaire une demande.

### Fournisseur / Vendor

Partie qui fournit un produit ou un service.

Dans FLOW, le fournisseur ne doit pas être confondu avec l'usine, l'agent, l'adresse de commande ou l'entité de facturation.

## G

### GBM — Groupe Beaumanoir

Périmètre des marques historiques du Groupe Beaumanoir, historiquement retail, ouvert ensuite au e-commerce puis plus difficilement au B2B.

### Golden Source / Source of Record

Termes MDM proches de la notion FLOW de source de référence.

Ils désignent une source reconnue comme faisant autorité pour un usage, un consommateur, une décision ou un contexte donné.

Dans FLOW, on préfère l'expression source de référence.

### Granularité d'échange

Échelle d'un échange d'information : unitaire, masse, événement, lot, snapshot ou flux continu.

## H

### Hotspot

Sujet de tension métier ou architecture qui nécessite une analyse avant d'être transformé en principe, arbitrage ou architecture cible.

## I

### Information

Donnée structurée suffisamment complète pour porter un sens métier.

Si on la découpe davantage, on perd le sens utile pour le métier, la décision ou le système.

### Insight

Constat, hypothèse, apprentissage ou conviction issu des observations du programme.

### Inventory Visibility

Capacité de rendre visibles les ressources de stock et leur contexte d'usage à l'échelle pertinente de l'entreprise.

## M

### Master Data

Notion historique issue de la distinction master file / transaction file, puis popularisée par les ERP.

Dans FLOW, elle est jugée trop large : les informations doivent être qualifiées par nature et par statut source de référence / projection.

### Master Data Management

Discipline de mise en qualité, gouvernance, consolidation, déduplication et diffusion d'informations partagées.

### Mode d'échange

Manière dont une information circule : API, event, query, stream, batch ou synchronisation.

### Module Négoce

Module StoreLand activé pour certaines marques premium.

Il mélange design commercial, assortment / commercial agreement et commandes d'achat ; FLOW doit découper ces responsabilités avant d'arbitrer quoi reprendre.

### Moteur de règles

Composant qui exécute des règles ou policies pour produire une décision, qualifier un traitement ou adapter un comportement selon le contexte.

## N

### Nature d'information

Catégorie qui induit un comportement commun : command, event, fact, policy, objet métier, document, nomenclature.

### NewStore

OMS BRD qui agrège notamment stock entrepôt SAP et stock magasin Cegid pour porter une partie du cycle de vie commande, de la promesse, de la réservation ou de l'allocation.

### Nomenclature

Ensemble contrôlé de valeurs, codes ou classifications partagés.

## O

### Objet métier

Objet portant une identité, un cycle de vie et la responsabilité de sa cohérence à chaque mise à jour.

### OMS — Order Management System

Système ou ensemble de responsabilités permettant de gérer le cycle de vie des commandes, statuts, orchestration, promesse, réservation ou exécution.

### Orchestration

Coordination de décisions, actions, événements, documents et systèmes autour d'une demande.

## P

### Packing list

Document ou jeu d'informations publié par un fournisseur fabricant pour décrire les objets expédiés et soutenir transport, taxes et conformité.

### Partner function

Rôle porté par une partie dans une relation commerciale ou opérationnelle : vendor, ordering address, invoicing party ou autre rôle spécialisé.

Les partner functions permettent de représenter des chaînes commerciales complexes sans réduire tous les rôles à un fournisseur unique.

### PIM — Product Information Management

Système de gestion et d'enrichissement des informations produit.

Dans FLOW, le PIM relève plutôt du design de l'offre ; FLOW consomme une projection d'exécution.

### PLM — Product Lifecycle Management

Système ou domaine portant la conception et le cycle de vie amont du produit.

### POS — Point of Sale

Système magasin qui observe ou provoque des mouvements de stock.

Le stock temps réel dépend de sa capacité à publier rapidement ces mouvements.

### Policy

Règle, politique, paramètre ou contrainte qui influence une décision ou un comportement.

### Product Agreement Catalog

Projection d'exécution qui met à disposition produits, articles, assortiments, conditions commerciales et agreements nécessaires au traitement d'une demande.

### Produit

Périmètre de gouvernance autonome par lequel une ou plusieurs capacités sont exposées, opérées et améliorées au contact de leurs consommateurs.

### Produit conçu / produit importé

Un produit conçu suit le processus de collection et PLM historique.

Un produit importé est acheté déjà designé par un fournisseur, souvent sous forme de variants / EAN qui ne suivent pas toujours les nomenclatures historiques.

### Projection

Représentation consommée par un domaine, issue d'une ou plusieurs sources et adaptée à son usage.

### Promesse

Obligation ou garantie à tenir sur la capacité à servir une demande : disponibilité, quantité, délai, lieu ou service.

La promesse relève du cœur Demand + Fulfillment : Demand porte la promesse attendue ou déjà donnée ; Fulfillment arbitre la promesse tenable à partir des ressources et contraintes Supply.

## R

### Réassort

Décision ou processus visant à réalimenter un magasin, dépôt, canal ou périmètre en stock.

### Réconciliation

Mécanisme permettant de détecter, expliquer et corriger les écarts entre sources, projections, événements ou systèmes.

### Responsabilité

Mission durable que l'entreprise doit assumer.

Elle constitue l'ancrage entre domaine, capacité, produit et fonctionnalités.

### Règle

Expression d'un comportement métier attendu.

Dans la nomenclature FLOW, une règle est généralement traitée comme une Policy.

## S

### SAP ECC

Socle ERP historique de BRD, fortement intégré et donc difficile à remplacer par lots sans analyse fine des responsabilités.

### SAV — Service après-vente

Famille de demandes client : réclamations, litiges, retours, échanges, remboursements ou incidents.

### Socle Case Management

Produit FLOW qui fournit le runtime et le cadre de développement des Cases.

### Socloz

Composant structurant du paysage GBM autour de l'e-commerce, de l'omnicanal, des stocks et des commandes.

### Source de référence

Application, service ou domaine où une information est créée, validée ou maintenue par un processus responsable, avec un niveau de qualité suffisant pour faire référence pour un usage donné.

Une source de référence ne doit pas être confondue avec une projection, une vue 360 ou un agrégat de consultation.

### Stock Unifié

Capacité d'entreprise qui consolide et expose une vision opérationnelle du stock afin de promettre, réserver, allouer et optimiser le fulfillment.

### StoreLand / STLD

Socle historique majeur du SI GBM, décliné en instances par marque.

### Supply

Domaine qui porte les responsabilités relatives à la disponibilité, à la mobilisation, à l'allocation et à l'exécution des ressources.

Supply expose les ressources, capacités, contraintes et événements que le [Fulfillment](#fulfillment) mobilise pour servir une [Demand / Demande](#demand-demande).

### Supply Service Registry

Référentiel des services Supply consommables par FLOW : API, SLA, contraintes, périmètres, conditions d'appel et événements attendus.

### SRM — Supplier Relationship Management

Référentiel ou système de gestion de la relation fournisseur.

Dans le contexte BRD, SRM est présenté comme référentiel officiel, mais orienté usine et sans mécanisme de synchronisation opérationnel observé avec SAP ou le PLM.

## T

### Tenant

Unité de gouvernance à laquelle s'appliquent des règles, données ou droits distincts : marque, enseigne, pays ou périmètre pertinent.

### TMS — Transport Management System

Système spécialisé dans la planification, l'exécution ou le suivi du transport.

### Transportation Zone

Zone de transport utilisée pour qualifier les contraintes, conditions ou routes d'acheminement associées à un fournisseur, une usine ou un service Supply.

## U

### UR — United Retail

Composant sur mesure .NET / C# du paysage GBM, consolidant les commandes B2C et leur cycle de vie dans un contexte StoreLand multi-instances.

### Usine / Factory

Site de fabrication ou de production.

Dans le contexte BRD, l'usine peut être le point réel de commande et porter des informations comme les lead times, distinctes du fournisseur juridique ou de l'entité de facturation.

Le terme `plant` doit être évité comme nom métier cible tant que son sens n'est pas clarifié : selon le contexte, il peut désigner une usine, un site de production, une capacité de fabrication ou un objet applicatif SAP.

## V

### Vues 360

Projections agrégées autour d'un objet ou d'un acteur : client, fournisseur, commande ou Case.

Elles donnent une lecture transverse en consultation, nourrie par événements, faits, documents, statuts et décisions.

## W

### Wholesale

Modèle de vente à des clients professionnels ou distributeurs.

Dans FLOW, Wholesale doit être analysé par responsabilités : engagement commercial, commandes, stock, promesse, exécution, retours et finance.

### WMS — Warehouse Management System

Système spécialisé dans les opérations d'entrepôt : réception, stockage, préparation, expédition, inventaire ou mouvements physiques.
