# Opérations de build et de contrôle

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
      <strong>6 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page décrit les opérations réalisées par les scripts de build et de contrôle du référentiel FLOW.

Elle sert à comprendre ce qui est réellement automatisé, ce qui est seulement vérifié, et ce qui doit être lancé avant un contrôle complet.

## Commandes principales

| Commande | Rôle | Quand l'utiliser |
| --- | --- | --- |
| `.\scripts\build-docs.ps1` | Construire le site local multilingue. | Quand on veut vérifier le rendu MkDocs local. |
| `.\scripts\check-site.ps1` | Construire le site puis contrôler la cohérence du référentiel. | Avant commit, push ou publication importante. |
| `.\scripts\check-site.ps1 -ExternalLinks` | Ajouter un contrôle réseau des liens externes. | Quand des références web ont été ajoutées ou modifiées. |
| `.\scripts\check-site.ps1 -StrictExternalLinks` | Transformer les échecs HTTP confirmés en erreurs. | Avant une publication importante, depuis un PowerShell Windows classique. |

## Ce que fait `build-docs`

`build-docs.ps1` est le wrapper PowerShell du build MkDocs.

Il réalise les opérations suivantes :

1. Vérifier que `.venv`, les packages Python et `scripts\build_multilang.py` existent.
2. Détecter si la commande s'exécute depuis Codex ou depuis un PowerShell Windows classique.
3. Masquer le warning MkDocs 2.0 via `NO_MKDOCS_2_WARNING`.
4. Utiliser le Python embarqué Codex avec les packages du `.venv` si le Python local est bloqué par la sandbox.
5. Sinon utiliser le Python du `.venv`.
6. Lancer `scripts\build_multilang.py`.
7. Restaurer les variables d'environnement modifiées.

`build_multilang.py` réalise ensuite le build applicatif :

1. Supprimer `site/` et `.generated/i18n/` pour repartir d'une sortie propre.
2. Charger `mkdocs.yml`.
3. Préparer la configuration temporaire française.
4. Copier la source française `docs/` vers `.generated/i18n/en/docs/` pour la version anglaise.
5. Ajouter le bandeau indiquant que la version anglaise est générée depuis la source française.
6. Générer les configurations MkDocs temporaires par langue.
7. Lancer `mkdocs build --strict` pour `/fr/`.
8. Lancer `mkdocs build --strict` pour `/en/`.
9. Générer `site/index.html`, qui aiguille la racine vers `/fr/`.
10. Générer `site/404.html`, qui redirige les anciens liens sans préfixe de langue vers `/fr/...`.
11. Ajouter une version de cache aux assets locaux publiés, par exemple `image.svg?v=<empreinte>`.

GitHub Pages ne permet pas de piloter finement les en-têtes HTTP de cache du site.

Le build compense cette limite en ajoutant une empreinte courte, calculée sur le contenu du fichier, aux URLs de styles, scripts, images, SVG et polices. Quand un asset change, son URL change aussi : le navigateur récupère donc la nouvelle version sans demander aux lecteurs de faire `Ctrl+F5`.

Le build produit du contenu local dans `site/` et `.generated/`.

Ces dossiers sont des sorties techniques. Ils ne doivent pas être committés.

## Ce que fait `check-site`

`check-site.ps1` est le wrapper PowerShell de validation du référentiel.

Il réalise les opérations suivantes :

1. Lire les options `-ExternalLinks`, `-StrictExternalLinks` et `-ExternalTimeoutSeconds`.
2. Détecter si la commande s'exécute depuis Codex.
3. Ignorer le contrôle des liens externes depuis Codex, car le runtime embarqué peut bloquer HTTPS.
4. Vérifier que `.venv`, les packages Python et `scripts\check_site.py` existent.
5. Lancer `.\scripts\build-docs.ps1`.
6. Utiliser le Python embarqué Codex avec les packages du `.venv` si nécessaire.
7. Sinon utiliser le Python du `.venv`.
8. Lancer `scripts\check_site.py` avec les options demandées.
9. Restaurer les variables d'environnement modifiées.

`check_site.py` exécute ensuite les contrôles de cohérence :

| Contrôle | Ce qui est vérifié |
| --- | --- |
| Navigation MkDocs | Toutes les pages Markdown sont couvertes par la navigation. |
| Alignement menu / titre | Les libellés explicites de navigation correspondent aux titres H1, sauf libellé court `nav_label` déclaré dans la page. |
| Contenus générés | `site/`, `.generated/`, `.venv/` et autres sorties locales ne sont pas suivis par Git. |
| `.gitignore` | Les chemins générés et locaux sont protégés. |
| `.gitattributes` | Les fins de ligne sont stabilisées pour éviter le bruit Windows / Linux. |
| Liens internes | Les liens et ancres du site construit sont valides. |
| Cache navigateur | Les assets locaux publiés portent une version de cache `?v=<empreinte>`. |
| Structure multilingue | Les versions `/fr/` et `/en/` sont générées. |
| Liens externes optionnels | Les liens HTTP(S) sont vérifiés si l'option réseau est activée. |
| Synchronisation Codex | `AGENTS.md` et la page publiée `instructions-codex.md` restent synchronisés sur les règles clés. |
| Workflow de publication | Le workflow construit le site multilingue, lance les contrôles de liens externes et déploie vers Cloudflare Pages. |
| Index de section | Les pages FAQ, Méthodologie et Administration restent cohérentes avec leur rôle. |
| Cartouches de lecture | Les publics cibles utilisent le référentiel des rôles. |
| Statistiques | Les cartouches et `page-metrics.json` sont à jour. |
| Garde-fous FLOW | Les formulations interdites ou dangereuses ne réapparaissent pas. |
| Glossaire | Les concepts FLOW essentiels restent présents. |
| SVG générés | Tous les SVG de `docs/assets/images/` sont pilotés par `scripts/generate_svg_diagrams.py` et à jour. |
| SVG | Les fichiers SVG sont valides, vectoriels, redimensionnables et exportables Word / PowerPoint. |
| Référentiel des schémas | Les SVG et leurs usages sont couverts par le registre d'impact. |

## Ce que `check-site` ne corrige pas

`check-site` est un contrôle, pas un outil de réparation.

Il ne met pas automatiquement à jour :

- les cartouches de lecture ;
- `docs/referentiel/page-metrics.json` ;
- `docs/referentiel/statistiques.md` ;
- les SVG générés par script ;
- les nouveaux SVG ajoutés hors générateur ;
- les références web obsolètes ;
- les erreurs de navigation ou de titre.

Lorsqu'un contrôle échoue, il faut corriger la source concernée puis relancer `check-site`.

## Opérations à lancer avant un contrôle

Avant `check-site`, lancer les opérations adaptées au type de modification.

| Modification réalisée | Commande à lancer avant `check-site` |
| --- | --- |
| Page ajoutée, renommée ou modifiée de façon significative | `.\scripts\update-reading-metrics.ps1` |
| Texte ou structure d'un SVG généré modifié | `.\scripts\generate-svg-diagrams.ps1` |
| Référence Internet ajoutée ou modifiée | `.\scripts\check-site.ps1 -ExternalLinks` depuis PowerShell Windows classique |
| Changement d'environnement local | `.\scripts\doctor.ps1` |

## Lecture GitHub Actions

Le workflow GitHub Actions reprend la même logique de publication :

1. Installer l'environnement Python.
2. Restaurer ou construire le cache de dépendances.
3. Construire le site multilingue.
4. Lancer les contrôles du référentiel, avec contrôle des liens externes.
5. Publier le contenu de `site/` sur Cloudflare Pages via `cloudflare/wrangler-action@v3`.
6. Publier aussi le contenu de `site/` sur GitHub Pages pendant le POC de sécurisation.

La publication Cloudflare utilise :

- la variable GitHub `CLOUDFLARE_PROJECT_NAME`, qui contient le nom du projet Cloudflare Pages ;
- le secret GitHub `CLOUDFLARE_API_TOKEN` ;
- le secret GitHub `CLOUDFLARE_ACCOUNT_ID`.

GitHub Pages reste temporairement actif pour éviter de couper la diffusion pendant le POC.

Pendant le POC, l'étape Cloudflare est configurée en `continue-on-error: true` afin qu'un incident de paramétrage Cloudflare ne bloque pas la publication GitHub Pages historique.

Une fois Cloudflare Access validé, GitHub Pages devra être désactivé ou ne plus être diffusé, sinon il restera une URL publique de contournement.

Le site publié est donc une sortie de build.

La source de vérité reste le contenu versionné dans `docs/`, `mkdocs.yml`, `scripts/`, `AGENTS.md` et les fichiers d'administration associés.
