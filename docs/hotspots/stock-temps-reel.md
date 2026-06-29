# Stock temps réel : obtenir les mouvements à la source

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsor, Architecte, Métier</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Pourquoi c'est un hotspot

Le Stock Unifié n'a de valeur opérationnelle que si les mouvements de stock remontent avec une fraîcheur suffisante.

Or cette fraîcheur ne dépend pas seulement de FLOW.

Elle dépend aussi de la capacité des systèmes qui observent ou provoquent les mouvements de stock à les transmettre rapidement.

Les systèmes concernés sont notamment :

- le Point of Sale, porté par une application éditeur ;
- les solutions logistiques opérées par des entreprises externes ou des filiales ;
- les WMS, transporteurs, partenaires et systèmes d'exécution qui manipulent physiquement le stock.

## Risque principal

Sans événements suffisamment frais, FLOW peut consolider une vision de stock, mais ne peut pas garantir une décision de promesse, d'allocation ou de fulfillment fiable à l'échelle omnicanale.

Le risque n'est donc pas seulement technique.

Il touche directement la capacité à promettre, réserver, allouer, réorienter ou expliquer une décision.

## Ce que FLOW doit clarifier

Pour tendre vers un stock temps réel, les systèmes sources devront accepter de publier les mouvements de stock en événementiel, en asynchrone court.

FLOW doit donc clarifier :

- les capacités événementielles réellement disponibles côté POS et solutions logistiques ;
- les contrats d'événements nécessaires ;
- les exigences de fraîcheur par usage métier ;
- les responsabilités en cas de retard, perte ou incohérence d'événement ;
- les mécanismes de rattrapage et de réconciliation.

## Lien avec les capacités d'intégration

Ce hotspot traite le cas particulier du stock.

Il ne doit pas porter seul tout le sujet de l'intégration des systèmes existants.

Les exigences de publication d'événements, d'APIs, de statuts, de corrélation, de réconciliation ou de supervision sont traitées plus largement dans le hotspot [Capacités d'intégration des systèmes réintégrés](capacites-integration-systemes-reintegres.md).

Le stock temps réel en est l'un des cas les plus critiques, car la fraîcheur des mouvements conditionne directement la promesse, l'allocation et l'optimisation du fulfillment.

## À retenir

Le stock temps réel n'est pas seulement une capacité FLOW.

C'est une exigence d'écosystème : les systèmes qui créent ou observent les mouvements doivent accepter de les publier avec la bonne fraîcheur, selon des contrats gouvernés.
