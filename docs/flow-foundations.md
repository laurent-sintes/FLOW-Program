# FLOW Foundations

## Pourquoi ce document ?

Ce document constitue le point d'entrée du programme FLOW.

Il résume les constats, convictions, concepts et principes qui structurent aujourd'hui la réflexion.

Son objectif est de permettre à un nouvel arrivant — humain ou IA — de comprendre rapidement :

- pourquoi FLOW existe ;
- quel problème de convergence il cherche à résoudre ;
- pourquoi la réponse ne peut pas être une simple centralisation applicative ;
- comment FLOW est conçu ;
- quels principes guident son évolution ;
- où trouver les pages structurantes du référentiel.

## Contexte

FLOW est un programme de transformation mené conjointement pour GBM et BRD.

Le programme a initialement été présenté comme un projet de remplacement d'applications existantes.

```text
GBM : StoreLand / Socloz
BRD : SAP / NewStore
```

Les travaux ont progressivement montré que cette lecture était insuffisante.

Le vrai sujet n'est pas seulement de remplacer des outils.

Le vrai sujet est de réussir une convergence complexe entre des marques, canaux, business models et héritages IT très différents, sans perdre les singularités qui font leur valeur.

FLOW est donc un programme de convergence IT et business model.

Il cherche à identifier ce qui doit devenir commun, transverse et gouverné, tout en laissant vivre ce qui doit rester spécialisé, différencié ou local.

## Le problème fondamental

Les patrimoines BRD et GBM partent de trajectoires différentes.

GBM est plutôt issu d'un SI retail ouvert au e-commerce, puis au B2B.

BRD est plutôt issu d'un SI B2B / wholesale adapté au retail et à l'omnicanal.

Dans les deux cas, les mêmes responsabilités finissent par traverser les marques, canaux, applications, partenaires et business models :

- recevoir une demande ;
- comprendre son contexte ;
- appliquer un Agreement ;
- prendre des décisions ;
- promettre ;
- réserver ou allouer ;
- mobiliser un réseau d'exécution ;
- produire des événements, faits et documents ;
- suivre les exceptions ;
- expliquer ce qui s'est passé.

La question centrale devient donc :

> Comment créer un cœur commun pour ces responsabilités, sans construire un monolithe qui uniformiserait toute l'entreprise ?

## La rupture FLOW

Gérer des commandes ne suffit plus.

FLOW déplace le centre de gravité du système d'information : d'un SI organisé autour de l'ERP, des documents et de la comptabilité, vers une plateforme organisée autour de la demande, du Case, de la décision et de la satisfaction client / utilisateur.

```text
Ancien réflexe
    ERP / documents / comptabilité
    OMS / commande / canal

Nouveau réflexe FLOW
    Demande / Case / décision
    Fulfillment / satisfaction
    Réseau d'exécution
```

## Ce que FLOW n'est pas

FLOW n'est pas un ERP bis.

FLOW n'est pas seulement un OMS.

FLOW n'est pas une plateforme d'engagement client.

FLOW n'est pas un PIM, un CRM, un WMS, un TMS ou un outil Finance.

FLOW n'a pas vocation à remplacer tous les outils existants.

## Ce qu'est FLOW

FLOW est une réponse fédérée à la convergence.

Il prend la forme d'une plateforme Demand d'entreprise, capable de porter les responsabilités communes critiques : demandes, Cases, décisions, stock, réseau d'exécution, promesses, événements, documents et exceptions.

Les consommateurs peuvent rester différenciés.

La plateforme, elle, doit être décloisonnée.

## Les principaux insights

- FLOW n'est probablement pas un OMS : le sujet dépasse l'omnicanalité vente.
- FLOW réconcilie des responsabilités ERP et OMS dans une plateforme Demand.
- Les demandes sont plus stables que les processus, canaux ou organisations.
- Agreement est le pivot qui permet de piloter les variations de traitement.
- La variation métier doit être pilotée par le contexte, les Agreements et les règles, sans multiplication de processus spécialisés.
- Le SAV est une demande comme les autres lorsqu'il faut suivre, décider, résoudre et expliquer.
- Converger ne signifie pas uniformiser : la convergence se pilote par niveaux.
- Les organisations consomment la plateforme ; elles ne doivent pas la structurer.
- Inventory Visibility est une capacité d'entreprise.
- Les informations doivent être qualifiées par nature et par statut Source / Projection plutôt que rangées indistinctement dans “Master Data”.
- La Finance reste un domaine séparé, mais FLOW doit produire les faits et documents utiles à son intégration.

## Premiers produits candidats

La vision actuelle fait émerger les premiers produits candidats suivants :

- Plateforme de Case Management ;
- Stock Unifié ;
- Fulfillment Network / Réseau d'Exécution ;
- Supply Service Registry ;
- Product Agreement Catalog ;
- Vues 360.

Ces produits restent des hypothèses de cadrage.

Ils servent à structurer la discussion sur les capacités, les responsabilités et les frontières de FLOW.

## Adhérences structurantes

### SAP Finance / S/4HANA

La convergence Finance est portée par le programme SAP Finance / migration S/4HANA, hors périmètre FLOW.

Cette trajectoire conserve SAP SD/FI/CO comme socle de facturation B2B, de comptabilité et de contrôle de gestion.

En B2C, les factures peuvent être produites par les systèmes d'engagement client ou de vente, puis intégrées dans SAP.

En B2B, SAP SD demeure le support principal de production de facture et d'intégration native avec FI/CO.

FLOW doit donc s'intégrer avec cette trajectoire plutôt que la remplacer.

La question structurante devient : quels événements opérationnels, faits économiques et documents FLOW doit-il transmettre au domaine Finance ?

## Principes directeurs

Les principes directeurs constituent le cadre de décision durable de FLOW. Ils sont détaillés dans la section [Principes directeurs](principes-directeurs/index.md).

Les principes documentés sont :

1. Converger, c’est fédérer.
2. FLOW comme plateforme d’entreprise.
3. Les domaines avant les structures.
4. Séparer Demand et Supply.
5. Le processus émerge des décisions.
6. La demande comme objet métier central d’orchestration.
7. Qualifier les informations plutôt que parler de Master Data.

## Taxonomie FLOW

```text
Domaine
    ↓
Responsabilité
    ↓
Capacité
    ↓
Produit
    ↓
Fonctionnalité
```

Le produit constitue le périmètre de gouvernance et d'évolution par lequel une ou plusieurs capacités sont rendues consommables et évoluent au contact de leurs clients ou utilisateurs.

## Méthodologie Projet

La méthodologie de cadrage suit une progression volontairement lente :

```text
Existant
    ↓
Vision
    ↓
Principes
    ↓
Domaines / responsabilités
    ↓
Capacités
    ↓
Produits
    ↓
Fonctionnalités / solutions candidates
```

Elle évite de sauter directement des applications existantes vers des solutions.

## Transformation

FLOW est autant une transformation du système d'information qu'une transformation de la manière de penser l'entreprise.

Les changements principaux sont regroupés dans la page [Les changements à conduire avec FLOW](transformation/changements-a-conduire.md).

## Pages de référence

- [Vision du programme FLOW](vision/vision-programme-flow.md)
- [Overview de la plateforme FLOW](architecture-cible/overview-plateforme-flow.md)
- [Journal des insights](insights/journal-des-insights.md)
- [Glossaire FLOW](glossaire.md)

## À retenir

FLOW ne cherche pas à mieux gérer les commandes.

FLOW cherche à mieux satisfaire les demandes.

Sa valeur n'est pas de remplacer toutes les applications.

Sa valeur est de rendre cohérentes les demandes, décisions, ressources, promesses, événements, documents et exceptions qui traversent l'entreprise.

FLOW devient une plateforme qui configure des capacités d'action, pas un grand miroir administratif de l'entreprise.
