# C-LOG : une décision de fulfillment déjà distribuée

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

C-LOG ne doit pas être lu seulement comme un outil logistique ou un composant d'intégration.

Il porte déjà une partie des décisions de fulfillment : orientation, exécution, stock entrepôt, transport, événements et capacités opérationnelles.

L'atelier du 30 juin 2026 sur l'OMS C-LOG confirme que Crossroad met en concurrence des plans d'orchestration, score les options selon coût, délai et complétude, gère crossdock, split, sous-commandes et file manuelle.

Si FLOW porte une partie de la décision liée à la demande, et C-LOG une partie de la décision liée à l'exécution, le risque est de distribuer la décision sans gouvernance claire.

L'arbitrage ne porte donc pas seulement sur le maintien ou le remplacement d'une application.

Il porte sur le positionnement de l'OMS dans l'entreprise : la promesse client omnicanale doit-elle être portée par C-LOG, par FLOW, ou par une orchestration distribuée gouvernée explicitement ?

## Risques principaux

Cette distribution peut produire :

- des choix incompatibles entre demande et exécution ;
- des erreurs d'aiguillage ;
- des promesses impossibles à tenir ;
- une optimisation locale au détriment de l'optimisation globale ;
- une difficulté à expliquer pourquoi une décision a été prise.

## Ce que FLOW doit clarifier

FLOW doit définir précisément :

- la frontière entre décision de demande et décision d'exécution ;
- le propriétaire cible de la promesse client omnicanale ;
- le contrat d'échange entre FLOW et C-LOG ;
- les événements que C-LOG doit publier ;
- les décisions que FLOW garde, délègue ou orchestre ;
- les règles d'arbitrage lorsque plusieurs options d'exécution sont possibles ;
- le statut cible de l'OMS C-LOG : service conservé, service encapsulé, composant à remplacer ou moteur d'exécution spécialisé.

Trois hypothèses doivent être comparées :

| Hypothèse | Lecture |
| --- | --- |
| OMS C-LOG étendu | C-LOG prend en charge magasins et omnicanalité ; la promesse client est largement portée par la filiale logistique. |
| OMS remonté au niveau FLOW | FLOW porte la décision de source, transport et promesse ; C-LOG exécute ou expose des capacités Supply spécialisées. |
| OMS complémentaire hors C-LOG | Un autre OMS couvre les usages non pris par C-LOG ; le risque d'intégration et de double décision devient élevé. |

## Source détaillée

Voir la page de contexte : [OMS C-LOG - atelier du 30 juin 2026](../contexte/panorama-oms-c-log.md).

## À retenir

C-LOG est un hotspot parce qu'il révèle que la décision de fulfillment existe déjà dans le SI.

FLOW ne peut pas simplement ajouter une nouvelle décision centrale : il doit clarifier comment la décision de demande et la décision d'exécution collaborent sans se contredire.
