# Panorama applicatif BRD et GBM

## Intention

Cette page sert d'orientation entre les panoramas applicatifs BRD et GBM.

Les deux environnements doivent être documentés séparément, car ils racontent deux histoires SI différentes.

- [Panorama applicatif BRD](panorama-brd.md)
- [Panorama applicatif GBM](panorama-gbm.md)
- [Convergence B2B / Wholesale](convergence-b2b-wholesale.md)

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

## Une convergence aussi interne à GBM

La convergence ne concerne pas seulement BRD et GBM.

Elle concerne aussi les marques au sein de GBM.

Le module Négoce de StoreLand rend cette convergence interne très visible : il est activé pour les marques premium, tandis que d'autres marques opèrent encore certains flux de manière plus manuelle ou dispersée.

```text
Convergence inter-groupes
    GBM ↔ BRD

Convergence intra-GBM
    marques premium ↔ autres marques
```

Cette observation change la lecture du programme.

FLOW ne doit pas seulement rapprocher deux groupes. Il doit aussi aider GBM à expliciter ce qui doit être mutualisé entre marques, ce qui doit rester différenciant et ce qui doit être porté par une capacité commune.

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
| Signal fort | Allocation, ATP, stock disponible, cycle de vie commande | UR révèle le besoin d'orchestration transverse ; Négoce révèle la convergence intra-GBM |
| Risque | Confondre remplacement applicatif et clarification des responsabilités | Préserver l'autonomie mais reproduire les silos et les fragments d'instances |
| Enjeu d'urbanisme | Traduire une lecture déjà structurée du SI BRD dans une grille commune | Recomposer une lecture commune à partir d'un historique retail fédéral et multi-marques |

## Comparaison par responsabilités

La comparaison BRD / GBM est suffisamment mûre pour être faite par responsabilités.

Elle ne doit pas encore être lue comme un mapping définitif application à application. Les applications citées sont des points d'observation, pas une cible validée.

| Responsabilité | Lecture BRD | Lecture GBM | Implication FLOW |
| --- | --- | --- | --- |
| Cycle de vie commande | NewStore porte une partie du cycle de vie commande et de l'OMS ; SAP reste structurant sur le transactionnel | StoreLand porte des commandes par marque ; Socloz et UR reconstituent des visions transverses, notamment B2C | FLOW doit clarifier s'il porte un cycle de vie commande transverse ou s'il orchestre plusieurs cycles locaux |
| Vision stock | SAP porte le stock entrepôt ; Cegid porte le stock magasin ; NewStore agrège les deux | StoreLand, Socloz, Zoho, C-LOG / EAI et les stocks magasins contribuent à la visibilité | Inventory Visibility est une capacité transverse critique, pas une simple extraction d'un système |
| Promesse / allocation | NewStore, SAP et les règles d'allocation / ATP sont à clarifier | Socloz, StoreLand, stock virtuel, réassort et canaux contribuent à la décision | FLOW doit distinguer disponibilité, réservation, allocation, promesse et réassort |
| Retours / litiges / exceptions | NewStore et les systèmes d'exécution participent au cycle retour ; la responsabilité exacte reste à clarifier | UR porte explicitement retours, remboursements, litiges et réintégration stock | Les exceptions sont candidates à une capacité Case / Order Lifecycle transverse |
| Achat fournisseur | SAP et les outils amont contribuent aux achats et commandes fournisseur | StoreLand Négoce, CBS et processus manuels contribuent aux achats fournisseur | La commande d'achat peut être candidate FLOW, mais les processus spécialisés restent à séparer |
| Engagement commercial / catalogue | PIM / PLM / pricing / canaux contribuent à l'offre et aux contenus | Module Négoce, Zoho, Elastic, Product Live et processus manuels contribuent à l'assortiment et au catalogue | FLOW ne doit pas absorber le design de l'engagement ; il doit consommer les agreements utiles à l'exécution |
| B2B / Wholesale | Centre de gravité historique plus naturel côté BRD | Canal ajouté plus difficilement dans un SI historiquement retail | FLOW doit modéliser les responsabilités, pas plaquer une étiquette canal unique |
| Retail / magasins | Adaptation autour de Cegid, stock magasin et NewStore | Centre de gravité historique, mais fragmenté par marques et instances | FLOW doit unifier sans effacer l'autonomie utile des marques et magasins |
| Logistique / exécution | WMS, transport, douanes, partenaires et systèmes d'exécution à connecter | C-LOG / EAI, OMS C-LOG, Transport, CBS et suivi expéditions à connecter | FLOW doit exposer et consommer des événements, sans devenir tous les systèmes d'exécution |
| Finance / documents | SAP FI/CO et les documents financiers restent structurants | Finance, documents B2B, factures et pièces opérationnelles à raccorder selon les flux | FLOW doit porter le suivi documentaire nécessaire au Case sans absorber toute la comptabilité |

## Zones d'incertitude à assumer

La comparaison actuelle est utile, mais elle reste une première lecture.

Plusieurs points ne sont pas encore assez stabilisés pour trancher :

- le mapping précis entre les responsabilités Socloz, NewStore, UR et StoreLand ;
- le rôle exact de FLOW dans la commande d'achat ;
- la frontière cible entre FLOW, ERP, SI B2B et domaine engagement ;
- la granularité de la vision stock attendue par canal, dépôt, marque, pays ou client ;
- les règles d'allocation, de promesse, de réassort et de priorisation ;
- le rôle futur de CBS comme domaine consommateur ou comme source de responsabilités candidates FLOW ;
- le traitement des stocks confiés, parfois lus comme B2B côté BRD et retail côté GBM.

Ces incertitudes ne bloquent pas la comparaison. Elles doivent être affichées comme des hypothèses à instruire.

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

Le cas du module Négoce StoreLand ajoute un autre enseignement : certaines responsabilités actuellement regroupées dans une application devront probablement être séparées dans la cible entre engagement commercial et exécution / achat.

Le cas de CBS ajoute une nuance supplémentaire : certains systèmes sont surtout des domaines consommateurs de FLOW, mais manipulent des objets ou événements qui peuvent relever d'une responsabilité transverse FLOW.

## À retenir

Le contexte applicatif BRD / GBM confirme l'intuition fondatrice de FLOW :

> FLOW n'est pas seulement une convergence applicative. C'est une convergence de deux trajectoires SI opposées : un retail ouvert au digital et au B2B côté GBM, et un B2B adapté au retail côté BRD.

Il confirme aussi que le remplacement applicatif initial ne suffit pas à définir FLOW.

> Il faut identifier les responsabilités communes que l'entreprise doit gouverner durablement, puis décider quels systèmes FLOW remplace, connecte, orchestre ou laisse hors périmètre.

Enfin, il élargit la notion de convergence : FLOW devra traiter à la fois la convergence BRD / GBM et la convergence interne GBM entre marques, notamment sur le B2B, le Négoce, les commandes d'achat et les processus encore manuels.

Il confirme un enjeu de méthode : FLOW devra redéfinir un urbanisme unifié pour rendre comparables les positionnements applicatifs des deux groupes dans le SI.
