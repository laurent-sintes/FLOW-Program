# Environnement Codex sous Windows

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
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

Le résultat est écrit dans :

```powershell
site/
```

Ce répertoire est généré automatiquement. Il ne doit pas être poussé sur GitHub.

Le warning Material for MkDocs sur MkDocs 2.0 n'est pas bloquant pour le build actuel. Les messages `INFO` sur des ancres manquantes signalent des liens à nettoyer, mais ils ne bloquent pas la génération.

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
Token scopes: repo
```

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
- `mkdocs build --strict` construit le site ;
- `gh auth status` confirme l'authentification GitHub ;
- `git fetch` passe ;
- `git status -sb` ne montre pas de changements inattendus hors contenu volontaire.
