# Positionnement de FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsor, Architecte, Change Manager</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Comprendre le périmètre FLOW et ses impacts d'adoption</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page explicite le périmètre de FLOW au niveau de la vision.

Elle ne décrit pas encore l'architecture détaillée. Elle fixe le message de positionnement : FLOW porte le cœur Demand + Fulfillment ; Engagement et Supply sont adhérents à FLOW sans être absorbés par FLOW.

![Positionnement de FLOW entre Engagement, Demand, Fulfillment et Supply](../assets/images/positionnement-flow-4-domaines.svg)

## Message central

FLOW n'est pas une plateforme d'engagement.

FLOW n'est pas non plus un système Supply complet.

FLOW porte le cœur de cohérence qui relie ce qui est demandé à ce qui peut être exécuté :

```text
Engagement
    capte l'intention et porte les parcours

Demand
    qualifie la demande et porte la promesse à tenir

Fulfillment
    arbitre la promesse tenable et la trajectoire d'exécution

Supply
    expose les ressources, capacités et contraintes
```

Le cœur de FLOW est donc <span class="flow-keyword">Demand + Fulfillment</span>.

→ Voir aussi : [Modèle de fonctionnement de FLOW](modele-fonctionnement-flow.md), pour comprendre les notions manipulées et la chronologie de traitement au niveau Vision.

## Pourquoi ne pas appeler cette page “Périmètre” ?

Dans la vision, le mot périmètre peut donner l'impression d'un découpage projet ou d'une architecture déjà figée.

La notion importante ici est le positionnement :

- ce que FLOW doit porter durablement ;
- ce que FLOW ne doit pas absorber ;
- quels domaines doivent être raccordés pour que la promesse soit cohérente de bout en bout.

Le périmètre fonctionnel détaillé appartient plutôt à l'architecture cible.

## Domaines adhérents

Engagement et Supply sont adhérents à FLOW.

Cela signifie qu'ils gardent leurs responsabilités propres, mais qu'ils ne peuvent pas rester isolés.

| Domaine | Responsabilité | Adhérence avec FLOW |
| --- | --- | --- |
| Engagement | Capter l'intention, porter les parcours, gérer les interfaces, négociations et interactions. | Créer des demandes, consulter des promesses, suivre les Cases, recevoir des statuts, publier des événements. |
| Demand | Qualifier la demande, porter son cycle de vie, son contexte, ses priorités et la promesse à tenir. | Cœur FLOW. |
| Fulfillment | Arbitrer la promesse tenable, réserver, allouer, sourcer, prioriser et construire la trajectoire d'exécution. | Cœur FLOW. |
| Supply | Exposer les stocks, capacités, contraintes, services, SLA et événements d'exécution. | Publier la disponibilité, exécuter, confirmer, signaler les exceptions et contraintes. |

## Ce que ce positionnement protège

Ce positionnement évite deux erreurs.

La première serait de faire de FLOW une plateforme d'engagement qui absorberait les parcours, front-offices, CRM, portails, marketplaces ou outils partenaires.

La seconde serait de faire de FLOW un système Supply complet qui absorberait WMS, TMS, POS, usines, fournisseurs, transporteurs ou opérations physiques.

FLOW doit plutôt gouverner la promesse transverse : une demande qualifiée, une décision de Fulfillment explicable, une trajectoire d'exécution cohérente, des statuts et événements partagés.

## Conséquence

La question de conception n'est pas “FLOW remplace-t-il tel système ?”.

La question devient :

> Quelle responsabilité doit être dans le cœur Demand + Fulfillment, et quelle responsabilité doit rester dans Engagement ou Supply tout en étant contractuellement raccordée à FLOW ?

Cette règle permet de discuter le périmètre sans confondre convergence, centralisation et absorption.
