# Panorama applicatif BRD et GBM

## Intention

Ce panorama documente le contexte applicatif observé avant la formalisation de FLOW.

Il s'appuie sur le référentiel documentaire préexistant, notamment l'étude Synvance de 2025, les supports COPROJ / COPIL, les livrables d'existant et de besoins cibles, ainsi que les supports SI BRD et GBM.

L'objectif n'est pas de produire une cartographie exhaustive et définitive.

L'objectif est de conserver une lecture structurée du point de départ : deux patrimoines applicatifs différents, mais confrontés à des problèmes de convergence proches.

## Lecture générale

Le contexte initial est celui d'une convergence entre deux histoires SI.

BRD présente une trajectoire plus centralisée autour de SAP et de solutions satellites spécialisées.

GBM présente une trajectoire plus fédérale, historiquement structurée par marque, avec Storeland comme socle applicatif majeur et des solutions complémentaires pour répondre à des besoins transverses ou spécialisés.

```text
BRD
    → logique plus centralisée autour de SAP
    → solutions satellites spécialisées
    → forte technicité des règles d'allocation et de stock

GBM
    → logique plus fédérale par marque
    → Storeland comme socle historique
    → UR et autres solutions pour coordonner certains besoins transverses
```

Le point important n'est pas seulement la différence d'outils.

Le point important est que les deux patrimoines traitent souvent les mêmes responsabilités, mais selon des découpages, règles et niveaux de maturité différents.

## Panorama BRD

Le paysage BRD est principalement décrit comme un système organisé autour d'un cœur SAP.

Autour de ce cœur gravitent plusieurs solutions spécialisées.

### Applications et composants mentionnés

- SAP : cœur ERP et support majeur des processus achats, ventes, finance, stocks et allocations.
- NewStore : solution liée aux parcours retail / omnicanaux.
- Salesforce : relation client et capacités d'engagement.
- Elastic : usages de recherche, catalogue ou exposition selon les contextes documentés.
- Optimate : planification, achats ou supply selon les périmètres étudiés.
- PIM / PLM : gestion ou contribution aux données produits selon les flux.
- WMS et partenaires logistiques : exécution opérationnelle et flux physiques.
- Maersk et partenaires : contribution aux opérations logistiques.

### Caractéristiques observées

BRD dispose d'une logique plus intégrée autour de SAP.

Cette centralisation donne de la robustesse, notamment sur certains flux structurants.

Elle s'accompagne cependant d'une forte complexité de paramétrage, en particulier sur les allocations, les règles de stock, les horizons, les priorités, les commandes spéciales, les précommandes et les traitements batch.

BRD illustre donc une situation où la mutualisation applicative existe déjà partiellement, mais où les responsabilités de décision restent difficiles à lire.

## Panorama GBM

Le paysage GBM historique est plus fédéral.

Il s'est construit autour des marques, des enseignes et de leurs spécificités.

### Applications et composants mentionnés

- Storeland : socle historique majeur, notamment pour les marques historiques.
- UR : application transverse apparue pour centraliser certaines demandes et leur cycle de vie.
- Cegid Y2 : périmètre magasin / POS et back-office selon les contextes.
- SoCloz : capacités omnicanales ou OMS selon les périmètres documentés.
- OMS C-LOG : orchestration logistique ou omnicanale selon les flux.
- Salesforce : relation client ou engagement selon les usages.
- Elastic : recherche, exposition ou contribution catalogue selon les contextes.
- Talend : intégration et échanges de données.
- PLM / PIM : données produit, articles, catalogues, saisons et attributs.
- MAP / BPC / CBS / SNC : outils ou composants spécialisés mentionnés dans les supports existants.
- WMS : exécution logistique et opérations physiques.

### Caractéristiques observées

GBM présente une logique historiquement distribuée et différenciée par marque.

Cette organisation préserve les spécificités métier, mais rend plus difficile la gouvernance transverse des demandes, ressources, règles et engagements.

L'apparition de UR est un signal important : malgré une logique ségrégée par marque, certaines demandes nécessitent un pilotage commun ou transverse.

GBM illustre donc une situation où l'autonomie locale est forte, mais où certains besoins dépassent naturellement les frontières applicatives et organisationnelles.

## Comparaison synthétique

| Dimension | BRD | GBM |
| --- | --- | --- |
| Logique dominante | Centralisation autour de SAP | Fédération historique par marque |
| Force principale | Robustesse d'un cœur commun | Préservation des spécificités métiers |
| Limite principale | Complexité des règles, paramétrages et responsabilités dispersées | Multiplication des outils et difficulté de gouvernance transverse |
| Signal fort | Allocation et stock très structurés mais complexes | UR révèle le besoin de fédération |
| Risque | Mutualiser sans clarifier les responsabilités | Préserver l'autonomie mais reproduire les silos |

## Responsabilités communes observées

Malgré des architectures différentes, les mêmes responsabilités apparaissent régulièrement :

- gérer les demandes ;
- gérer les engagements ;
- rendre les stocks et ressources visibles ;
- décider des allocations ;
- prioriser les demandes, clients, canaux ou marchés ;
- traiter les commandes d'achat et de vente ;
- suivre les jalons et retards ;
- déclencher préparation, expédition, livraison ou retour ;
- produire ou transmettre les documents nécessaires ;
- alimenter Finance et les systèmes d'exécution.

Cette convergence des responsabilités est plus importante que la diversité des applications.

Elle prépare le passage d'une lecture applicative à une lecture par domaines, responsabilités et capacités.

## Ce que ce panorama apprend à FLOW

Le panorama applicatif montre que FLOW ne peut pas être pensé comme un simple remplacement d'application.

BRD et GBM ne partent pas du même point.

Ils n'ont pas les mêmes outils, pas les mêmes règles, pas la même maturité applicative, pas le même niveau de centralisation.

Pourtant, ils doivent traiter des problématiques communes.

FLOW doit donc éviter deux pièges :

- imposer un modèle unique qui effacerait les spécificités utiles ;
- reproduire les silos existants sous une forme modernisée.

## À retenir

Le contexte applicatif BRD / GBM confirme l'intuition fondatrice de FLOW :

> La convergence ne doit pas commencer par le choix d'une solution unique, mais par l'identification des responsabilités communes que l'entreprise doit gouverner durablement.

Le panorama applicatif est donc un contexte, pas une cible.

Il explique d'où vient FLOW, mais il ne doit pas enfermer FLOW dans les catégories applicatives héritées.
