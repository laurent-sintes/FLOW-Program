# Environnement Codex sous Windows

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
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Objectif

Cette page décrit l'environnement local nécessaire pour mettre à jour et piloter le référentiel FLOW avec Codex sous Windows.

Elle sert à distinguer trois choses qui peuvent se ressembler quand une commande échoue :

- l'installation Windows réelle ;
- l'environnement Python du projet ;
- les autorisations propres au bac à sable Codex.

## Repère de départ

Le projet se trouve dans :

```powershell
C:\Users\laure\Documents\Codex\FLOW-Program
```

Les commandes doivent être lancées depuis ce répertoire.

## Diagnostic rapide

La commande de diagnostic local est :

```powershell
.\scripts\doctor.ps1
```

Elle vérifie les chemins attendus, `.venv`, les packages Python, Git, GitHub CLI, `.gitattributes` et le contexte d'exécution.

Depuis Codex, certains contrôles peuvent afficher des alertes liées au bac à sable. Depuis un PowerShell Windows classique, l'option suivante ajoute un test HTTPS léger :

```powershell
.\scripts\doctor.ps1 -Network
```

## Python

Python est installé côté Windows dans le profil utilisateur.

Validation attendue :

```powershell
python --version
python -m pip --version
```

Résultat observé :

```text
Python 3.14.6
pip 26.1.2
```

L'exécutable réel peut se trouver dans :

```powershell
C:\Users\laure\AppData\Local\Python\pythoncore-3.14-64\python.exe
```

Le menu Démarrer peut afficher des raccourcis dans `Start Menu\Programs\Python\Python 3.14`, mais ce ne sont pas les exécutables à utiliser comme référence.

## Environnement Python du projet

Le projet utilise un environnement virtuel local :

```powershell
.\.venv
```

Validation attendue :

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m mkdocs --version
```

Résultat observé :

```text
Python 3.14.6
python -m mkdocs, version 1.6.1
```

Si l'environnement doit être recréé :

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install mkdocs-material
```

## Construire le site local

Le site généré localement sert uniquement à tester le rendu.

Commande :

```powershell
.\scripts\build-docs.ps1
```

Le résultat est écrit dans :

```powershell
site/
```

Ce répertoire est généré automatiquement. Il ne doit pas être poussé sur GitHub.

Cette commande active `NO_MKDOCS_2_WARNING` avant le build afin de masquer le bandeau d'alerte Material for MkDocs sur MkDocs 2.0. Le projet reste construit avec `mkdocs build --strict`.

Dans un PowerShell Windows classique, elle utilise le Python du `.venv`. Depuis Codex, elle peut utiliser le Python embarqué de Codex avec les paquets du `.venv`, afin d'éviter les blocages du bac à sable sur l'exécutable Python local.

Si la commande directe `.\.venv\Scripts\python.exe -m mkdocs build --strict` est utilisée, le bandeau Material peut réapparaître. Ce bandeau vient du paquet `mkdocs-material`, pas d'un problème du référentiel FLOW.

## Vérifier le site

La commande de validation complète est :

```powershell
.\scripts\check-site.ps1
```

Elle lance d'abord le build local, puis exécute des contrôles Python sur le site et le référentiel :

- pages Markdown déclarées dans `mkdocs.yml` ;
- liens internes et ancres du site généré ;
- absence de contenu généré versionné ;
- synchronisation entre `AGENTS.md` et la page publiée `AGENTS.md - Instructions Codex` ;
- présence des concepts FLOW structurants ;
- détection de formulations contraires au positionnement de FLOW.

Le contrôle des liens externes est volontairement optionnel, car il dépend du réseau :

```powershell
.\scripts\check-site.ps1 -ExternalLinks
```

Avant une publication importante, le mode strict permet de transformer les échecs HTTP confirmés en erreurs :

```powershell
.\scripts\check-site.ps1 -StrictExternalLinks
```

Depuis Codex, ce contrôle peut être ignoré si le runtime embarqué bloque HTTPS. Dans ce cas, lancer la commande depuis un PowerShell Windows classique, où le Python du projet peut accéder au réseau.

Les erreurs `ERROR` doivent être corrigées avant commit. Les alertes `WARN` signalent un point à examiner, sans bloquer automatiquement.

## Fins de ligne Git

Le fichier `.gitattributes` force les fichiers texte du dépôt en `LF`.

Cette règle évite les avertissements du type `LF will be replaced by CRLF` et limite le bruit dans les diffs entre Windows, Codex et GitHub Actions.

## Git et GitHub

Validation Git :

```powershell
git status -sb
git fetch
```

Validation GitHub CLI :

```powershell
gh auth status
```

Résultat attendu :

```text
Logged in to github.com account laurent-sintes
Git operations protocol: https
Token scopes: gist, read:org, repo
```

Le scope `workflow` est nécessaire dès qu'un commit modifie un fichier dans `.github/workflows/`.

Sans ce scope, le push peut être refusé par GitHub avec un message proche de :

```text
refusing to allow an OAuth App to create or update workflow `.github/workflows/...` without `workflow` scope
```

Les droits GitHub CLI peuvent expirer, être réinitialisés ou avoir été accordés avant qu'un nouveau besoin apparaisse. Dans ce cas, relancer l'autorisation depuis un PowerShell Windows classique :

```powershell
gh auth refresh --hostname github.com --scopes workflow
```

Puis vérifier :

```powershell
gh auth status
```

Résultat attendu pour modifier les workflows :

```text
Token scopes: gist, read:org, repo, workflow
```

Cette procédure doit être faite côté Windows, pas depuis Codex, car elle peut ouvrir le navigateur et accéder au keyring Windows.

Pour pousser les changements :

```powershell
git status -sb
git add <fichiers>
git commit -m "Message clair"
git push
```

## Particularité Codex

Codex peut exécuter certaines commandes dans un bac à sable plus restrictif que le PowerShell Windows classique.

Ce bac à sable, ou sandbox, est une protection : il limite ce qu'un agent peut faire sur le poste sans validation explicite. Il peut empêcher l'écriture dans certains répertoires sensibles, l'accès à des secrets Windows, l'utilisation du keyring GitHub ou l'exécution de certains programmes installés dans le profil utilisateur.

Il faut donc distinguer deux niveaux de validation :

- la commande fonctionne dans Windows ou dans PowerShell ;
- la commande fonctionne depuis Codex, avec ou sans autorisation hors sandbox.

Une erreur dans Codex ne signifie pas automatiquement que l'installation Windows est mauvaise.

Deux symptômes peuvent alors apparaître :

- `Permission denied` lors d'un `git fetch`, parce que Git doit écrire dans `.git/FETCH_HEAD` ;
- `Accès refusé` ou `python` non résolu lors de l'exécution du Python installé localement.
- `gh auth status` peut échouer dans la sandbox si Codex n'accède pas correctement au keyring Windows.
- un push qui modifie `.github/workflows/` peut être refusé si le token GitHub CLI n'a pas le scope `workflow`.

La bonne méthode est de tester la même commande hors bac à sable, avec l'autorisation Codex demandée à l'écran, ou dans un PowerShell Windows classique.

Si la commande passe hors sandbox, le composant est considéré comme sain :

- Git est sain si `git fetch` passe hors sandbox ;
- GitHub CLI est sain si `gh auth status` confirme l'authentification hors sandbox ;
- Python est sain si `python --version`, `python -m pip --version` et `.\.venv\Scripts\python.exe -m mkdocs --version` passent hors sandbox.

Le problème n'est alors pas l'installation elle-même, mais le niveau d'autorisation utilisé par Codex pour exécuter la commande.

Dans ce projet, c'est le fonctionnement attendu : les commandes sensibles peuvent demander une autorisation ponctuelle ou persistante, puis le travail peut continuer normalement.

## État de référence

L'environnement est considéré comme sain lorsque :

- Python Windows répond en `3.14.6` ;
- le `.venv` du projet répond en `3.14.6` ;
- MkDocs répond en `1.6.1` ;
- `.\scripts\build-docs.ps1` construit le site ;
- `.\scripts\check-site.ps1` valide les contrôles automatisés ;
- `gh auth status` confirme l'authentification GitHub ;
- `gh auth status` affiche le scope `workflow` lorsque les workflows GitHub Actions doivent être modifiés ;
- `git fetch` passe ;
- `git status -sb` ne montre pas de changements inattendus hors contenu volontaire.
