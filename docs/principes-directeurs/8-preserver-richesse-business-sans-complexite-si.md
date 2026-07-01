# Principe 8 — Préserver la richesse business sans complexifier le SI

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Sponsor</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>7 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

FLOW ne cherche pas l'uniformisation.

Le groupe doit conserver ce qui fait sa richesse : marques différentes, modèles clients, retail, e-commerce, marketplace, wholesale, B2B, B2C, services et promesses différenciées.

Mais cette richesse devient dangereuse si elle est traduite directement dans le SI par des variantes de processus, des modules spécifiques ou des enchaînements de `if / elseif`.

Le risque porte un nom : l'<span class="flow-keyword">explosion combinatoire</span>.

Chaque nouvelle marque, canal, type de client, agreement, règle de stock, promesse ou contrainte Supply peut multiplier le nombre de cas à gérer.

Dans le code ou les workflows, le symptôme est souvent une <span class="flow-keyword">complexité conditionnelle</span> : des règles métier dispersées dans des branches, difficiles à tester, expliquer, faire évoluer ou gouverner.

Dans l'architecture, un autre symptôme apparaît : la <span class="flow-keyword">complexité de dépendance</span>.

Une décision devient fragile lorsqu'elle dépend en temps réel de plusieurs APIs externes, référentiels ou services dont FLOW ne maîtrise ni le SLA, ni la latence, ni la disponibilité.

FLOW doit donc changer de paradigme.

La richesse business doit être préservée, mais la variabilité doit être modélisée, gouvernée et exécutée avec les bons mécanismes.

## Principe

> FLOW ne doit pas transformer la richesse business du groupe en complexité SI.
>
> Les singularités de marque, canal, client, agreement ou service doivent être portées par une variabilité gouvernée : règles, contraintes, policies, modèles de décision, moteurs spécialisés, patterns d'extension et données de configuration.
>
> Une règle métier qui varie doit être explicite, testable, versionnée, observable et gouvernée.
>
> Elle ne doit pas être enfouie dans une chaîne de conditions applicatives.
>
> Une décision critique doit aussi maîtriser ses dépendances : les référentiels nécessaires au calcul doivent être disponibles sous forme de projections locales de décision, et non appelés en cascade au moment de décider.

Ce principe protège deux ambitions en même temps :

- préserver les différences business utiles ;
- éviter que chaque différence crée une dette applicative durable.

## Ce que ce principe ne signifie pas

Ce principe ne dit pas que tout doit être remplacé par un moteur de règles.

Il ne dit pas non plus que l'IA, l'optimisation ou les algorithmes résolvent seuls les problèmes d'architecture.

Il dit que la variabilité business doit être conçue comme un objet de premier ordre.

Selon le cas, elle peut être portée par :

- un moteur de règles ;
- un moteur de contraintes ;
- un modèle de décision ;
- une policy ;
- un pattern d'extension ;
- une configuration gouvernée ;
- un algorithme d'optimisation ;
- une assistance IA pour analyser, proposer, expliquer ou détecter des incohérences.
- une projection locale de décision pour sécuriser le SLA et éviter les appels synchrones aux référentiels externes.

La question n'est donc pas : quel outil magique va absorber la complexité ?

La question est :

> Quelle variabilité doit rester gouvernée par le métier, quelle variabilité doit être optimisée par un algorithme, et quelle variabilité doit rester dans le code parce qu'elle est stable ?

## Mauvais réflexe : coder la richesse en branches

Le mauvais réflexe consiste à traduire chaque singularité par une condition supplémentaire.

```text
si marque = A et canal = eCom
    appliquer le comportement 1
sinon si marque = A et canal = marketplace
    appliquer le comportement 2
sinon si marque = B et client = wholesale et stock = faible
    appliquer le comportement 3
sinon si ...
```

Cette approche peut sembler rapide au départ.

Mais elle crée progressivement :

- des règles invisibles ;
- des tests incomplets ;
- des effets de bord ;
- des exceptions difficiles à expliquer ;
- des dépendances fortes entre canaux, marques et applications ;
- des dépendances synchrones à des APIs externes dans le chemin de décision ;
- une difficulté à introduire un nouveau business model sans régression.

Dans ce modèle, plus le groupe est riche, plus le SI devient fragile.

## Cas révélateur : repriorisation Wholesale BRD

Le sujet a été observé concrètement chez BRD.

Lorsqu'une grosse commande Wholesale arrive pour un grand distributeur stratégique, le moteur de repriorisation peut déplacer dans le futur des promesses déjà associées à des Sales Orders.

La logique métier est compréhensible : prioriser un client stratégique peut être légitime dans un modèle Wholesale.

Mais la mise en œuvre actuelle révèle le risque du principe : un batch SQL nocturne orchestre plusieurs dizaines de règles, avec une complexité devenue difficile à maintenir.

Le problème n'est donc pas la priorisation commerciale.

Le problème est que la variabilité est enfouie dans un traitement opaque, peu explicable, peu simulable et risqué à faire évoluer.

Ce cas montre pourquoi FLOW doit rendre les règles de promesse, d'allocation et de repriorisation explicites, testables, versionnées et gouvernées.

## Bon réflexe : gouverner la variabilité

FLOW doit privilégier une autre approche.

```text
Demande
    + contexte
    + agreement
    + règles
    + contraintes
    + ressources disponibles
    + objectif d'optimisation
    = décision traçable
```

Dans cette lecture, les singularités business ne disparaissent pas.

Elles sont explicitées dans des règles, contraintes, policies ou paramètres gouvernés.

Le cœur du SI reste stable : il sait qualifier une demande, charger un contexte, évaluer des règles, arbitrer une promesse, mobiliser des capacités Supply et expliquer la décision.

Ce qui varie, ce sont les règles, contraintes, priorités, agreements, seuils, poids d'optimisation et conditions d'usage.

Le moteur de décision doit aussi maîtriser les informations nécessaires à son calcul.

Cela ne signifie pas que FLOW devient source de référence de toutes les informations.

Cela signifie que FLOW consomme des projections locales de décision, alimentées par les sources de référence et maintenues par contrats de données.

```text
Sources de référence
    → contrats de données
    → projections locales de décision
    → moteur de règles / contraintes
    → décision rapide et traçable
```

## Les mécanismes à combiner

Les mécanismes ne sont pas interchangeables.

| Mécanisme | Utile quand... | Exemple FLOW |
| --- | --- | --- |
| Moteur de règles | la décision repose sur des règles métier explicites et maintenables | éligibilité d'un service, priorité client, condition de traitement |
| Moteur de contraintes | il faut choisir le meilleur plan sous contraintes multiples | sourcing, allocation, transport, crossdock, capacité magasin |
| Pattern Strategy / Policy | le code doit sélectionner un comportement stable selon un contexte | variation d'un calcul, d'une politique de promesse ou d'un mode d'exécution |
| Modèle de décision | il faut rendre une décision lisible, testable et discutable | promesse tenable, choix de source, arbitrage d'exception |
| Projection locale de décision | le moteur doit décider vite sans dépendre du SLA d'une API externe | catalogue d'exécution, network, services Supply, règles d'éligibilité |
| IA | il faut aider à classifier, recommander, détecter ou expliquer | aide à la qualification d'exception, détection d'anomalie, suggestion de règle |

Le point commun est la gouvernance.

Une variabilité non gouvernée reste de la complexité, même si elle est portée par un outil moderne.

## Conséquences de conception

Ce principe impose plusieurs réflexes.

- Identifier les dimensions de variabilité : marque, canal, pays, client, agreement, stock, promesse, service, transport, fournisseur, usine ou capacité Supply.
- Séparer le cœur stable du traitement de la demande et les règles qui le paramètrent.
- Éviter d'encoder les variantes métier dans les workflows ou interfaces point à point.
- Rendre les règles testables, versionnées et traçables.
- Prévoir des simulations ou jeux de tests couvrant les combinaisons critiques.
- Choisir explicitement quand utiliser un moteur de règles, un moteur de contraintes, un pattern de code, une configuration ou une assistance IA.
- Construire des projections locales de décision lorsque le SLA de calcul interdit de dépendre d'APIs externes.
- Définir la fraîcheur suffisante, les règles de reprise et la réconciliation des projections.
- Découper les produits critiques dans une logique [Self-contained System](../architecture-cible/patterns/self-contained-system.md) : responsabilité claire, autonomie suffisante, contrats explicites et dépendances asynchrones autant que possible.
- Donner aux métiers une capacité de lecture et de gouvernance des règles, sans leur faire porter la complexité technique.

## Changement de paradigme

Pour Beaumanoir, ce principe est important parce qu'il déplace le débat.

L'alternative n'est pas :

```text
uniformiser
ou
subir la complexité
```

L'alternative devient :

```text
préserver la richesse business
en gouvernant la variabilité
avec des mécanismes adaptés
```

La technologie ne sert pas à masquer la complexité.

Elle sert à donner une forme contrôlable à une complexité métier légitime.

## Liens avec les autres principes

Ce principe prolonge directement :

- le [principe 1](1-converger-c-est-federer.md), car le bon niveau de commun doit préserver les singularités utiles ;
- le [principe 5](5-le-processus-emerge-des-decisions.md), car la variation doit être portée par des décisions explicites plutôt que par des workflows figés ;
- le [principe 6](6-demande-objet-metier-central-orchestration.md), car le Case donne le contexte nécessaire à l'évaluation des règles ;
- le [principe 7](7-qualifier-les-informations-plutot-que-master-data.md), car les règles et contraintes ont besoin d'informations qualifiées, projetées et gouvernées.
- le pattern [Self-contained System (SCS)](../architecture-cible/patterns/self-contained-system.md), car la richesse business doit être portée par des produits autonomes plutôt que par un monolithe distribué ;
- le pattern [Projection locale de décision](../architecture-cible/patterns/projection-locale-de-decision.md), car une décision rapide doit maîtriser ses modèles de lecture et ses dépendances de SLA.

## Références utiles

- [Replace Conditional with Polymorphism — Martin Fowler](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html), pour le symptôme logiciel des conditionnels remplacés par un modèle plus adapté.
- [Drools documentation](https://docs.jboss.org/drools/release/latest/drools-docs/drools/introduction/index.html), pour l'approche moteur de règles et gestion de décision.
- [Timefold](https://timefold.ai/), pour l'usage de solveurs de contraintes sur des problèmes de planification, routage ou scheduling à forte variabilité.
- [CQRS — Microservices.io](https://microservices.io/patterns/data/cqrs.html), pour les read models matérialisés optimisés pour des lectures ou décisions spécifiques.
- [Event-Carried State Transfer — Martin Fowler](https://martinfowler.com/articles/201701-event-driven.html#Event-CarriedStateTransfer), pour le découplage par copie locale mise à jour par événements.
- [Self-contained Systems — scs-architecture.org](https://scs-architecture.org/), pour l'autonomie des systèmes, la maîtrise de la logique et des données, et la préférence pour les dépendances asynchrones.

---

← Principe précédent : [Master Data : des objets maîtres aux sources gouvernées](7-qualifier-les-informations-plutot-que-master-data.md)
