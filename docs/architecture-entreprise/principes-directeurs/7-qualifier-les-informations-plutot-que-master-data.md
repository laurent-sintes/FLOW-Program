# Principe 7 — Qualifier les informations plutôt que parler de Master Data

## Intention

FLOW ne doit pas reprendre sans recul la notion ERP de `Master Data`.

Cette notion a une histoire utile, mais elle est devenue trop ambiguë pour concevoir une plateforme distribuée comme FLOW.

Dans un ERP, `Master Data` désigne souvent les objets stables qui donnent du contexte aux transactions : client, fournisseur, article, site, emplacement, condition, centre de coût ou compte comptable.

Dans une démarche de Master Data Management, le même terme renvoie plutôt à des processus de mise en qualité, de déduplication, de consolidation, de gouvernance et de diffusion d'informations partagées.

Dans FLOW, ces deux lectures ne suffisent pas.

Le programme doit qualifier les informations selon plusieurs dimensions explicites, plutôt que les enfermer dans une catégorie unique appelée `Master Data`.

## Principe

> FLOW ne classe pas les informations en `Master Data` par héritage ERP.
>
> FLOW qualifie chaque information selon sa nature, sa gouvernance au repos, son mode d'échange, sa granularité d'échange et sa source faisant foi pour un usage donné.

Ce principe permet de concevoir la plateforme autour de la cohérence opérationnelle, et non autour d'une taxonomie héritée d'un progiciel.

## D'où vient la notion de Master Data ?

Historiquement, la notion vient de l'informatique de gestion batch et de la distinction entre `master file` et `transaction file`.

```text
Master file
    → fichier principal, relativement stable
    → contient les enregistrements nécessaires au traitement

Transaction file
    → fichier des mouvements ou opérations
    → vient utiliser ou mettre à jour le master file
```

Dans cette lecture historique, les master data sont les données principales qui décrivent les entités métier utilisées par les transactions.

Par exemple :

```text
Customer master file
    → client, adresse, conditions, statut

Transaction file
    → commandes, paiements, retours
```

Cette distinction était utile dans des systèmes structurés autour de traitements batch, de fichiers principaux et de mouvements.

Elle devient cependant insuffisante dans un SI distribué, événementiel, composé de domaines, de plateformes, d'applications spécialisées et de projections multiples.

## Ce que SAP a popularisé

SAP n'a pas inventé la notion de Master Data, mais l'a rendue très visible dans les projets ERP.

Dans SAP, les master data sont des objets stables du modèle applicatif qui contextualisent les transactions.

Exemples typiques :

```text
Material
Customer
Vendor
Business Partner
Plant
Storage Location
Condition Record
Cost Center
G/L Account
```

Cette approche est cohérente dans un ERP, car le progiciel impose un modèle intégré dans lequel les transactions s'appuient sur des objets structurants.

Mais pour FLOW, cette catégorie devient trop large.

Elle mélange :

- des entités métier ;
- des lieux ;
- des structures organisationnelles ;
- des conditions commerciales ;
- des objets de configuration ;
- des référentiels ;
- des informations utilisées pour décider ;
- des éléments qui n'ont pas la même temporalité, la même gouvernance ni le même mode d'échange.

Le risque est alors de déplacer dans FLOW le fourre-tout ERP sans clarifier les responsabilités réelles.

## Master Data Management n'a pas le même sens

Le Master Data Management ne désigne pas seulement une catégorie de données.

Il désigne une discipline et des processus permettant de rendre certaines informations cohérentes, fiables, gouvernées et réutilisables dans plusieurs systèmes.

Il traite notamment de :

- qualité ;
- déduplication ;
- consolidation ;
- rapprochement ;
- stewardship ;
- diffusion ;
- gouvernance ;
- source de vérité ;
- version ou enregistrement de référence.

Cette discipline reste utile pour FLOW.

Mais elle ne suffit pas à définir les types d'informations manipulées par la plateforme.

FLOW doit donc distinguer :

```text
Master Data au sens ERP
    → catégorie applicative d'un progiciel

Master Data Management
    → discipline de qualité, gouvernance et diffusion

Qualification des informations FLOW
    → modèle multi-dimensions pour concevoir la plateforme
```

## Définition de base : information

Dans FLOW, une information est une donnée structurée suffisamment complète pour porter un sens métier.

Si on la découpe davantage, on perd le sens utile pour le métier, la décision ou le système.

Exemples :

```text
Stock disponible
Produit demandé
Décision d'allocation
Événement de retard d'expédition
Document de livraison
Vue 360 d'un Case
```

Une quantité seule, un code isolé ou un libellé peuvent être des attributs.

Ils ne constituent pas toujours une information métier complète.

## Dimension 1 — Nature d'information

La nature d'information est une catégorie qui induit un comportement commun à toutes les informations associées.

FLOW distingue au minimum les natures suivantes.

| Nature | Définition | Comportement attendu |
| --- | --- | --- |
| Objet métier / Aggregate Root | Entité métier portant une identité, un cycle de vie et des invariants | Gouverné, versionnable selon les cas, producteur d'événements |
| Événement | Signal indiquant qu'un fait ou un état significatif a changé | Immuable, historisé, consommable par d'autres domaines |
| Fait | Réalité métier observée ou calculée à un instant donné | Utilisé pour constater, décider ou expliquer |
| Décision | Choix explicite pris à partir d'un contexte, de faits et de règles | Traçable, explicable, susceptible de créer un engagement ou une action |
| Document | Pièce ou preuve métier, opérationnelle, financière ou réglementaire | Reçu, généré, attaché, validé, conservé ou transmis |
| Vue | Agrégation de plusieurs informations accessible en lecture seule | Consultable, exposable, reconstruite ou dérivée selon les besoins |
| Configuration | Paramètre ou structure qui influence le comportement du système | Gouvernée, contrôlée, versionnée ou auditée selon criticité |

Cette liste ne cherche pas à reproduire les catégories ERP.

Elle cherche à identifier les comportements de conception : ce qui se modifie, ce qui se publie, ce qui se calcule, ce qui se décide, ce qui se prouve, ce qui se consulte et ce qui paramètre.

## Dimension 2 — Gouvernance au repos

La gouvernance au repos décrit comment une information est maîtrisée dans un domaine.

Elle ne décrit pas la nature de l'information.

Une même nature peut être self managed, imported ou derived selon le domaine qui la manipule.

| Gouvernance au repos | Définition |
| --- | --- |
| Self Managed | L'information est gérée par le domaine qui en est responsable. Le domaine maîtrise son cycle de vie, sa qualité, ses règles de modification et son exposition. |
| Imported | L'information est ingérée depuis une source externe. Le domaine consommateur peut la stocker, la contrôler ou la projeter, mais il n'en est pas le maître. |
| Derived | L'information est produite à partir d'autres informations par calcul, règle, agrégation ou transformation. Le domaine est responsable de la méthode de dérivation. |

Exemples :

| Information | Nature | Gouvernance dans FLOW |
| --- | --- | --- |
| Case | Objet métier | Self Managed |
| Product execution view | Vue | Imported |
| Stock position source | Fait | Imported ou Self Managed selon la source |
| Available stock | Fait | Derived |
| Promise date | Décision ou fait dérivé selon le modèle | Derived puis éventuellement Self Managed |
| Allocation decision | Décision | Self Managed |
| ShipmentDelayed | Événement | Imported |
| Case timeline | Vue | Derived |
| Packing list | Document | Imported |

Cette distinction est essentielle.

FLOW peut ne pas être maître du produit, du client ou du stock physique, tout en étant responsable de la disponibilité calculée, de la promesse, de l'allocation ou de l'explication de décision.

## Dimension 3 — Mode d'échange

Le mode d'échange décrit comment une information circule entre domaines ou systèmes.

Il ne doit pas être confondu avec la gouvernance.

| Mode d'échange | Définition |
| --- | --- |
| Event | Un domaine informe qu'un changement significatif s'est produit. |
| Query | Un domaine interroge un autre domaine pour obtenir une information ou une vue. |
| Command | Un domaine demande explicitement à un autre de réaliser une action. |
| Synchronization | Un domaine maintient une projection alignée avec une source ou un ensemble de sources. |
| Stream | Un domaine diffuse un flux continu d'observations, d'événements ou de mesures. |

`Pub/Sub` est un mécanisme possible pour transporter des événements ou des flux.

Ce n'est pas, en soi, une catégorie métier d'information.

Exemples :

```text
ShipmentDelayed
    → Nature : Événement
    → Mode d'échange : Event

Product execution view
    → Nature : Vue
    → Mode d'échange : Synchronization ou Query

ReserveStock
    → Mode d'échange : Command

Stock movements
    → Mode d'échange : Stream
```

## Dimension 4 — Granularité d'échange

La granularité d'échange décrit la quantité ou l'échelle de l'information échangée.

FLOW distingue au minimum :

| Granularité | Définition |
| --- | --- |
| Unitaire | Échange ciblé autour d'un objet, d'une demande, d'une décision ou d'une action précise. |
| Masse | Échange portant sur un ensemble d'informations, souvent pour synchroniser, charger, recalculer ou alimenter une projection. |

Une même information peut circuler dans les deux granularités selon l'interface.

Exemples :

```text
Product execution view
    → Synchronization / Masse
    → Query / Unitaire

Stock position
    → Event ou Stream / Unitaire
    → Synchronization / Masse

Allocation
    → Command / Unitaire
    → Command ou traitement de recalcul / Masse
```

Cette dimension prépare la conception future des interfaces.

Elle évite de dire seulement :

> Il faut une API stock.

Elle oblige à préciser :

```text
Quelle information stock ?
Quelle nature ?
Quelle gouvernance au repos ?
Quel mode d'échange ?
Quelle granularité ?
Pour quel usage ?
```

## Dimension 5 — Source faisant foi pour un usage donné

Dans un SI distribué, une information peut être accessible depuis plusieurs sources.

Ces sources ne portent pas nécessairement la même profondeur, la même fraîcheur, la même finalité ni la même responsabilité.

La question n'est donc plus :

> Où est la Master Data ?

La question devient :

> Pour ce consommateur, cet usage et cette décision, quelle source fait foi ?

La source faisant foi est contextuelle.

Elle dépend de l'usage.

Exemple produit :

| Usage | Source faisant foi possible |
| --- | --- |
| Conception produit | PLM |
| Contenu enrichi client | PIM |
| Recherche et navigation | Elastic ou plateforme commerce |
| Fulfillment | Product execution view consommée par FLOW |
| Facturation ou comptabilité | ERP / Finance |

Exemple stock :

| Usage | Source faisant foi possible |
| --- | --- |
| Stock physique entrepôt | WMS ou ERP selon le modèle |
| Stock magasin | Système magasin ou back-office retail |
| Stock disponible pour promesse | FLOW Inventory Visibility |
| Stock comptable | ERP / Finance |
| Stock affiché au client | Projection commerce alimentée par FLOW ou une autre source autoritative |

Une information n'est donc pas maître de manière absolue.

Elle fait autorité pour un usage, un consommateur, une décision ou un contexte donné.

## Conséquences pour FLOW

Ce principe conduit FLOW à :

- abandonner la question générique `est-ce de la Master Data ?` ;
- qualifier chaque information selon plusieurs dimensions indépendantes ;
- distinguer la nature de l'information de sa gouvernance ;
- distinguer la gouvernance au repos du mode d'échange ;
- distinguer la source de création de la source faisant foi pour un usage ;
- éviter de transformer FLOW en méga-MDM ;
- éviter d'importer dans FLOW le modèle SAP sans le challenger ;
- concevoir les interfaces à partir des informations, de leurs usages et de leurs modes d'échange ;
- permettre à FLOW de produire des informations derived comme la disponibilité, la promesse ou l'allocation sans devenir maître de toutes les sources.

## Matrice de qualification

Pour chaque information importante, FLOW devrait pouvoir renseigner une matrice simple.

| Question | Exemple de réponse |
| --- | --- |
| Quelle information ? | Available stock |
| Quelle nature ? | Fait |
| Quelle gouvernance au repos dans FLOW ? | Derived |
| Quel mode d'échange ? | Query, Event, Stream ou Synchronization selon le cas |
| Quelle granularité ? | Unitaire ou masse |
| Quelle source fait foi pour l'usage ? | FLOW Inventory Visibility pour la promesse |
| Quel consommateur ? | Case Management, commerce, service client, reporting |
| Quelle décision ou action sert-elle ? | Promettre, allouer, substituer, réorienter |

Cette matrice permet de passer d'un vocabulaire vague à une conception explicite.

## À retenir

FLOW ne remplace pas `Master Data` par une autre catégorie unique.

FLOW qualifie les informations.

La plateforme doit savoir dire :

```text
Ce que l'information représente
Comment elle se comporte
Qui la gouverne au repos
Comment elle circule
À quelle granularité elle circule
Quelle source fait foi pour quel usage
Quelle décision ou action elle sert
```

Ce principe complète le principe sur la demande comme objet métier central.

La demande répond à la question :

> Par quoi commence le modèle ?

La qualification des informations répond à la question :

> Comment organiser les informations autour de ce modèle sans retomber dans le fourre-tout Master Data ?
