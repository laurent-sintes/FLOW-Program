# Les changements à conduire avec FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Change Manager, Sponsor, Métier</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>8 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer l'adoption et les changements de posture</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page identifie les grands changements de posture à conduire avec le programme FLOW.

Elle ne cherche pas à lister tous les impacts possibles.

Un programme de transformation qui pousse trop de sujets en parallèle devient difficile à comprendre, à piloter et à faire adopter.

La recommandation est donc de regrouper les impacts autour de cinq grands déplacements maximum.

Ces changements doivent inspirer la transformation : ils disent ce que les équipes doivent apprendre à regarder autrement, ce qu'elles doivent arrêter de reproduire, et ce que FLOW rend possible.

## Les cinq grands changements

| Changement | Ancien réflexe | Nouveau réflexe FLOW |
| --- | --- | --- |
| 1. Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise | Partir des marques, canaux, directions ou organisations existantes. | Partir des problèmes durables de l'entreprise, des domaines et des responsabilités à gouverner. |
| 2. Passer de “j'achète / je vends” à Engagement / Demand / Fulfillment / Supply | Séparer les sujets selon achat, vente, B2C, B2B, retail, wholesale ou SAV. | Reconnaître où l'intention est captée, quelle demande est à instruire, comment la servir, puis quel réseau d'exécution mobiliser. |
| 3. Réconcilier ERP et OMS dans une plateforme Demand | Penser séparément l'ERP, l'OMS et leurs transferts de données. | Construire une cohérence unique autour du Case, du stock, de la promesse, de l'allocation et de l'orchestration. |
| 4. Penser fulfillment et satisfaction client avant documents | Commencer par les documents à produire : facture, livraison, commande, écritures. | Commencer par la demande à satisfaire, puis intégrer les documents et la finance au bon moment. |
| 5. Construire le bon niveau de commun | Choisir entre tout centraliser ou tout laisser spécifique. | Décider ce qui doit être commun, fédéré ou différencié selon la responsabilité et l'exigence business. |

## Changement 1 — Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise

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

### Message de transformation

FLOW ne sert pas l'organisation telle qu'elle est.

FLOW aide l'entreprise à résoudre ses problèmes durables avec une structure plus lisible.

## Changement 2 — Passer de “j'achète / je vends” à Engagement / Demand / Fulfillment / Supply

### Changement attendu

Les discussions sont souvent structurées par des oppositions historiques :

```text
J'achète / je vends
B2C / B2B
Retail / wholesale
Commande / retour / SAV
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

Une demande reste une demande.

Elle peut être une commande, un retour, une réclamation, un litige, une demande SAV, une demande d'échange, une demande de remboursement ou une demande de réintégration en stock.

Le point commun est qu'elle touche à un engagement envers un client, un magasin, un partenaire, un fournisseur ou une organisation interne.

### Impacts principaux

- Les équipes doivent apprendre à reconnaître une demande au-delà du canal, du type de vente ou du processus historique.
- Les sujets B2C, B2B, retail, wholesale ou SAV doivent être comparés par responsabilité, pas isolés par vocabulaire historique.
- Les achats, ventes, retours et demandes de service peuvent partager des mécanismes communs : demande, engagement, promesse, allocation, exécution, exception, résolution.
- Les débats doivent moins opposer “achat” et “vente”, et davantage distinguer ce qui relève de Demand ou Supply.
- Les services orientés client, comme certains services SAV Sarenza, peuvent s'intégrer à la plateforme dès lors qu'ils manipulent des demandes, statuts, événements, exceptions ou engagements clients.

### Message de transformation

FLOW ne part pas de “j'achète” ou “je vends”.

FLOW part d'une demande à satisfaire et d'un réseau d'exécution à mobiliser.

## Changement 3 — Réconcilier ERP et OMS dans une plateforme Demand

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

### Message de transformation

FLOW n'empile pas un nouvel OMS sur un nouvel ERP.

FLOW cherche à réconcilier les responsabilités de demande dans une plateforme cohérente.

## Changement 4 — Penser fulfillment et satisfaction client avant documents

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

### Message de transformation

On ne nie pas la facture.

On la remet à sa place : elle documente et comptabilise une réalité opérationnelle que FLOW doit d'abord savoir instruire, promettre et exécuter.

## Changement 5 — Construire le bon niveau de commun

### Changement attendu

La convergence FLOW ne consiste pas à choisir entre deux extrêmes :

```text
tout centraliser
ou
tout laisser spécifique
```

Cette lecture est trop manichéenne.

La convergence doit devenir un choix explicite du bon niveau de commun.

Selon la responsabilité, le contexte et l'exigence business, le programme peut décider de :

- centraliser une capacité ;
- unifier un modèle ;
- standardiser une règle ou un processus ;
- fédérer plusieurs pratiques ;
- laisser une différenciation locale ;
- préserver une singularité business lorsqu'elle crée de la valeur.

FLOW n'est donc pas une boîte à outil unique dans laquelle tout doit entrer.

FLOW est une plateforme qui aide à décider le bon niveau de commun et le bon niveau de différenciation.

### Impacts principaux

- Les équipes doivent arrêter de traiter la convergence comme un choix binaire entre uniformisation et autonomie totale.
- Les différences doivent être qualifiées : différenciantes, historiques, contraintes, transitoires ou à résorber.
- Les responsabilités doivent être analysées une par une pour déterminer le bon niveau de convergence.
- Les trajectoires de retrait ou remplacement applicatif doivent être expliquées par responsabilité.
- Les populations impactées doivent comprendre ce qui sera commun, ce qui sera standardisé, ce qui restera autonome et pourquoi.

### Message de transformation

FLOW ne cherche pas à tout uniformiser.

FLOW organise une convergence à tiroirs : commune là où c'est nécessaire, différenciée là où le business l'exige.

## Sujets volontairement regroupés

Certains sujets auraient pu être séparés, mais doivent être rattachés aux cinq changements ci-dessus pour éviter de diluer la conduite du changement.

| Sujet détaillé | À rattacher à |
| --- | --- |
| Domain-Driven Design | Ne plus servir l'organisation, mais résoudre les problèmes de l'entreprise |
| Urbanisme commun BRD / GBM | Ne plus servir l'organisation + construire le bon niveau de commun |
| B2C / B2B / retail / wholesale | Passer à Engagement / Demand / Fulfillment / Supply |
| Achats / ventes | Passer à Engagement / Demand / Fulfillment / Supply |
| SAV / litiges / retours / remboursements | Passer à Engagement / Demand / Fulfillment / Supply avant documents |
| Services SAV Sarenza | Passer à Engagement / Demand / Fulfillment / Supply |
| Case Management | Réconcilier ERP et OMS dans une plateforme Demand |
| Stock unifié | Réconcilier ERP et OMS + fulfillment avant documents |
| Allocation et promesse | Réconcilier ERP et OMS + Engagement / Demand / Fulfillment / Supply |
| Facture, bon de livraison, avoir, écritures | Fulfillment et satisfaction client avant documents |
| Finance | Fulfillment et satisfaction client avant documents |
| Remplacement SAP / NewStore / StoreLand / Socloz / UR | Réconcilier ERP et OMS + construire le bon niveau de commun |
| Product ownership | Support de gouvernance pour tous les changements, mais pas un sujet autonome au départ |
| Nomenclature data | Support de langage pour fulfillment, ERP / OMS et Finance, mais pas un sujet autonome au départ |

## Points de vigilance

- Ne pas présenter tous les concepts FLOW comme des sujets de changement séparés.
- Ne pas transformer chaque composant cible en campagne de change autonome.
- Ne pas commencer les ateliers par les documents si le sujet réel est la satisfaction de la demande.
- Ne pas reconduire la séparation ERP / OMS uniquement parce qu'elle existe dans l'architecture actuelle.
- Ne pas confondre convergence et uniformisation.
- Ne pas confondre différenciation business et héritage applicatif subi.
- Ne pas réduire le change au déploiement applicatif final.

## À retenir

La conduite du changement FLOW doit être concrète et inspirante.

Les impacts sont nombreux, mais ils doivent être racontés à travers cinq grands déplacements de posture.

Le changement central est le suivant : FLOW demande de passer d'une lecture par organisation, canal, application ou document à une lecture par problème d'entreprise, demande, responsabilité, fulfillment et convergence par niveaux.
