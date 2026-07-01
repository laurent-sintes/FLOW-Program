# Embarquement différencié de la Core Team

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Change Manager, Sponsor, Métier</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>7 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer l'adoption et les changements de posture</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

La Core Team FLOW rassemble des profils très différents : experts business, direction de projet, Product Managers ou Product Owners, architectes IT, responsables d'application, profils habitués à intégrer un progiciel et profils habitués à développer une application sur mesure.

Cette diversité est une richesse, mais elle crée un risque d'embarquement inégal.

Tous les membres de la Core Team n'ont pas :

- le même bagage IT ;
- la même expérience des plateformes ;
- le même niveau d'abstraction ;
- la même familiarité avec les patterns d'architecture ;
- la même attente vis-à-vis du programme ;
- le même type de contribution utile.

L'objectif du Change Management n'est donc pas de rendre tout le monde architecte plateforme.

L'objectif est de donner à chacun le bon niveau de compréhension pour contribuer utilement, se sentir légitime et porter un récit commun.

## Problème adressé

FLOW demande de raisonner avec des concepts qui ne sont pas naturels pour tous les profils :

```text
Demand / Fulfillment / Supply
Case Management
Self-contained System
projection locale de décision
source de référence
variabilité gouvernée
plateforme plutôt qu'application
```

Un expert métier peut très bien contribuer aux exigences, aux irritants et aux règles sans être à l'aise avec les patterns de plateforme.

Un responsable d'application peut être très solide pour expliquer le fonctionnement existant, mais se sentir moins légitime lorsque la discussion passe au découpage produit cible.

Un profil habitué à acheter et intégrer un progiciel peut chercher le bon module ou le bon éditeur, alors que FLOW demande parfois de concevoir une capacité de plateforme.

Un profil habitué au sur-mesure local peut chercher une réponse rapide à un besoin précis, alors que FLOW demande de préserver une responsabilité commune et durable.

Ces écarts ne sont pas des faiblesses individuelles.

Ce sont des positions de lecture différentes.

## Principe

> La vision FLOW doit être partagée, mais l'implication doit être différenciée.
>
> Chaque membre de la Core Team doit comprendre le récit commun, puis contribuer au niveau où sa compétence apporte le plus de valeur : exigence, usage, arbitrage, architecture, produit, intégration ou adoption.

Cette règle évite deux erreurs :

- pousser un discours trop abstrait qui exclut les profils métier ou applicatifs ;
- simplifier excessivement la vision au point de perdre les contributeurs qui doivent concevoir la plateforme.

## Niveaux de vision partagée

Tout le monde n'a pas besoin d'aller au même niveau de détail.

Mais les niveaux doivent être explicites.

| Niveau | Objectif | Public typique | Signe de maîtrise |
| --- | --- | --- | --- |
| 1. Récit commun | Comprendre pourquoi FLOW existe et ce qui change. | Toute la Core Team | La personne sait expliquer FLOW sans le réduire à un remplacement d'outil. |
| 2. Vocabulaire commun | Utiliser les notions Demand, Fulfillment, Supply, Case, promesse, source de référence. | Core Team élargie | La personne sait reformuler un sujet avec le vocabulaire FLOW. |
| 3. Contribution structurée | Apporter des exigences, irritants, règles, contraintes ou arbitrages dans le bon cadre. | Métiers, responsables d'application, PM / PO, IT | La personne sait contribuer sans revenir automatiquement à son application ou organisation d'origine. |
| 4. Conception cible | Discuter produits, patterns, responsabilités, projections, APIs et trajectoires. | Architectes, PM / PO, responsables IT, profils plateforme | La personne sait challenger ou enrichir la solution cible. |
| 5. Relais d'adoption | Porter le récit, détecter les incompréhensions et adapter les messages. | Sponsors, Change Managers, managers relais | La personne sait embarquer d'autres acteurs sans déformer le message. |

Le Change Management doit aider chaque profil à atteindre le niveau nécessaire à sa contribution attendue.

Il ne doit pas exiger que tout le monde atteigne le niveau 4.

## Typologie d'embarquement

La segmentation doit être pragmatique.

Elle ne remplace pas les rôles projet officiels.

Elle aide à adapter l'accompagnement.

| Profil de lecture | Apport attendu | Risque si non accompagné | Embarquement recommandé |
| --- | --- | --- | --- |
| Sponsor / direction projet | Arbitrer, prioriser, protéger l'ambition. | Réduire FLOW à un choix d'outil ou à une trajectoire de remplacement applicatif. | Messages courts, arbitrages, risques, valeur, décisions à prendre. |
| Expert business | Expliquer les usages, règles, exceptions, irritants et besoins de satisfaction. | Se sentir exclu lorsque le vocabulaire devient trop architecture. | Ateliers par cas d'usage, exemples concrets, traduction en exigences et règles. |
| Product Manager / Product Owner | Transformer la vision en capacités, fonctionnalités et backlog de cadrage. | Mélanger exigence, solution et arbitrage ; chercher trop tôt le détail de delivery. | Vocabulaire de cadrage, niveaux de spécification, lien entre capacité, fonctionnalité et produit. |
| Architecte IT / profil plateforme | Challenger les responsabilités, patterns, découplages et trajectoires. | Concevoir une cible trop technique ou trop éloignée du récit métier. | Principes directeurs, patterns, produits FLOW, arbitrages d'architecture. |
| Responsable d'application | Expliquer l'existant, les contraintes, interfaces, données et trajectoires. | Défendre l'application existante ou se limiter à l'intégration point à point. | Cartographie par responsabilité, contrats, sources de référence, périmètre conservé ou réintégré. |
| Profil progiciel / intégration | Apporter le réalisme éditeur, processus standard, contraintes d'intégration. | Chercher le module qui couvre le besoin avant d'avoir clarifié la responsabilité cible. | Comparer Build / Buy après clarification des capacités et exigences structurantes. |
| Profil sur-mesure local | Apporter la connaissance fine des usages et adaptations terrain. | Reproduire des solutions locales qui complexifient la plateforme commune. | Distinguer singularité utile, variation gouvernée et cas particulier à résorber. |

## Matrice de suivi d'embarquement

Le suivi doit mesurer un état d'embarquement, pas évaluer les personnes.

Il sert aux Change Managers, PMO et sponsors à savoir où adapter l'accompagnement.

| Dimension | Question de suivi | Niveau 0 | Niveau 1 | Niveau 2 | Niveau 3 |
| --- | --- | --- | --- | --- | --- |
| Compréhension | La personne comprend-elle pourquoi FLOW existe ? | Ne voit qu'un projet outil. | Comprend le récit général. | Relie FLOW aux arbitrages clés. | Sait l'expliquer à d'autres. |
| Vocabulaire | Utilise-t-elle le vocabulaire FLOW ? | Utilise uniquement les catégories historiques. | Reconnaît les termes. | Les utilise dans les ateliers. | Reformule les sujets avec le vocabulaire FLOW. |
| Adhésion | Accepte-t-elle le déplacement de posture ? | Résistance forte ou incompréhension. | Accord de principe. | Adhésion active sur son périmètre. | Devient relais du changement. |
| Implication | Contribue-t-elle au bon niveau ? | Présence passive. | Réagit aux propositions. | Apporte exigences, faits ou contraintes. | Structure ou challenge les options. |
| Confort d'abstraction | Peut-elle suivre les discussions plateforme ? | Perdue dès que le sujet sort du concret. | Suit avec exemples. | Manipule quelques concepts. | Contribue à la conception cible. |
| Contribution attendue | Son rôle dans la construction FLOW est-il clair ? | Non identifié. | Rôle pressenti. | Contribution explicitée. | Contribution tenue et reconnue. |

Cette matrice peut être tenue sous forme simple : personne, profil de lecture, niveau cible, niveau actuel, points de blocage, prochaine action d'accompagnement.

Elle doit rester un outil de pilotage du Change Management.

Elle ne doit pas devenir un outil de jugement individuel.

## Processus d'embarquement recommandé

### 1. Identifier la position de lecture

Pour chaque membre de la Core Team, clarifier :

- son rôle officiel ;
- son univers de référence ;
- son expérience principale : progiciel, intégration, plateforme, sur-mesure, métier, run applicatif, architecture ;
- sa contribution attendue ;
- son niveau cible dans la vision partagée.

### 2. Donner le bon premier récit

Ne pas commencer par les mêmes contenus pour tout le monde.

Exemples :

- un sponsor commence par la vision, la note de choix et les arbitrages ;
- un expert business commence par les questions simples, les hotspots et les cas d'usage ;
- un responsable d'application commence par l'existant, les responsabilités et les contrats ;
- un architecte commence par les principes, produits et patterns.

### 3. Créer des passerelles

Les ateliers doivent aider les profils à changer de niveau.

```text
Irritant terrain
    -> exigence
    -> responsabilité
    -> capacité
    -> produit FLOW
    -> arbitrage ou pattern
```

Cette passerelle permet de co-construire la vision sans demander à tous de parler directement au niveau architecture.

### 4. Mesurer les signaux faibles

Les Change Managers doivent repérer :

- les personnes qui disent oui mais reviennent toujours au modèle existant ;
- les profils qui contribuent moins dès que le sujet devient abstrait ;
- les tensions entre logique progiciel et logique plateforme ;
- les incompréhensions sur ERP / OMS, Demand / Fulfillment ou source de référence ;
- les personnes qui portent déjà le récit et peuvent devenir relais.

### 5. Adapter le plan d'accompagnement

L'accompagnement doit ensuite être différencié :

- capsules de vulgarisation pour les concepts clés ;
- ateliers de reformulation par cas d'usage ;
- séances architecture pour les profils qui doivent contribuer à la cible ;
- temps d'échange individuel pour les personnes clés ;
- supports de lecture courts pour les relais.

## Rôle des Change Managers

Les deux Change Managers doivent porter ce dispositif ensemble.

Le Change Manager interne peut :

- identifier les relais crédibles ;
- repérer les sensibilités politiques ;
- adapter les messages au langage de l'entreprise ;
- détecter les personnes qui décrochent sans le dire.

Le Change Manager externe peut :

- structurer la typologie d'embarquement ;
- challenger les modèles mentaux hérités ;
- repérer les retours implicites au modèle ERP, progiciel ou application locale ;
- aider à formuler les changements de posture.

La valeur vient de leur complémentarité : rendre l'ambition intelligible sans la diluer.

## À lire ensuite

- [Les changements à conduire](changements-a-conduire.md), pour rattacher l'embarquement aux grands messages de transformation.
- [Pourquoi deux Change Managers dans la Core Team FLOW ?](pourquoi-deux-change-managers.md), pour comprendre la gouvernance du dispositif.
- [Questions pour les nouveaux](../faq/questions-pour-les-nouveaux.md), pour disposer de formulations simples.
- [Processus de cadrage](../methode/processus-de-cadrage.md), pour clarifier les niveaux exigence, capacité, fonctionnalité, solution et Build / Buy.

## À retenir

Construire une vision partagée ne signifie pas demander à chacun de contribuer au même niveau d'abstraction.

FLOW doit organiser une contribution différenciée : certains portent les usages, d'autres les arbitrages, d'autres les contraintes applicatives, d'autres les patterns ou la solution cible.

La stratégie de change doit donc mesurer et accompagner la compréhension, l'adhésion et l'implication de chaque membre clé, sans transformer cette mesure en jugement individuel.
