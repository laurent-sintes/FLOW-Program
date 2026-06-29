# L'allocation révèle la vraie nature de la convergence

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Sponsor, Contributeur</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>4 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Contexte

Dans le référentiel documentaire constitué avant FLOW, la problématique d'allocation apparaît de manière récurrente.

Elle est présente dans les ateliers, les besoins cibles, les comparaisons BRD / GBM, les scénarios de scoring ERP et les discussions autour des OMS.

À première vue, l'allocation peut sembler être une fonctionnalité parmi d'autres : réserver du stock, affecter des quantités, prioriser des commandes, recalculer une promesse ou déclencher une expédition.

Pourtant, plus on l'analyse, plus elle révèle un problème beaucoup plus profond.

L'allocation n'est pas seulement une fonction applicative.

C'est un point de rencontre entre la demande, les engagements, les ressources, les règles, les priorités et l'exécution.

## Ce que l'étude Synvance a mis en visibilité

L'étude Synvance a objectivé les disparités entre BRD et GBM dans une logique de convergence ERP Achat / Vente.

Elle a montré que les outils, les règles et les modes opératoires diffèrent, mais que les problèmes sous-jacents reviennent régulièrement :

- visibilité des stocks ;
- précommandes et engagements ;
- commandes fermes ;
- priorisation des clients, canaux ou marchés ;
- saisonnalité, permanents et carry-over ;
- allocation de stocks futurs ;
- modification ou réallocation ;
- simulation d'impacts ;
- suivi des commandes et des jalons ;
- préparation, expédition et livraison.

Ces sujets sont souvent traités comme des critères de couverture ERP.

Mais ils décrivent en réalité une capacité transverse de décision.

## Pourquoi l'allocation est un sujet saillant

Allouer consiste rarement à affecter simplement une quantité disponible à une demande.

Une décision d'allocation peut dépendre de nombreux éléments :

- le type de demande : précommande, commande ferme, réassort, transfert, retour ;
- le cadre d'engagement : client, contrat, canal, SLA, saison, priorité commerciale ;
- la ressource disponible ou attendue : stock physique, stock futur, PO, ASN, capacité fournisseur ;
- les règles de priorité : client stratégique, canal prioritaire, taille centrale, marché, pays, marge, retard ;
- les contraintes opérationnelles : colisage, entrepôt, transport, date de mise à disposition, capacité de préparation ;
- les événements : réception, retard, changement de quantité, annulation, modification de date ;
- les arbitrages : maintenir une promesse, répartir une pénurie, privilégier un canal, réallouer un stock.

```text
Demande
    +
Engagement
    +
Stock / ressource
    +
Règles de priorité
    +
Événements
        ↓
Décision d'allocation
        ↓
Promesse, réservation, réallocation ou exécution
```

Cette complexité explique pourquoi l'allocation revient sans cesse dans les discussions.

Elle concentre les tensions entre commerce, supply, finance, logistique et systèmes.

## Lecture ERP

Dans une lecture ERP classique, l'allocation est souvent étudiée comme une fonctionnalité de solution :

```text
Besoin métier
    ↓
Fonctionnalité ERP
    ↓
Scoring éditeur
```

La question devient alors :

> Quelle solution couvre le mieux les règles d'allocation attendues ?

Cette question est légitime.

Mais elle ne suffit pas à comprendre la responsabilité métier sous-jacente.

Elle peut conduire à enfermer l'allocation dans le paramétrage d'un outil, alors qu'elle traverse plusieurs domaines et plusieurs temporalités.

## Lecture FLOW

FLOW propose une autre lecture.

L'allocation est une décision explicite qui fait progresser une demande.

Elle relie :

- Demand, qui porte l'intention et les engagements ;
- Supply, qui porte la disponibilité et la mobilisation des ressources ;
- Decision Services, qui portent les règles, critères et arbitrages ;
- Inventory Visibility, qui rend les ressources visibles et qualifiées ;
- Execution, qui transforme la décision en action opérationnelle.

```text
Demand
    ↓
Décision d'allocation
    ↑
Supply / Inventory Visibility
    ↓
Execution
```

L'allocation devient donc un excellent révélateur de la nature de FLOW.

FLOW ne cherche pas seulement à choisir où paramétrer l'allocation.

FLOW cherche à rendre explicite la responsabilité de décider comment une ressource doit être affectée à une demande.

## Allocation et Case

Dans FLOW, l'allocation devrait être comprise comme une décision prise dans le cycle de vie d'un Case.

Le Case conserve :

- la demande initiale ;
- le contexte de l'engagement ;
- les ressources envisagées ;
- les règles appliquées ;
- les décisions d'allocation successives ;
- les événements ayant déclenché une révision ;
- les promesses ou réservations produites ;
- les actions d'exécution associées.

Cela permet de traiter les transactions longues.

Une allocation peut être calculée, réservée, confirmée, modifiée, libérée, réallouée ou annulée.

Le processus observé n'est alors que la conséquence des décisions successives prises sur la demande.

## Ce que cela change pour la modélisation

L'allocation montre pourquoi FLOW ne peut pas commencer uniquement par les objets classiques :

```text
Customer
Product
Stock
Order
Warehouse
```

Ces objets sont nécessaires, mais ils ne suffisent pas à expliquer la décision.

La bonne question devient :

> Quelle demande cherche-t-on à satisfaire, sous quel engagement, avec quelle ressource, selon quelles règles ?

L'allocation confirme donc le déplacement de FLOW :

```text
Master data
    ↓
Processus
    ↓
Décisions
```

vers :

```text
Demande
    ↓
Décisions
    ↓
Données et ressources nécessaires
```

## Conséquences pour FLOW

Ce constat conduit à plusieurs conséquences :

- l'allocation doit être analysée comme une responsabilité de décision, pas seulement comme une fonctionnalité ERP ou OMS ;
- les règles d'allocation doivent être explicites, gouvernées, simulables et traçables ;
- les événements qui déclenchent une allocation ou une réallocation doivent être identifiés ;
- les données nécessaires à la décision doivent être distinguées des données de support ;
- Inventory Visibility doit qualifier les ressources disponibles, futures ou réservables ;
- le Case doit conserver l'historique des décisions d'allocation ;
- les systèmes d'exécution peuvent rester autonomes, mais la logique de décision doit être compréhensible au niveau transverse.

## Insight

L'allocation est souvent présentée comme une fonctionnalité complexe à couvrir par un ERP ou un OMS.

Dans FLOW, elle révèle surtout une responsabilité transverse : décider comment une ressource doit être affectée à une demande, dans un cadre d'engagement donné, selon des règles explicites et gouvernées.

## À retenir

L'allocation est un point saillant parce qu'elle concentre presque toute la problématique FLOW :

```text
Demande
    +
Engagement
    +
Ressource
    +
Règles
    +
Événements
        ↓
Décision
        ↓
Exécution
```

C'est probablement l'un des meilleurs cas d'usage pour démontrer pourquoi FLOW n'est ni simplement un ERP, ni simplement un OMS, mais une plateforme fédérée de capacités de décision, d'orchestration et de gouvernance.
