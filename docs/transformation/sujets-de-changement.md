# Sujets de changement FLOW

## Intention

Cette page identifie les principaux sujets de changement à conduire avec le programme FLOW.

Elle ne cherche pas à lister tous les impacts possibles.

Un programme de transformation qui pousse trop de sujets de changement en parallèle devient difficile à comprendre, à piloter et à faire adopter.

La recommandation est donc de regrouper les impacts autour de cinq grands sujets maximum.

Ces sujets doivent être formulés comme de vrais changements de posture : ce que les équipes doivent arrêter de faire, ce qu'elles doivent apprendre à faire autrement, et pourquoi cela compte pour FLOW.

## Les cinq sujets de changement

| Sujet | Ancien réflexe | Nouveau réflexe FLOW |
| --- | --- | --- |
| 1. Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise | Partir des marques, canaux, directions ou organisations existantes. | Partir des problèmes durables de l'entreprise, des domaines et des responsabilités à gouverner. |
| 2. Passer de “j'achète / je vends” à Demand / Supply | Séparer les sujets selon achat, vente, B2C, B2B, retail ou wholesale. | Distinguer ce qui relève de la demande à instruire et ce qui relève de l'exécution à mobiliser. |
| 3. Réconcilier ERP et OMS dans une plateforme Demand | Penser séparément l'ERP, l'OMS et leurs transferts de données. | Construire une cohérence unique autour du Case, du stock, de la promesse, de l'allocation et de l'orchestration. |
| 4. Penser fulfillment et satisfaction client avant documents | Commencer par les documents à produire : facture, livraison, commande, écritures. | Commencer par la demande à satisfaire, puis intégrer les documents et la finance au bon moment. |
| 5. Converger sans uniformiser | Chercher un modèle unique ou laisser chaque groupe garder son modèle. | Fédérer les capacités communes tout en préservant les différences utiles de BRD, GBM et des marques. |

## Sujet 1 — Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise

### Changement attendu

FLOW doit s'appuyer sur une logique proche du Domain-Driven Design : on ne modélise pas l'organisation telle qu'elle existe, on cherche à comprendre les problèmes durables que l'entreprise doit résoudre.

Les organisations, marques, canaux et applications sont des points d'entrée utiles.

Mais ils ne doivent pas devenir automatiquement la structure cible.

Le changement consiste à passer de :

```text
Qui fait quoi aujourd'hui ?
```

à :

```text
Quel problème d'entreprise doit être résolu durablement ?
```

### Impacts principaux

- Les ateliers doivent chercher les responsabilités derrière les organisations.
- Les irritants doivent être reformulés comme problèmes d'entreprise, pas seulement comme problèmes locaux.
- Les cartographies doivent montrer les domaines et responsabilités, pas seulement les équipes ou applications.
- Les arbitrages doivent éviter de reproduire l'organisation existante dans la plateforme cible.

### Message de change

FLOW ne sert pas l'organisation telle qu'elle est.

FLOW aide l'entreprise à résoudre ses problèmes durables avec une structure plus lisible.

## Sujet 2 — Passer de “j'achète / je vends” à Demand / Supply

### Changement attendu

Les discussions sont souvent structurées par des oppositions historiques :

```text
J'achète / je vends
B2C / B2B
Retail / wholesale
BRD / GBM
Marque A / marque B
```

Ces distinctions restent importantes pour comprendre les contextes.

Mais elles ne doivent pas être le premier principe de conception.

FLOW propose une lecture plus transverse :

```text
Demand
    → la demande à instruire, décider, promettre, suivre et arbitrer

Supply
    → les ressources, lieux, partenaires et capacités d'exécution à mobiliser
```

### Impacts principaux

- Les équipes doivent apprendre à reconnaître une demande au-delà du canal ou du type de vente.
- Les sujets B2C, B2B, retail ou wholesale doivent être comparés par responsabilité, pas isolés par vocabulaire historique.
- Les achats et ventes peuvent partager des mécanismes communs : demande, engagement, promesse, allocation, exécution, exception.
- Les débats doivent moins opposer “achat” et “vente”, et davantage distinguer ce qui relève de Demand ou Supply.

### Message de change

FLOW ne part pas de “j'achète” ou “je vends”.

FLOW part d'une demande à satisfaire et d'un réseau d'exécution à mobiliser.

## Sujet 3 — Réconcilier ERP et OMS dans une plateforme Demand

### Changement attendu

Dans beaucoup de SI, l'ERP et l'OMS se partagent artificiellement une même réalité métier.

L'ERP porte des objets transactionnels, du stock, des documents ou de la finance.

L'OMS porte le cycle de vie commande, la promesse, la réservation ou l'orchestration omnicanale.

Cette séparation crée des transferts de données, des duplications, des statuts divergents et des zones grises de responsabilité.

FLOW cherche à dépasser cette séparation en construisant une plateforme Demand unique autour du Case.

### Impacts principaux

- Les équipes doivent arrêter de demander trop vite : “est-ce ERP ou OMS ?”.
- Les responsabilités doivent être redécoupées autour du Case, de la décision, du stock, de la promesse et de l'allocation.
- Le remplacement de SAP, NewStore, StoreLand, Socloz ou UR doit être analysé par responsabilité, pas application par application.
- Les transferts de données entre ERP et OMS ne doivent pas être reconduits automatiquement dans la cible.

### Message de change

FLOW n'empile pas un nouvel OMS sur un nouvel ERP.

FLOW cherche à réconcilier les responsabilités de demande dans une plateforme cohérente.

## Sujet 4 — Penser fulfillment et satisfaction client avant documents

### Changement attendu

Une conception orientée ERP conduit souvent à penser d'abord les documents :

```text
commande
facture
bon de livraison
avoir
écriture comptable
```

Ces documents sont indispensables.

Mais ils ne doivent pas être le point de départ de la conception FLOW.

FLOW doit d'abord répondre à une question opérationnelle :

> Comment satisfaire la demande de manière fiable, explicable et traçable ?

La finance et les documents doivent ensuite être intégrés comme conséquences, preuves, obligations ou artefacts de cette exécution.

### Impacts principaux

- Les ateliers ne doivent pas commencer systématiquement par “comment fait-on la facture ?”.
- La première question doit être : quelle demande, quelle promesse, quelle exécution, quelle exception ?
- Les documents doivent être rattachés au Case et à son cycle de vie.
- La Finance doit être intégrée proprement, mais sans piloter seule la modélisation opérationnelle.
- Les équipes doivent distinguer l'événement métier, le fait opérationnel, le document et l'écriture financière.

### Message de change

On ne nie pas la facture.

On la remet à sa place : elle documente et comptabilise une réalité opérationnelle que FLOW doit d'abord savoir instruire, promettre et exécuter.

## Sujet 5 — Converger sans uniformiser

### Changement attendu

La convergence FLOW ne consiste pas à imposer un seul modèle opérationnel à BRD, GBM et aux marques.

Elle consiste à fédérer des capacités communes tout en respectant les différences utiles.

La convergence se joue à plusieurs niveaux :

- entre BRD et GBM ;
- entre les marques au sein de GBM ;
- entre retail, e-commerce, B2B et wholesale ;
- entre les systèmes historiques et la plateforme cible.

### Impacts principaux

- Les équipes doivent distinguer ce qui doit être commun de ce qui peut rester spécifique.
- Les différences doivent être qualifiées : différenciantes, historiques, contraintes ou à résorber.
- Les trajectoires de retrait ou remplacement applicatif doivent être expliquées par responsabilité.
- Les populations impactées doivent comprendre ce qu'elles gagnent en commun, et ce qu'elles conservent en autonomie.

### Message de change

FLOW ne cherche pas l'uniformisation complète.

FLOW cherche le bon niveau de fédération.

## Sujets volontairement regroupés

Certains sujets auraient pu être séparés, mais doivent être rattachés aux cinq thèmes ci-dessus pour éviter de diluer la conduite du changement.

| Sujet détaillé | À rattacher à |
| --- | --- |
| Domain-Driven Design | Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise |
| Urbanisme commun BRD / GBM | Ne plus servir l'organisation + converger sans uniformiser |
| B2C / B2B / retail / wholesale | Passer à Demand / Supply |
| Achats / ventes | Passer à Demand / Supply |
| Case Management | Réconcilier ERP et OMS dans une plateforme Demand |
| Stock unifié | Réconcilier ERP et OMS + fulfillment avant documents |
| Allocation et promesse | Réconcilier ERP et OMS + Demand / Supply |
| Facture, bon de livraison, avoir, écritures | Fulfillment et satisfaction client avant documents |
| Finance | Fulfillment et satisfaction client avant documents |
| Remplacement SAP / NewStore / StoreLand / Socloz / UR | Réconcilier ERP et OMS + converger sans uniformiser |
| Product ownership | Support de gouvernance pour tous les sujets, mais pas un sujet de change autonome au départ |
| Nomenclature data | Support de langage pour fulfillment, ERP / OMS et Finance, mais pas un sujet de change autonome au départ |

## Points de vigilance

- Ne pas présenter tous les concepts FLOW comme des sujets de changement séparés.
- Ne pas transformer chaque composant cible en campagne de change autonome.
- Ne pas commencer les ateliers par les documents si le sujet réel est la satisfaction de la demande.
- Ne pas reconduire la séparation ERP / OMS uniquement parce qu'elle existe dans l'architecture actuelle.
- Ne pas confondre convergence et uniformisation.
- Ne pas réduire le change au déploiement applicatif final.

## À retenir

La conduite du changement FLOW doit être concrète.

Les impacts sont nombreux, mais ils doivent être racontés à travers cinq grands déplacements de posture.

Le changement central est le suivant : FLOW demande de passer d'une lecture par organisation, canal, application ou document à une lecture par problème d'entreprise, demande, responsabilité, fulfillment et fédération.
