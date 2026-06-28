# Hotspots : les risques à arbitrer pour rendre FLOW réaliste

La vision FLOW ne peut pas être portée uniquement comme une cible théorique.

Elle doit aussi traiter explicitement les points durs du programme.

Un <span class="flow-keyword">hotspot</span> n'est pas un problème isolé.

C'est un point où plusieurs dimensions se croisent : trajectoire de migration, décision métier, intégration technique, donnée, finance, gouvernance ou transformation.

<div class="flow-conviction">
  <p>Les hotspots ne contredisent pas la vision.</p>
  <p>Ils indiquent les endroits où la vision doit devenir une décision robuste.</p>
</div>

## Vue synthétique des familles de risques

<div class="flow-conviction">
  <p>Un hotspot n'est pas une difficulté à subir.</p>
  <p>C'est une décision structurante à rendre explicite.</p>
</div>

| Famille de risque | Hotspots concernés | Question structurante |
| --- | --- | --- |
| Trajectoire de migration | SAP ECC Boardriders | Comment sortir d'un socle monolithique sans créer un big bang ? |
| Décision distribuée | C-LOG, promesse Wholesale Boardriders | Où se prennent les décisions de fulfillment, de priorisation et d'allocation ? |
| Intégration et temps réel | Stock temps réel, capacités technologiques des systèmes réintégrés | Les systèmes autour de FLOW savent-ils exposer APIs, événements, statuts et réconciliation ? |
| Données produit et amont | PLM, catalogue, Article / EAN | Quel catalogue FLOW consomme-t-il pour vendre, acheter, promettre et exécuter ? |
| Gouvernance métier | Promesse Wholesale, règles, Agreements | Comment absorber les variations métier sans multiplier processus et applications ? |
| Périmètre fonctionnel | Module Négoce StoreLand | Quelles responsabilités doivent être reprises dans FLOW, et lesquelles doivent rester dans un domaine consommateur ? |

Cette lecture permet de ne pas voir les hotspots comme une simple liste de sujets.

Elle montre les catégories de décisions à sécuriser pour rendre FLOW opérable.

## Risque de trajectoire : SAP ECC Boardriders

<div class="flow-conviction">
  <p>Le monolithe SAP ECC ne se découpe pas comme une application modulaire.</p>
  <p>La trajectoire de sortie doit être pensée comme un sujet d'architecture, pas seulement comme un planning de migration.</p>
</div>

Boardriders s'appuie fortement sur SAP ECC.

La nature monolithique de cette solution rend une migration progressive vers FLOW plus difficile qu'un simple remplacement par lots fonctionnels.

Le risque est de devoir arbitrer entre :

- Une trajectoire de migration longue et complexe.
- Des adhérences fortes entre finance, stock, commandes et exécution.
- Une difficulté à découper proprement les responsabilités.
- Une bascule trop large ou trop risquée.

Ce hotspot impose de clarifier très tôt quelles responsabilités doivent sortir de SAP ECC, lesquelles doivent rester articulées avec SAP Finance, et dans quel ordre la migration peut réellement être sécurisée.

## Risque de décision distribuée : C-LOG et fulfillment

<div class="flow-conviction">
  <p>Distribuer l'exécution est normal.</p>
  <p>Distribuer la décision sans gouvernance claire crée des promesses incompatibles.</p>
</div>

C-LOG ne doit pas être lu seulement comme un outil logistique ou un composant d'intégration.

Il porte déjà une partie des décisions de fulfillment : orientation, exécution, stock entrepôt, transport, événements et capacités opérationnelles.

Si FLOW porte une partie de la décision liée à la demande, et C-LOG une partie de la décision liée à l'exécution, le risque est de distribuer la décision sans gouvernance claire.

Cela peut produire :

- Des choix incompatibles entre demande et exécution.
- Des erreurs d'aiguillage.
- Des promesses impossibles à tenir.
- Une optimisation locale au détriment de l'optimisation globale.
- Une difficulté à expliquer pourquoi une décision a été prise.

Ce hotspot impose de définir précisément la frontière entre décision de demande et décision d'exécution, ainsi que le contrat d'échange entre FLOW et C-LOG.

## Risque d'intégration et de fraîcheur : stock temps réel

<div class="flow-conviction">
  <p>Un stock unifié n'est utile que si les mouvements remontent assez vite.</p>
  <p>La promesse omnicanale dépend donc aussi des capacités événementielles du POS, des WMS et des partenaires logistiques.</p>
</div>

Le <span class="flow-keyword">Stock Unifié</span> n'a de valeur opérationnelle que si les mouvements de stock remontent avec une fraîcheur suffisante.

Or cette fraîcheur ne dépend pas seulement de FLOW.

Elle dépend aussi de la capacité des systèmes qui observent ou provoquent les mouvements de stock à les transmettre rapidement.

Les systèmes concernés sont notamment :

- Le Point of Sale, porté par une application éditeur.
- Les solutions logistiques opérées par des entreprises externes ou des filiales.
- Les WMS, transporteurs, partenaires et systèmes d'exécution qui manipulent physiquement le stock.

Pour tendre vers un stock temps réel, ces systèmes devront accepter de publier les mouvements de stock en événementiel, en asynchrone court.

Ce hotspot impose donc de clarifier :

- Les capacités événementielles réellement disponibles côté POS et solutions logistiques.
- Les contrats d'événements nécessaires.
- Les exigences de fraîcheur par usage métier.
- Les responsabilités en cas de retard, perte ou incohérence d'événement.
- Les mécanismes de rattrapage et de réconciliation.

Sans cette capacité, FLOW pourra consolider une vision de stock, mais pas garantir une décision de promesse, d'allocation ou de fulfillment suffisamment fiable à l'échelle omnicanale.

## Capacités technologiques : réintégrer les systèmes existants

<div class="flow-conviction">
  <p>Réintégrer un outil existant ne suffit pas : il doit savoir dialoguer avec la colonne vertébrale FLOW.</p>
  <p>API, événements, statuts, documents et réconciliation deviennent des prérequis d'architecture.</p>
</div>

FLOW ne vise pas à réécrire tous les services existants.

Il doit pouvoir réintégrer les outils qui portent une valeur métier spécifique, par exemple CBS, le SAV Client Sarenza, des outils fournisseurs ou des systèmes logistiques spécialisés.

Mais cette réintégration suppose des capacités techniques minimales.

Un service existant peut être métier-pertinent, mais difficile à conserver s'il ne sait pas exposer des APIs, publier des événements, partager ses statuts, corréler ses objets avec les Cases ou participer à la réconciliation.

Ce hotspot impose de clarifier :

- Les capacités API nécessaires.
- Les événements métier attendus.
- Les statuts et jalons à exposer.
- Les identifiants de corrélation.
- Les documents à produire, consommer ou référencer.
- Les mécanismes de reprise, rejeu, supervision et réconciliation.
- Les critères permettant de décider : conserver, encapsuler, faire évoluer, remplacer ou rapatrier certaines responsabilités dans FLOW.

Le hotspot Stock temps réel est un cas critique de cette problématique, mais il ne doit pas porter tout le sujet.

## Catalogue produit : FLOW ne peut pas dépendre d'un PLM unique

<div class="flow-conviction">
  <p>Le PLM est essentiel pour concevoir certains produits.</p>
  <p>Il ne peut pas devenir le catalogue unique de tout le SI.</p>
</div>

Beaumanoir dispose d'un PLM structurant pour gérer les collections, les fiches produits, les grilles taille / couleur, les échanges avec les fournisseurs et les engagements industriels très tôt dans la saison.

Ce modèle est adapté aux produits conçus dans le processus historique de collection.

Mais d'autres stratégies existent, notamment avec Sarenza ou certaines collections Boardriders : l'entreprise peut acheter des produits déjà designés par les fournisseurs, fournis directement sous forme de variantes produit avec EAN, parfois sans respecter les nomenclatures taille / couleur du PLM historique.

Le hotspot est donc le suivant : FLOW devra gérer à la fois des produits conçus et des produits importés.

La question n'est pas seulement produit.

Elle touche à la frontière entre conception amont, catalogue d'exécution, achat, vente, promesse et fulfillment.

FLOW doit clarifier s'il doit connaître la structure du PLM ou consommer un catalogue au niveau Article / EAN, suffisamment riche pour exécuter, mais découplé des variations de processus de conception de saison.

Ce hotspot impose de clarifier :

- La granularité produit minimale nécessaire à FLOW.
- Le rôle du Product Agreement Catalog.
- La frontière entre PLM, PIM, catalogue d'exécution et FLOW.
- La gestion des produits conçus et des produits importés.
- La gouvernance des nomenclatures taille / couleur.
- Le découplage entre processus de conception amont et capacités Demand / Fulfillment.

## Promesse commerciale : prioriser sans rompre les engagements

<div class="flow-conviction">
  <p>Prioriser un client ne consiste pas seulement à lui donner du stock.</p>
  <p>Cela peut décaler les autres commandes et rompre des promesses déjà perçues comme acquises.</p>
</div>

La stratégie Wholesale de Boardriders repose sur une logique de priorisation des meilleurs clients.

Cette logique est très différente d'une approche “premier arrivé, premier servi”.

Dans une logique de priorisation, une nouvelle commande d'un client prioritaire peut consommer un stock insuffisant et décaler dans le temps des commandes déjà enregistrées pour des clients moins prioritaires.

Le sujet n'est donc pas seulement : “qui a droit au stock ?”

Le sujet est aussi : “quelle promesse a déjà été donnée, à qui, et peut-on la déplacer ?”

Côté Beaumanoir, l'adage “premier arrivé, premier servi” porte une autre philosophie : lorsqu'une promesse est faite, elle doit être tenue.

Ces deux modèles ne sont pas simplement deux règles de stock.

Ils traduisent deux manières différentes de gouverner la relation commerciale, l'allocation, la priorité et la responsabilité de la promesse.

FLOW doit donc clarifier explicitement :

- Si une promesse peut être déplacée après avoir été donnée.
- Qui a le droit de provoquer ce déplacement.
- Quels clients, canaux ou agreements peuvent être prioritaires.
- Comment les commandes décalées sont identifiées, expliquées et traitées.
- Comment éviter qu'une optimisation commerciale locale dégrade la confiance globale dans la promesse.

Ce hotspot montre pourquoi FLOW doit être capable de gérer des règles métier explicites.

La plateforme ne doit pas seulement dire : y a-t-il du stock ?

Elle doit aussi pouvoir dire : ce stock peut-il être réservé à un client prioritaire, même si cela décale d'autres engagements ?

C'est typiquement le genre de variation métier que FLOW doit absorber sans multiplier les processus ou les applications spécifiques.

## Module Négoce StoreLand : découper avant de reprendre

<div class="flow-conviction">
  <p>Le module Négoce n'est pas un bloc à reprendre tel quel.</p>
  <p>C'est un révélateur de responsabilités mélangées entre engagement commercial et Demand & Fulfillment.</p>
</div>

Le module Négoce de StoreLand porte plusieurs responsabilités : client, assortiment, commercial agreement, catalogue, prix, conditions commerciales et commandes d'achat.

Certaines relèvent plutôt du design commercial et du domaine d'Engagement.

D'autres peuvent relever de FLOW si elles participent au cycle de vie transverse d'une demande, à l'approvisionnement, à la promesse, à l'allocation ou à l'exécution.

Le hotspot n'est donc pas de savoir si FLOW doit reprendre “le module Négoce”.

Il est de découper les responsabilités pour savoir ce qui doit être repris, réintégré, consommé ou laissé dans un domaine consommateur de la plateforme.

Ce hotspot impose de clarifier :

- Les responsabilités Négoce réellement candidates à FLOW.
- La frontière entre commercial agreement, catalogue, commande d'achat et promesse.
- Les capacités à généraliser pour toutes les marques GBM.
- La manière de traiter la convergence intra-GBM entre marques premium outillées et marques opérées plus manuellement.
- Le rôle du Product Agreement Catalog comme point d'interface potentiel entre Engagement et FLOW.

## Synthèse des hotspots

<div class="flow-conviction">
  <p>La synthèse des hotspots n'est pas une liste de risques.</p>
  <p>C'est la carte des décisions qui conditionnent la crédibilité de FLOW.</p>
</div>

| Hotspot | Famille de risque | Ce que FLOW doit clarifier |
| --- | --- | --- |
| SAP ECC Boardriders | Trajectoire de migration | Découpage des responsabilités, trajectoire de sortie, articulation avec Finance |
| C-LOG | Décision distribuée | Frontière demande / exécution, contrat de décision, gouvernance des arbitrages |
| Stock temps réel | Intégration et fraîcheur | Événements POS et logistiques, fraîcheur attendue, contrats d'événements, réconciliation |
| Capacités technologiques des systèmes réintégrés | Intégration des services existants | APIs, événements, statuts, documents, corrélation, réconciliation, trajectoire d'encapsulation ou remplacement |
| Catalogue produit et PLM | Données produit et amont | Granularité Article / EAN, Product Agreement Catalog, frontière conception / exécution, nomenclatures |
| Promesse Wholesale Boardriders | Gouvernance métier | Règles, policies, allocation, promesses déplaçables ou non, priorisation client |
| Module Négoce StoreLand | Périmètre fonctionnel | Responsabilités à reprendre dans FLOW, responsabilités Engagement, commandes d'achat, Product Agreement Catalog |

## À retenir

<div class="flow-conviction">
  <p>La valeur de cette page n'est pas de lister les difficultés.</p>
  <p>Elle est de montrer les décisions à sécuriser pour que FLOW tienne réellement sa promesse.</p>
</div>

Ces hotspots montrent que FLOW n'est pas seulement un outil cible.

FLOW est aussi un cadre de décision pour traiter les tensions réelles de convergence du groupe.

Ils obligent à rendre explicites les choix qui conditionnent la crédibilité de la plateforme : trajectoire, décision, intégration, données, promesse et gouvernance.

---

← Page précédente : [Solution](3-plateforme-flow.md) · → Page suivante : [Valeur attendue](5-valeur-attendue.md)
