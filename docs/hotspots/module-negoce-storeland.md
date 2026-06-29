# Module Négoce StoreLand

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsors, architecture, métiers concernés</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page documente le hotspot lié au module Négoce de StoreLand.

Le sujet est distinct du hotspot sur la promesse commerciale et la priorisation Wholesale.

Ici, la question n'est pas d'abord : comment prioriser le stock ?

La question est : quelles responsabilités du module Négoce doivent être reprises, réintégrées ou laissées dans un domaine consommateur de FLOW ?

## Pourquoi c'est un hotspot

Le module Négoce regroupe aujourd'hui plusieurs responsabilités qui ne relèvent pas forcément du même domaine cible.

Il permet notamment :

- d'entrer un client ;
- de construire un assortiment ;
- de préparer un commercial agreement ;
- de manipuler un catalogue et des conditions commerciales ;
- de passer des commandes d'achat ;
- de soutenir certains processus B2B / Wholesale.

Ces responsabilités sont aujourd'hui regroupées dans un même outil.

Mais dans la cible FLOW, elles pourraient relever de zones différentes : Engagement, Demand, Supply, Finance ou systèmes spécialisés.

## Couverture différenciée dans GBM

Le module Négoce est coûteux.

Il n'est donc activé que pour les marques premium.

Pour les autres marques, certaines commandes ou opérations B2B sont traitées de manière plus manuelle ou dispersée : mail, Excel, imports depuis d'autres référentiels ou autres mécanismes opérationnels.

Cette situation révèle que la convergence n'est pas seulement une convergence BRD / GBM.

Elle est aussi une convergence intra-GBM.

```text
Marques premium
    → module Négoce StoreLand
    → processus outillé

Autres marques
    → mail / Excel / imports / référentiels divers
    → processus plus manuel ou dispersé
```

L'idée cible est d'offrir une capacité Négoce plus largement disponible.

Mais cela ne signifie pas que toutes les responsabilités du module Négoce actuel doivent être reprises dans FLOW.

## Découpler les responsabilités du Négoce

Le module Négoce mélange au moins deux familles de responsabilités.

### 1. Design commercial et engagement

Cette famille concerne la manière dont l'offre est construite, négociée, rendue vendable et présentée aux clients B2B.

Elle couvre notamment :

- client ;
- assortiment ;
- commercial agreement ;
- catalogue ;
- prix ;
- conditions commerciales ;
- portail ou expérience B2B.

Cette famille relève plutôt du monde de l'Engagement ou d'un domaine consommateur de FLOW.

FLOW peut consommer le résultat de ces décisions, mais il n'a pas vocation à devenir l'outil de construction commerciale.

### 2. Commandes, engagements et exécution

Cette famille concerne les responsabilités qui touchent au cycle de vie d'une demande ou d'un engagement opérationnel.

Elle peut couvrir :

- commande d'achat ;
- engagement d'approvisionnement ;
- disponibilité future ;
- promesse ;
- allocation ;
- suivi d'exécution ;
- événements ;
- réception ;
- documents associés.

Cette famille peut entrer dans le champ FLOW lorsqu'elle participe à la cohérence du Demand & Fulfillment.

## Recommandation d'architecture

La recommandation d'architecture est de ne pas raisonner “module Négoce = à reprendre ou à exclure”.

Il faut découper le module par responsabilités.

```text
Engagement / Commercial Design
    → client
    → assortiment
    → commercial agreement
    → catalogue
    → prix / conditions
    → expérience B2B

FLOW
    → commande d'achat si elle participe au cycle de vie transverse
    → engagement d'approvisionnement
    → promesse commerciale
    → allocation et priorisation
    → suivi d'exécution
    → événements
    → disponibilité future
```

Le processus de négociation, d'assortiment et de fabrication du catalogue relève plutôt d'un domaine consommateur de FLOW.

La commande d'achat peut entrer dans FLOW si elle participe à l'exécution de la demande, à l'approvisionnement, à la promesse ou à la visibilité des engagements.

FLOW ne doit pas devenir l'outil de construction d'assortiment ou de commercial agreement.

En revanche, FLOW peut avoir besoin de consommer le résultat de ces agreements et de porter ou exposer les commandes, engagements, promesses, allocations, priorisations et événements associés.

## Questions structurantes pour FLOW

Ce hotspot doit permettre de clarifier :

- Quelles responsabilités du module Négoce sont réellement candidates à FLOW ?
- Quelles responsabilités doivent rester dans un domaine Engagement / Commercial Design ?
- La commande d'achat B2B / Négoce est-elle une capacité FLOW lorsqu'elle participe au cycle de vie transverse d'une demande ?
- Le Product Agreement Catalog est-il le bon point d'interface entre Engagement et FLOW ?
- Quelles capacités Négoce doivent être généralisées à toutes les marques GBM ?
- La convergence intra-GBM doit-elle précéder la convergence avec BRD sur certains sujets ?
- Quelles responsabilités doivent être remplacées, encapsulées, conservées ou réintégrées autour de FLOW ?

## À retenir

Le module Négoce StoreLand n'est pas un bloc à reprendre tel quel.

C'est un révélateur de responsabilités mélangées.

Certaines responsabilités relèvent du design commercial et de l'engagement.

D'autres touchent à la demande, à la commande, à la promesse, à l'approvisionnement et à l'exécution.

FLOW doit instruire ce découpage pour éviter deux erreurs : absorber trop de responsabilités commerciales dans la plateforme, ou laisser hors de FLOW des responsabilités nécessaires à la cohérence Demand & Fulfillment.
