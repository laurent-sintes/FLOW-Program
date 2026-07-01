# AGENTS.md - Instructions Codex pour FLOW

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
      <strong>16 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page rend visible la mémoire de travail utilisée par Codex pour contribuer au référentiel FLOW.

Elle reprend les règles du fichier racine `AGENTS.md` dans une forme consultable depuis le site.

Elle ne remplace pas les pages de fond du référentiel. Elle sert à guider la contribution : comment construire le site, où vérifier les impacts d'un changement, et quels concepts FLOW préserver dans le temps.

## Administrer et construire le site

Le projet est un site MkDocs Material.

Le site généré localement n'est pas un livrable final :

- `site/` est généré par MkDocs en mode multilingue ;
- `site/fr/` contient la version française ;
- `site/en/` contient la version anglaise générée ;
- `.generated/` contient les sources temporaires de build multilingue ;
- `site/` ne doit jamais être committé ;
- `.generated/` ne doit jamais être committé ;
- `.venv/` ne doit jamais être committé ;
- `.agents/` est un dossier local éventuel, non versionné.
- `.gitattributes` stabilise les fins de ligne du dépôt en `LF` pour éviter le bruit Windows / Linux.

Pour diagnostiquer l'environnement local, utiliser :

```powershell
.\scripts\doctor.ps1
```

Cette commande vérifie les chemins du projet, `.venv`, Git, GitHub CLI, MkDocs, le contexte Codex / PowerShell classique et `.gitattributes`. L'option `-Network` ajoute un test HTTPS léger depuis un PowerShell Windows classique.

Pour construire le site local, utiliser :

```powershell
.\scripts\build-docs.ps1
```

Cette commande :

- lance `scripts\build_multilang.py` ;
- génère les configurations MkDocs temporaires pour `/fr/` et `/en/` ;
- lance `mkdocs build --strict` pour chaque langue ;
- masque le bandeau Material for MkDocs sur MkDocs 2.0 via `NO_MKDOCS_2_WARNING` ;
- fonctionne dans un PowerShell Windows classique ;
- fonctionne aussi depuis Codex en utilisant le runtime Python embarqué si la sandbox bloque le Python local.

Pour maintenir la stratégie multilingue, se référer à :

```text
docs/administration/multilingue-traduction.md
```

Le français reste la source de référence dans `docs/`. La version anglaise est générée dans `.generated/i18n/en/` puis publiée dans `site/en/`. Tant que le cache de traduction n'est pas branché, le build anglais ajoute un bandeau indiquant que la page est générée depuis la source française.

Le build génère aussi `site/index.html`, qui aiguille la racine vers `/fr/`, et `site/404.html`, qui redirige les anciens liens profonds sans préfixe de langue vers `/fr/...` sans rediriger les chemins déjà préfixés par `/fr/` ou `/en/`.

Le build ajoute également une version de cache aux assets locaux publiés (`?v=<empreinte>`). Cette empreinte est calculée sur le contenu des styles, scripts, images, SVG et polices afin d'éviter d'imposer un `Ctrl+F5` aux lecteurs quand ces fichiers changent.

Pour lancer la validation complète du référentiel, utiliser :

```powershell
.\scripts\check-site.ps1
```

Cette commande lance le build local, puis exécute les contrôles Python de cohérence du site : navigation MkDocs, alignement entre libellés de menu et titres de page ou libellés courts déclarés, liens internes, ancres, version de cache des assets publiés, index FAQ, SVG valides et exportables Office, SVG générés à jour, absence de SVG hors générateur, contenus générés non versionnés, synchronisation entre `AGENTS.md` et la page publiée, et garde-fous conceptuels FLOW.

Le contrôle des liens externes est optionnel, car il dépend du réseau et peut être plus lent :

```powershell
.\scripts\check-site.ps1 -ExternalLinks
```

Utiliser ce contrôle quand une page ajoute ou modifie des références Internet. Le mode strict existe pour transformer les échecs HTTP confirmés en erreurs avant une publication importante :

```powershell
.\scripts\check-site.ps1 -StrictExternalLinks
```

Depuis Codex, ce contrôle peut être ignoré si le runtime embarqué bloque HTTPS. Dans ce cas, lancer la commande depuis un PowerShell Windows classique.

GitHub Actions construit aussi le site multilingue et exécute `scripts\check_site.py --external-links` avant publication GitHub Pages. Le scope GitHub CLI `workflow` est nécessaire pour modifier ce workflow.

Pour ajouter du contenu documentaire, en particulier à partir d'une réunion ou d'un atelier, se référer à :

```text
docs/administration/guide-contribution-contenu.md
```

Cette page rappelle comment dater la source, séparer les faits des analyses, formuler les insights, signaler les hypothèses et vérifier les impacts sur les autres pages. Utiliser le vocabulaire ubiquitaire du référentiel facilite l'analyse humaine et l'intégration par Codex.

Pour comprendre le modèle mental qui permet de ranger l'information et mesurer les impacts, se référer à :

```text
docs/administration/modele-mental-connaissances.md
```

Cette page décrit les liens entre source datée, fait observé, insight, vision, principe directeur, concept clé, domaine, capacité, produit FLOW, pattern, hotspot, transformation et règles d'administration.

Pour mettre à jour les cartouches de lecture, le fichier de comptage unitaire par page et la page Statistiques du référentiel, utiliser :

```powershell
.\scripts\update-reading-metrics.ps1
```

Cette commande maintient :

- le cartouche `Repère de lecture` en tête de chaque page ;
- les rôles de public cible, qui doivent provenir de `docs/administration/referentiel-roles.md` ;
- `docs/referentiel/page-metrics.json`, qui conserve les comptages unitaires par page ;
- `docs/referentiel/statistiques.md`, qui agrège les volumes, temps de lecture, concepts, hotspots, composants et nuage de mots.

Les métriques sont calculées sur la source canonique française `docs/`, pas sur les sorties publiées `site/fr/` et `site/en/`. `docs/referentiel/page-metrics.json` doit conserver `metrics_scope: canonical_source`, `source_language: fr` et `published_languages: ["fr", "en"]`. Ne jamais additionner les langues publiées : tant que l'anglais est généré depuis la source française, ses cartouches de lecture reprennent les métriques de référence françaises.

Pour régénérer les schémas SVG, utiliser :

```powershell
.\scripts\generate-svg-diagrams.ps1
```

Cette commande maintient tous les SVG de `docs/assets/images/` via `scripts/generate_svg_diagrams.py`. Les PNG d'atelier restent des sources documentaires statiques. Le générateur découpe les textes selon la largeur disponible, calcule la hauteur nécessaire des cartes et aligne la hauteur d'une même rangée. Il n'utilise aucune librairie Python externe : seulement la bibliothèque standard (`argparse`, `dataclasses`, `html`, `pathlib`). Modifier les données du schéma dans `scripts/generate_svg_diagrams.py` plutôt que d'ajuster manuellement les coordonnées d'un SVG généré.

Après toute modification documentaire significative, relancer `.\scripts\update-reading-metrics.ps1` avant `.\scripts\check-site.ps1`.

Avant de committer :

- vérifier `git status -sb` ;
- vérifier le diff ;
- lancer `.\scripts\check-site.ps1` ;
- lancer `.\scripts\doctor.ps1` si le problème ressemble à un souci d'environnement ;
- ne mettre en stage que les fichiers utiles ;
- ne pas inclure de contenu généré.

Après un changement validé :

- créer un commit avec un message clair ;
- pousser sur `main` si l'utilisateur a demandé ou validé la publication ;
- vérifier que `git status -sb` revient à `main...origin/main`.

Si un push qui modifie `.github/workflows/` est refusé, vérifier le scope GitHub CLI `workflow`. La procédure est documentée dans `docs/administration/environnement-codex-windows.md`.

Pour les détails d'environnement Windows, se référer à :

```text
docs/administration/environnement-codex-windows.md
```

## Structure du site et impacts à vérifier

La navigation principale est portée par `mkdocs.yml`. Quand une page est ajoutée, renommée ou déplacée, vérifier aussi :

- l'entrée correspondante dans `mkdocs.yml` ;
- la page d'index de la section ;
- le libellé explicite du menu, qui doit correspondre au titre H1 de la page, sauf si la page déclare volontairement un libellé court `nav_label` ;
- les liens depuis le glossaire ;
- les liens depuis les pages de vision, principes, architecture ou insights ;
- les ancres Markdown si un titre a changé.

## Sections du référentiel

### Accueil

Fichier clé :

- `docs/index.md`

Rôle :

- donner la promesse du référentiel ;
- orienter vers les grandes sections ;
- rester synthétique.

Impact à vérifier :

- toute nouvelle section majeure doit apparaître dans l'accueil si elle change le parcours de lecture.

### FAQ

Fichiers clés :

- `docs/faq/index.md`
- `docs/faq/questions-pour-les-nouveaux.md`
- `docs/faq/`

Rôle :

- donner une entrée FAQ autonome ;
- répondre aux questions des nouveaux sans les noyer dans l'architecture ;
- séparer les questions pour les nouveaux des questions pour les experts ;
- orienter vers les analyses expertes sans alourdir la page des nouveaux.

Impact à vérifier :

- `docs/faq/index.md` est la page d'accueil de la FAQ, pas la page des questions pour les nouveaux ;
- une question pour les nouveaux doit rester courte dans `docs/faq/questions-pour-les-nouveaux.md` ;
- une question pour les experts doit avoir une page dédiée dans `docs/faq/`, avec un résumé et un lien depuis `docs/faq/index.md` ;
- toute page autonome dans `docs/faq/` doit rester liée depuis l'index FAQ ;
- toute réponse experte doit être rapprochée des pages internes concernées : vision, principes, hotspots, insights, architecture cible ou glossaire.

Procédure pour ajouter une question experte :

1. Créer une page dédiée dans `docs/faq/` avec un nom de fichier stable et un H1 identique au libellé prévu dans `mkdocs.yml`.
2. Structurer la réponse avec le problème posé, l'analyse, le rapprochement avec les hotspots / insights, le lien avec la proposition de solution, les pratiques complémentaires et les références utiles.
3. Rechercher sur le web si le problème est traité par des standards, bonnes pratiques, éditeurs de référence, retours d'expérience ou études, puis citer les sources utiles. Si aucune référence solide n'est trouvée, le signaler explicitement.
4. Ajouter la page dans `mkdocs.yml`, sous `FAQ > Questions pour les experts`, avec un libellé identique au H1.
5. Ajouter un lien vers cette page depuis `docs/faq/index.md`.
6. Si la question aide aussi les nouveaux, ajouter ou ajuster une réponse courte dans `docs/faq/questions-pour-les-nouveaux.md` qui pointe vers la page experte.
7. Vérifier les impacts sur glossaire, principes, hotspots, architecture cible, référentiel des schémas, cartouches et statistiques.
8. Si des références web ont été ajoutées, lancer `.\scripts\check-site.ps1 -ExternalLinks` depuis un PowerShell Windows classique quand le réseau est disponible.

### Vision

Fichiers clés :

- `docs/vision/index.md`
- `docs/vision/abstract.md`
- `docs/vision/vision.md`
- `docs/vision/positionnement-flow.md`
- `docs/vision/modele-fonctionnement-flow.md`
- `docs/vision/vision-detaillee/`
- `docs/vision/concepts-cles.md`
- `docs/vision/note-choix-strategique.md`

Rôle :

- expliquer pourquoi FLOW existe ;
- poser l'ambition ;
- stabiliser le vocabulaire conceptuel ;
- éviter de réduire FLOW à une application ou à un remplacement d'outil.

Impact à vérifier :

- toute évolution de l'ambition doit être répercutée dans l'abstract, la vision détaillée, les concepts clés et le glossaire ;
- tout changement de titre doit être vérifié dans les liens d'ancre ;
- toute nouvelle notion structurante doit être évaluée pour ajout dans `concepts-cles.md` et `glossaire.md`.

### Principes directeurs

Fichiers clés :

- `docs/principes-directeurs/index.md`
- `docs/principes-directeurs/abstract.md`
- `docs/principes-directeurs/1-converger-c-est-federer.md`
- `docs/principes-directeurs/2-flow-comme-plateforme-d-entreprise.md`
- `docs/principes-directeurs/3-domaines-avant-les-structures.md`
- `docs/principes-directeurs/4-separer-demand-et-supply.md`
- `docs/principes-directeurs/5-le-processus-emerge-des-decisions.md`
- `docs/principes-directeurs/6-demande-objet-metier-central-orchestration.md`
- `docs/principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md`
- `docs/principes-directeurs/8-preserver-richesse-business-sans-complexite-si.md`

Rôle :

- formuler les règles de conception durables ;
- servir de garde-fou dans les arbitrages ;
- traduire la vision en décisions d'architecture.

Impact à vérifier :

- tout changement d'un principe peut impacter la vision, les fiches produits, les patterns d'architecture et les insights ;
- le principe 07 porte aussi la doctrine MDM sur les contrats de données ; vérifier les impacts sur la pratique transverse `docs/architecture-cible/produits/gouvernance-donnees-transit.md` ;
- le principe 08 porte la variabilité business gouvernée ; vérifier les impacts sur la vision, les règles, policies, moteurs de contraintes, patterns d'extension et messages de transformation ;
- le principe 01 doit conserver l'idée de bon niveau de commun plutôt qu'une opposition simpliste entre convergence et uniformisation.

### Architecture cible

Fichiers clés :

- `docs/architecture-cible/index.md`
- `docs/architecture-cible/overview-plateforme-flow.md`
- `docs/architecture-cible/flux-fonctionnels-flow.md`
- `docs/architecture-cible/patterns/`
- `docs/architecture-cible/produits/`
- `docs/architecture-cible/flow-dans-ecosysteme-gbm.md`
- `docs/architecture-cible/flow-dans-ecosysteme-brd.md`
- `docs/assets/images/`
- `docs/administration/referentiel-schemas.md`

Rôle :

- décrire le positionnement cible de FLOW ;
- expliciter les patterns ;
- décrire les produits à instruire ;
- montrer l'articulation avec les écosystèmes GBM et BRD.

Impact à vérifier :

- toute évolution d'un produit FLOW peut impacter l'overview, les schémas, les concepts clés, les hotspots et le glossaire ;
- toute évolution d'un schéma doit rester cohérente avec la page qui l'explique et avec `docs/administration/referentiel-schemas.md` ;
- tout ajout, renommage ou suppression de concept structurant doit conduire à relire les schémas listés comme dépendants dans le référentiel des schémas ;
- la gouvernance des données en transit est une pratique transverse, pas un produit FLOW à instruire ; ne pas la représenter comme bloc produit dans les schémas d'overview ;
- le pattern `Self-contained System (SCS)` a guidé le découpage de FLOW en produits ; un produit critique doit être autonome sur son périmètre de responsabilité : logique, informations utiles, contrats explicites et dépendances asynchrones autant que possible ;
- le pattern `Projection locale de décision` rappelle qu'une décision critique ne doit pas dépendre d'appels synchrones à des APIs externes ; vérifier la source de référence, la fraîcheur, la réconciliation et le contrat de données avant de créer une projection locale ;
- tous les SVG de `docs/assets/images/` sont générés par `scripts/generate_svg_diagrams.py` et doivent être modifiés via le générateur afin de préserver les retours à la ligne, les hauteurs automatiques de blocs et le contrôle de cohérence ;
- tous les SVG doivent rester exportables dans Word / PowerPoint : vectoriels, avec `viewBox`, `preserveAspectRatio="xMidYMid meet"`, sans image bitmap embarquée et sans `foreignObject` ;
- les nouveaux SVG d'architecture ou de produit doivent suivre la charte des derniers schémas produits : fond clair `#f8fbfa`, panneaux blancs bordés vert pâle, cœur vert FLOW `#236159`, accent ocre `#e09238`, police Aptos / Calibri / Segoe UI, sans grand fond noir sauf justification forte ;
- ne pas introduire un composant technique sans clarifier sa responsabilité métier ou de plateforme.

### Hotspots

Fichiers clés :

- `docs/hotspots/index.md`
- pages de hotspot dans `docs/hotspots/`

Rôle :

- documenter les points durs de convergence ;
- éviter de masquer les tensions structurantes ;
- préparer les arbitrages.

Impact à vérifier :

- un hotspot résolu ou reformulé peut nécessiter une mise à jour de la vision détaillée, des principes ou de l'architecture cible ;
- un nouveau hotspot doit être relié à au moins une tension métier, applicative ou de gouvernance.

### Contexte

Fichiers clés :

- `docs/contexte/index.md`
- `docs/contexte/panorama-brd.md`
- `docs/contexte/panorama-gbm.md`
- `docs/contexte/trajectoires-si-convergence.md`

Rôle :

- documenter le point de départ ;
- garder la mémoire des patrimoines applicatifs ;
- expliquer les différences BRD, GBM, StoreLand et systèmes associés.

Impact à vérifier :

- une correction de contexte peut impacter les insights et les hotspots ;
- ne pas transformer le contexte en cible : il décrit d'abord l'existant et les tensions observées.

### Insights

Fichiers clés :

- `docs/insights/index.md`
- `docs/insights/journal-des-insights.md`
- pages dans `docs/insights/`

Rôle :

- conserver la mémoire de raisonnement ;
- documenter les hypothèses, bascules de compréhension et choix de positionnement ;
- nourrir la vision, les principes et l'architecture cible.

Impact à vérifier :

- un insight stabilisé peut devoir être repris dans la vision ou les principes ;
- un insight obsolète doit être reformulé ou daté plutôt que supprimé sans trace.

### Méthodologie Projet

Fichiers clés :

- `docs/methode/index.md`
- `docs/methode/processus-de-cadrage.md`

Rôle :

- expliquer comment le programme passe des observations aux choix de conception et à la trajectoire Build / Buy ;

Impact à vérifier :

- tout changement de méthode doit rester cohérent avec la chaîne vision, principes, domaines, responsabilités, capacités, produits, options de solution, arbitrage Build / Buy et trajectoire de réalisation.

### Administration du référentiel

Fichiers clés :

- `docs/administration/index.md`
- `docs/administration/guide-contribution-contenu.md`
- `docs/administration/modele-mental-connaissances.md`
- `docs/administration/referentiel-roles.md`
- `docs/administration/operations-build-check-site.md`
- `docs/administration/environnement-codex-windows.md`
- `docs/administration/instructions-codex.md`
- `docs/referentiel/statistiques.md`
- `docs/referentiel/page-metrics.json`

Rôle :

- documenter l'environnement local de contribution ;
- expliciter les opérations réalisées par le build, les contrôles locaux et les contrôles de publication ;
- guider l'ajout de contenu issu des réunions, ateliers, analyses et transcripts ;
- expliciter le modèle mental des connaissances qui relie vision, principes, concepts, domaines, capacités, produits, patterns, hotspots et impacts ;
- rendre visible la mémoire de contribution utilisée par Codex ;
- gouverner les rôles autorisés dans les cartouches de lecture ;
- garder la construction, les contrôles, les statistiques de lecture et la publication du site reproductibles.

Impact à vérifier :

- tout changement d'outillage doit être répercuté dans `docs/administration/environnement-codex-windows.md` ;
- tout changement de build, contrôle, génération SVG, métriques ou publication doit être répercuté dans `docs/administration/operations-build-check-site.md` ;
- tout ajout de contenu issu d'une réunion doit conserver la date de source, distinguer faits, insights, analyse co-construite et questions ouvertes ;
- tout changement de règle de contribution doit être répercuté dans `AGENTS.md` et `docs/administration/instructions-codex.md` ;
- tout changement de rôle de public cible doit être répercuté dans `docs/administration/referentiel-roles.md` avant de modifier les cartouches ;
- tout changement documentaire doit maintenir les cartouches de lecture et `docs/referentiel/page-metrics.json` via `scripts/update-reading-metrics.ps1`.

### Transformation

Fichiers clés :

- `docs/transformation/index.md`
- `docs/transformation/pourquoi-deux-change-managers.md`
- `docs/transformation/embarquement-differencie-core-team.md`
- `docs/transformation/changements-a-conduire.md`

Rôle :

- documenter les changements de posture et d'adoption ;
- relier FLOW à la transformation des pratiques, pas seulement à l'architecture.
- organiser l'embarquement différencié de la Core Team selon les profils, niveaux de compréhension, adhésion, implication et contribution attendue.

Impact à vérifier :

- une évolution de la vision ou des principes peut nécessiter une mise à jour des changements à conduire.
- une évolution majeure des concepts, produits ou patterns peut nécessiter une mise à jour du parcours d'embarquement de la Core Team.

### Référentiel

Fichier clé :

- `docs/glossaire.md`
- `docs/referentiel/statistiques.md`
- `docs/referentiel/page-metrics.json`

Rôle :

- stabiliser le langage commun ;
- servir d'index vers les pages de référence ;
- donner une lecture quantitative du référentiel.

Impact à vérifier :

- toute notion nouvelle ou renommée doit être vérifiée dans le glossaire ;
- les ancres vers les titres doivent être revérifiées après un renommage ;
- le glossaire ne doit pas devenir une seconde vision : il définit, il n'argumente pas longuement ;
- les statistiques sont générées, ne pas les recalculer manuellement.

## Concepts FLOW à préserver

FLOW n'est pas un ERP, pas un OMS classique et pas une simple couche d'intégration.

FLOW est une plateforme Demand et une colonne vertébrale opérationnelle permettant de fédérer les demandes, les décisions métier, le stock, les promesses, les événements, les statuts, les exceptions et les contrats de données.

Concepts à maintenir dans le temps :

- convergence sans nécessairement uniformiser ;
- bon niveau de commun ;
- plateforme fédérale et multi-tenant ;
- articulation Engagement / Demand / Fulfillment / Supply ;
- demande comme objet métier central ;
- Case comme support durable de la demande ;
- décision métier explicite, traçable et gouvernée ;
- processus qui émerge des décisions métier ;
- Agreement comme pivot de variation ;
- Fulfillment Network comme réseau d'exécution configurable ;
- stock unifié comme capacité d'entreprise ;
- produits critiques pensés comme unités autonomes de responsabilité, dans l'esprit Self-contained System, et non comme simples blocs applicatifs ou couches techniques ;
- distinction source de référence / projection ;
- éviter la copie devenue maître par accident : une projection ou une vue ne devient source de référence que si la gouvernance et la responsabilité sont explicitement transférées ;
- projections locales de décision pour maîtriser le SLA des décisions critiques ;
- données en transit gouvernées comme des actifs ;
- contrats de données plutôt que flux projet opportunistes ;
- domaines, responsabilités, capacités et produits avant applications ou organigrammes ;
- rôles, relations et policies plutôt que cardinalités figées dans le cœur ;
- variabilité gouvernée plutôt que chaînes de conditions ou cas particuliers codés en dur ;
- hotspots comme points de tension à instruire, pas comme détails à masquer.

Règle de vocabulaire :

- utiliser `information` quand l'enjeu porte sur le sens métier, la décision, la responsabilité, la qualité, la source de référence, la projection ou l'usage ;
- réserver `donnée` aux cas où l'on parle explicitement de donnée brute, modèle de données, jeu de données, contrat de données, master data, data management ou gouvernance des données en transit ;
- ne pas remplacer mécaniquement : `contrat de données` et `gouvernance des données en transit` restent des termes d'architecture reconnus.

Formulations à éviter :

- présenter FLOW comme un simple remplacement d'application ;
- confondre convergence et standardisation totale ;
- réduire Demand à la commande ;
- confondre décision métier et arbitrage de programme ;
- parler de Master Data sans qualifier la nature de l'information ;
- ajouter une solution technique sans expliciter la responsabilité qu'elle porte.

Quand un contenu est ajouté ou modifié, vérifier au minimum :

- la cohérence avec la vision ;
- les principes directeurs impactés ;
- les concepts clés et le glossaire ;
- les pages d'architecture ou de produit concernées ;
- les hotspots associés ;
- les liens et ancres ;
- les cartouches de lecture et statistiques via `.\scripts\update-reading-metrics.ps1` ;
- les rôles de cartouche, qui doivent rester dans le référentiel `docs/administration/referentiel-roles.md` ;
- le build MkDocs.
