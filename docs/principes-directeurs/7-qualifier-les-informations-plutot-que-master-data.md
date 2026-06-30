# Principe 7 — Master Data : des objets maîtres aux sources gouvernées

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Sponsor</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>11 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

FLOW ne doit pas reprendre sans recul la notion ERP de `Master Data`.

Cette notion a une histoire utile, mais elle est devenue trop ambiguë pour concevoir une plateforme distribuée comme FLOW.

Le piège est de croire que le MDM consiste à lister les objets "maîtres" de l'entreprise.

La culture ERP conduit souvent les concepteurs à représenter l'entreprise comme un modèle complet : objets, attributs, tables de paramétrage, relations et cardinalités, comme si tout devait être stabilisé au même endroit.

Cette étape devient risquée si elle arrive trop tôt.

Avant la spécification détaillée, FLOW doit d'abord découper l'information en sources, identifier les responsabilités, déterminer les processus de contrôle et expliciter la gouvernance de ces sources.

Ce changement de pratique est central : on ne part plus d'un modèle unique à compléter, on part des responsabilités qui rendent une information fiable pour un usage donné.

Pour FLOW, faire du MDM consiste plutôt à identifier les sources de référence, les projections et les responsabilités de gouvernance qui rendent une information fiable pour un usage donné.

Cette gouvernance couvre deux situations complémentaires :

- les informations au repos : objets stables, politiques, facts, documents, nomenclatures ou projections maintenus dans un domaine ;
- les informations en circulation : commands, events, facts, documents ou vues publiés vers d'autres domaines sous contrat de données.

Une approche MDM utile ne commence donc pas par demander quelle liste d'objets doit être déclarée `Master Data`.

Elle commence par identifier quelles informations font référence, pour quel domaine, quel usage, quel niveau de qualité, quel processus de contrôle, quelles projections de consommation et quels contrats de circulation.

Dans un ERP, `Master Data` désigne souvent les objets stables qui donnent du contexte aux transactions : client, fournisseur, article, site, emplacement, condition, centre de coût ou compte comptable.

Dans une démarche de Master Data Management, le même terme renvoie plutôt à des processus de mise en qualité, de déduplication, de consolidation, de gouvernance et de diffusion d'informations partagées.

Dans FLOW, ces deux lectures ne suffisent pas.

Le programme doit qualifier les informations selon des dimensions explicites, simples et utilisables pour la cartographie fonctionnelle.

## Principe

> FLOW ne transforme pas le MDM en inventaire d'objets "maîtres".
>
> Faire du MDM, c'est identifier les sources de référence, les projections et les responsabilités de gouvernance qui rendent une information fiable pour un usage donné.
>
> FLOW ne classe pas les informations en `Master Data` par héritage ERP.
>
> FLOW qualifie chaque information selon sa nature et son statut dans le domaine : source de référence ou projection.
>
> Une information ne fait référence que pour un domaine, un usage, un consommateur ou une décision explicitement qualifiés.
>
> Lorsqu'elle circule, cette information doit être publiée, consommée, supervisée et réconciliée sous contrat de données.

Ce principe permet de concevoir la plateforme autour de la cohérence opérationnelle, et non autour d'une taxonomie héritée d'un progiciel.

Les dimensions plus techniques — mode d'échange, granularité unitaire ou masse, protocole, synchronisation, API ou événement — seront utiles plus tard pour concevoir les interfaces.

Elles ne doivent pas alourdir la première cartographie fonctionnelle.

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

- des objets métier ;
- des nomenclatures ;
- des documents ou références documentaires ;
- des politiques, règles et paramètres ;
- des faits utilisés pour décider ;
- des informations sources et des projections ;
- des éléments qui n'ont pas la même responsabilité dans l'architecture fonctionnelle.

Le risque est alors de déplacer dans FLOW le fourre-tout ERP sans clarifier les responsabilités réelles.

## Master Data Management n'a pas le même sens

Le Master Data Management ne désigne pas seulement une catégorie de données.

Il désigne une discipline et des processus permettant de rendre certaines informations cohérentes, fiables, gouvernées et réutilisables dans plusieurs systèmes.

Autrement dit, faire du MDM ne consiste pas seulement à décider que `Customer`, `Vendor`, `Article` ou `Plant` sont des master data.

La vraie question MDM est plus opérationnelle :

```text
Quelle information doit faire référence ?
Qui la crée, la valide ou la maintient ?
Pour quel usage fait-elle autorité ?
Quelle qualité minimale est garantie ?
Quelles projections peuvent la consommer sans devenir maîtres ?
```

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

Mais elle ne suffit pas à définir les natures d'information manipulées par la plateforme.

FLOW doit donc distinguer :

```text
Master Data au sens ERP
    → catégorie applicative d'un progiciel

Master Data Management
    → discipline de qualité, gouvernance, diffusion et contrats

Qualification des informations FLOW
    → nomenclature simple pour cartographier la plateforme

Contrat de données FLOW
    → règle durable de publication, consommation, fraîcheur, qualité et réconciliation
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
Nomenclature des statuts commande
```

Une quantité seule, un code isolé ou un libellé peuvent être des attributs.

Ils ne constituent pas toujours une information métier complète.

## Dimension 1 — Nature d'information

La nature d'information est une catégorie qui induit un comportement commun à toutes les informations associées.

Pour une première cartographie fonctionnelle, FLOW retient les natures suivantes.

| Nature | Définition | Comportement attendu |
| --- | --- | --- |
| Command | Intention adressée à un système ou domaine pour demander une action | Déclenche un traitement, peut être acceptée, refusée, mise en attente ou produire des événements |
| Event | Signal indiquant qu'un changement significatif s'est produit | Immuable, historisé, consommable par d'autres domaines |
| Fact | Réalité métier observée, reçue ou calculée à un instant donné | Utilisé pour constater, décider, promettre, allouer ou expliquer |
| Policy | Règle, politique, paramètre ou contrainte qui influence une décision ou un comportement | Gouvernée, versionnée ou contrôlée selon criticité ; appliquée par des décisions ou traitements |
| Objet métier | Objet portant une identité, un cycle de vie et la responsabilité de sa cohérence à chaque mise à jour | Gouverné par un domaine, protecteur de ses invariants, producteur d'événements |
| Document | Pièce, preuve ou artefact métier reçu, généré, attaché ou transmis | Conservé, référencé, validé, partagé ou transmis selon les obligations métier |
| Nomenclature | Ensemble contrôlé de valeurs, codes ou classifications partagés | Stabilise le vocabulaire, les statuts, les catégories ou les classifications utilisées par plusieurs domaines |

Cette liste ne cherche pas à reproduire les catégories ERP.

Elle cherche à identifier ce que l'information fait dans la cartographie fonctionnelle : commander, signaler, constater, orienter, porter un cycle de vie, prouver ou classifier.

## Dimension 2 — Statut dans le domaine : source de référence ou projection

La deuxième dimension décrit le statut de l'information dans un domaine donné.

FLOW retient volontairement deux statuts simples.

| Statut | Définition |
| --- | --- |
| Source de référence | Le domaine, l'application ou le service crée, valide ou maintient l'information comme référence pour son périmètre ou son usage, avec un processus de contrôle identifié. |
| Projection | Le domaine consomme une représentation issue d'une ou plusieurs sources de référence, adaptée à son usage. |

Une information peut être source de référence dans un domaine et projection dans un autre.

C'est cette distinction qui remplace utilement la question trop vague :

> Est-ce une master data ?

La bonne question devient :

> Dans ce domaine, cette information est-elle source de référence ou projection ?

Exemples :

| Information | Nature | Statut dans FLOW |
| --- | --- | --- |
| Case | Objet métier | Source de référence |
| Allocation command | Command | Source de référence |
| Allocation decided | Event | Source de référence |
| Allocation decision | Objet métier ou Fact selon le niveau de matérialisation | Source de référence |
| Available stock | Fact | Source de référence si FLOW le calcule et l'expose ; projection s'il le consomme d'un autre domaine |
| Product execution view | Objet métier représenté sous forme de projection | Projection |
| Customer / Party view | Objet métier représenté sous forme de projection | Projection |
| Commercial agreement view | Objet métier ou Policy selon l'usage | Projection |
| Return policy | Policy | Source de référence ou projection selon le domaine responsable |
| Packing list | Document | Projection dans FLOW si produite par CBS ou un fournisseur |
| Order status nomenclature | Nomenclature | Source de référence ou projection selon le domaine qui la gouverne |
| Shipment delayed | Event | Projection dans FLOW si produit par Transport |

Cette distinction est essentielle.

FLOW peut ne pas être source de référence du produit, du client ou d'un document fournisseur, tout en étant source de référence du Case, de certaines décisions, de certains événements et de certaines informations calculées comme la disponibilité ou la promesse.

## Source de référence pour un usage donné

Dans un SI distribué, une information peut être accessible depuis plusieurs sources.

Ces sources ne portent pas nécessairement la même profondeur, la même fraîcheur, la même finalité ni la même responsabilité.

La question n'est donc plus :

> Où est la Master Data ?

La question devient :

> Pour ce consommateur, cet usage et cette décision, quelle source de référence fait foi ?

La source de référence est contextuelle.

Elle dépend de l'usage.

Exemple produit :

| Usage | Source de référence possible |
| --- | --- |
| Conception produit | PLM |
| Contenu enrichi client | PIM |
| Recherche et navigation | Elastic ou plateforme commerce |
| Fulfillment | Projection produit d'exécution consommée par FLOW |
| Facturation ou comptabilité | ERP / Finance |

Exemple stock :

| Usage | Source de référence possible |
| --- | --- |
| Stock physique entrepôt | WMS ou ERP selon le modèle |
| Stock magasin | Système magasin ou back-office retail |
| Stock disponible pour promesse | FLOW Inventory Visibility, si FLOW calcule et expose cette information |
| Stock comptable | ERP / Finance |
| Stock affiché au client | Projection commerce alimentée par FLOW ou une autre source de référence |

Une information n'est donc pas maître de manière absolue.

Elle fait autorité pour un usage, un consommateur, une décision ou un contexte donné.

## Dimension 3 — Circulation sous contrat

Le MDM ne doit pas gouverner seulement les informations au repos.

Dans un SI distribué, une information devient souvent utile lorsqu'elle circule : un événement de stock, une décision d'allocation, une projection produit d'exécution, une nomenclature de statut ou un document fournisseur.

Une information en circulation n'est donc pas un simple flux technique.

C'est une information qualifiée qui quitte un domaine pour être consommée par un autre.

Elle doit conserver son contexte de gouvernance :

- quelle information est publiée ;
- quelle est sa nature : command, event, fact, policy, objet métier, document ou nomenclature ;
- le domaine qui la publie est-il source de référence ou projection ;
- quelle source de référence fait foi pour l'usage ;
- quels consommateurs sont connus ;
- quel mode d'échange est utilisé : event, API, query, synchronisation, stream ou batch ;
- quelle granularité est attendue : unitaire ou masse ;
- quelle fraîcheur est promise ;
- quelle qualité minimale est garantie ;
- quels mécanismes de supervision, reprise et réconciliation sont prévus.

Le contrat de données est l'objet de gouvernance qui porte ces engagements.

Il prolonge la qualification source de référence / projection dans la circulation entre domaines.

```text
Information au repos
    → nature
    → source de référence ou projection
    → usage et qualité

Information en circulation
    → contrat de données
    → mode d'échange
    → consommateurs
    → fraîcheur et qualité promises
    → supervision, reprise, réconciliation
```

Ces dimensions ne doivent pas être confondues avec la nature de l'information.

Par exemple, `Command` est une nature utile dans la cartographie fonctionnelle, mais `Command` peut aussi devenir un mode d'échange dans la conception d'interface.

Le même mot peut donc être utilisé à deux niveaux différents, à condition d'expliciter le niveau d'analyse.

Le produit d'architecture [Gouvernance des données en transit](../architecture-cible/produits/gouvernance-donnees-transit.md) détaille cette responsabilité cible.

L'overview de la plateforme applique aussi la nomenclature `command`, `event`, `fact`, `policy`, objet métier, document et nomenclature aux produits FLOW dans la section [Nomenclature d'information appliquée](../architecture-cible/overview-plateforme-flow.md#nomenclature-dinformation-appliquee).

## Conséquences pour FLOW

Ce principe conduit FLOW à :

- abandonner la question générique `est-ce de la Master Data ?` ;
- éviter le piège `MDM = inventaire des objets "maîtres" de l'entreprise` ;
- qualifier chaque information selon sa nature ;
- qualifier chaque information comme source de référence ou projection dans un domaine donné ;
- éviter de transformer FLOW en méga-MDM ;
- éviter d'importer dans FLOW le modèle SAP sans le challenger ;
- distinguer ce que FLOW contrôle comme source de référence de ce qu'il consomme sous forme de projection ;
- contractualiser les informations qui circulent entre domaines ;
- distinguer publication et consommation ;
- expliciter les consommateurs, la fraîcheur, la qualité, la supervision, la reprise et la réconciliation ;
- permettre à FLOW de produire des facts, events, commands ou objets métier sans devenir source de référence de toutes les informations du SI.

## Matrice de qualification

Pour chaque information importante, FLOW devrait pouvoir renseigner une matrice simple.

| Question | Exemple de réponse |
| --- | --- |
| Quelle information ? | Available stock |
| Quelle nature ? | Fact |
| Dans FLOW, est-ce une source de référence ou une projection ? | Source de référence si FLOW calcule et expose l'information |
| Quelle source de référence fait foi pour l'usage ? | FLOW Inventory Visibility pour la promesse |
| Quel consommateur ? | Case Management, commerce, service client, reporting |
| Quelle décision ou action sert-elle ? | Promettre, allouer, substituer, réorienter |
| Circule-t-elle vers d'autres domaines ? | Oui, vers commerce et service client |
| Quel contrat de données la gouverne ? | Contrat `AvailableStockPublished` avec fraîcheur, qualité, consommateurs et réconciliation |

Cette matrice permet de passer d'un vocabulaire vague à une conception explicite.

## À retenir

FLOW ne remplace pas `Master Data` par une autre catégorie unique.

FLOW évite le piège `MDM = inventaire des objets "maîtres" de l'entreprise`.

FLOW qualifie les informations avec quatre questions simples pour la cartographie fonctionnelle :

```text
Quelle est la nature de cette information ?
Dans ce domaine, est-elle source de référence ou projection ?
Pour quel usage cette source fait-elle autorité ?
Si elle circule, quel contrat de données la gouverne ?
```

Ce principe complète le principe sur la demande comme objet métier central.

La demande répond à la question :

> Par quoi commence le modèle ?

La qualification des informations répond à la question :

> Comment organiser les informations autour de ce modèle sans retomber dans le fourre-tout Master Data ?

Le pattern [Sources de référence, projections et vues](../architecture-cible/patterns/sources-reference-projections-vues.md) détaille cette méthode de cartographie.

Il explicite aussi les références MDM associées : `System of Record`, `Source of Record`, `Golden Record`, Master Data Management, DAMA-DMBOK et ISO 8000.
