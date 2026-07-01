# Pattern — Event-Driven Architecture

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Développeur, Delivery</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

L'Event-Driven Architecture organise les échanges autour d'événements métier publiés par les systèmes qui observent ou produisent un fait opérationnel.

![Pattern — Event-Driven Architecture](../../assets/images/pattern-event-driven-architecture.svg)

<div class="flow-conviction">
  <p>Un événement ne demande pas à un autre système de faire quelque chose.</p>
  <p>Il déclare qu'une chose significative s'est produite.</p>
</div>

## Problème adressé

Les flux projet point à point créent une dépendance forte entre applications, équipes et budgets projet.

Le résultat est souvent :

- des batchs spécifiques ;
- une logique de transformation dispersée ;
- une faible gouvernance des données en transit ;
- des difficultés de diagnostic ;
- une faible capacité de rejeu ;
- une multiplication des flux opportunistes.

## Principe

Les systèmes publient des événements métier stables : StockSold, StockReceived, CaseCreated, ShippingConfirmed, PaymentCaptured.

Les consommateurs s'abonnent aux événements dont ils ont besoin pour maintenir leurs projections, déclencher des décisions ou alimenter des vues opérationnelles.

Pour les décisions critiques, certains événements doivent transporter assez d'information pour maintenir une [projection locale de décision](projection-locale-de-decision.md). Le consommateur peut alors décider vite, sans rappeler la source au moment du calcul.

## Usage dans FLOW

Ce pattern est structurant pour :

- le Socle Case Management ;
- le Stock Unifié ;
- les Vues 360 ;
- la gouvernance des données en transit ;
- l'intégration des systèmes réintégrés.

## Risques

- Publier des événements trop techniques, non métier.
- Confondre événement et commande.
- Ne pas gouverner les contrats d'événements.
- Ne pas prévoir rejeu, idempotence, observabilité et gestion du retard.

## Produits associés

- [Socle Case Management](../produits/socle-case-management.md)
- [Stock Unifié](../produits/stock-unifie.md)
- [Gouvernance des données en transit](../produits/gouvernance-donnees-transit.md)
- [Vues 360](../produits/vues-360.md)
