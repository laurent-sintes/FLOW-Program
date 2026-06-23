# Gouvernance Logistique : BRD vs GBM

## Point commun

Boardriders et Groupe Beaumanoir possèdent finalement une Supply Chain amont très proche.

Les deux groupes :

- planifient leurs collections plusieurs mois à l'avance ;
- produisent principalement en Asie du Sud-Est ;
- fonctionnent selon une logique de saison ;
- passent des commandes de masse auprès des fournisseurs ;
- organisent ensuite un acheminement international vers l'Europe.

La différence ne réside donc pas fondamentalement dans la Supply Chain.

## Modèle Boardriders

### Amont

Boardriders passe ses commandes auprès des fournisseurs et s'appuie sur l'offre 4PL de Maersk.

Maersk prend notamment en charge :

- enlèvement usine ;
- consolidation ;
- transport international ;
- douane ;
- déchargement.

### Aval

Pour le fulfillment, Boardriders s'appuie sur plusieurs partenaires logistiques gérant :

- stockage ;
- préparation ;
- transport.

### Décision

La décision opérationnelle est portée principalement par NewStore.

NewStore décide notamment :

- sourcing ;
- allocation ;
- promesse ;
- transport.

Cependant SAP conserve également certaines capacités décisionnelles.

Dans environ 5 % des cas, SAP modifie ou contredit une décision initialement prise par NewStore.

Le problème observé n'est donc pas logistique.

Le problème est la coexistence de deux moteurs de décision.

## Modèle Groupe Beaumanoir

### Amont

GBM a filialisé sa fonction logistique au travers de C-LOG.

C-LOG gère notamment :

- transport amont ;
- réception ;
- entrepôts.

### Aval

C-LOG gère également :

- stockage ;
- picking ;
- packing ;
- light-touch ;
- transport.

### Décision

C-LOG possède son propre OMS.

UR gère principalement :

- les demandes ;
- leur cycle de vie ;
- les statuts.

La décision opérationnelle est portée par l'OMS de C-LOG.

La responsabilité est donc beaucoup plus claire.

## Insight FLOW

La différence majeure entre BRD et GBM n'est pas :

- l'ERP ;
- le WMS ;
- le transport ;
- les prestataires logistiques.

La différence majeure est :

> l'endroit où réside la responsabilité de décision.

Cette observation renforce l'idée que FLOW doit être urbanisé autour des responsabilités suivantes :

Party → Agreement → Demand → Decision → Execution

plutôt qu'autour des organisations historiques Achat, B2B ou B2C.

## Conclusion

L'un des principaux enseignements de FLOW est que la décision constitue une responsabilité architecturale à part entière.

Les problèmes observés sont souvent moins liés à la logistique elle-même qu'à la gouvernance de la décision logistique.