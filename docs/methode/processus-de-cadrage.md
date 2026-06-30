# Processus de cadrage

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>PMO, Architecte, Change Manager</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>13 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Cadrer la démarche, les arbitrages Build / Buy et les messages d'accompagnement</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Introduction

Le programme FLOW ne part pas des produits du marché.

Il ne part pas non plus des fonctionnalités.

La conception commence par la compréhension de l'entreprise, de ses contraintes et de ses modèles opérationnels.

La méthodologie projet fait émerger progressivement les capacités à mutualiser à partir des réalités observées sur le terrain.

L'enjeu est de conserver une chaîne logique claire : chaque phase produit un livrable qui devient l'entrée de la phase suivante.

## Périmètre de cet article

Cet article décrit la méthodologie de cadrage et de conception amont du programme FLOW.

Il couvre le passage des observations terrain aux choix d'urbanisme, de capacités, de produits, d'options de solution et de trajectoire Build / Buy.

Il décrit aussi la bascule vers la trajectoire de réalisation : achat d'une solution du marché, construction sur la plateforme, ou combinaison des deux.

Il ne décrit pas encore la méthodologie de delivery détaillée.

La méthode de delivery — organisation des équipes, incréments, backlog de réalisation, pilotage de build, tests, déploiement, run et adoption opérationnelle — fera l'objet d'un article dédié plus tard.

```text
Cet article
    → cadrage
    → compréhension
    → vision
    → principes
    → urbanisme
    → capacités
    → produits à instruire
    → options de solution
    → arbitrage Build / Buy
    → trajectoire de sourcing ou de construction

Article futur
    → delivery
    → construction
    → tests
    → déploiement
    → run
    → adoption
```

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
Fonctionnalités / options de solution
    ↓
Build / Buy
    ↓
Trajectoire Buy ou Build
```

## Vue d'ensemble

![Vue d'ensemble du processus de cadrage FLOW](../assets/images/methodologie-flow-overview.svg)

Cette vue doit être lue comme une chaîne de cadrage et de conception.

On ne passe pas directement d'un irritant terrain à une solution.

On transforme progressivement les observations en choix d'architecture, puis en produits gouvernables, puis en fonctionnalités consommables, puis en trajectoire de réalisation.

## Vocabulaire de cadrage

Cette méthode emploie des termes qui peuvent être compris différemment selon les équipes.

Pour éviter les déceptions sur le niveau de détail attendu, cette page utilise les définitions suivantes.

Ces termes sont aussi stabilisés dans le [glossaire FLOW](../glossaire.md).

| Terme | Définition dans le cadrage FLOW | Exemple |
| --- | --- | --- |
| Existant | Situation réellement observée : applications, usages, flux, irritants, responsabilités implicites. | L'OMS C-LOG orchestre certains flux et délègue d'autres décisions selon les marques. |
| Insight | Compréhension nouvelle issue de l'existant, utile pour orienter la cible. | Le découpage ERP / OMS peut masquer deux centres de décision concurrents. |
| Vision | Ambition commune qui explique pourquoi le programme existe et quel changement de modèle il porte. | Déplacer le centre de gravité du SI de l'ERP vers une plateforme Demand + Fulfillment. |
| Principe directeur | Règle de conception durable qui aide à arbitrer les choix futurs. | Séparer Engagement, Demand, Fulfillment et Supply au lieu de structurer le cœur par `J'achète / Je vends`. |
| Domaine | Grand espace de responsabilité métier durable, indépendant des applications actuelles. | Demand, Fulfillment, Supply, Finance, Engagement. |
| Responsabilité | Mission durable que l'entreprise doit assumer dans un domaine. | Déterminer une promesse client tenable ; exposer les contraintes Supply ; gouverner une source de référence. |
| Capacité | Ce que l'entreprise doit savoir faire durablement pour assumer une responsabilité. | Calculer une disponibilité, réserver du stock, publier un événement, instruire un Case. |
| Produit | Périmètre de gouvernance qui expose, opère et fait évoluer une ou plusieurs capacités. | Stock Unifié, Socle Case Management, Product Agreement Catalog. |
| Fonctionnalité | Usage concret attendu d'un produit ou d'une capacité, sans descendre encore au design détaillé. Pendant le cadrage, une fonctionnalité reste candidate tant qu'elle n'est pas retenue dans une trajectoire. | Rechercher une disponibilité, créer une réservation limitée dans le temps, consulter l'historique d'un Case. |
| Donnée | Élément représenté dans un système, un échange ou un stockage. Une donnée peut être brute, technique ou déjà structurée. | Code article, quantité, identifiant magasin, timestamp, code statut. |
| Information | Donnée contextualisée et qualifiée, suffisamment complète pour porter un sens métier ou soutenir une décision. | Disponibilité d'un article pour un canal, promesse de livraison, statut métier d'un Case. |
| Exigence | Condition attendue pour qu'une capacité, un produit ou une solution soit acceptable. Elle peut venir du métier, de l'architecture, de la sécurité, du run ou de l'intégration. | Le stock doit être consultable par canal ; une décision doit être traçable ; un événement doit être rejouable. |
| Solution | Option de mise en œuvre possible pour couvrir un ensemble de fonctionnalités et contraintes. Pendant le cadrage, plusieurs solutions peuvent rester candidates avant l'arbitrage Build / Buy. | Étendre un OMS existant, acheter une solution de Case Management, construire un socle FLOW. |
| Arbitrage Build / Buy | Décision argumentée entre acheter, construire ou hybrider. | Lancer une RFI éditeur ou préparer une plateforme de développement interne. |
| Delivery | Phase de réalisation, intégration, tests, déploiement, run et adoption. | Développer les Cases, brancher les APIs, exécuter les tests de bout en bout, déployer. |
| Spécification | Description précise nécessaire à la réalisation. Elle appartient au delivery et détaille les règles, écrans, APIs, données, tests ou comportements d'erreur. | Contrat OpenAPI, mapping d'événement, règles de scoring, maquette d'écran, critères d'acceptation. |

Le cadrage ne doit donc pas être lu comme une spécification.

Il sert à stabiliser le bon niveau de raisonnement avant de produire les spécifications : responsabilités, capacités, produits, fonctionnalités, exigences et trajectoire de réalisation.

Si un lecteur cherche directement les règles fines, les champs d'écran, les contrats API complets ou les plans de test, il cherche déjà un livrable de delivery.

---

## Étape 0 — Comprendre l'existant

Question :

> Que nous apprend réellement l'entreprise ?

### Objectif

Cette étape sert à construire une compréhension partagée de la situation réelle.

Il ne s'agit pas encore de concevoir la cible.

Il s'agit de qualifier les faits, les irritants, les écarts entre les organisations, les applications existantes, les responsabilités implicites et les zones de tension.

### Activités

- conduire des interviews ;
- animer des ateliers de découverte ;
- analyser les processus existants ;
- analyser les applications et leurs responsabilités réelles ;
- cartographier les flux et les dépendances majeures ;
- identifier les irritants opérationnels ;
- repérer les divergences entre BRD, GBM et les marques ;
- distinguer les faits établis, les hypothèses et les sujets ouverts.

### Livrables attendus

- panorama applicatif et métier ;
- liste des constats qualifiés ;
- irritants et tensions structurantes ;
- questions ouvertes ;
- premiers insights ;
- éléments de contexte réutilisables dans la suite du programme.

### Critère de sortie

L'étape est suffisamment mûre lorsque l'équipe sait formuler les problèmes réels à résoudre sans les réduire prématurément à une solution ou à une application à remplacer.

### Ce que cette étape apporte à la suivante

Elle fournit la matière brute de la vision : les faits, tensions et insights qui justifient l'ambition cible.

---

## Étape 1 — Construire une vision

Question :

> Quelle est l'ambition commune ?

### Objectif

Cette étape transforme les constats en ambition partagée.

La vision ne doit pas être une liste de fonctionnalités.

Elle doit expliquer pourquoi FLOW existe, quel problème d'entreprise il adresse, et quel changement de modèle il porte.

### Activités

- reformuler les problèmes structurants issus de l'existant ;
- expliciter l'ambition de convergence ;
- distinguer ce qui relève de la plateforme FLOW et ce qui reste autour ;
- définir le récit cible : pourquoi FLOW, pour qui, et à quelle échelle ;
- identifier les promesses de valeur : cohérence, transversalité, réduction des doubles saisies, pilotage de la demande, stock unifié, capacité de décision métier.

### Livrables attendus

- vision cible ;
- problème d'entreprise reformulé ;
- promesse de valeur ;
- périmètre d'intention ;
- premières hypothèses de positionnement de FLOW dans le SI.

### Critère de sortie

L'étape est suffisamment mûre lorsque les parties prenantes peuvent expliquer, avec les mêmes mots, ce que FLOW cherche à devenir et ce qu'il ne cherche pas à devenir.

### Ce que cette étape apporte à la suivante

Elle fournit le cap.

Les principes directeurs peuvent alors être définis comme les règles de conception nécessaires pour protéger cette vision dans les arbitrages futurs.

---

## Étape 2 — Définir les principes directeurs

Question :

> Comment souhaitons-nous concevoir la plateforme ?

### Objectif

Cette étape transforme la vision en règles de conception.

Les principes directeurs servent à éviter que chaque arbitrage soit rejoué de zéro.

Ils formalisent les convictions d'architecture qui guident FLOW : fédérer plutôt qu'uniformiser, articuler Engagement, Demand, Fulfillment et Supply, faire émerger le processus des décisions, faire du MDM par les sources de référence, les projections et les contrats de données plutôt que définir une Master Data indistincte, etc.

### Activités

- identifier les arbitrages récurrents du programme ;
- formuler les convictions d'architecture ;
- expliciter les conséquences pratiques de chaque principe ;
- vérifier que les principes sont utilisables pour arbitrer ;
- relier les principes à des exemples concrets issus de BRD et GBM.

### Livrables attendus

- principes directeurs ;
- implications concrètes ;
- exemples d'application ;
- points de vigilance ;
- critères d'arbitrage.

### Critère de sortie

L'étape est suffisamment mûre lorsque les principes permettent de trancher ou cadrer une discussion d'architecture sans revenir systématiquement aux préférences individuelles.

### Ce que cette étape apporte à la suivante

Elle fournit les garde-fous de l'urbanisation.

La cartographie cible peut alors être construite selon des critères explicites, et non seulement selon l'existant applicatif.

---

## Étape 3 — Urbaniser

Question :

> Quelles sont les missions durables de l'entreprise ?

### Objectif

Cette étape transforme la vision et les principes en structure d'urbanisme.

Elle ne consiste pas à déplacer les applications existantes dans des cases.

Elle consiste à identifier les domaines, responsabilités et frontières durables qui doivent rester compréhensibles au-delà des solutions actuelles.

La chaîne de lecture privilégiée est :

```text
Domaine
    ↓
Responsabilité
```

### Activités

- identifier les grands domaines fonctionnels ;
- clarifier les responsabilités durables ;
- distinguer Engagement, Demand, Supply et Finance ;
- positionner les applications existantes par responsabilité réelle ;
- repérer les responsabilités dispersées entre plusieurs systèmes ;
- identifier les zones à remplacer, conserver, connecter, encapsuler ou clarifier.

### Livrables attendus

- cartographie des domaines ;
- responsabilités par domaine ;
- premières frontières FLOW / hors FLOW ;
- analyse des écarts entre BRD et GBM ;
- positionnement des systèmes existants par responsabilité ;
- sujets ouverts d'urbanisme.

### Critère de sortie

L'étape est suffisamment mûre lorsque l'équipe sait dire où se situe une responsabilité métier, indépendamment du nom de l'application qui la porte aujourd'hui.

### Ce que cette étape apporte à la suivante

Elle fournit les responsabilités stables à partir desquelles on peut identifier les capacités nécessaires.

On passe alors de la question “qui porte quoi ?” à la question “que doit-on savoir faire durablement ?”.

---

## Étape 4 — Identifier les capacités

Question :

> Que doit être capable de faire l'entreprise pour assumer ces responsabilités ?

### Objectif

Cette étape transforme les responsabilités en capacités.

Une capacité décrit ce que l'entreprise doit savoir faire de manière durable, réutilisable et gouvernable.

Elle ne décrit pas encore une application, une équipe ou une fonctionnalité détaillée.

La chaîne de lecture devient :

```text
Responsabilité
    ↓
Capacité
```

### Activités

- identifier les capacités nécessaires pour chaque responsabilité ;
- distinguer les capacités transverses des capacités locales ;
- repérer les capacités à mutualiser dans FLOW ;
- qualifier les informations nécessaires : Command, Event, Fact, Policy, Objet Métier, Document, Nomenclature ;
- distinguer les informations sources et les projections ;
- relier les capacités aux consommateurs attendus.

### Livrables attendus

- catalogue de capacités ;
- description courte de chaque capacité ;
- responsabilité de rattachement ;
- consommateurs cibles ;
- informations manipulées ou exposées ;
- capacités FLOW à instruire ;
- capacités conservées hors FLOW.

### Critère de sortie

L'étape est suffisamment mûre lorsque les capacités peuvent être regroupées en périmètres de gouvernance cohérents, avec des consommateurs identifiés.

### Ce que cette étape apporte à la suivante

Elle fournit la matière pour concevoir les produits FLOW.

Un produit devient alors un périmètre de gouvernance et d'évolution naturelle autour d'une ou plusieurs capacités.

---

## Étape 5 — Concevoir les produits

Question :

> Quel périmètre de gouvernance permet de rendre ces capacités consommables et de les faire évoluer au contact de leurs clients ou utilisateurs ?

### Objectif

Cette étape regroupe les capacités dans des produits gouvernables.

Un produit FLOW n'est pas seulement un composant technique ou une application.

C'est le périmètre autonome par lequel une ou plusieurs capacités sont exposées, opérées, arbitrées et améliorées au fil des usages.

### Livrables attendus

- produits ;
- owners ;
- périmètres de gouvernance ;
- capacités rattachées ;
- consommateurs cibles ;
- backlog initial de cadrage ;
- trajectoire d'évolution.

---

## Étape 6 — Concevoir les fonctionnalités et options de solution

Question :

> Comment les consommateurs utilisent-ils concrètement ces capacités ?

### Objectif

Cette étape transforme les produits et capacités en fonctionnalités consommables et en options de solution.

C'est seulement à ce stade que l'on descend vers les interfaces, API, événements, batchs, écrans, workflows ou intégrations.

Dans cet article, cette étape reste une étape de cadrage.

Elle permet de formuler les options de solution et la trajectoire de réalisation, sans décrire encore la méthode de delivery.

### Livrables attendus

- fonctionnalités attendues ;
- APIs à préciser ;
- événements à préciser ;
- interfaces à préciser ;
- batchs à préciser ;
- projections à préciser ;
- solutions consommatrices envisagées ;
- exigences pour le choix de solution ;
- critères de décision Build / Buy ;
- trajectoire de réalisation envisagée.

### Critère de sortie

L'étape est suffisamment mûre lorsque l'équipe sait décrire ce que la solution doit permettre, quelles contraintes elle doit respecter et quels critères permettront de comparer une construction interne, une solution du marché ou une trajectoire hybride.

### Ce que cette étape apporte à la suivante

Elle fournit le dossier d'arbitrage Build / Buy.

L'équipe peut alors décider si elle cherche d'abord une solution du marché, si elle prépare une construction sur la plateforme, ou si elle combine les deux.

---

## Étape 7 — Arbitrer Build / Buy et préparer la trajectoire

Question :

> Faut-il acheter, construire ou hybrider ?

### Objectif

Cette étape transforme les options de solution en trajectoire de réalisation.

Le choix Build / Buy ne doit pas être posé au début du cadrage, quand le problème est encore mal qualifié.

Il devient pertinent lorsque les capacités attendues, les responsabilités de gouvernance, les consommateurs, les contraintes d'intégration, les informations et les critères de valeur sont suffisamment clairs.

L'objectif n'est pas de choisir entre "logiciel du marché" et "développement interne" par principe.

Il s'agit de choisir la trajectoire qui respecte le mieux les responsabilités cibles, le niveau de commun souhaité, les délais, les risques, les coûts complets, la capacité d'évolution et la gouvernance attendue.

### Activités communes

- stabiliser les cas d'usage et les exigences non négociables ;
- relier chaque exigence aux capacités et produits FLOW concernés ;
- qualifier les contraintes d'intégration avec l'existant ;
- identifier les exigences d'information, d'événements, de sécurité, de traçabilité et de run ;
- évaluer la couverture attendue du marché et la faisabilité d'une construction interne ;
- comparer les coûts complets : licences, build, intégration, migration, run, accompagnement, dette future ;
- formaliser les critères d'arbitrage et les risques ;
- identifier les trajectoires hybrides possibles.

### Variante Buy — Enchaîner RFI, RFP et RFQ

La trajectoire Buy sert à vérifier si une solution du marché peut couvrir le besoin sans déformer les principes FLOW.

Elle enchaîne trois niveaux de consultation :

- RFI : explorer le marché, comprendre les éditeurs, les capacités disponibles, les limites et les architectures proposées ;
- RFP : demander une réponse structurée sur les cas d'usage, les exigences, les intégrations, les informations, la sécurité, la gouvernance et la roadmap ;
- RFQ : chiffrer une cible contractualisable : licences, services, intégration, exploitation, niveaux de service, accompagnement et options.

Cette trajectoire doit rester pilotée par les capacités et responsabilités cibles.

Le risque à éviter est de laisser le vocabulaire ou le découpage d'un éditeur remplacer le modèle FLOW sans arbitrage explicite.

### Variante Build — Préparer la plateforme de développement

La trajectoire Build sert à préparer une construction maîtrisée sur un socle de développement gouverné.

Elle doit enchaîner sur la préparation de la plateforme de développement :

- confirmer le product ownership et les responsabilités d'équipe ;
- définir le backlog initial de réalisation ;
- préparer les environnements de développement, test, recette et démonstration ;
- mettre en place les dépôts, règles de contribution, pipelines CI/CD et contrôles de qualité ;
- définir les standards d'API, d'événements, de contrats de données, de sécurité et d'observabilité ;
- préparer les jeux de données, bouchons, simulateurs et scénarios de test ;
- clarifier le framework de développement attendu pour les Cases, règles, projections, statuts, événements et paramétrages.

Cette trajectoire ne signifie pas que tout doit être développé from scratch.

Elle signifie que le programme assume une responsabilité de construction et doit préparer le socle qui rend cette construction industrialisable, testable, gouvernable et réutilisable.

### Livrables attendus

- décision Build / Buy argumentée ;
- critères de décision et hypothèses ;
- trajectoire Buy, Build ou hybride ;
- dossier RFI / RFP / RFQ si la trajectoire Buy est retenue ;
- cadrage de plateforme de développement si la trajectoire Build est retenue ;
- risques, dépendances, coûts complets et points d'arbitrage restants ;
- préparation de la phase de delivery.

### Critère de sortie

L'étape est suffisamment mûre lorsque le programme sait dire pourquoi il achète, pourquoi il construit, ou pourquoi il combine les deux, avec des critères vérifiables et une trajectoire opérationnelle.

### Ce que cette étape apporte à la suivante

Elle fournit le point d'entrée du delivery.

Dans une trajectoire Buy, le delivery démarre par la consultation marché, la sélection, la contractualisation et l'intégration.

Dans une trajectoire Build, le delivery démarre par la mise en place du socle de développement, du backlog, des environnements et des pratiques d'ingénierie.

---

## Synthèse

La méthodologie FLOW suit une logique progressive de cadrage :

```text
Insights
    ↓
Vision
    ↓
Principes
    ↓
Domaines
    ↓
Responsabilités
    ↓
Capacités
    ↓
Produits
    ↓
Fonctionnalités
    ↓
Options de solution
    ↓
Arbitrage Build / Buy
    ↓
Trajectoire Buy
    → RFI
    → RFP
    → RFQ

ou

Trajectoire Build
    → préparation de la plateforme de développement
    → backlog de réalisation
    → delivery
```

Chaque niveau évite de sauter trop vite à la solution.

C'est ce qui permet de ne pas confondre :

- une application existante avec une responsabilité durable ;
- une responsabilité avec une capacité ;
- une capacité avec un produit ;
- un produit avec une liste de fonctionnalités.

---

## À retenir

Cet article décrit le cadrage de FLOW, pas son delivery.

Le programme FLOW ne cherche pas à partir des applications pour comprendre l'entreprise.

Il cherche à comprendre l'entreprise pour faire émerger les capacités qu'il convient de mutualiser.

Les produits ne sont pas le point de départ de la réflexion. Ils deviennent le périmètre de gouvernance et d'évolution naturelle des capacités au contact de leurs consommateurs.

La chaîne méthodologique protège donc le programme contre une dérive classique : remplacer trop vite des applications sans avoir clarifié les responsabilités, les capacités et les produits cibles.

Le cadrage se termine par une décision Build / Buy explicite.

Cette décision protège le programme contre deux dérives symétriques : acheter trop tôt une solution qui impose son modèle, ou construire trop vite sans avoir préparé le socle de développement, de gouvernance et de run.

La méthodologie de delivery sera documentée séparément lorsqu'il faudra décrire la manière de sélectionner, construire, tester, déployer, opérer et faire adopter les solutions FLOW.
