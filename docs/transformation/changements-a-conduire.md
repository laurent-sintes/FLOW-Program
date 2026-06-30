# Les changements à conduire

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
      <strong>13 min</strong>
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

La recommandation est donc de regrouper les impacts de posture autour de cinq grands déplacements maximum.

Ces changements doivent inspirer la transformation : ils disent ce que les équipes doivent apprendre à regarder autrement, ce qu'elles doivent arrêter de reproduire, et ce que FLOW rend possible.

La [note de choix stratégique](../vision/note-choix-strategique.md), la réunion leaders et l'[atelier OMS C-LOG](../contexte/panorama-oms-c-log.md) du 30 juin 2026 précisent l'ordre de priorité du récit : déplacer le centre de gravité de l'ERP vers la demande, réconcilier ERP et OMS, clarifier la promesse omnicanale, expliquer le découpage Engagement / Demand / Fulfillment / Supply, et rappeler que FLOW n'embarque pas tout.

La gouvernance de l'information est un arbitrage prioritaire de nature différente : ce n'est pas un arbitrage de positionnement ou de périmètre, mais un arbitrage de gouvernance. Côté transformation, il doit être porté comme un message transverse : distinguer l'information au repos, qui pose la question des sources de référence et projections, et l'information en transit, qui pose la question des contrats d'échange.

## Parcours de lecture conseillé

Cette page peut servir de point d'entrée aux Change Managers.

Pour préparer un plan d'accompagnement, lire en priorité :

1. [Note de choix stratégique : FLOW](../vision/note-choix-strategique.md), pour comprendre les arbitrages à rendre et les messages à porter.
2. [Positionnement de FLOW](../vision/positionnement-flow.md), pour visualiser ce que FLOW porte et ce qui reste adhérent.
3. [Questions pour les nouveaux](../faq/questions-pour-les-nouveaux.md), pour identifier les formulations simples à réutiliser en communication.
4. [C-LOG : une décision de fulfillment déjà distribuée](../hotspots/c-log-decision-fulfillment.md), pour comprendre le sujet sensible de la promesse omnicanale.
5. [Master Data : des objets maîtres aux sources gouvernées](../principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md), pour expliquer l'approche MDM sans tomber dans l'inventaire d'objets maîtres.
6. [Processus de cadrage](../methode/processus-de-cadrage.md), pour relier les messages de transformation aux étapes projet et aux arbitrages Build / Buy.

## Les cinq grands changements

| Changement | Ancien réflexe | Nouveau réflexe FLOW | À lire ensuite |
| --- | --- | --- | --- |
| 1. Déplacer le centre de gravité vers la demande, la promesse et la satisfaction client | Partir de l'ERP, des documents, des applications ou des organisations existantes. | Partir de la demande à satisfaire, de la promesse à tenir, des décisions à gouverner et des responsabilités durables à organiser. | [Note de choix stratégique](../vision/note-choix-strategique.md) · [Vision détaillée - ruptures](../vision/vision-detaillee/2-ruptures-structurantes.md) |
| 2. Passer de “j'achète / je vends” à Engagement / Demand / Fulfillment / Supply | Séparer les sujets selon achat, vente, B2C, B2B, retail, wholesale ou SAV. | Reconnaître où l'intention est captée, quelle demande est à instruire, comment la servir, puis quel réseau d'exécution mobiliser. | [Principe 4](../principes-directeurs/4-separer-demand-et-supply.md) · [FAQ experte](../faq/pourquoi-flow-pas-structure-jachete-je-vends.md) |
| 3. Réconcilier ERP et OMS dans une plateforme Demand | Penser séparément l'ERP, l'OMS et leurs transferts d'informations. | Construire une cohérence unique autour du Case, du stock, de la promesse, de l'allocation et de l'orchestration. | [FAQ ERP / OMS](../faq/supprimer-erp-oms-folie.md) · [Socle Case Management](../architecture-cible/produits/socle-case-management.md) |
| 4. Clarifier qui détient la promesse et penser fulfillment avant documents | Traiter la promesse comme un détail OMS, logistique ou transport. | Décider où vit la promesse client, puis intégrer les documents et la finance comme conséquences maîtrisées. | [Hotspot C-LOG](../hotspots/c-log-decision-fulfillment.md) · [Atelier OMS C-LOG](../contexte/panorama-oms-c-log.md) |
| 5. Construire le bon niveau de commun sans tout embarquer dans FLOW | Choisir entre tout centraliser ou tout laisser spécifique. | Décider ce qui doit être commun, fédéré, adhérent ou différencié selon la responsabilité et l'exigence business. | [Positionnement de FLOW](../vision/positionnement-flow.md) · [Principe 1](../principes-directeurs/1-converger-c-est-federer.md) |

Ces cinq changements restent les messages principaux de posture. La gouvernance de l'information est une décision prioritaire, mais elle traverse ces changements plutôt que de constituer une sixième campagne de transformation séparée.

## Changement 1 — Déplacer le centre de gravité vers la demande, la promesse et la satisfaction client

### Changement attendu

FLOW doit déplacer le point de départ de la conception.

Le centre de gravité ne doit plus être l'ERP, le document ou l'application historique.

Il doit devenir la demande à satisfaire, la promesse à tenir, les décisions métier à gouverner et la satisfaction client ou utilisateur à expliquer.

FLOW doit donc s'appuyer sur une logique proche du Domain-Driven Design : on ne modélise pas l'organisation telle qu'elle existe, on cherche à comprendre les problèmes durables que l'entreprise doit résoudre.

Les organisations, marques, canaux et applications sont des points d'entrée utiles.

Mais ils ne doivent pas devenir automatiquement la structure cible.

Le changement consiste à passer de :

```text
Quelle application ou organisation traite le sujet aujourd'hui ?
```

à :

```text
Quelle demande faut-il satisfaire, avec quelle promesse, quelle décision et quelle responsabilité durable ?
```

### Impacts principaux

- Les ateliers doivent chercher les responsabilités derrière les organisations.
- Les irritants doivent être reformulés comme problèmes d'entreprise, pas seulement comme problèmes locaux ou applicatifs.
- Les cartographies doivent montrer les domaines et responsabilités, pas seulement les équipes ou applications.
- Les arbitrages doivent éviter de reproduire l'organisation existante dans la plateforme cible.
- Les discussions doivent expliciter si le sujet relève de la demande, de la promesse, du fulfillment, de l'exécution Supply ou d'un domaine adhérent.

### Message de transformation

FLOW ne se construit pas autour de l'ERP tel qu'il existe.

FLOW se construit autour des demandes, des promesses et des décisions qui doivent rester cohérentes à l'échelle du groupe.

À lire ensuite : [Note de choix stratégique : FLOW](../vision/note-choix-strategique.md) et [Ruptures : déplacer le centre de gravité du SI](../vision/vision-detaillee/2-ruptures-structurantes.md).

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
Engagement
    → l'intention est captée dans un canal, une relation ou une interaction

Demand
    → la demande à instruire, décider, promettre, suivre et arbitrer

Fulfillment
    → la promesse est calculée, arbitrée et pilotée

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

À lire ensuite : [Principe 4 - Articuler Engagement, Demand, Fulfillment et Supply](../principes-directeurs/4-separer-demand-et-supply.md) et [Pourquoi FLOW n'est-il pas structuré autour de J'achète / Je vends ?](../faq/pourquoi-flow-pas-structure-jachete-je-vends.md).

## Changement 3 — Réconcilier ERP et OMS dans une plateforme Demand

### Changement attendu

Dans beaucoup de SI, l'ERP et l'OMS se partagent artificiellement une même réalité métier.

L'ERP porte des objets transactionnels, du stock, des documents ou de la finance.

L'OMS porte le cycle de vie commande, la promesse, la réservation ou l'orchestration omnicanale.

Cette séparation crée des transferts d'informations, des duplications, des statuts divergents et des zones grises de responsabilité.

FLOW cherche à dépasser cette séparation en construisant une plateforme Demand unique autour du Case.

L'atelier C-LOG ajoute une nuance importante : l'OMS n'est pas toujours seulement l'autre moitié de l'ERP.

Dans certains contextes, comme Crossroad chez C-LOG, l'OMS porte déjà des décisions de fulfillment, un scoring coût / délai / complétude, des règles de crossdock, de split et de file manuelle.

Le changement ne consiste donc pas à dire “supprimer l'OMS”.

Il consiste à clarifier où vit la décision, qui la gouverne, et comment FLOW, ERP, OMS et C-LOG coopèrent sans créer plusieurs centres de promesse concurrents.

### Impacts principaux

- Les équipes doivent arrêter de demander trop vite : “est-ce ERP ou OMS ?”.
- Les responsabilités doivent être redécoupées autour du Case, de la décision, du stock, de la promesse et de l'allocation.
- Le remplacement de SAP, NewStore, StoreLand, Socloz ou UR doit être analysé par responsabilité, pas application par application.
- Les transferts d'informations entre ERP et OMS ne doivent pas être reconduits automatiquement dans la cible.
- Les capacités OMS existantes, notamment C-LOG, doivent être instruites comme décisions et services à gouverner, pas seulement comme applications à brancher ou à remplacer.

### Message de transformation

FLOW n'empile pas un nouvel OMS sur un nouvel ERP.

FLOW cherche à réconcilier les responsabilités de demande et de fulfillment dans une plateforme cohérente, en explicitant ce qui reste délégué à des capacités spécialisées comme C-LOG.

À lire ensuite : [Supprimer ERP et OMS ? Une folie !](../faq/supprimer-erp-oms-folie.md), [Socle Case Management](../architecture-cible/produits/socle-case-management.md) et [De l'OMS au Demand Management](../insights/oms-vers-demand-management.md).

## Changement 4 — Clarifier qui détient la promesse et penser fulfillment avant documents

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

FLOW doit d'abord répondre à deux questions opérationnelles :

> Qui détient la promesse client, et comment satisfaire la demande de manière fiable, explicable et traçable ?

L'atelier C-LOG rend cette question concrète.

Si C-LOG porte la promesse omnicanale, FLOW doit gouverner un service Supply très structurant.

Si FLOW porte la promesse, C-LOG doit exposer ses capacités, contraintes, événements et engagements de service comme un partenaire d'exécution.

La finance et les documents doivent ensuite être intégrés comme conséquences, preuves, obligations ou artefacts de cette exécution.

### Impacts principaux

- Les ateliers ne doivent pas commencer systématiquement par “comment fait-on la facture ?”.
- La première question doit être : quelle demande, quelle promesse, quelle exécution, quelle exception ?
- Les documents doivent être rattachés au Case et à son cycle de vie.
- La Finance doit être intégrée proprement, mais sans piloter seule la modélisation opérationnelle.
- Les équipes doivent distinguer l'événement métier, le fait opérationnel, le document et l'écriture financière.
- Les équipes doivent comprendre que le choix FLOW / C-LOG sur la promesse est un arbitrage de gouvernance, pas seulement une décision technique.

### Message de transformation

On ne nie pas la facture.

On la remet à sa place : elle documente et comptabilise une réalité opérationnelle que FLOW doit d'abord savoir instruire, promettre, déléguer et expliquer.

À lire ensuite : [C-LOG : une décision de fulfillment déjà distribuée](../hotspots/c-log-decision-fulfillment.md), [OMS C-LOG - atelier du 30 juin 2026](../contexte/panorama-oms-c-log.md) et [Fulfillment Network Configuration](../architecture-cible/produits/fulfillment-network-configuration.md).

## Changement 5 — Construire le bon niveau de commun sans tout embarquer dans FLOW

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

Cela vaut aussi pour le périmètre du programme : FLOW porte le cœur Demand + Fulfillment, mais des applications Engagement ou Supply peuvent rester adhérentes, être développées par d'autres projets, ou être portées par FLOW selon arbitrage.

### Impacts principaux

- Les équipes doivent arrêter de traiter la convergence comme un choix binaire entre uniformisation et autonomie totale.
- Les différences doivent être qualifiées : différenciantes, historiques, contraintes, transitoires ou à résorber.
- Les responsabilités doivent être analysées une par une pour déterminer le bon niveau de convergence.
- Les trajectoires de retrait ou remplacement applicatif doivent être expliquées par responsabilité.
- Les populations impactées doivent comprendre ce qui sera commun, ce qui sera standardisé, ce qui restera autonome et pourquoi.
- Les équipes doivent distinguer la plateforme FLOW, le programme FLOW et les domaines adhérents qui peuvent nécessiter des chantiers connexes.

### Message de transformation

FLOW ne cherche pas à tout uniformiser.

FLOW organise une convergence à tiroirs : commune là où c'est nécessaire, adhérente là où la responsabilité reste externe, différenciée là où le business l'exige.

À lire ensuite : [Positionnement de FLOW](../vision/positionnement-flow.md), [Principe 1 - Construire le bon niveau de commun](../principes-directeurs/1-converger-c-est-federer.md) et [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md).

## Message transverse — Gouverner l'information au repos et en transit

Ce message correspond au sixième arbitrage prioritaire de la note de choix stratégique : instituer une gouvernance MDM de l'information.

Pour le change, il ne doit pas devenir une sixième campagne isolée.

Il accompagne les cinq changements précédents, car FLOW ne peut pas devenir une plateforme cohérente si les équipes continuent à traiter l'information comme un stock de tables à lire ou comme une succession de flux projet.

### Au repos : ne plus chercher la bonne base

Le premier réflexe à faire évoluer concerne les informations au repos.

Le sujet n'est pas de demander “dans quelle base trouve-t-on cette information ?”.

Le sujet est de demander :

```text
Quelle information fait référence ?
Qui la crée, la valide ou la maintient ?
Pour quel usage fait-elle autorité ?
Quelle projection peut la rendre consommable ?
```

Ce message permet d'expliquer l'approche MDM sans retomber dans l'inventaire d'objets `Master Data`.

### En transit : ne plus commander un flux de plus

Le second réflexe concerne les informations en circulation.

Un besoin d'information ne doit pas conduire automatiquement à analyser une base applicative, écrire une spécification de flux et commander un batch Talend supplémentaire.

La question devient :

```text
Quel contrat expose l'information ?
Par quelle interface stable ?
Avec quelle fraîcheur, qualité, compatibilité et supervision ?
```

Une base de données applicative ne doit pas devenir une ressource publique d'échange.

Le `base à base` est un réflexe legacy : il contourne la responsabilité de l'application, fragilise son modèle interne et rend les flux difficiles à gouverner dans le temps.

À lire ensuite : [Master Data : des objets maîtres aux sources gouvernées](../principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) et [Gouvernance des données en transit](../architecture-cible/produits/gouvernance-donnees-transit.md).

## Sujets volontairement regroupés

Certains sujets auraient pu être séparés, mais doivent être rattachés aux cinq changements ci-dessus pour éviter de diluer la conduite du changement.

| Sujet détaillé | À rattacher à |
| --- | --- |
| Domain-Driven Design | Déplacer le centre de gravité vers la demande, la promesse et la satisfaction client |
| Urbanisme commun BRD / GBM | Déplacer le centre de gravité + construire le bon niveau de commun |
| B2C / B2B / retail / wholesale | Passer à Engagement / Demand / Fulfillment / Supply |
| Achats / ventes | Passer à Engagement / Demand / Fulfillment / Supply |
| SAV / litiges / retours / remboursements | Passer à Engagement / Demand / Fulfillment / Supply avant documents |
| Services SAV Sarenza | Passer à Engagement / Demand / Fulfillment / Supply |
| Case Management | Réconcilier ERP et OMS dans une plateforme Demand |
| Stock unifié | Réconcilier ERP et OMS + fulfillment avant documents |
| Allocation et promesse | Réconcilier ERP et OMS + Engagement / Demand / Fulfillment / Supply |
| Promesse omnicanale FLOW / C-LOG | Clarifier qui détient la promesse + réconcilier ERP et OMS |
| OMS C-LOG, Crossroad, scoring et crossdock | Réconcilier ERP et OMS + clarifier qui détient la promesse |
| Facture, bon de livraison, avoir, écritures | Fulfillment et satisfaction client avant documents |
| Finance | Fulfillment et satisfaction client avant documents |
| Remplacement SAP / NewStore / StoreLand / Socloz / UR | Réconcilier ERP et OMS + construire le bon niveau de commun |
| Périmètre plateforme FLOW vs programme FLOW | Construire le bon niveau de commun sans tout embarquer dans FLOW |
| Demandes de flux, batchs Talend et lectures base à base | Message transverse : gouverner l'information en transit |
| MDM vs inventaire de Master Data | Message transverse : qualifier les sources de référence et projections |
| Product ownership | Support de gouvernance pour tous les changements, mais pas un sujet autonome au départ |
| Nomenclature d'information | Support de langage pour fulfillment, ERP / OMS et Finance, mais pas un sujet autonome au départ |

## Points de vigilance

- Ne pas présenter tous les concepts FLOW comme des sujets de changement séparés.
- Ne pas transformer chaque composant cible en campagne de change autonome.
- Ne pas commencer les ateliers par les documents si le sujet réel est la satisfaction de la demande.
- Ne pas reconduire la séparation ERP / OMS uniquement parce qu'elle existe dans l'architecture actuelle.
- Ne pas réduire C-LOG à un exécutant logistique si l'OMS porte déjà des décisions de fulfillment.
- Ne pas laisser la promesse omnicanale devenir implicite entre FLOW, C-LOG et les domaines d'engagement.
- Ne pas confondre convergence et uniformisation.
- Ne pas confondre différenciation business et héritage applicatif subi.
- Ne pas mélanger dans le même message terrain les problèmes d'information au repos et les problèmes d'information en transit.
- Ne pas présenter une base de données applicative comme une interface publique d'échange.
- Ne pas accepter qu'un nouveau besoin d'information se transforme automatiquement en batch Talend ou en flux point à point.
- Ne pas réduire le change au déploiement applicatif final.

## À retenir

La conduite du changement FLOW doit être concrète et inspirante.

Les impacts sont nombreux, mais ils doivent être racontés à travers cinq grands déplacements de posture.

Le changement central est le suivant : FLOW demande de passer d'une lecture par ERP, OMS, organisation, canal, application ou document à une lecture par demande, promesse, responsabilité, fulfillment, source de décision et bon niveau de commun.

En transverse, FLOW demande aussi de séparer deux réflexes : pour l'information au repos, identifier la source de référence ; pour l'information en transit, définir le contrat d'échange.

À relier en priorité à la [note de choix stratégique](../vision/note-choix-strategique.md) et au hotspot [C-LOG : une décision de fulfillment déjà distribuée](../hotspots/c-log-decision-fulfillment.md).
