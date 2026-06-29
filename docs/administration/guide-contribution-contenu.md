# Guide de contribution éditoriale

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Mainteneur, Contributeur, Codex</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>4 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page décrit comment ajouter du contenu dans le référentiel FLOW, en particulier lorsqu'il provient d'une réunion, d'un atelier ou d'une analyse menée avec Codex.

L'objectif n'est pas d'archiver des notes brutes. L'objectif est de transformer une matière vivante en contenu utile : faits observés, insights, analyse co-construite, décisions, questions ouvertes et impacts sur les pages existantes.

## Avant d'ajouter du contenu

Avant de modifier le référentiel, relire les repères utiles :

- `AGENTS.md`, pour comprendre comment Codex maintient la cohérence du site ;
- [Instructions Codex](instructions-codex.md), pour la version publiée de ces consignes ;
- [Modèle mental des connaissances](modele-mental-connaissances.md), pour comprendre où ranger une information et quels impacts vérifier ;
- [Référentiel des rôles](referentiel-roles.md), pour les publics cibles autorisés dans les cartouches ;
- [Glossaire](../glossaire.md), pour vérifier le vocabulaire déjà stabilisé.

Il est plus facile pour un humain comme pour Codex de comprendre et d'intégrer une contribution quand elle utilise le vocabulaire ubiquitaire du référentiel : demande, supply, fulfillment, case, agreement, source de référence, projection, hotspot, domaine, capacité, produit FLOW.

Si un mot important manque, il faut le traiter explicitement : soit le rattacher à un concept existant, soit proposer une entrée de glossaire, soit ouvrir une question.

## Ajouter du contenu issu d'une réunion

Quand le contenu provient d'une réunion, commencer par qualifier la source :

- date complète de la réunion ;
- nom de l'atelier ou du contexte ;
- périmètre concerné ;
- personnes ou rôles impliqués, si cela aide à comprendre le point de vue ;
- niveau de fiabilité : fait confirmé, hypothèse, interprétation, question ouverte.

Exemple de source attendue : `Atelier BoardRiders du 29/06/2026`.

Ensuite, séparer la matière en plusieurs blocs.

## Structure recommandée

### Faits observés

Les faits décrivent ce qui a été dit, constaté ou confirmé.

Ils doivent rester aussi neutres que possible : systèmes cités, règles métier, flux, dépendances, limites connues, exceptions, exemples opérationnels.

### Insights

Les insights sont les enseignements tirés des faits.

Un insight doit formuler ce que la réunion change dans la compréhension de FLOW : tension nouvelle, confirmation d'un principe, risque de convergence, responsabilité à clarifier, pattern qui émerge.

### Analyse co-construite

L'analyse co-construite explicite le raisonnement entre le contributeur humain et Codex.

Elle peut contenir des interprétations, mais celles-ci doivent être nommées comme telles. Codex doit distinguer ce qui vient des notes de réunion, ce qui relève d'une inférence, et ce qui reste à confirmer.

### Impacts à vérifier

Chaque ajout de contenu doit se demander quelles pages sont touchées.

À vérifier au minimum :

- vision et principes directeurs, si le contenu change la doctrine ;
- hotspots, si le contenu révèle un arbitrage sensible ;
- architecture cible, si le contenu touche un domaine, une capacité, un produit ou un pattern ;
- glossaire, si un terme devient structurant ;
- statistiques et cartouches, via le script de métriques.

### Questions ouvertes

Les questions ouvertes doivent être conservées quand elles conditionnent une décision future.

Elles évitent de transformer trop tôt une hypothèse en vérité documentaire.

## Utiliser Codex pour intégrer une réunion

Quand les notes sont encore brutes, demander d'abord une analyse sans mise à jour du site.

La bonne séquence est souvent :

- fournir les notes ou le transcript ;
- demander à Codex ce qui semble nouveau, manquant ou contradictoire ;
- décider humainement ce qui doit entrer dans le référentiel ;
- demander ensuite l'intégration dans les pages concernées ;
- relire les formulations politiquement sensibles avant commit.

Codex doit éviter d'inventer des faits. Il peut proposer des liens, des impacts, des reformulations et des patterns, mais il doit signaler ce qui est une inférence.

## Où ranger le contenu

Les contenus ne doivent pas être rangés selon leur origine, mais selon leur rôle dans le référentiel.

- Une observation métier va plutôt dans `contexte/`, `hotspots/` ou `insights/`.
- Un choix de doctrine va plutôt dans `vision/` ou `principes-directeurs/`.
- Une responsabilité cible va plutôt dans `architecture-cible/`.
- Un terme durable va dans `glossaire.md`.
- Une règle de contribution va dans `administration/` et, si elle guide Codex, dans `AGENTS.md`.

## Checklist de contribution

Avant de considérer une contribution comme intégrée :

- la source est datée ;
- les faits sont séparés des analyses ;
- les insights sont formulés ;
- les hypothèses et questions ouvertes sont visibles ;
- les impacts sur les pages existantes ont été vérifiés ;
- le vocabulaire est cohérent avec le glossaire ;
- les cartouches et statistiques ont été régénérés ;
- `.\scripts\check-site.ps1` passe sans erreur.
