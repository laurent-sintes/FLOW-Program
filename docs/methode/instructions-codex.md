# Instructions Codex pour FLOW

Cette page rend visible la mémoire de travail utilisée par Codex pour contribuer au référentiel FLOW.

Elle reprend les règles du fichier racine `AGENTS.md` dans une forme consultable depuis le site.

Elle ne remplace pas les pages de fond du référentiel. Elle sert à guider la contribution : comment construire le site, où vérifier les impacts d'un changement, et quels concepts FLOW préserver dans le temps.

## Administrer et construire le site

Le projet est un site MkDocs Material.

Le site généré localement n'est pas un livrable final :

- `site/` est généré par MkDocs ;
- `site/` ne doit jamais être committé ;
- `.venv/` ne doit jamais être committé ;
- `.agents/` est un dossier local éventuel, non versionné.

Pour construire le site local, utiliser :

```powershell
.\scripts\build-docs.ps1
```

Cette commande :

- lance `mkdocs build --strict` ;
- masque le bandeau Material for MkDocs sur MkDocs 2.0 via `NO_MKDOCS_2_WARNING` ;
- fonctionne dans un PowerShell Windows classique ;
- fonctionne aussi depuis Codex en utilisant le runtime Python embarqué si la sandbox bloque le Python local.

Pour lancer la validation complète du référentiel, utiliser :

```powershell
.\scripts\check-site.ps1
```

Cette commande lance le build local, puis exécute les contrôles Python de cohérence du site : navigation MkDocs, liens internes, ancres, contenus générés non versionnés, synchronisation entre `AGENTS.md` et la page publiée, et garde-fous conceptuels FLOW.

Avant de committer :

- vérifier `git status -sb` ;
- vérifier le diff ;
- lancer `.\scripts\check-site.ps1` ;
- ne mettre en stage que les fichiers utiles ;
- ne pas inclure de contenu généré.

Après un changement validé :

- créer un commit avec un message clair ;
- pousser sur `main` si l'utilisateur a demandé ou validé la publication ;
- vérifier que `git status -sb` revient à `main...origin/main`.

Pour les détails d'environnement Windows, se référer à :

```text
docs/methode/environnement-codex-windows.md
```

## Structure du site et impacts à vérifier

La navigation principale est portée par `mkdocs.yml`. Quand une page est ajoutée, renommée ou déplacée, vérifier aussi :

- l'entrée correspondante dans `mkdocs.yml` ;
- la page d'index de la section ;
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

### Vision

Fichiers clés :

- `docs/vision/index.md`
- `docs/vision/abstract.md`
- `docs/vision/vision.md`
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
- `docs/principes-directeurs/1-converger-c-est-federer.md`
- `docs/principes-directeurs/2-flow-comme-plateforme-d-entreprise.md`
- `docs/principes-directeurs/3-domaines-avant-les-structures.md`
- `docs/principes-directeurs/4-separer-demand-et-supply.md`
- `docs/principes-directeurs/5-le-processus-emerge-des-decisions.md`
- `docs/principes-directeurs/6-demande-objet-metier-central-orchestration.md`
- `docs/principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md`
- `docs/principes-directeurs/8-gouverner-la-donnee-en-transit.md`

Rôle :

- formuler les règles de conception durables ;
- servir de garde-fou dans les arbitrages ;
- traduire la vision en décisions d'architecture.

Impact à vérifier :

- tout changement d'un principe peut impacter la vision, les fiches produits, les patterns d'architecture et les insights ;
- le principe 01 doit conserver l'idée de bon niveau de commun plutôt qu'une opposition simpliste entre convergence et uniformisation.

### Architecture cible

Fichiers clés :

- `docs/architecture-cible/index.md`
- `docs/architecture-cible/overview-plateforme-flow.md`
- `docs/architecture-cible/patterns/`
- `docs/architecture-cible/produits/`
- `docs/architecture-cible/flow-dans-ecosysteme-gbm.md`
- `docs/architecture-cible/flow-dans-ecosysteme-brd.md`
- `docs/assets/images/`

Rôle :

- décrire le positionnement cible de FLOW ;
- expliciter les patterns ;
- décrire les produits candidats ;
- montrer l'articulation avec les écosystèmes GBM et BRD.

Impact à vérifier :

- toute évolution d'un produit FLOW peut impacter l'overview, les schémas, les concepts clés, les hotspots et le glossaire ;
- toute évolution d'un schéma doit rester cohérente avec la page qui l'explique ;
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
- `docs/methode/environnement-codex-windows.md`
- `docs/methode/instructions-codex.md`

Rôle :

- expliquer comment le programme passe des observations aux choix de conception ;
- documenter l'environnement local de contribution ;
- rendre visible la mémoire de contribution utilisée par Codex.

Impact à vérifier :

- tout changement d'outillage doit être répercuté dans `environnement-codex-windows.md` ;
- tout changement de règle de contribution doit être répercuté dans `AGENTS.md` et `instructions-codex.md` ;
- tout changement de méthode doit rester cohérent avec la chaîne vision, principes, domaines, responsabilités, capacités, produits, solutions candidates.

### Transformation

Fichiers clés :

- `docs/transformation/index.md`
- `docs/transformation/pourquoi-deux-change-managers.md`
- `docs/transformation/changements-a-conduire.md`

Rôle :

- documenter les changements de posture et d'adoption ;
- relier FLOW à la transformation des pratiques, pas seulement à l'architecture.

Impact à vérifier :

- une évolution de la vision ou des principes peut nécessiter une mise à jour des changements à conduire.

### Référentiel

Fichier clé :

- `docs/glossaire.md`

Rôle :

- stabiliser le langage commun ;
- servir d'index vers les pages de référence.

Impact à vérifier :

- toute notion nouvelle ou renommée doit être vérifiée dans le glossaire ;
- les ancres vers les titres doivent être revérifiées après un renommage ;
- le glossaire ne doit pas devenir une seconde vision : il définit, il n'argumente pas longuement.

## Concepts FLOW à préserver

FLOW n'est pas un ERP, pas un OMS classique et pas une simple couche d'intégration.

FLOW est une plateforme Demand et une colonne vertébrale opérationnelle permettant de fédérer les demandes, les décisions métier, le stock, les promesses, les événements, les statuts, les exceptions et les contrats de données.

Concepts à maintenir dans le temps :

- convergence sans nécessairement uniformiser ;
- bon niveau de commun ;
- plateforme fédérale et multi-tenant ;
- séparation Demand / Supply ;
- demande comme objet métier central ;
- Case comme support durable de la demande ;
- décision métier explicite, traçable et gouvernée ;
- processus qui émerge des décisions métier ;
- Agreement comme pivot de variation ;
- Fulfillment Network comme réseau d'exécution configurable ;
- stock unifié comme capacité d'entreprise ;
- distinction source / projection ;
- données en transit gouvernées comme des actifs ;
- contrats de données plutôt que flux projet opportunistes ;
- domaines, responsabilités, capacités et produits avant applications ou organigrammes ;
- rôles, relations et policies plutôt que cardinalités figées dans le cœur ;
- hotspots comme points de tension à instruire, pas comme détails à masquer.

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
- le build MkDocs.
