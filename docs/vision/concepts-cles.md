# Concepts clés du programme FLOW

Cette page rassemble les concepts qui structurent la vision FLOW.

Elle ne remplace pas le [glossaire](../glossaire.md).

Le glossaire définit les termes. Cette page explique les idées qui changent la manière de lire le programme.

## Les phrases qui portent FLOW

<div class="flow-conviction">
  <p>FLOW ne cherche pas à mieux gérer les commandes.</p>
  <p>FLOW cherche à mieux satisfaire les demandes.</p>
</div>

<div class="flow-conviction">
  <p>La convergence n'est pas l'uniformisation.</p>
  <p>Elle consiste à choisir le bon niveau de commun, au bon endroit, pour la bonne responsabilité.</p>
</div>

<div class="flow-conviction">
  <p>Les consommateurs peuvent rester différenciés.</p>
  <p>La plateforme doit être décloisonnée.</p>
</div>

<div class="flow-conviction">
  <p>FLOW ne remplace pas tous les organes du SI.</p>
  <p>FLOW reconstruit la colonne vertébrale qui leur permet de fonctionner ensemble.</p>
</div>

<div class="flow-conviction">
  <p>FLOW ne doit pas seulement remplacer des applications.</p>
  <p>Il doit remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.</p>
</div>

<div class="flow-conviction">
  <p>FLOW configure des capacités d'action.</p>
  <p>Il ne reconstruit pas un grand miroir administratif de l'entreprise.</p>
</div>

## Carte des concepts

| Concept | Message clé |
| --- | --- |
| <span class="flow-keyword">Convergence pilotée par niveaux</span> | On ne choisit pas entre tout centraliser et tout laisser local : on centralise, unifie, standardise, fédère ou différencie selon la responsabilité. |
| <span class="flow-keyword">Demande / Demand</span> | Le point de départ n'est plus la commande ou le document, mais l'intention à comprendre, décider, promettre, satisfaire et expliquer. |
| <span class="flow-keyword">Case</span> | Le Case porte une demande dans la durée : intention, contexte, décisions, événements, ressources, actions et documents. |
| <span class="flow-keyword">Plateforme Demand</span> | FLOW devient le lieu de cohérence des demandes, décisions, stock, promesses, événements et exceptions. |
| <span class="flow-keyword">Colonne vertébrale opérationnelle</span> | FLOW porte les responsabilités qui doivent rester cohérentes — demandes, décisions, statuts, événements, stock, promesses et orchestration — sans réécrire tout le SI. |
| <span class="flow-keyword">Capacités d'intégration</span> | Un service réintégré autour de FLOW doit pouvoir exposer des APIs, publier des événements, partager des statuts, corréler ses objets et participer à la réconciliation. |
| <span class="flow-keyword">Contrat de données</span> | Une donnée en transit doit être publiée, consommée, supervisée et gouvernée comme un actif durable, pas comme un flux projet opportuniste. |
| <span class="flow-keyword">Stock Unifié</span> | Le stock devient une capacité d'entreprise, pas une donnée locale extraite d'un système. |
| <span class="flow-keyword">Fulfillment Network</span> / <span class="flow-keyword">Réseau d'exécution</span> | Le réseau d'exécution décrit les nœuds, services, capacités, contraintes et conditions d'usage mobilisables pour satisfaire une demande. |
| <span class="flow-keyword">Agreement</span> | L'Agreement porte les conditions et règles de traitement qui permettent de gérer la variation sans multiplier les processus. |
| <span class="flow-keyword">Décision</span> / <span class="flow-keyword">règles</span> / <span class="flow-keyword">policies</span> | Les décisions doivent être explicites, traçables, gouvernées et capables de faire évoluer le Case. |
| <span class="flow-keyword">Vues 360</span> | Les vues 360 donnent une lecture transverse d'une activité, d'un client, d'un fournisseur, d'une commande ou d'un Case. |
| <span class="flow-keyword">Source / projection</span> | Une information peut être source dans un domaine et projection dans un autre ; la question n'est plus “est-ce une Master Data ?”. |
| <span class="flow-keyword">Hotspot</span> | Un hotspot est un point de tension à instruire avant de figer une décision ou une architecture cible. |
| <span class="flow-keyword">Domaine / responsabilité / capacité / produit</span> | FLOW découpe les problèmes durables avant de parler d'applications, d'organisations ou de fonctionnalités. |

## Convergence pilotée par niveaux

La <span class="flow-keyword">convergence</span> ne signifie pas que tout doit être identique partout.

FLOW propose une lecture plus fine :

```text
Centraliser
    lorsque la cohérence est critique

Unifier
    lorsque le modèle doit être partagé

Standardiser
    lorsque la variation n'apporte pas de valeur

Fédérer
    lorsque plusieurs modèles doivent coexister

Différencier
    lorsque le business l'exige
```

Ce concept est important parce qu'il permet de sortir d'un débat trop pauvre : centraliser ou laisser local.

FLOW cherche le bon niveau de commun pour chaque responsabilité.

## Demande / Demand

La <span class="flow-keyword">demande</span> est le concept central de FLOW.

Elle représente une intention à traiter : commande, retour, litige, SAV, exception, engagement, demande fournisseur ou autre situation à instruire.

Ce que cela change :

- on ne part plus d'abord de la facture, de la commande ou du module applicatif ;
- on part de ce que l'entreprise doit comprendre, décider, promettre, satisfaire et expliquer ;
- les canaux et organisations deviennent des contextes de traitement, pas le centre du modèle.

## Case

Le <span class="flow-keyword">Case</span> est la forme durable de la demande.

Il conserve :

- l'intention initiale ;
- le contexte ;
- les parties concernées ;
- les décisions ;
- les règles appliquées ;
- les événements ;
- les ressources mobilisées ;
- les actions réalisées ;
- les documents associés ;
- l'état courant.

Le Case permet de traiter des transactions longues qui traversent plusieurs processus, applications, domaines ou partenaires.

## Plateforme Demand

FLOW est une <span class="flow-keyword">plateforme Demand</span>.

Cela signifie qu'elle porte le cœur commun nécessaire pour traiter les demandes, gouverner les décisions et mobiliser les ressources d'exécution.

Une plateforme n'est pas seulement une application centrale.

Elle gouverne des ressources communes, tout en ouvrant des processus contrôlés permettant à d'autres domaines de configurer, développer, étendre ou consommer ses capacités.

## Colonne vertébrale opérationnelle

FLOW n'est pas tout le SI.

Il est la <span class="flow-keyword">colonne vertébrale opérationnelle</span> qui porte les responsabilités qui doivent rester cohérentes à l'échelle du groupe : demandes, décisions, statuts, événements, stock, promesses, allocations et orchestration transverse.

Les services spécialisés peuvent rester autonomes lorsqu'ils portent une valeur métier propre.

Mais ils doivent se brancher sur cette colonne vertébrale commune plutôt que reconstruire chacun leur propre logique de demande, statut, stock ou décision.

## Capacités d'intégration des systèmes réintégrés

Réintégrer un service existant ne signifie pas seulement le conserver.

Cela suppose qu'il puisse interagir proprement avec FLOW.

Les <span class="flow-keyword">capacités d'intégration</span> minimales à étudier sont notamment : APIs contractuelles, événements métier, statuts, documents, identifiants de corrélation, supervision, reprise et réconciliation.

Sans ces capacités, on ne réintègre pas vraiment l'outil : on conserve un silo.

## Contrat de données

Un <span class="flow-keyword">contrat de données</span> décrit la manière dont une information circule durablement entre une source, des consommateurs et une responsabilité métier.

Il précise notamment :

- l'information publiée ;
- la source responsable ;
- les consommateurs connus ;
- le mode d'échange ;
- la granularité ;
- la fraîcheur attendue ;
- la qualité attendue ;
- les règles de supervision ;
- les mécanismes de reprise et de réconciliation.

Ce concept permet de sortir d'une logique de flux projet point-à-point.

Il prolonge l'intuition du demi-flux : distinguer la publication d'une information de sa consommation.

## Stock Unifié

Le <span class="flow-keyword">Stock Unifié</span> n'est pas seulement une consolidation de données.

C'est une capacité d'entreprise qui doit permettre de répondre à des questions opérationnelles :

- quel stock existe ?
- quel stock est disponible ?
- quel stock peut être promis ?
- quel stock peut être réservé ou alloué ?
- selon quel contexte business cette disponibilité est-elle vraie ?

Le stock devient une ressource de décision.

## Fulfillment Network / Réseau d'exécution

Le <span class="flow-keyword">réseau d'exécution</span> ne décrit pas seulement des lieux.

Il décrit ce que le réseau sait faire :

```text
Nœud logistique
    ↓
Capacités disponibles
    ↓
Contraintes
    ↓
Services exposés
    ↓
Conditions d'usage
```

Ce concept permet à FLOW de raisonner sur la capacité réelle d'exécution, pas seulement sur une liste d'entrepôts, de magasins ou de partenaires.

## Agreement

L'<span class="flow-keyword">Agreement</span> devient un concept central parce qu'il porte les conditions de traitement.

Il permet de rendre les commandes plus génériques : ce n'est plus la multiplication des types de commandes qui porte toutes les variations métier.

Le contexte, les Agreements et les règles pilotent dynamiquement les variations de processus.

## Décision / règles / policies

Une <span class="flow-keyword">décision</span> est un choix explicite qui fait progresser une demande.

Elle s'appuie sur des faits, des données et des règles de comportement.

Elle doit pouvoir être comprise, tracée, auditée, simulée et modifiée.

Dans FLOW, le processus émerge des décisions successives prises sur le Case.

## Vues 360

Les <span class="flow-keyword">Vues 360</span> agrègent des informations autour d'un objet, d'un acteur ou d'une activité.

Elles permettent de lire transversalement ce qui s'est passé : événements, statuts, documents, décisions, exceptions et faits utiles.

Elles ne remplacent pas les domaines sources.

Elles rendent l'activité plus lisible.

## Source / projection

FLOW ne reprend pas la catégorie `Master Data` comme un fourre-tout.

Une information doit être qualifiée par nature et par statut dans un domaine : <span class="flow-keyword">source</span> ou <span class="flow-keyword">projection</span>.

La bonne question devient :

> Pour cet usage, cette décision et ce consommateur, quelle source fait foi ?

Cette lecture est essentielle dans un SI distribué.

## Hotspot

Un <span class="flow-keyword">hotspot</span> est un point de tension à instruire.

Il n'est pas encore une décision stabilisée.

Il concentre souvent plusieurs dimensions : business model, application existante, responsabilité cible, règle, donnée, finance, exécution ou trajectoire de transformation.

Les hotspots évitent de masquer trop tôt les zones difficiles sous une architecture trop propre.

## Domaine / responsabilité / capacité / produit

FLOW ne part pas d'abord des applications ou des organisations.

Il part des problèmes durables de l'entreprise.

```text
Domaine
    ↓
Responsabilité
    ↓
Capacité
    ↓
Produit
    ↓
Fonctionnalité
```

Cette taxonomie permet de ne pas confondre un outil existant, une équipe, un processus et la responsabilité durable que l'entreprise doit continuer à assumer.

## À retenir

Les concepts FLOW ne sont pas des mots nouveaux pour faire moderne.

Ils servent à déplacer le raisonnement : de l'application vers la responsabilité, du document vers la demande, de la donnée miroir vers la capacité d'action, du flux projet vers le contrat de données, et de l'uniformisation vers la convergence pilotée.
