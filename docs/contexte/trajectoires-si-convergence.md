# Trajectoires SI et contexte de convergence

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Contributeur</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>10 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Comprendre le point de départ et les tensions observées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page n'est pas un panorama applicatif détaillé.

Elle sert à comprendre l'histoire et les trajectoires SI qui expliquent pourquoi FLOW existe.

Les panoramas applicatifs détaillés sont documentés séparément :

- [Panorama applicatif BRD](panorama-brd.md)
- [Panorama applicatif GBM](panorama-gbm.md)

Les points de tension à instruire sont documentés dans la section [Hotspots](../hotspots/index.md), notamment [Promesse commerciale et priorisation Wholesale](../hotspots/promesse-commerciale-wholesale.md).

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

Les applications initialement visées ne sont pas isolées. Elles s'inscrivent dans un paysage d'applications, d'intégrations, de référentiels, de systèmes d'exécution, de flux logistiques, d'informations produit, de canaux et de solutions de pilotage.

## Trois trajectoires à comprendre

La vision du programme mentionne BRD, GBM et Sarenza parce que ces trajectoires ne racontent pas la même histoire.

Elles produisent une richesse métier et IT, mais aussi une convergence difficile.

### GBM : un SI retail ouvert progressivement au digital et au B2B

GBM est historiquement plutôt un SI retail.

Le SI s'est structuré autour de StoreLand, avec une logique par marques et par instances.

Il a ensuite été ouvert au e-commerce, notamment avec Socloz et des composants autour de l'omnicanal.

Le B2B y a été intégré plus difficilement, avec des écarts de maturité entre marques.

Le module Négoce de StoreLand illustre cette situation : il est activé pour certaines marques premium, tandis que d'autres marques opèrent encore certains flux de manière plus manuelle ou dispersée.

### Sarenza : une trajectoire digitale et microservices

Sarenza apporte une culture différente : plus digitale, plus orientée développement spécifique, APIs, microservices et autonomie produit.

Cette trajectoire est importante pour FLOW parce qu'elle montre une autre manière de construire le SI : moins centrée sur un socle ERP ou retail historique, davantage sur des composants spécialisés et évolutifs.

Elle renforce l'idée que FLOW ne peut pas être pensé comme une simple centralisation applicative.

Le programme doit être capable d'intégrer des cultures IT différentes : progiciel, applications autonomes, systèmes par marque, composants digitaux et services spécialisés.

### BRD : un SI B2B / wholesale adapté au retail et à l'omnicanal

BRD semble plutôt issu d'un socle B2B / wholesale, ensuite adapté au retail et à l'omnicanal.

SAP y joue un rôle structurant, avec NewStore comme composant omnicanal / OMS.

Cette trajectoire donne un centre de gravité différent de GBM : plus centralisé, plus ERP, plus B2B / wholesale, puis adapté aux enjeux de retail, stock magasin, promesse et omnicanal.

## Deux centres de gravité presque inverses

Un insight client permet de résumer cette différence de manière très structurante.

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

Sarenza
Digital d'abord
    ↓
Composants spécifiques et microservices
    ↓
Culture produit / API / autonomie
```

Cette différence ne relève pas seulement des applications.

Elle décrit des centres de gravité historiques presque inverses.

FLOW ne doit donc pas chercher à aligner des SI équivalents.

Il doit créer une couche cible commune au-dessus d'héritages différents.

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

Le contexte applicatif ne doit pas seulement enregistrer une liste d'applications.

BRD, GBM et Sarenza ne diffèrent pas seulement par leurs applications. Ils diffèrent aussi par leur manière de représenter les responsabilités, les domaines, les flux et les frontières applicatives.

FLOW devra donc produire un urbanisme unifié permettant de positionner les applications et composants selon une grille comparable.

L'objectif n'est pas d'imposer immédiatement une cible unique, mais de rendre les points de vue comparables :

- même vocabulaire pour nommer les domaines ;
- mêmes critères pour positionner une application ;
- même distinction entre application, capacité, responsabilité et processus ;
- même lecture des systèmes remplacés, conservés, connectés ou laissés hors périmètre ;
- même capacité à identifier les écarts entre l'existant BRD, l'existant GBM, les apports Sarenza et la cible FLOW.

Sans cette grille commune, chaque périmètre risque de décrire son SI avec ses propres repères, ce qui rendrait la convergence difficile à piloter.

## Comparaison synthétique

| Dimension | BRD | GBM | Sarenza |
| --- | --- | --- |
| Trajectoire historique | B2B / wholesale adapté au retail et à l'omnicanal | Retail ouvert au e-commerce puis au B2B | Digital / e-commerce construit avec une culture de composants spécifiques |
| Logique dominante | Centralisation autour de SAP et NewStore | Fédération historique par marque | Autonomie produit, APIs, microservices |
| Socle principal | SAP, NewStore | StoreLand, Socloz, UR comme composant transverse | Composants digitaux et services spécialisés |
| Force principale | Robustesse transactionnelle et structuration des flux | Préservation des spécificités métiers retail et marques | Capacité d'évolution, culture produit et intégration par services |
| Limite principale | Complexité des règles, paramétrages et responsabilités de décision | Dispersion des outils, règles, instances et informations | Risque de spécialisation locale ou d'intégration spécifique |
| Signal fort pour FLOW | Allocation, ATP, stock disponible, cycle de vie commande | UR révèle le besoin d'orchestration transverse ; Négoce révèle la convergence intra-GBM | FLOW doit rester ouvert aux architectures plus modulaires |

## Comparaison par responsabilités

La comparaison BRD / GBM est suffisamment mûre pour être faite par responsabilités.

Elle ne doit pas encore être lue comme un mapping définitif application à application. Les applications citées sont des points d'observation, pas une cible validée.

| Responsabilité | Lecture BRD | Lecture GBM | Implication FLOW |
| --- | --- | --- |
| Cycle de vie commande | NewStore porte une partie du cycle de vie commande et de l'OMS ; SAP reste structurant sur le transactionnel | StoreLand porte des commandes par marque ; Socloz et UR reconstituent des visions transverses, notamment B2C | FLOW doit clarifier et probablement réunifier le cycle de vie commande transverse lorsque sa dispersion crée de la dette opérationnelle |
| Vision stock | SAP porte le stock entrepôt ; Cegid porte le stock magasin ; NewStore agrège les deux | StoreLand, Socloz, Zoho, l'écosystème C-LOG et les stocks magasins contribuent à la visibilité | Inventory Visibility est une capacité transverse critique, pas une simple extraction d'un système |
| Promesse / allocation | NewStore, SAP et les règles d'allocation / ATP sont à clarifier | Socloz, StoreLand, stock virtuel, réassort et canaux contribuent à la décision | FLOW doit distinguer disponibilité, réservation, allocation, promesse et réassort |
| Retours / litiges / exceptions | NewStore et les systèmes d'exécution participent au cycle retour ; la responsabilité exacte reste à clarifier | UR porte explicitement retours, remboursements, litiges et réintégration stock | Les exceptions sont candidates à une capacité Case / Order Lifecycle transverse |
| Achat fournisseur | SAP et les outils amont contribuent aux achats et commandes fournisseur | StoreLand Négoce, CBS et processus manuels contribuent aux achats fournisseur | La commande d'achat peut être candidate FLOW si elle participe au cycle de vie transverse, à la disponibilité future ou à un engagement d'approvisionnement ; CBS devra aussi pouvoir distinguer fournisseur et usine lorsque cette granularité conditionne la promesse |
| Engagement commercial / catalogue | PIM / PLM / pricing / canaux contribuent à l'offre et aux contenus | Module Négoce, Zoho, Elastic, Product Live et processus manuels contribuent à l'assortiment et au catalogue | FLOW ne doit pas absorber le design de l'engagement ; il doit consommer les agreements utiles à l'exécution |
| B2B / Wholesale | Centre de gravité historique plus naturel côté BRD | Canal ajouté plus difficilement dans un SI historiquement retail | FLOW doit modéliser les responsabilités, pas plaquer une étiquette canal unique |
| Logistique / exécution | WMS, transport, douanes, partenaires et systèmes d'exécution à connecter | C-LOG comme opérateur logistique, OMS C-LOG, EAI C-LOG, WMS, TMS / Transware, CBS et suivi expéditions à connecter | FLOW doit exposer et consommer des événements, sans devenir tous les systèmes d'exécution |
| Finance / documents | SAP FI/CO et les documents financiers restent structurants | Finance, documents B2B, factures et pièces opérationnelles à raccorder selon les flux | FLOW doit porter le suivi documentaire nécessaire au Case sans absorber toute la comptabilité |

## Zones d'incertitude à assumer

La comparaison actuelle est utile, mais elle reste une première lecture.

Plusieurs points ne sont pas encore assez stabilisés pour trancher :

- le mapping précis entre les responsabilités Socloz, NewStore, UR et StoreLand ;
- le rôle exact de FLOW dans la commande d'achat ;
- les responsabilités à réconcilier dans FLOW par rapport à celles qui restent portées par l'ERP, les expériences B2B, le domaine engagement ou les systèmes spécialisés ;
- la granularité de la vision stock attendue par canal, dépôt, marque, pays ou client ;
- les règles d'allocation, de promesse, de réassort et de priorisation ;
- le rôle futur de CBS comme domaine consommateur / contributeur ou comme source de responsabilités candidates FLOW ;
- l'hypothèse CBS comme SRM cible du groupe, ou comme premier lieu de recensement des fournisseurs, usines et sites de production ;
- l'adaptation fonctionnelle de CBS pour voir les usines ou sites de production, et pas seulement les fournisseurs ;
- le traitement des stocks confiés, parfois lus comme B2B côté BRD et retail côté GBM.

Ces incertitudes ne bloquent pas la comparaison. Elles doivent être affichées comme des hypothèses à instruire.

## Ce que ce contexte apprend à FLOW

Le contexte SI montre que FLOW ne peut pas être pensé comme un simple remplacement technique.

Le remplacement de StoreLand / Socloz côté GBM et de SAP / NewStore côté BRD impose de clarifier les responsabilités : lesquelles doivent être réunifiées dans FLOW, lesquelles restent dans Finance, lesquelles restent dans les systèmes d'exécution, lesquelles sont connectées, consommées ou contributrices ?

FLOW doit donc éviter trois pièges :

- remplacer des applications sans clarifier les responsabilités métier ;
- élargir indéfiniment son périmètre au motif que tout est connecté ;
- comparer BRD, GBM et Sarenza uniquement à partir des noms d'applications.

La comparaison doit se faire à partir d'une grille d'urbanisme commune, faute de quoi deux applications peuvent sembler équivalentes alors qu'elles ne portent pas les mêmes responsabilités, ou sembler différentes alors qu'elles participent à la même capacité métier.

Le cas d'UR côté GBM illustre ce point : UR entre dans le champ d'étude non parce qu'il figurait dans le périmètre applicatif initial, mais parce qu'il porte une responsabilité transverse qui ressemble fortement à une capacité cible FLOW.

Le cas du module Négoce StoreLand ajoute un autre enseignement : certaines responsabilités actuellement regroupées dans une application devront probablement être séparées dans la cible entre engagement commercial et exécution / achat.

Le cas de CBS ajoute une nuance supplémentaire : certains systèmes sont surtout des domaines consommateurs ou contributeurs de FLOW, mais manipulent des objets ou événements qui peuvent relever d'une responsabilité transverse FLOW.

La trajectoire CBS ne devra donc pas être lue uniquement comme une adaptation technique. Elle devra aussi intégrer une évolution fonctionnelle : voir les usines ou sites de production lorsque ces informations conditionnent les lead times, la promesse, les documents ou les événements d'exécution.

Elle devra surtout clarifier si CBS devient la SRM cible du groupe, s'il est le premier lieu de recensement fournisseur / usine, ou s'il reste un domaine spécialisé qui consomme une source de référence maintenue ailleurs.

## À retenir

Le contexte BRD / GBM / Sarenza confirme l'intuition fondatrice de FLOW :

> FLOW n'est pas seulement une convergence applicative. C'est une convergence de trajectoires SI différentes : un retail ouvert au digital et au B2B côté GBM, un B2B adapté au retail côté BRD, et une culture digitale plus modulaire côté Sarenza.

Il confirme aussi que le remplacement applicatif initial ne suffit pas à définir FLOW.

> Il faut identifier les responsabilités communes que l'entreprise doit gouverner durablement, puis décider lesquelles doivent être réunifiées dans FLOW, lesquelles restent dans des systèmes spécialisés, et lesquelles doivent seulement consommer ou produire des événements.

Enfin, il élargit la notion de convergence : FLOW devra traiter à la fois la convergence BRD / GBM, la convergence interne GBM entre marques, et l'intégration des cultures IT issues de trajectoires différentes.

Il confirme un enjeu de méthode : FLOW devra redéfinir un urbanisme unifié pour rendre comparables les positionnements applicatifs des différents périmètres dans le SI.
