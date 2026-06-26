# Panorama applicatif BRD et GBM

## Intention

Cette page sert d'orientation entre les panoramas applicatifs BRD et GBM.

Les deux environnements doivent être documentés séparément, car ils racontent deux histoires SI différentes.

- [Panorama applicatif BRD](panorama-brd.md)
- [Panorama applicatif GBM](panorama-gbm.md)

## Point de départ du programme

Le point de départ opérationnel du programme est concret : FLOW est envisagé comme le remplacement de deux socles applicatifs distincts selon les groupes.

```text
GBM : remplacer StoreLand / Socloz
BRD : remplacer SAP / NewStore
```

Cette formulation est importante pour un entrant du projet.

Elle évite de présenter FLOW uniquement comme une réflexion théorique sur les capacités.

Mais cette formulation ne suffit pas à définir le périmètre réel.

Côté GBM, l'analyse fait apparaître que UR entre également dans le champ d'étude de FLOW, car il porte déjà une responsabilité transverse de cycle de vie commande B2C, de retours, remboursements, litiges et réintégration stock.

La question de départ peut donc être formulée ainsi :

> FLOW doit remplacer StoreLand / Socloz côté GBM et SAP / NewStore côté BRD. Quelles autres responsabilités applicatives doivent entrer dans le champ d'étude parce qu'elles portent déjà une responsabilité FLOW-native ?

Cette question ouvre immédiatement une analyse d'urbanisme.

Les applications initialement visées ne sont pas isolées. Elles s'inscrivent dans un paysage d'applications, d'intégrations, de référentiels, de systèmes d'exécution, de flux logistiques, de données produit, de canaux et de solutions de pilotage.

## Deux histoires SI différentes

BRD et GBM ne partent pas du même point.

Un insight client permet de résumer cette différence de manière très structurante.

GBM est historiquement plutôt un SI retail, ouvert progressivement au e-commerce, puis étendu plus difficilement au B2B.

BRD semble plutôt issu d'un socle B2B / wholesale, ensuite adapté au retail et à l'omnicanal.

```text
GBM
Retail d'abord
    ↓
E-commerce ajouté
    ↓
B2B intégré plus difficilement

BRD
B2B / wholesale d'abord
    ↓
Retail ajouté
    ↓
Omnicanal à recomposer
```

Cette différence ne relève pas seulement des applications. Elle décrit deux centres de gravité historiques presque inverses.

FLOW ne doit donc pas chercher à aligner deux SI équivalents. Il doit créer une couche cible commune au-dessus de deux héritages différents.

```text
BRD
    → logique plus centralisée autour de SAP
    → NewStore comme OMS
    → socle historiquement plus B2B / wholesale
    → adaptation au retail, au stock magasin, à l'omnicanal et à la promesse

GBM
    → logique historiquement fédérale par marque
    → StoreLand comme socle retail historique
    → une instance StoreLand par marque
    → Socloz comme composant omnicanal / e-commerce
    → UR comme signal d'un besoin transverse
    → B2B intégré plus difficilement dans un paysage d'abord retail
```

## Deux lectures d'urbanisme à rendre comparables

Le panorama applicatif ne doit pas seulement enregistrer une liste d'applications.

BRD et GBM ne diffèrent pas seulement par leurs applications. Ils diffèrent aussi par leur manière de représenter les responsabilités, les domaines, les flux et les frontières applicatives.

FLOW devra donc produire un urbanisme unifié permettant de positionner les applications BRD et GBM selon une grille comparable.

L'objectif n'est pas d'imposer immédiatement une cible unique, mais de rendre les points de vue comparables :

- même vocabulaire pour nommer les domaines ;
- mêmes critères pour positionner une application ;
- même distinction entre application, capacité, responsabilité et processus ;
- même lecture des systèmes remplacés, conservés, connectés ou laissés hors périmètre ;
- même capacité à identifier les écarts entre l'existant BRD, l'existant GBM et la cible FLOW.

Sans cette grille commune, chaque groupe risque de décrire son SI avec ses propres repères, ce qui rendrait la convergence difficile à piloter.

## Comparaison synthétique

| Dimension | BRD | GBM |
| --- | --- | --- |
| Trajectoire historique | B2B / wholesale adapté au retail et à l'omnicanal | Retail ouvert au e-commerce puis au B2B |
| Logique dominante | Centralisation autour de SAP et NewStore | Fédération historique par marque |
| Socle principal | SAP, NewStore | StoreLand, Socloz, puis UR comme composant transverse |
| Structure historique | Socle plus centralisé, fortement paramétré | Instances StoreLand par marque, plus StoreLand Fournitures mutualisé |
| Force principale | Robustesse transactionnelle et structuration des flux | Préservation des spécificités métiers retail et marques |
| Limite principale | Complexité des règles, paramétrages et responsabilités de décision | Dispersion des outils, règles, instances et données |
| Signal fort | Allocation, ATP, stock disponible, cycle de vie commande | UR révèle le besoin d'orchestration transverse |
| Risque | Confondre remplacement applicatif et clarification des responsabilités | Préserver l'autonomie mais reproduire les silos et les fragments d'instances |
| Enjeu d'urbanisme | Traduire une lecture déjà structurée du SI BRD dans une grille commune | Recomposer une lecture commune à partir d'un historique retail fédéral et multi-marques |

## Responsabilités communes observées

Malgré des architectures différentes, les mêmes responsabilités apparaissent régulièrement :

- gérer les demandes ;
- gérer les engagements ;
- rendre les stocks et ressources visibles ;
- décider des allocations ;
- prioriser les demandes, clients, canaux ou marchés ;
- traiter les commandes d'achat et de vente ;
- suivre les jalons et retards ;
- gérer les retours, litiges et exceptions ;
- déclencher préparation, expédition, livraison ou retour ;
- produire ou transmettre les documents nécessaires ;
- alimenter Finance et les systèmes d'exécution.

Cette convergence des responsabilités est plus importante que la diversité des applications.

Elle prépare le passage d'une lecture applicative à une lecture par domaines, responsabilités et capacités.

## Ce que ce panorama apprend à FLOW

Le panorama applicatif montre que FLOW ne peut pas être pensé comme un simple remplacement technique.

Le remplacement de StoreLand / Socloz côté GBM et de SAP / NewStore côté BRD impose de clarifier les responsabilités : lesquelles sont reprises par FLOW, lesquelles restent dans Finance, lesquelles restent dans les systèmes d'exécution, lesquelles sont seulement connectées ou consommées ?

FLOW doit donc éviter deux pièges :

- remplacer des applications sans clarifier les responsabilités métier ;
- élargir indéfiniment son périmètre au motif que tout est connecté.

FLOW doit aussi éviter un troisième piège : comparer BRD et GBM uniquement à partir des noms d'applications.

La comparaison doit se faire à partir d'une grille d'urbanisme commune, faute de quoi deux applications peuvent sembler équivalentes alors qu'elles ne portent pas les mêmes responsabilités, ou sembler différentes alors qu'elles participent à la même capacité métier.

Le cas d'UR côté GBM illustre ce point : UR entre dans le champ d'étude non parce qu'il figurait dans le périmètre applicatif initial, mais parce qu'il porte une responsabilité transverse qui ressemble fortement à une capacité cible FLOW.

## À retenir

Le contexte applicatif BRD / GBM confirme l'intuition fondatrice de FLOW :

> FLOW n'est pas seulement une convergence applicative. C'est une convergence de deux trajectoires SI opposées : un retail ouvert au digital et au B2B côté GBM, et un B2B adapté au retail côté BRD.

Il confirme aussi que le remplacement applicatif initial ne suffit pas à définir FLOW.

> Il faut identifier les responsabilités communes que l'entreprise doit gouverner durablement, puis décider quels systèmes FLOW remplace, connecte, orchestre ou laisse hors périmètre.

Enfin, il confirme un enjeu de méthode : FLOW devra redéfinir un urbanisme unifié pour rendre comparables les positionnements applicatifs des deux groupes dans le SI.
