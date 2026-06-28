# C-LOG : une décision de fulfillment déjà distribuée

## Pourquoi c'est un hotspot

C-LOG ne doit pas être lu seulement comme un outil logistique ou un composant d'intégration.

Il porte déjà une partie des décisions de fulfillment : orientation, exécution, stock entrepôt, transport, événements et capacités opérationnelles.

Si FLOW porte une partie de la décision liée à la demande, et C-LOG une partie de la décision liée à l'exécution, le risque est de distribuer la décision sans gouvernance claire.

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
- le contrat d'échange entre FLOW et C-LOG ;
- les événements que C-LOG doit publier ;
- les décisions que FLOW garde, délègue ou orchestre ;
- les règles d'arbitrage lorsque plusieurs options d'exécution sont possibles.

## À retenir

C-LOG est un hotspot parce qu'il révèle que la décision de fulfillment existe déjà dans le SI.

FLOW ne peut pas simplement ajouter une nouvelle décision centrale : il doit clarifier comment la décision de demande et la décision d'exécution collaborent sans se contredire.