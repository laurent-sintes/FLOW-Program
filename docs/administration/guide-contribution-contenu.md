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
      <strong>7 min</strong>
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

## Procédure réunion et transcript

Cette procédure s'applique lorsqu'un contributeur assiste à une réunion, récupère ensuite un transcript, puis veut intégrer les informations utiles dans le référentiel.

### 1. Préparer la réunion

Avant ou pendant la réunion, noter les informations de contexte qui permettront de comprendre le transcript plus tard :

- date complète ;
- nom de la réunion ou de l'atelier ;
- sujet traité ;
- périmètre métier ou applicatif ;
- systèmes cités ;
- décisions attendues ou questions à instruire ;
- niveau de sensibilité politique ou organisationnelle.

Le but n'est pas de tout prendre en note. Le but est de garder les repères que le transcript ne donnera pas toujours clairement.

### 2. Récupérer le transcript

Après la réunion, récupérer le transcript si les droits le permettent.

Si le transcript n'est pas accessible directement, demander son extraction à l'organisateur ou au propriétaire de la réunion.

Avant de l'utiliser, vérifier :

- si le transcript est complet ou coupé ;
- si les intervenants sont correctement identifiés ;
- si certaines formulations sont ambiguës à cause de la transcription automatique ;
- si le contenu peut être utilisé dans le référentiel ou doit rester comme matière de travail locale ;
- si des passages sensibles doivent être reformulés avant publication.

Le transcript brut n'est pas le livrable documentaire. Il ne doit pas être committé tel quel sauf décision explicite. Il sert de matière d'analyse.

### 3. Demander une première analyse sans mise à jour

La première interaction avec Codex doit viser la compréhension, pas l'écriture immédiate.

Demande recommandée :

```text
Voici le transcript de la réunion du [date / sujet].
Analyse sans mettre à jour les fichiers.
Dis-moi :
- les faits nouveaux ;
- les points déjà connus ;
- les contradictions ou tensions ;
- les insights potentiels ;
- les concepts FLOW concernés ;
- les pages probablement impactées ;
- les questions à clarifier avant intégration.
```

À ce stade, Codex doit distinguer explicitement :

- ce qui vient du transcript ;
- ce qui est une inférence ;
- ce qui semble important mais reste à confirmer ;
- ce qui relève d'une reformulation politique ou pédagogique.

### 4. Arbitrer humainement ce qui entre dans le référentiel

Le contributeur décide ensuite ce qui mérite d'être intégré.

Toutes les informations d'une réunion ne doivent pas devenir du contenu publié.

À conserver en priorité :

- les faits structurants ;
- les décisions ou arbitrages confirmés ;
- les tensions qui deviennent des hotspots ;
- les insights qui changent la compréhension de FLOW ;
- les questions ouvertes qui conditionnent une décision future ;
- les exemples qui éclairent un concept déjà présent.

À éviter :

- les détails anecdotiques ;
- les formulations trop personnelles ;
- les citations sensibles ;
- les hypothèses non signalées ;
- les débats qui ne changent pas le modèle de connaissance.

### 5. Mapper les informations sur le modèle mental

Avant d'écrire, rattacher chaque information à une catégorie du [modèle mental des connaissances](modele-mental-connaissances.md).

Questions utiles :

- Est-ce un fait observé, un insight, une question ouverte ou une décision ?
- Est-ce que cela modifie la vision ou seulement un exemple ?
- Est-ce un principe durable ou un cas particulier ?
- Est-ce un hotspot à instruire ?
- Est-ce un concept de glossaire ?
- Est-ce une responsabilité de domaine, une capacité, un produit FLOW ou un pattern ?
- Est-ce que cela impacte la transformation ou l'adoption ?

Cette étape évite de ranger directement une observation brute comme une solution cible.

### 6. Intégrer dans les pages concernées

L'intégration doit être faite dans les pages existantes lorsque c'est possible.

Créer une nouvelle page seulement si le sujet devient autonome : nouveau hotspot, nouveau pattern, nouvelle fiche produit, nouveau principe ou nouveau guide d'administration.

Lors de l'écriture :

- citer la réunion comme source datée quand c'est utile ;
- reformuler les faits dans le vocabulaire ubiquitaire FLOW ;
- distinguer les faits des analyses ;
- signaler les hypothèses ;
- conserver les questions ouvertes ;
- relier les pages concernées par des liens internes ;
- relire les formulations sensibles avant commit.

### 7. Contrôler la cohérence

Après intégration :

- relancer `.\scripts\update-reading-metrics.ps1` ;
- relancer `.\scripts\check-site.ps1` ;
- lancer `.\scripts\check-site.ps1 -ExternalLinks` si des références Internet ont été ajoutées ou modifiées ;
- lancer `.\scripts\doctor.ps1` si le problème observé ressemble à un souci d'environnement local ;
- vérifier le [multilingue et traduction](multilingue-traduction.md) si le changement touche le build, la navigation, la structure de page ou le glossaire ;
- vérifier le diff ;
- vérifier que les cartouches utilisent les rôles du référentiel ;
- vérifier que les liens, concepts, hotspots et pages d'impact sont cohérents.

Si le transcript a révélé une règle de contribution nouvelle, mettre à jour cette page et, si nécessaire, `AGENTS.md`.

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
- les libellés explicites du menu correspondent aux titres H1 des pages, sauf libellé court `nav_label` déclaré dans la page ;
- les pages autonomes FAQ sont reliées depuis l'index FAQ ;
- les questions expertes FAQ suivent la procédure décrite dans `AGENTS.md` et les [Instructions Codex](instructions-codex.md) ;
- les questions expertes FAQ citent, quand elles existent, les standards, bonnes pratiques, retours d'expérience ou études externes qui éclairent le problème ;
- les références Internet nouvelles ou modifiées ont été contrôlées avec `.\scripts\check-site.ps1 -ExternalLinks` quand le réseau est disponible ;
- les schémas SVG ajoutés ou modifiés sont valides ;
- les schémas impactés par un concept ajouté, renommé ou supprimé ont été vérifiés dans le [Référentiel des schémas](referentiel-schemas.md) ;
- les alertes d'environnement ont été diagnostiquées avec `.\scripts\doctor.ps1` quand elles ne relèvent pas du contenu ;
- le build multilingue `/fr/` et `/en/` reste cohérent si le changement touche la structure du site ;
- `.\scripts\check-site.ps1` passe sans erreur.
