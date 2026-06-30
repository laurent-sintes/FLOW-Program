# AGENTS.md - Instructions Codex pour FLOW

Ce fichier sert de mémoire de travail pour Codex et les agents qui interviennent sur le référentiel FLOW.

Il ne remplace pas la documentation publiée dans `docs/`. Il décrit les règles de contribution, les impacts à vérifier et les concepts à préserver quand le contenu évolue.

Une version lisible dans le site est publiée dans :

```text
docs/administration/instructions-codex.md
```

Lorsqu'une règle structurante change ici, mettre à jour cette page également.

## 1. Administrer et construire le site

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

Pour lancer la validation complète du référentiel, utiliser :

```powershell
.\scripts\check-site.ps1
```

Cette commande lance le build local, puis exécute les contrôles Python de cohérence du site : navigation MkDocs, alignement entre libellés de menu et titres de page, liens internes, ancres, index FAQ, SVG, contenus générés non versionnés, synchronisation entre `AGENTS.md` et la page publiée, et garde-fous conceptuels FLOW.

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

## 2. Structure du site et impacts à vérifier

La navigation principale est portée par `mkdocs.yml`. Quand une page est ajoutée, renommée ou déplacée, vérifier aussi :

- l'entrée correspondante dans `mkdocs.yml` ;
- la page d'index de la section ;
- le libellé explicite du menu, qui doit correspondre au titre H1 de la page ;
- les liens depuis le glossaire ;
- les liens depuis les pages de vision, principes, architecture ou insights ;
- les ancres Markdown si un titre a changé.

### Accueil

Fichiers clés :

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

Rôle :

- formuler les règles de conception durables ;
- servir de garde-fou dans les arbitrages ;
- traduire la vision en décisions d'architecture.

Impact à vérifier :

- tout changement d'un principe peut impacter la vision, les fiches produits, les patterns d'architecture et les insights ;
- le principe 07 porte aussi la doctrine MDM sur les contrats de données ; vérifier les impacts sur `docs/architecture-cible/produits/gouvernance-donnees-transit.md` ;
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
- décrire les produits candidats ;
- montrer l'articulation avec les écosystèmes GBM et BRD.

Impact à vérifier :

- toute évolution d'un produit FLOW peut impacter l'overview, les schémas, les concepts clés, les hotspots et le glossaire ;
- toute évolution d'un schéma doit rester cohérente avec la page qui l'explique et avec `docs/administration/referentiel-schemas.md` ;
- tout ajout, renommage ou suppression de concept structurant doit conduire à relire les schémas listés comme dépendants dans le référentiel des schémas ;
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

- expliquer comment le programme passe des observations aux choix de conception ;

Impact à vérifier :

- tout changement de méthode doit rester cohérent avec la chaîne vision, principes, domaines, responsabilités, capacités, produits, solutions candidates.

### Administration du référentiel

Fichiers clés :

- `docs/administration/index.md`
- `docs/administration/guide-contribution-contenu.md`
- `docs/administration/modele-mental-connaissances.md`
- `docs/administration/referentiel-roles.md`
- `docs/administration/environnement-codex-windows.md`
- `docs/administration/instructions-codex.md`
- `docs/referentiel/statistiques.md`
- `docs/referentiel/page-metrics.json`

Rôle :

- documenter l'environnement local de contribution ;
- guider l'ajout de contenu issu des réunions, ateliers, analyses et transcripts ;
- expliciter le modèle mental des connaissances qui relie vision, principes, concepts, domaines, capacités, produits, patterns, hotspots et impacts ;
- rendre visible la mémoire de contribution utilisée par Codex ;
- gouverner les rôles autorisés dans les cartouches de lecture ;
- garder la construction, les contrôles, les statistiques de lecture et la publication du site reproductibles.

Impact à vérifier :

- tout changement d'outillage doit être répercuté dans `docs/administration/environnement-codex-windows.md` ;
- tout ajout de contenu issu d'une réunion doit conserver la date de source, distinguer faits, insights, analyse co-construite et questions ouvertes ;
- tout changement de règle de contribution doit être répercuté dans `AGENTS.md` et `docs/administration/instructions-codex.md` ;
- tout changement de rôle de public cible doit être répercuté dans `docs/administration/referentiel-roles.md` avant de modifier les cartouches ;
- tout changement documentaire doit maintenir les cartouches de lecture et `docs/referentiel/page-metrics.json` via `scripts/update-reading-metrics.ps1`.

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

## 3. Concepts FLOW à préserver

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
- distinction source de référence / projection ;
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
- les cartouches de lecture et statistiques via `.\scripts\update-reading-metrics.ps1` ;
- les rôles de cartouche, qui doivent rester dans le référentiel `docs/administration/referentiel-roles.md` ;
- le build MkDocs.
