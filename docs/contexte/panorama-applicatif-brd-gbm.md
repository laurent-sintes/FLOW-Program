# Panorama applicatif BRD et GBM

## Intention

Cette page sert d'orientation entre les panoramas applicatifs BRD et GBM.

Les deux environnements doivent être documentés séparément, car ils racontent deux histoires SI différentes.

- [Panorama applicatif BRD](panorama-brd.md)
- [Panorama applicatif GBM](panorama-gbm.md)

## Point de départ du programme

Le point de départ opérationnel du programme est concret : FLOW est envisagé comme le remplacement de SAP et NewStore.

Cette formulation est importante pour un entrant du projet.

Elle évite de présenter FLOW uniquement comme une réflexion théorique sur les capacités.

La question de départ peut être formulée ainsi :

> FLOW doit remplacer SAP et NewStore. Doit-il remplacer autre chose également ?

Cette question ouvre immédiatement une analyse d'urbanisme.

SAP et NewStore ne sont pas isolés. Ils s'inscrivent dans un paysage d'applications, d'intégrations, de référentiels, de systèmes d'exécution, de flux logistiques, de données produit, de canaux et de solutions de pilotage.

## Deux histoires SI différentes

BRD et GBM ne partent pas du même point.

```text
BRD
    → logique plus centralisée autour de SAP
    → NewStore comme OMS
    → solutions spécialisées autour du cœur transactionnel
    → forte technicité des règles d'allocation et de stock

GBM
    → logique historiquement fédérale par marque
    → Storeland comme socle historique
    → UR comme signal d'un besoin transverse
    → multiplication d'outils spécialisés et de frontières locales
```

## Comparaison synthétique

| Dimension | BRD | GBM |
| --- | --- | --- |
| Logique dominante | Centralisation autour de SAP et NewStore | Fédération historique par marque |
| Socle principal | SAP, NewStore | Storeland, puis solutions complémentaires |
| Force principale | Robustesse transactionnelle et structuration des flux | Préservation des spécificités métiers |
| Limite principale | Complexité des règles, paramétrages et responsabilités de décision | Dispersion des outils, règles et données |
| Signal fort | Allocation, ATP, stock disponible, cycle de vie commande | UR révèle le besoin d'orchestration transverse |
| Risque | Confondre remplacement applicatif et clarification des responsabilités | Préserver l'autonomie mais reproduire les silos |

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

Le panorama applicatif montre que FLOW ne peut pas être pensé comme un simple remplacement technique.

Le remplacement de SAP et NewStore impose de clarifier les responsabilités : lesquelles sont reprises par FLOW, lesquelles restent dans Finance, lesquelles restent dans les systèmes d'exécution, lesquelles sont seulement connectées ou consommées ?

FLOW doit donc éviter deux pièges :

- remplacer des applications sans clarifier les responsabilités métier ;
- élargir indéfiniment son périmètre au motif que tout est connecté.

## À retenir

Le contexte applicatif BRD / GBM confirme l'intuition fondatrice de FLOW :

> Le remplacement de SAP et NewStore ne suffit pas à définir FLOW. Il faut identifier les responsabilités communes que l'entreprise doit gouverner durablement, puis décider quels systèmes FLOW remplace, connecte, orchestre ou laisse hors périmètre.
