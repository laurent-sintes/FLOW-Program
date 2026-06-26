# Convergence B2B / Wholesale

## Intention

Cette page documente les enseignements relatifs au B2B / Wholesale dans le programme FLOW.

Le sujet est structurant car il se situe à la frontière entre plusieurs mondes :

- le front office B2B ;
- le CRM et le portail client ;
- l'engagement commercial ;
- le catalogue et l'assortiment ;
- les commandes d'achat et de vente ;
- le futur ERP ;
- FLOW et ses responsabilités de demande, stock, promesse, allocation et exécution.

L'objectif est de ne pas faire entrer mécaniquement tout le B2B dans FLOW, tout en identifiant les responsabilités B2B qui touchent directement au fulfillment.

## Point de départ

Le B2B / Wholesale apparaît comme un domaine pouvant converger entre GBM et BRD sur une partie importante des briques middle office, front office et BI.

La difficulté principale se situe moins dans les usages front / middle que dans les frontières avec :

- le back-office achat / vente ;
- les ERP ;
- les commandes ;
- les catalogues ;
- les prix ;
- les stocks ;
- les règles d'allocation et de promesse ;
- les responsabilités qui pourraient être reprises par FLOW.

Le sujet doit donc être traité comme un domaine adjacent à FLOW, et non comme un sous-ensemble automatique de FLOW.

```text
Front B2B / CRM / portail / BI / support
        ≠
Back-office ERP / achat / vente / finance / logistique
        ≠
FLOW / orchestration / fulfillment / stock / promesse
```

## GBM : un B2B greffé sur un SI historiquement retail

GBM est historiquement un SI retail, ouvert ensuite au e-commerce, puis plus difficilement au B2B.

Cette trajectoire explique pourquoi le B2B GBM s'appuie sur plusieurs composants :

- StoreLand ;
- le module Négoce de StoreLand ;
- Zoho CRM ;
- Zoho Analytics ;
- Zoho Campaigns ;
- Zoho Desk / Sign selon les usages ;
- Elastic ;
- Product Live ;
- Azure B2C ;
- C-LOG / COSMOS ;
- des imports, fichiers ou traitements manuels selon les marques.

Le B2B GBM ne doit donc pas être lu comme un domaine homogène déjà complètement outillé.

## Module Négoce StoreLand

Le module Négoce de StoreLand permet d'adresser deux grandes familles de fonctionnalités.

### 1. Design commercial et engagement

Le module permet d'entrer un client, de construire un assortiment et de préparer un commercial agreement.

Cette famille de responsabilités relève plutôt du monde de l'engagement :

```text
Client
Assortiment
Commercial agreement
Catalogue
Prix
Conditions commerciales
```

Elle concerne la manière dont l'offre est construite, négociée, rendue vendable et présentée aux clients B2B.

### 2. Commandes d'achat

Le module permet également de passer des commandes d'achat.

Cette responsabilité est d'une autre nature.

Elle touche potentiellement à FLOW si la commande d'achat participe à l'exécution d'une demande, à l'approvisionnement, à la disponibilité future, à la promesse ou au suivi d'exécution.

```text
Commande d'achat
Engagement d'approvisionnement
Suivi d'exécution
Réception
Événements
Disponibilité future
```

## Couverture différenciée selon les marques

Le module Négoce est coûteux.

Il n'est donc activé que pour les marques premium.

Pour les autres marques, certaines commandes sont passées de manière plus manuelle ou dispersée : mail, Excel, imports depuis d'autres référentiels ou autres mécanismes opérationnels.

Cette situation révèle que GBM n'est pas homogène en interne.

```text
Marques premium
    → module Négoce StoreLand
    → processus outillé

Autres marques
    → mail / Excel / imports / référentiels divers
    → processus plus manuel ou dispersé
```

L'idée cible est d'avoir un module ou une capacité Négoce pour tout le monde.

Mais cela ne signifie pas nécessairement que toutes les responsabilités du module Négoce actuel doivent être reprises au même endroit.

## Insight : la convergence est aussi intra-GBM

Un insight important est que la convergence ne concerne pas seulement BRD et GBM.

Elle concerne aussi les marques au sein de GBM.

```text
Convergence inter-groupes
    GBM ↔ BRD

Convergence intra-GBM
    marques premium ↔ autres marques
```

Le module Négoce rend cette convergence interne très visible : certaines marques disposent d'un processus outillé, tandis que d'autres opèrent encore par des moyens plus manuels ou dispersés.

FLOW doit donc éviter de considérer GBM comme un bloc homogène.

La convergence doit être pensée à deux niveaux :

- convergence entre groupes ;
- convergence entre marques et niveaux de maturité au sein de GBM.

## Recommandation d'architecture — découpler les responsabilités du Négoce

Le module Négoce regroupe aujourd'hui des responsabilités qui pourraient relever de domaines cibles différents.

La recommandation d'architecture est de découpler ces responsabilités dans la cible.

```text
Engagement / Commercial Design
    → client
    → assortiment
    → commercial agreement
    → catalogue
    → prix / conditions

FLOW
    → commande d'achat
    → engagement d'approvisionnement
    → suivi d'exécution
    → événements
    → disponibilité future
```

Le processus de négociation, d'assortiment et de fabrication du catalogue relève plutôt du domaine engagement / commercial / consommateur.

La commande d'achat peut entrer dans le champ FLOW si elle participe à l'exécution de la demande, à l'approvisionnement, à la promesse ou à la visibilité des engagements.

FLOW ne doit pas devenir l'outil de construction d'assortiment ou de commercial agreement.

En revanche, FLOW peut avoir besoin de consommer le résultat de ces agreements et de piloter les commandes d'achat ou les événements associés.

## Front B2B et domaine d'engagement

Le SI B2B doit conserver ses responsabilités propres autour du front office, du CRM, du portail, du support, des campagnes, des documents et du pilotage commercial.

Ces responsabilités ne sont pas naturellement des responsabilités FLOW.

Elles relèvent plutôt du domaine de l'engagement :

- relation client B2B ;
- segmentation commerciale ;
- portail client ;
- documents commerciaux ;
- campagnes ;
- support ;
- pilotage commercial ;
- construction ou publication de catalogues.

FLOW doit donc se concentrer sur les responsabilités transverses nécessaires à l'exécution d'une demande.

## Stocks confiés : un révélateur de divergence BRD / GBM

Le sujet des stocks confiés montre que les mêmes réalités opérationnelles peuvent être classées différemment selon les groupes.

Des objets comme les corners, les franchisés ou les magasins en stocks confiés peuvent être lus comme du B2B côté BRD, alors qu'ils relèvent plutôt du retail côté GBM.

Cette divergence est importante.

Elle montre que le périmètre FLOW ne doit pas être défini uniquement par les canaux — retail, e-commerce, marketplace ou B2B — mais par les responsabilités transverses nécessaires à l'exécution d'une demande.

## Questions structurantes pour FLOW

Le sujet B2B / Wholesale conduit à plusieurs questions :

- La commande d'achat B2B / Négoce doit-elle être une capacité FLOW ?
- La négociation, l'assortiment et le catalogue doivent-ils rester dans le domaine engagement ?
- Quelles responsabilités du module Négoce doivent être généralisées à toutes les marques GBM ?
- La convergence GBM doit-elle d'abord harmoniser les marques avant de converger avec BRD ?
- Le B2B doit-il être traité comme un canal spécifique ou comme une variation d'un même objet demande / commande ?
- Où se situe la frontière cible entre CRM B2B, portail client, ERP, FLOW et systèmes d'exécution ?
- Les stocks confiés doivent-ils être modélisés par canal, par responsabilité ou par type d'engagement ?
- Quels demi-flux doivent être pérennes, et lesquels peuvent rester transitoires pendant la trajectoire ?

## À retenir

Le B2B / Wholesale ne doit pas être absorbé en bloc dans FLOW.

FLOW doit reprendre ou exposer les capacités nécessaires au fulfillment : stock, promesse, allocation, commande, exécution, retour, réintégration et événements.

Le SI B2B doit conserver ses responsabilités propres de front office, CRM, portail client, support, campagnes, documents et pilotage commercial.

Le module Négoce StoreLand est un bon révélateur : il regroupe aujourd'hui des responsabilités de design commercial et des responsabilités d'achat / exécution qui pourraient être séparées dans la cible.

Enfin, la convergence ne se limite pas à BRD et GBM. Elle doit aussi traiter les écarts de maturité entre marques GBM, notamment entre les marques premium outillées par le module Négoce et les autres marques encore opérées de manière plus manuelle.
