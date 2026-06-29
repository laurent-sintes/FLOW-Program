# Promesse commerciale et priorisation Wholesale

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
      <strong>4 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page documente le hotspot lié au business model des allocations, de la promesse et de la priorisation entre BRD et GBM.

Le sujet est structurant pour FLOW car il touche directement à la manière dont une demande consomme du stock, reçoit une promesse, peut être priorisée, puis est exécutée.

Il ne s'agit pas seulement d'un sujet B2B / Wholesale.

Il s'agit d'un choix de gouvernance métier : une promesse donnée peut-elle être déplacée pour servir un client plus prioritaire ?

## Pourquoi c'est un hotspot

La pratique Wholesale observée chez Boardriders repose sur une logique de priorisation des meilleurs clients.

Cette logique est différente d'une approche “premier arrivé, premier servi”, plus proche de la culture Beaumanoir.

Dans une logique de priorisation, une nouvelle commande d'un client prioritaire peut consommer un stock insuffisant et décaler dans le temps des commandes déjà enregistrées pour des clients moins prioritaires.

Le sujet n'est donc pas seulement : “qui a droit au stock ?”

Le sujet est aussi : “quelle promesse a déjà été donnée, à qui, et peut-on la déplacer ?”

```text
Premier arrivé, premier servi
    → la promesse donnée est protégée
    → la priorité vient du moment d'engagement

Priorisation Wholesale
    → le client prioritaire peut passer devant
    → certaines promesses peuvent être déplacées
```

Ce hotspot révèle une tension forte entre deux philosophies métier :

- protéger la stabilité de l'engagement déjà pris ;
- optimiser commercialement le stock disponible au bénéfice des clients prioritaires.

## Deux modèles de promesse

### Modèle “premier arrivé, premier servi”

Dans ce modèle, la promesse donnée à une commande est considérée comme stable.

Lorsqu'une commande a reçu un engagement, le système protège cet engagement sauf événement exceptionnel : rupture fournisseur, anomalie stock, incident logistique ou arbitrage explicite.

Ce modèle est lisible pour les opérations et rassurant pour les clients.

Il limite toutefois la capacité à réallouer le stock à un client plus stratégique après coup.

### Modèle de priorisation Wholesale

Dans ce modèle, la valeur commerciale du client peut modifier l'ordre de traitement.

Une commande plus récente, mais portée par un client prioritaire, peut passer devant une commande plus ancienne si le stock disponible ne permet pas de tout servir.

Ce modèle peut être pertinent commercialement.

Mais il crée un risque de rupture de promesse pour les clients moins prioritaires, surtout si ces clients avaient déjà perçu leur commande comme engagée.

## Pourquoi FLOW est concerné

FLOW porte la demande, la promesse, l'allocation, les règles de priorité et la cohérence du fulfillment.

La plateforme ne doit donc pas seulement répondre à la question : y a-t-il du stock ?

Elle doit aussi répondre à des questions plus exigeantes :

- Ce stock est-il libre, réservé ou déjà promis ?
- Cette promesse est-elle ferme ou déplaçable ?
- Quel client, canal, marque ou agreement peut être prioritaire ?
- Qui peut déplacer une promesse déjà donnée ?
- Comment les commandes impactées sont-elles identifiées, expliquées et traitées ?

Ce hotspot montre que la promesse n'est pas seulement un calcul de disponibilité.

C'est une décision gouvernée par des règles commerciales, des agreements, des priorités, des engagements et une politique explicite de rupture ou non-rupture de promesse.

## Risques à maîtriser

Si ce sujet n'est pas traité explicitement, FLOW risque de produire :

- des décisions d'allocation incomprises ;
- des promesses contradictoires entre canaux ou organisations ;
- des décalages de commandes non expliqués ;
- une optimisation commerciale locale au détriment de la confiance globale ;
- une difficulté à expliquer pourquoi un client a été servi avant un autre ;
- une complexité cachée dans des règles locales, des contournements ou des arbitrages manuels.

## Questions structurantes pour FLOW

Le sujet doit être arbitré avant de stabiliser les règles de promesse et d'allocation :

- Une promesse commerciale est-elle ferme dès qu'elle est donnée ?
- Peut-elle être déplacée selon une priorité client, canal, marque ou agreement ?
- Dans quels cas le déplacement est-il autorisé ?
- Qui porte la responsabilité de cette décision ?
- Comment les commandes décalées sont-elles identifiées et expliquées ?
- Quelle information doit être visible dans les Vues 360 ou dans le suivi de Case ?
- Comment éviter qu'une optimisation commerciale locale dégrade la confiance globale dans la promesse ?
- Quelles règles doivent être communes au groupe, et quelles règles peuvent rester propres à un business model ?

## Lien avec le module Négoce StoreLand

Le module Négoce StoreLand est un autre hotspot.

Il concerne le périmètre fonctionnel à reprendre, conserver ou réintégrer autour de FLOW : client, assortiment, commercial agreement, catalogue, prix, commandes d'achat et processus B2B.

Il ne doit pas être confondu avec le présent hotspot.

Le présent hotspot traite la politique de promesse, d'allocation et de priorisation.

Le module Négoce traite plutôt le découpage des responsabilités entre Engagement, FLOW et les systèmes consommateurs de la plateforme.

## À retenir

Le point décisif n'est pas seulement la convergence B2B / Wholesale.

Le point décisif est la promesse commerciale.

Boardriders et Beaumanoir ne portent pas spontanément la même philosophie entre priorisation client et “premier arrivé, premier servi”.

FLOW devra rendre cette politique explicite, gouvernée, traçable et explicable, car elle conditionne directement la confiance dans la promesse client.
