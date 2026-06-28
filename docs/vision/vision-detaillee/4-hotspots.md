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

| Famille de risque | Hotspots concernés | Question structurante |
| --- | --- | --- |
| Trajectoire de migration | SAP ECC Boardriders | Comment sortir d'un socle monolithique sans créer un big bang ? |
| Décision distribuée | C-LOG, Wholesale Boardriders | Où se prennent les décisions de fulfillment, de priorisation et d'allocation ? |
| Intégration et temps réel | Stock temps réel, systèmes réintégrés | Les systèmes autour de FLOW savent-ils exposer APIs, événements, statuts et réconciliation ? |
| Données produit et amont | PLM, catalogue, Article / EAN | Quel catalogue FLOW consomme-t-il pour vendre, acheter, promettre et exécuter ? |
| Gouvernance métier | Wholesale, règles, Agreements | Comment absorber les variations métier sans multiplier processus et applications ? |

Cette lecture permet de ne pas voir les hotspots comme une simple liste de sujets.

Elle montre les catégories de décisions à sécuriser pour rendre FLOW opérable.

## Risque de trajectoire : SAP ECC Boardriders

Boardriders s'appuie fortement sur SAP ECC.

La nature monolithique de cette solution rend une migration progressive vers FLOW plus difficile qu'un simple remplacement par lots fonctionnels.

Le risque est de devoir arbitrer entre :

- Une trajectoire de migration longue et complexe.
- Des adhérences fortes entre finance, stock, commandes et exécution.
- Une difficulté à découper proprement les responsabilités.
- Une bascule trop large ou trop risquée.

Ce hotspot impose de clarifier très tôt quelles responsabilités doivent sortir de SAP ECC, lesquelles doivent rester articulées avec SAP Finance, et dans quel ordre la migration peut réellement être sécurisée.

## Risque de décision distribuée : C-LOG et fulfillment

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

## Risque d'intégration : brancher les systèmes réintégrés

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

## Risque données produit et amont : PLM, catalogue, Article / EAN

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

## Risque de gouvernance métier : Wholesale Boardriders

La stratégie Wholesale de Boardriders repose sur une logique de priorisation des meilleurs clients.

Cette logique n'est pas alignée avec une approche simple de type “premier arrivé, premier servi”.

Le sujet dépasse donc la gestion de stock.

Il touche à la politique commerciale, aux engagements clients, à l'allocation, à la promesse et à la gouvernance des règles.

Ce hotspot montre pourquoi FLOW doit être capable de gérer des règles métier explicites.

La plateforme ne doit pas seulement dire : y a-t-il du stock ?

Elle doit aussi pouvoir dire : pour qui ce stock doit-il être priorisé, selon quel engagement, quelle règle commerciale et quel arbitrage ?

C'est typiquement le genre de variation métier que FLOW doit absorber sans multiplier les processus ou les applications spécifiques.

## Synthèse des hotspots

| Hotspot | Famille de risque | Ce que FLOW doit clarifier |
| --- | --- | --- |
| SAP ECC Boardriders | Trajectoire de migration | Découpage des responsabilités, trajectoire de sortie, articulation avec Finance |
| C-LOG | Décision distribuée | Frontière demande / exécution, contrat de décision, gouvernance des arbitrages |
| Stock temps réel | Intégration et fraîcheur | Événements POS et logistiques, fraîcheur attendue, contrats d'événements, réconciliation |
| Capacités d'intégration des systèmes réintégrés | Intégration des services existants | APIs, événements, statuts, documents, corrélation, réconciliation, trajectoire d'encapsulation ou remplacement |
| PLM, catalogue, Article / EAN | Données produit et amont | Granularité Article / EAN, Product Agreement Catalog, frontière conception / exécution, nomenclatures |
| Wholesale Boardriders | Gouvernance métier | Rules, policies, allocation, engagements, promesse client |

## À retenir

Ces hotspots montrent que FLOW n'est pas seulement un outil cible.

FLOW est aussi un cadre de décision pour traiter les tensions réelles de convergence du groupe.

La valeur de cette page n'est donc pas de lister les difficultés.

Elle est de montrer les décisions à sécuriser pour que la plateforme puisse réellement tenir sa promesse.

---

← Page précédente : [Solution](3-plateforme-flow.md) · → Page suivante : [Valeur attendue](5-valeur-attendue.md)