# Supprimer ERP et OMS ? Une folie !

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Tous lecteurs</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>11 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Lire et maintenir le référentiel FLOW</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Question

Le découpage paraît clair :

- le transactionnel et la master data sont gérés par l'ERP ;
- les problématiques externes de multicanalité sont gérées par l'OMS ;
- les variations de vente ne doivent pas impacter le cœur métier, qui doit rester stable.

Pourquoi fusionner les deux alors que le cycle de vie des règles multi / omnicanales est différent de celui des processus d'entreprise ?

La crainte est que la complexité des canaux de vente vienne interférer avec la stabilité des processus cœur.

## Réponse courte

La crainte est saine.

Si FLOW consistait à fusionner ERP et OMS dans un nouveau gros système qui porterait à la fois la finance, les référentiels, les canaux, les règles omnicanales, la promesse, le stock, les documents et l'exécution, ce serait effectivement une mauvaise idée.

Mais ce n'est pas le raisonnement FLOW.

FLOW ne cherche pas à supprimer l'ERP comme système de référence des écritures, engagements financiers, obligations comptables ou responsabilités transactionnelles stables.

FLOW ne cherche pas non plus à absorber la complexité des interfaces d'engagement ou de vente.

FLOW cherche à sortir d'une opposition trop simple entre :

- un ERP stable, mais trop monolithique ;
- un OMS flexible, mais parfois devenu second cœur opérationnel.

L'objection paraît très crédible tant qu'on raisonne à partir des catégories logicielles.

Elle devient moins solide quand on regarde les responsabilités réellement portées par les systèmes : un ERP legacy et un OMS ne sont pas deux composants complémentaires dessinés selon un modèle cible commun. Ce sont souvent deux systèmes complets, chacun doté de ses propres données, règles, décisions, orchestrations, statuts et processus.

Le bon sujet n'est donc pas :

> Faut-il fusionner ERP et OMS ?

Le bon sujet est :

> Où doivent vivre les responsabilités transverses de Demand + Fulfillment pour qu'elles restent cohérentes sans polluer ni l'ERP, ni les canaux, ni les systèmes d'exécution ?

## Pourquoi l'objection paraît crédible

L'objection paraît crédible parce qu'elle raconte une histoire simple :

- l'ERP porte le cœur stable ;
- l'OMS absorbe les variations omnicanales ;
- le cœur reste protégé.

Cette histoire est utile comme première protection contre la pollution du cœur transactionnel.

Mais elle suppose que l'ERP et l'OMS se partagent naturellement les responsabilités selon une frontière logique.

Or, dans un SI réel, cette frontière est souvent plus historique qu'architecturale.

Un ERP est déjà un système complet. Il porte des référentiels, des transactions, des statuts, des règles, des documents, des décisions implicites ou explicites, et une orchestration de processus d'entreprise.

Un OMS est lui aussi un système complet. Il porte des commandes, des statuts, de l'orchestration, des règles de promesse, d'allocation, de split, de substitution, de priorisation et d'exécution.

La séparation ERP / OMS ne vient donc pas toujours d'un découpage logique cible. Elle vient souvent d'une limite de l'ERP legacy : il ne sait pas absorber proprement le niveau de variation apporté par l'omnicanalité sans complexifier ou rigidifier son cœur.

L'OMS a alors été ajouté comme système spécialisé pour traiter cette variation.

Cela résout un problème local, mais en crée un autre : ERP et OMS deviennent deux monolithes qui ne partagent ni le même modèle, ni les mêmes concepts, ni les mêmes cycles de décision.

FLOW doit donc éviter deux erreurs symétriques :

- croire que l'ERP peut absorber toute la variation omnicanale ;
- croire que l'OMS peut devenir le cœur cible de Demand + Fulfillment sans recréer un monolithe parallèle.

## Ce que la crainte protège

L'objection protège trois principes importants.

### Le cœur ne doit pas être pollué par les canaux

Les règles de vente, d'expérience client, de marketplace, de Ship From Store, de B2B, de retail ou de négoce changent vite.

Les règles comptables, fiscales, de clôture, de valorisation, de conformité ou d'écriture financière ne doivent pas suivre le même rythme.

Il serait dangereux de faire entrer toutes les variations commerciales dans le cœur transactionnel.

### Les cycles de vie sont différents

Une règle de promesse ou de priorisation commerciale peut changer pour une opération, une saison, une marque, un pays, un client ou un canal.

Une règle de facturation, de comptabilisation ou de traçabilité légale doit être gouvernée avec un niveau de stabilité et de contrôle différent.

FLOW doit donc séparer les cycles de vie :

- règles d'engagement ;
- règles de promesse ;
- règles de fulfillment ;
- règles de supply ;
- règles financières et comptables ;
- référentiels et sources de référence.

### Le modèle cible ne doit pas recréer un monolithe

Remplacer un ERP et un OMS par une plateforme unique mal découpée ne résout rien.

Cela déplace seulement la dette architecturale.

La vraie cible est une plateforme cohérente, mais découpée en responsabilités explicites, gouvernées par contrats, APIs, événements, projections et décisions métier.

## Pourquoi ERP + OMS ne suffit pas toujours

Le découpage ERP / OMS est utile, mais il devient fragile lorsque les responsabilités clés de la promesse sont dispersées.

Dans beaucoup de SI retail, l'OMS finit par porter :

- la vision exploitable de la demande ;
- la promesse client ;
- l'allocation ;
- la réservation ;
- les substitutions ;
- les splits ;
- les exceptions ;
- les statuts ;
- une partie des règles commerciales ;
- une partie de la disponibilité stock.

L'ERP, de son côté, garde souvent :

- les commandes ou documents transactionnels ;
- les écritures ;
- les référentiels ;
- certains stocks ;
- des statuts ;
- des règles historiques ;
- des dépendances finance / supply / achat.

Le risque n'est alors plus seulement que les canaux polluent l'ERP.

Le risque est d'avoir deux cœurs opérationnels qui doivent se synchroniser en permanence pour reconstituer une vérité métier.

Le problème s'aggrave lorsque les deux systèmes ne partagent pas le découpage cible Demand / Fulfillment / Supply.

Dans un ERP legacy, la commande, le stock, les conditions commerciales, les statuts, la facturation, les documents, les achats, la finance et l'exécution sont souvent entremêlés dans un même modèle transactionnel.

Dans un OMS, la commande, la promesse, l'allocation, le stock disponible, les règles de sourcing, les statuts et les exceptions sont souvent modélisés autour de la vente omnicanale.

Les deux systèmes orchestrent donc une partie du réel, mais avec des modèles différents.

L'intégration ne consiste plus seulement à transférer des données.

Elle consiste à traduire en permanence des décisions, des statuts, des règles et des responsabilités entre deux visions du monde.

Dans cette situation, la question devient : qui porte vraiment la demande ? Qui promet ? Qui arbitre ? Qui explique l'exception ? Qui est source de référence de quel fait ? Qui publie quel événement ?

## Découpage cible FLOW

FLOW ne propose pas une fusion applicative.

FLOW propose un découpage par responsabilités.

| Domaine | Responsabilité cible | Ce qu'il ne doit pas absorber |
| --- | --- | --- |
| Engagement | Capturer l'intention, porter l'expérience, le canal, la relation et la négociation. | La logique profonde de promesse, d'allocation ou d'exécution. |
| Demand | Qualifier la demande, porter le Case, le contexte, les priorités, les statuts et la promesse à tenir. | Les interfaces canal et les écritures financières. |
| Fulfillment | Arbitrer une promesse tenable, choisir une trajectoire, réserver, allouer, split, substituer ou ouvrir une exception. | La comptabilité, la fiscalité, les référentiels amont complets. |
| Supply | Exposer ressources, capacités, contraintes, services d'exécution et événements terrain. | La décision commerciale ou la qualification de la demande. |
| ERP / Finance | Porter les responsabilités financières, comptables, fiscales, de contrôle et les documents transactionnels qui relèvent de son domaine. | Les variations omnicanales rapides et les règles de promesse opérationnelle. |
| Référentiels spécialisés | Créer ou maintenir les données dont ils sont sources de référence. | Les projections d'exécution et les décisions qui appartiennent à FLOW. |

Dans cette lecture, FLOW protège l'ERP au lieu de le polluer.

Il évite aussi que l'OMS devienne un deuxième monolithe omnicanal où s'empilent toutes les règles.

## Rapprochement avec les hotspots et insights

Cette question prolonge directement l'insight [ERP + OMS : séparation utile ou dette architecturale ?](../insights/erp-oms-separation-ou-plateforme-integree.md).

Elle rejoint aussi le hotspot [Sortie progressive de SAP ECC : découper les responsabilités](../hotspots/sap-ecc-boardriders.md) : la question n'est pas de sortir un bloc applicatif, mais de comprendre quelles responsabilités SAP porte aujourd'hui et lesquelles doivent être réallouées.

Elle éclaire également :

- le principe [Articuler Engagement, Demand, Fulfillment et Supply](../principes-directeurs/4-separer-demand-et-supply.md) ;
- le principe [Le processus émerge des décisions métier](../principes-directeurs/5-le-processus-emerge-des-decisions.md) ;
- le principe [Master Data : des objets maîtres aux sources gouvernées](../principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) ;
- le pattern [Externalisation des décisions métier](../architecture-cible/patterns/externalisation-des-decisions.md) ;
- le pattern [Sources de référence, projections et vues](../architecture-cible/patterns/sources-reference-projections-vues.md).

## Rapprochement avec la proposition de solution

La proposition FLOW est de créer une plateforme Demand + Fulfillment qui centralise la cohérence des demandes et des décisions, pas toutes les responsabilités de l'entreprise.

Cela implique :

- un Case Management pour porter la demande longue ;
- un Stock Unifié pour exposer une disponibilité exploitable ;
- un Product Agreement Catalog pour gouverner les conditions de traitement ;
- un Fulfillment Network Configuration pour connaître les capacités mobilisables ;
- des décisions métier explicites pour éviter que chaque variation devienne une branche de processus ;
- des sources de référence identifiées pour éviter que la plateforme invente des données qu'elle ne contrôle pas ;
- des projections pour servir les usages sans déformer le modèle source ;
- des contrats d'API et d'événements pour articuler ERP, canaux, supply, finance et systèmes spécialisés.

FLOW n'est donc pas un ERP augmenté d'omnicanal.

FLOW n'est pas non plus un OMS renommé.

FLOW est le lieu où l'entreprise rend cohérentes les responsabilités qui ne doivent ni rester enfermées dans l'ERP, ni être dispersées dans les canaux, ni devenir une dette d'intégration autour d'un OMS.

## Ce qu'il faut éviter

| Risque | Pourquoi c'est dangereux | Garde-fou FLOW |
| --- | --- | --- |
| Refaire un monolithe | Toutes les règles changent ensemble, les cycles de vie se mélangent. | Découpage par domaines, produits FLOW, APIs et événements. |
| Polluer l'ERP avec l'omnicanal | Le cœur stable devient dépendant des promotions, canaux, parcours et exceptions commerciales. | ERP limité aux responsabilités financières, transactionnelles et de référence qui lui appartiennent. |
| Faire de l'OMS un second cœur | Les décisions, statuts et stocks se dupliquent entre ERP, OMS et canaux. | Demand + Fulfillment comme responsabilité explicite, avec sources de référence et projections. |
| Mettre toutes les règles dans un moteur opaque | La flexibilité devient illisible et ingouvernable. | Règles et policies tracées, versionnées, expliquées et reliées au Case. |
| Confondre master data et projections | Une vue d'exécution devient faussement source de vérité. | Pattern sources de référence, projections et vues. |
| Découper seulement par logiciel | Les responsabilités métier restent floues derrière les noms ERP / OMS / WMS. | Cartographie par domaines, capacités et décisions. |

## Références externes

Les références externes ne disent pas qu'il faut supprimer ERP et OMS. Elles confortent plutôt l'idée qu'il faut découpler les responsabilités et expliciter les décisions.

- [MACH Alliance - MACH technology](https://machalliance.org/mach-technology) met en avant une architecture modulaire, API-first, cloud-native et headless. Cette approche confirme que la flexibilité des canaux ne doit pas imposer un couplage fort au cœur applicatif.
- [Microsoft Dynamics 365 Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) positionne l'order management comme une orchestration configurable entre fournisseurs, systèmes et règles de fulfillment. Cela confirme que l'enjeu moderne n'est pas seulement de stocker une commande, mais de coordonner des décisions entre systèmes.
- [ASCM - SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) distingue les capacités supply chain comme `Order`, `Fulfill` et `Orchestrate`. Cette séparation soutient l'idée que la commande, l'exécution et l'orchestration ne sont pas une seule responsabilité monolithique.
- [OMG - Case Management Model and Notation](https://www.omg.org/spec/CMMN/) fournit un standard pour modéliser des Cases, utile lorsque le traitement dépend du contexte, d'événements et d'actions non entièrement prévisibles.
- [OMG - Decision Model and Notation](https://www.omg.org/spec/DMN/) fournit un standard pour modéliser des décisions et règles métier séparément des processus. C'est cohérent avec l'idée FLOW : les variations omnicanales doivent être gouvernées par décisions explicites, pas enfouies dans le cœur transactionnel.

## Références spécifiques à l'approche décision

L'approche plateforme + moteur de décision est particulièrement appuyée par trois familles de références.

### Standardiser les décisions

[OMG - Decision Model and Notation](https://www.omg.org/spec/DMN/) est la référence la plus directe.

DMN sert à modéliser des décisions, leurs dépendances, les données d'entrée et la logique exécutable. Il est conçu pour être compréhensible par les métiers, analystes, architectes et développeurs, et utilisable avec BPMN.

Pour FLOW, cela justifie une règle importante : les décisions de promesse, allocation, priorisation, substitution ou exception doivent être explicites, testables et gouvernées, au lieu d'être enfouies dans un workflow ERP, OMS ou canal.

### Exécuter et gouverner les décisions

[Camunda - DMN Decision Engine](https://camunda.com/platform/decision-engine/) illustre l'usage industriel d'un moteur DMN : exécuter des modèles de décision, réutiliser la logique entre plusieurs processus, exposer les décisions par API et conserver l'historique des décisions exécutées.

[IBM Operational Decision Manager](https://www.ibm.com/products/operational-decision-manager) illustre la même famille côté BRMS / decision management : capturer, analyser, automatiser et gouverner des décisions métier fondées sur des règles, avec des mécanismes de test, simulation, permissions et gouvernance.

Ces références soutiennent l'idée qu'un moteur de décision n'est pas un gadget technique. C'est une capacité de gouvernance : elle permet de séparer le cycle de vie des règles métier du cycle de vie des applications qui les appellent.

### Articuler Case, processus et décisions

[OMG - Case Management Model and Notation](https://www.omg.org/spec/CMMN/) complète DMN pour les situations où le traitement dépend du contexte et ne suit pas toujours un workflow prédictible.

Dans FLOW, le Case porte la demande, les faits, les événements et l'historique. Le moteur de décision produit les arbitrages. Les processus ou systèmes d'exécution appliquent ensuite ces arbitrages.

Cette séparation est précisément ce qui permet d'éviter le piège ERP / OMS : ne pas chercher quel logiciel doit absorber toutes les variations, mais définir une plateforme où les décisions transverses sont explicites, gouvernées et appelables par plusieurs domaines.

## À retenir

L'objection est juste si elle vise à empêcher la création d'un nouveau monolithe.

FLOW doit protéger cette vigilance.

Mais conserver la séparation ERP / OMS ne suffit pas si la promesse, l'allocation, la disponibilité, les statuts et les exceptions sont dispersés entre plusieurs systèmes.

La cible n'est pas de fusionner ERP et OMS.

La cible est de clarifier les responsabilités :

- l'ERP porte ce qui relève du cœur transactionnel, financier et référentiel ;
- les canaux portent l'engagement et l'expérience ;
- Supply porte les capacités et l'exécution ;
- FLOW porte Demand + Fulfillment, c'est-à-dire la cohérence des demandes, promesses, décisions et événements transverses.

La stabilité ne vient donc pas d'un ERP qui absorbe tout.

Elle vient d'un découpage clair entre ce qui doit rester stable, ce qui doit varier vite, et ce qui doit arbitrer entre les deux.
