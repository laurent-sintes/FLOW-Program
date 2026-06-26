# FLOW dans l’écosystème GBM

## Intention

Cette page propose un premier positionnement de FLOW dans l'écosystème applicatif GBM.

Elle ne cherche pas à représenter tous les flux existants.

Elle sert à montrer comment FLOW se place par rapport :

- aux expériences et applications d'engagement ;
- aux systèmes produit, catalogue et agreements ;
- aux systèmes Supply et d'exécution ;
- aux socles historiques StoreLand, Socloz et UR, qui sont dans la trajectoire de transformation.

## Schéma de positionnement

![FLOW dans l’écosystème GBM](../assets/images/architecture-cible-flow-ecosysteme-gbm.svg)

## Lecture du schéma

FLOW ne remplace pas tout le SI GBM.

FLOW se positionne comme la plateforme Demand qui reprend les responsabilités transverses aujourd'hui dispersées entre plusieurs composants.

| Zone | Rôle dans l'écosystème |
| --- | --- |
| Engagement / Expériences | Captent les intentions, exposent les parcours client et consomment les capacités FLOW. |
| Produit / Offre / Agreements | Construisent ou gouvernent les produits, catalogues, assortiments, agreements et conditions. |
| Plateforme FLOW | Porte les Cases, le stock unifié, le réseau d'exécution et les projections nécessaires à l'instruction des demandes. |
| Supply / Exécution | Exécute, confirme, transporte, documente, alimente Finance ou publie des événements opérationnels. |
| Socles GBM dans la trajectoire | StoreLand, Socloz et UR portent aujourd'hui des responsabilités transverses candidates FLOW. |

## Socles GBM dans la trajectoire

StoreLand, Socloz et UR ne sont pas de simples satellites.

Ils sont au cœur de la trajectoire de transformation GBM.

```text
StoreLand
    → socle historique retail multi-instances
    → commandes, stocks, opérations par marque

Socloz
    → orchestration omnicanale / e-commerce
    → stock, promesse ou réservation à clarifier

UR / United Retail
    → cycle de vie commande B2C transverse
    → retours, remboursements, litiges, réintégration stock
```

Ces systèmes doivent être analysés par responsabilité.

La question n'est pas seulement :

> Quelle application remplace-t-on ?

La question est :

> Quelles responsabilités FLOW doit-il reprendre, généraliser ou rendre explicites ?

## Applications satellites

Les applications d'engagement, de produit, de Supply, de Finance ou d'exécution ne disparaissent pas mécaniquement.

Elles peuvent rester :

- consommatrices de FLOW ;
- contributrices de projections ;
- systèmes d'exécution ;
- sources d'événements ;
- domaines spécialisés conservant leur autonomie.

Exemples :

```text
SFCC / Mirakl / Zoho / Elastic
    → expériences, commerce, B2B, recherche, engagement

PLM / PIM / Product Live / Négoce
    → produits, catalogues, assortiments, agreements

C-LOG / EAI / CBS / Transport / Dépôts / Finance
    → exécution, collaboration fournisseur, documents, statuts, événements
```

## Positionnement cible

La cible ne consiste pas à déplacer tout GBM dans FLOW.

La cible consiste à clarifier ce qui relève de FLOW :

- le Case ;
- les décisions ;
- les promesses ;
- les facts stock ;
- les réservations ;
- les allocations / tagging ;
- les besoins d'exécution ;
- les projections opérationnelles nécessaires ;
- les événements qui enrichissent les Vues 360.

Et ce qui reste autour :

- les expériences client ;
- la conception produit ;
- l'enrichissement catalogue ;
- la relation client spécialisée ;
- l'exécution logistique physique ;
- les documents fournisseur spécialisés ;
- la comptabilité et la finance.

## À retenir

FLOW devient le point de cohérence Demand dans l'univers GBM.

Il ne remplace pas tout le paysage applicatif.

Il reprend les responsabilités transverses aujourd'hui dispersées, tout en laissant les applications satellites jouer leur rôle de consommateurs, contributeurs ou systèmes d'exécution.
