# Hotspots : points à approfondir et arbitrer

La vision FLOW ne peut pas être portée uniquement comme une cible théorique.

Elle doit aussi traiter explicitement les points durs du programme.

Trois hotspots apparaissent déjà comme structurants.

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

## Wholesale Boardriders : priorisation commerciale vs premier arrivé, premier servi

La stratégie Wholesale de Boardriders repose sur une logique de priorisation des meilleurs clients.

Cette logique n'est pas alignée avec une approche simple de type “premier arrivé, premier servi”.

Le sujet dépasse donc la gestion de stock.

Il touche à la politique commerciale, aux engagements clients, à l'allocation, à la promesse et à la gouvernance des règles.

Ce hotspot montre pourquoi FLOW doit être capable de gérer des règles métier explicites.

La plateforme ne doit pas seulement dire :

> Y a-t-il du stock ?

Elle doit aussi pouvoir dire :

> Pour qui ce stock doit-il être priorisé, selon quel engagement, quelle règle commerciale et quel arbitrage ?

C'est typiquement le genre de variation métier que FLOW doit absorber sans multiplier les processus ou les applications spécifiques.

## Synthèse des hotspots

| Hotspot | Risque | Ce que FLOW doit clarifier |
| --- | --- | --- |
| SAP ECC Boardriders | Migration difficile à phaser, adhérences fortes, risque de big bang | Découpage des responsabilités, trajectoire de sortie, articulation avec Finance |
| C-LOG | Décision de fulfillment distribuée, erreurs d'aiguillage, optimisation locale | Frontière demande / exécution, contrat de décision, gouvernance des arbitrages |
| Wholesale Boardriders | Priorisation commerciale incompatible avec une logique FIFO simple | Rules, policies, allocation, engagements, promesse client |

Ces hotspots montrent que FLOW n'est pas seulement un outil cible.

FLOW est aussi un cadre de décision pour traiter les tensions réelles de convergence du groupe.

---

← Page précédente : [Plateforme FLOW](4-plateforme-flow.md) · → Page suivante : [Valeur attendue](6-valeur-attendue.md)