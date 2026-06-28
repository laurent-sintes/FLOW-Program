# Hotspots : points à approfondir et arbitrer

La vision FLOW ne peut pas être portée uniquement comme une cible théorique.

Elle doit aussi traiter explicitement les points durs du programme.

Cinq <span class="flow-keyword">hotspots</span> apparaissent déjà comme structurants.

## Boardriders / SAP ECC : une migration difficile à phaser

Boardriders s'appuie fortement sur SAP ECC.

La nature monolithique de cette solution rend une migration progressive vers FLOW plus difficile qu'un simple remplacement par lots fonctionnels.

Le risque est de devoir arbitrer entre :

- Une trajectoire de migration longue et complexe.
- Des adhérences fortes entre finance, stock, commandes et exécution.
- Une difficulté à découper proprement les responsabilités.
- Une bascule trop large ou trop risquée.

Ce hotspot impose de clarifier très tôt quelles responsabilités doivent sortir de SAP ECC, lesquelles doivent rester articulées avec SAP Finance, et dans quel ordre la migration peut réellement être sécurisée.

## C-LOG : une décision de fulfillment déjà distribuée

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

## Stock temps réel : obtenir les mouvements à la source

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

## PLM, catalogue, Article / EAN : découpler conception et exécution

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

## Wholesale Boardriders : priorisation commerciale vs premier arrivé, premier servi

La stratégie Wholesale de Boardriders repose sur une logique de priorisation des meilleurs clients.

Cette logique n'est pas alignée avec une approche simple de type “premier arrivé, premier servi”.

Le sujet dépasse donc la gestion de stock.

Il touche à la politique commerciale, aux engagements clients, à l'allocation, à la promesse et à la gouvernance des règles.

Ce hotspot montre pourquoi FLOW doit être capable de gérer des règles métier explicites.

La plateforme ne doit pas seulement dire : y a-t-il du stock ?

Elle doit aussi pouvoir dire : pour qui ce stock doit-il être priorisé, selon quel engagement, quelle règle commerciale et quel arbitrage ?

C'est typiquement le genre de variation métier que FLOW doit absorber sans multiplier les processus ou les applications spécifiques.

## Synthèse des hotspots

| Hotspot | Risque | Ce que FLOW doit clarifier |
| --- | --- | --- |
| SAP ECC Boardriders | Migration difficile à phaser, adhérences fortes, risque de big bang | Découpage des responsabilités, trajectoire de sortie, articulation avec Finance |
| C-LOG | Décision de fulfillment distribuée, erreurs d'aiguillage, optimisation locale | Frontière demande / exécution, contrat de décision, gouvernance des arbitrages |
| Stock temps réel | Stock unifié trop peu frais pour promettre, allouer ou optimiser de manière fiable | Événements POS et logistiques, fraîcheur attendue, contrats d'événements, réconciliation |
| PLM, catalogue, Article / EAN | Dépendance excessive de FLOW au modèle PLM historique, difficulté à gérer produits conçus et produits importés | Granularité Article / EAN, Product Agreement Catalog, frontière conception / exécution, nomenclatures |
| Wholesale Boardriders | Priorisation commerciale incompatible avec une logique FIFO simple | Rules, policies, allocation, engagements, promesse client |

Ces hotspots montrent que FLOW n'est pas seulement un outil cible.

FLOW est aussi un cadre de décision pour traiter les tensions réelles de convergence du groupe.

---

← Page précédente : [Solution](3-plateforme-flow.md) · → Page suivante : [Valeur attendue](5-valeur-attendue.md)