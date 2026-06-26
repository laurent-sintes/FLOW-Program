# Panorama applicatif GBM

## Intention

Cette page documente l'environnement applicatif des marques historiques du Groupe Beaumanoir.

Elle constitue le pendant du panorama BRD.

À ce stade, elle s'appuie sur les éléments déjà présents dans le référentiel documentaire et dans l'étude Synvance. Elle devra être enrichie avec les supports spécifiques GBM lorsque les slides ou cartographies sources seront analysées plus finement.

## Lecture générale

Le paysage GBM historique est plus fédéral que celui de BRD.

Il s'est construit autour des marques, des enseignes, des canaux et de leurs spécificités.

Cette organisation a permis de préserver des modes de fonctionnement différenciés.

Elle a aussi conduit à une multiplication des applications, des règles locales et des intégrations.

```text
GBM
    → logique historiquement fédérale par marque
    → Storeland comme socle historique majeur
    → outils spécialisés autour du cycle produit, commerce, magasin et logistique
    → apparition de solutions transverses lorsque les besoins dépassent une marque
```

## Storeland

Storeland est le socle historique majeur des marques GBM.

Il porte une partie importante des processus et données liés aux marques historiques.

Dans l'histoire GBM, Storeland a contribué à préserver les spécificités des marques et de leurs modes de gestion.

Cette logique a toutefois ses limites lorsque les responsabilités deviennent transverses : demandes communes, stock, allocation, visibilité, engagement, pilotage ou coordination multi-marques.

## UR

UR est un signal important dans le paysage GBM.

Son apparition montre que la logique par marque ne suffit pas toujours.

Certaines demandes ont besoin d'être centralisées, coordonnées ou suivies au-delà du périmètre d'une seule marque ou application.

Pour FLOW, UR constitue donc une preuve terrain : même dans un modèle fortement fédéré, certains objets métier réclament une orchestration transverse.

## Applications et composants mentionnés

Les supports existants mentionnent notamment :

- Storeland ;
- UR ;
- Cegid Y2 ;
- SoCloz ;
- OMS C-LOG ;
- Salesforce ;
- Elastic ;
- Talend ;
- PLM ;
- PIM ;
- MAP ;
- BPC ;
- CBS ;
- SNC ;
- WMS.

Ces composants ne doivent pas être lus comme une cible FLOW.

Ils représentent le paysage de départ, avec ses spécialisations, ses héritages et ses frontières applicatives.

## Caractéristiques observées

GBM présente une forte autonomie locale.

Cette autonomie protège certaines spécificités métier.

Elle peut cependant produire :

- des règles dispersées ;
- des données redondantes ou divergentes ;
- des intégrations multiples ;
- des responsabilités difficiles à localiser ;
- des limites lorsque les demandes traversent plusieurs marques, canaux ou domaines.

Le sujet n'est donc pas seulement de remplacer un outil par un autre.

Le sujet est d'identifier ce qui doit rester différenciant et ce qui doit devenir une capacité commune.

## Lecture FLOW

Dans une lecture FLOW, GBM met en évidence le risque inverse de BRD.

BRD montre les limites d'une forte centralisation applicative lorsque les responsabilités de décision restent peu explicites.

GBM montre les limites d'une forte fédération applicative lorsque certaines responsabilités dépassent les frontières locales.

FLOW doit donc préserver l'autonomie utile de GBM, sans reproduire les silos applicatifs.

## Responsabilités à investiguer

Plusieurs responsabilités devront être clarifiées dans les prochains travaux :

- cycle de vie des demandes ;
- rôle précis de Storeland ;
- rôle précis de UR ;
- gestion des stocks et disponibilités ;
- allocation et promesse ;
- orchestration omnicanale ;
- rôle de SoCloz et OMS C-LOG ;
- articulation magasin / eCommerce / logistique ;
- données produit, article, saison et assortiment ;
- interfaces avec Finance et systèmes d'exécution.

## Questions structurantes pour FLOW

Le panorama GBM conduit à plusieurs questions :

- Quelles responsabilités Storeland porte-t-il aujourd'hui qui devraient être reprises par FLOW ?
- UR est-il un précurseur du Case Management ou seulement un outil de coordination spécifique ?
- Quelles capacités sont réellement communes entre marques ?
- Quelles spécificités doivent rester locales ?
- Comment éviter de centraliser inutilement ce qui fait la différenciation des marques ?
- Quelles données doivent devenir partagées, gouvernées ou seulement projetées ?
- Quels systèmes doivent être remplacés, conservés, encapsulés ou connectés ?

## À retenir

GBM ne doit pas être lu comme un simple paysage applicatif à rationaliser.

GBM montre pourquoi la fédération est nécessaire : certaines spécificités doivent rester locales, mais certaines responsabilités dépassent naturellement les frontières des marques et des applications.

FLOW doit donc permettre de mutualiser les capacités transverses sans uniformiser les modes de fonctionnement utiles.
