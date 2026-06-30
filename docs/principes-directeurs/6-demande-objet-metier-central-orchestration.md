# Principe 6 — La demande comme objet métier central d’orchestration

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Sponsor</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

FLOW organise la plateforme autour des demandes que l’entreprise doit instruire, décider et exécuter.

La demande constitue un objet métier plus durable que les processus, les applications ou les parcours qui contribuent à son traitement. Elle permet de relier des intentions, des engagements, des décisions, des ressources, des actions et des documents au sein d’un même contexte.

## Principe

> FLOW traite la demande comme l’objet métier central d’orchestration transverse.

Le Case représente cette demande dans la durée. Il peut traverser plusieurs domaines, applications et processus sans perdre son intention, son historique ni ses engagements.

## La demande avant le processus

Un processus décrit une succession d’étapes. Une demande réelle peut cependant évoluer, se prolonger ou suivre des chemins différents selon son contexte, les règles applicables et les ressources disponibles.

```text
Demande
        ↓
Décisions successives
        ↓
Actions et exécution
```

FLOW ne cherche pas à imposer un processus unique. Il pilote la demande et laisse les processus émerger de son instruction.

## Le Case

Le Case conserve les éléments nécessaires au pilotage transverse d’une demande :

- l’intention initiale et son contexte ;
- les parties concernées ;
- les engagements pris ;
- les décisions rendues ;
- les règles appliquées ;
- les faits et événements significatifs ;
- les ressources mobilisées ;
- les actions réalisées ;
- les documents opérationnels et financiers associés ;
- l’état courant de la demande.

Les documents peuvent être des factures, bons de livraison, bons de retour, avoirs, contrats ou preuves de remise. Ils permettent au Case de s’intégrer avec Finance sans empiéter sur les responsabilités comptables de ce domaine.

## La décision fait progresser le Case

Une décision est un choix explicite, pris pour faire progresser le traitement d’un Case.

Elle s’appuie sur des faits, des informations de référence et des règles de comportement. Elle produit un résultat traçable, susceptible de créer un engagement, de mobiliser une ressource ou de déclencher une action.

```text
Faits + informations + règles de comportement
        ↓
Décision
        ↓
Évolution du Case
```

Une règle exprime la manière dont l’entreprise doit réagir, décider ou agir dans une situation donnée. Elle peut rendre une décision automatiquement, encadrer une décision humaine, déclencher une action, calculer une priorité ou interdire une action.

## L'allocation comme cas emblématique

L'allocation illustre particulièrement ce principe.

Allouer une ressource à une demande ne consiste pas seulement à réserver du stock. C'est une décision qui relie une intention, un cadre d'engagement, une ressource disponible ou future, des règles de priorité et des événements opérationnels.

```text
Demande
        ↓
Décision d'allocation
        ↓
Ressource affectée ou réservée
        ↓
Promesse ou exécution
```

Le Case doit donc pouvoir conserver les décisions d'allocation successives, les règles appliquées, les événements déclencheurs et les conséquences produites sur la promesse, la réservation ou l'exécution.

## Demand, Fulfillment et Supply

Demand porte l’intention, les engagements et le cycle de vie de la demande.

Fulfillment porte la décision opérationnelle : promettre, allouer, orienter, prioriser, adapter ou ouvrir une exception.

Supply porte la visibilité, la disponibilité et la mobilisation des ressources.

La décision de Fulfillment constitue le point de rencontre entre la demande et les ressources.

```text
Demande
        ↓
Décision de Fulfillment
        ↓
Ressource affectée
        ↓
Exécution
```

## Conséquences

Ce principe conduit FLOW à :

- concevoir des capacités réutilisables au-delà d’un seul canal ou processus ;
- traiter les transactions longues sans les enfermer dans une application ;
- rendre les décisions explicites, traçables et explicables ;
- relier les engagements, les ressources, les actions et les documents ;
- préserver l’autonomie des systèmes d’exécution existants ;
- structurer progressivement le modèle de l’entreprise à partir des situations réelles à traiter.

## Insights associés

- [Modèle conceptuel FLOW](../insights/modele-conceptuel-flow.md)
- [L'allocation révèle la vraie nature de la convergence](../insights/allocation-point-saillant-de-la-convergence.md)
- [FLOW n’est probablement pas un OMS : de l’OMS au Demand Management](../insights/oms-vers-demand-management.md)
- [L’organisation masque parfois les domaines](../insights/organisation-masque-domaines.md)
- [Inventory Visibility est une capacité d’entreprise](../insights/inventory-visibility-capacite-d-entreprise.md)

## À retenir

FLOW ne commence pas par demander quelles informations de référence doivent être centralisées.

FLOW commence par demander :

> Quelle demande l’entreprise doit-elle être capable d’instruire, de décider et d’exécuter ?
