# Cohérence des données : fraîcheur, DataHub et CEP

## Constat

Dans un SI composé de nombreuses applications spécialisées, les données circulent à des vitesses différentes.

Certaines intégrations fonctionnent en temps quasi réel, d'autres en micro-batch, d'autres encore en batchs planifiés.

Les délais peuvent varier de quelques secondes à plusieurs minutes, plusieurs heures ou J+1.

## Le vrai problème n'est pas seulement la fraîcheur

La fraîcheur de la donnée est importante, mais elle n'est pas toujours le problème principal.

Le problème fondamental est la cohérence entre systèmes.

Par exemple, si un événement de vente arrive :

- en 10 minutes dans NewStore ;
- en 1 heure dans SAP ;

alors pendant 50 minutes, les deux systèmes peuvent présenter un stock différent.

Les deux systèmes peuvent être techniquement corrects par rapport à ce qu'ils ont reçu, mais l'ensemble du SI est incohérent.

## Une donnée fraîche mais incohérente reste dangereuse

Le temps réel est utile, mais il ne suffit pas.

Une donnée très fraîche mais incohérente avec le reste du SI peut produire :

- une mauvaise promesse client ;
- une mauvaise allocation ;
- une mauvaise décision de sourcing ;
- une perte de confiance métier ;
- des diagnostics permanents entre équipes IT et métier.

## Le véritable objectif

L'objectif n'est donc pas seulement d'aller vers le temps réel.

L'objectif est de construire une cohérence opérationnelle maîtrisée.

Le temps réel est un moyen.

La cohérence est l'exigence.

## Pourquoi DataHub est indispensable

Le pattern DataHub permet de construire une vue cohérente, gouvernée et explicable des données opérationnelles.

Il permet notamment de :

- centraliser ou fédérer des projections opérationnelles ;
- identifier les sources de vérité ;
- tracer l'origine des données ;
- exposer des vues cohérentes aux consommateurs ;
- gérer la fraîcheur et la qualité des données ;
- éviter que chaque application reconstruise sa propre vision du monde.

Dans FLOW, le DataHub est particulièrement important pour Inventory Visibility.

## Pourquoi le Complex Event Processing est indispensable

Le Complex Event Processing permet de traiter, corréler et contrôler les événements.

Il permet notamment de :

- détecter les événements manquants ;
- détecter les événements arrivés dans le mauvais ordre ;
- corréler plusieurs événements appartenant à un même cycle de vie ;
- reconstruire un état cohérent ;
- identifier les écarts de séquence ;
- déclencher des alertes métier ou techniques.

Par exemple, si un événement d'expédition arrive avant l'événement d'allocation attendu, le CEP peut détecter une incohérence de cycle de vie.

## Impact sur FLOW

FLOW ne doit pas être pensé uniquement comme une plateforme temps réel.

FLOW doit être pensé comme une plateforme de cohérence opérationnelle.

Cela impacte directement :

- Inventory Visibility ;
- Decision Services ;
- Event Backbone ;
- DataHub ;
- Observability ;
- Case Management ;
- pilotage des intégrations.

## Formulation synthétique

Le temps réel est une optimisation.

La cohérence est une exigence.

Une donnée parfaitement fraîche mais incohérente est souvent moins utile qu'une donnée légèrement retardée mais cohérente, traçable et explicable.

## À retenir

La qualité de donnée ne doit pas être réduite à la fraîcheur.

Pour FLOW, la maîtrise de la donnée repose sur un triptyque :

- fraîcheur ;
- cohérence ;
- observabilité.

Les patterns DataHub et Complex Event Processing sont donc indispensables pour maîtriser la cohérence opérationnelle du SI.