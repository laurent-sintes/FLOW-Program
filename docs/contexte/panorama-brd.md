# Panorama applicatif BRD

## Intention

Cette page documente l'environnement IT de Boardriders tel qu'il apparaît dans les éléments de travail du projet et dans les échanges d'urbanisme.

Les éléments analysés ici ne décrivent que BRD.

Ils doivent donc être lus comme un panorama spécifique de l'existant BRD, et non comme une comparaison avec GBM.

## Point de départ du projet

Un entrant du projet doit d'abord comprendre le point de départ concret : FLOW est envisagé comme le remplacement de SAP et NewStore sur le périmètre BRD.

La question ouverte n'est donc pas seulement :

> Que doit être FLOW ?

La question initiale est aussi :

> Si FLOW remplace SAP et NewStore, doit-il remplacer autre chose également ?

Cette question oblige à regarder l'environnement applicatif BRD dans son ensemble.

SAP et NewStore ne sont pas isolés. Ils sont connectés à des solutions de planification, de produit, de commerce, de logistique, de stock, de finance, de pilotage et de collaboration fournisseur.

Comprendre BRD consiste donc à identifier :

- ce qui relève directement de SAP ;
- ce qui relève de NewStore ;
- ce qui gravite autour de ces deux socles ;
- ce qui pourrait être repris par FLOW ;
- ce qui doit rester hors FLOW.

## Une lecture déjà urbanisée du SI BRD

La vue d'urbanisme BRD analysée ne présente pas seulement des applications isolées.

Les applications y sont placées dans des blocs qui s'apparentent à une lecture d'urbanisme : le SI est représenté selon des zones, des responsabilités ou des ensembles cohérents.

Les blocs visibles sont les suivants :

| Bloc BRD | Applications / composants visibles |
| --- | --- |
| Sourcing | SNC, Fast |
| PLM / Planning | PLM, BPC, Optimate |
| Achat / Stock | SAP |
| E-commerce & B2B | Salesforce, Elastic, CMS / Web platform |
| Sustainability | DTT |
| WMS | KTN BE, C-Logistics, Bleckmann UK, FMS FR |
| Douanes | Connex |
| Cegid Y2 | Cegid Y2 |

Cette observation est importante pour FLOW.

Elle montre que BRD dispose déjà d'une manière de structurer et de raconter son système d'information. Cette manière de voir peut être très utile, mais elle ne doit pas être confondue avec une grille commune à tout le programme.

La lecture BRD mélange naturellement plusieurs types de blocs : des domaines métier, des zones fonctionnelles, des familles applicatives, des partenaires d'exécution et des progiciels structurants. Ce n'est pas un défaut ; c'est souvent ainsi qu'un SI réel est représenté par les équipes qui le pilotent.

Mais pour FLOW, cette lecture doit être traduite dans un urbanisme unifié.

Un point attire particulièrement l'attention : Cegid Y2, qui porte le back-office centralisé des stores retail et le stock magasin, apparaît comme un élément isolé, sans être clairement rattaché à une case d'urbanisme comparable aux autres.

C'est une anomalie de lecture intéressante.

Cegid n'est pas un simple système périphérique : il porte une responsabilité structurante pour le retail, les magasins et la disponibilité de stock. Son positionnement devrait donc être explicité dans un bloc de type `Retail / Store Operations` ou `Store Back-office & Store Inventory`.

Cette situation illustre bien la limite de la lecture actuelle : certains blocs sont des domaines, certains sont des systèmes, certains sont des partenaires ou des zones d'exécution. FLOW devra rendre ces positionnements comparables.

FLOW devra redéfinir un urbanisme commun, capable de rendre comparables les positionnements applicatifs BRD et GBM.

Autrement dit, il faudra pouvoir répondre aux questions suivantes avec les mêmes critères pour les deux groupes :

- dans quel domaine se situe une application ?
- quelle responsabilité porte-t-elle réellement ?
- quelle capacité métier sert-elle ?
- est-elle remplacée, conservée, connectée, encapsulée ou laissée hors périmètre ?
- quelle différence existe entre son positionnement actuel et son positionnement cible ?

Cette grille commune est nécessaire pour éviter que chaque groupe décrive son SI avec ses propres catégories, ce qui rendrait les comparaisons fragiles.

Le schéma suivant est une synthèse FLOW produite à partir de cette lecture. Il vise à rendre le panorama plus lisible dans le site.

## Synthèse visuelle de l'écosystème BRD

![Synthèse de l'écosystème applicatif BRD](../assets/images/panorama-brd-ecosystem.svg)

## Lecture globale

Le panorama BRD peut être lu selon un enchaînement de grandes responsabilités :

```text
PLAN
    ↓
DESIGN
    ↓
SOURCE
    ↓
SALES
    ↓
DELIVER / RETURN
    ↓
BILLING
```

La lecture distingue aussi deux temporalités :

```text
Long term / Plan oriented
Short term / Flux oriented
```

Cette distinction est importante pour FLOW.

BRD ne présente pas seulement une chaîne transactionnelle. Le paysage fait apparaître une tension entre planification long terme, pilotage court terme, flux opérationnels, allocation, promesse et exécution.

## Socle SAP

SAP constitue le cœur transactionnel de BRD.

Les modules et périmètres explicitement mentionnés sont :

- SAP MM — Material Management ;
- SAP SD — Sales & Distribution ;
- SAP FI/CO — finance, comptabilité et contrôle de gestion ;
- SAP AFS — Apparel and Footwear Solution ;
- Logistics ;
- Billing ;
- Inventory.

SAP porte notamment :

- les achats ;
- les commandes ;
- le stock entrepôt ;
- la distribution ;
- la facturation ;
- la finance ;
- une partie des règles et traitements liés à l'allocation.

SAP ne porte donc pas, à lui seul, toute la réalité du stock BRD. Dans le panorama actuel, SAP contient le stock entrepôt, tandis que le stock magasin est porté par Cegid.

Dans le point de départ du projet, SAP est explicitement dans le périmètre de remplacement envisagé par FLOW.

## NewStore / OMS

NewStore est présenté comme l'OMS de BRD.

Il intervient notamment sur :

- Sales Order ;
- cycle de vie des commandes ;
- précommandes ;
- multicanal ;
- retours ;
- transferts ;
- promesse ;
- allocation / réservation selon les flux ;
- intégration du stock entrepôt et du stock magasin.

NewStore agrège donc deux réalités de stock qui ne sont pas portées par la même source :

- SAP pour le stock entrepôt ;
- Cegid pour le stock magasin.

Dans le point de départ du projet, NewStore est également dans le périmètre de remplacement envisagé par FLOW.

La présence de NewStore aux côtés de SAP rend immédiatement visible une difficulté : le cycle de vie de la demande, la promesse, l'allocation, la vision de disponibilité et l'exécution ne sont pas naturellement contenus dans un seul système.

### Périmètre fonctionnel observé de NewStore

Le périmètre fonctionnel de NewStore dépasse une simple vision OMS centrée sur la commande.

Il couvre ou orchestre plusieurs responsabilités opérationnelles :

| Responsabilité | Fonctionnalités observées |
| --- | --- |
| Stock omnicanal | Gestion du stock e-commerce, marketplace et extension de gamme. |
| Annulation | Gestion des annulations en cas de rupture de stock et notification client. |
| Préparation | Choix du mode de préparation, dont Ship From Store, et règles d'affectation. |
| Ship From Store | Pick, pack, print label et gestion de l'extension de gamme. |
| Mouvements de stock | Déclenchement du mouvement de stock après confirmation d'expédition. |
| Suivi commande | Réception et transition du shipping, URL de tracking et suivi de statut. |
| Notifications client | Notifications liées aux statuts de commande. |
| Facturation | Déclenchement de la facturation via notification shipping vers SAP pour les SFS. |
| Entités fiscales | Split des commandes en fonction des entités fiscales, notamment Napali / Emerald. |
| Fidélité | Gestion de flux liés à Cegid et Salesforce. |
| SAV / litiges | Gestion des litiges, traitements SAV et remboursements. |
| Reporting IT | Notifications AWS Stream. |
| Paiement | Traitement ou déclenchement de capture et d'autorisation de paiement. |

Cette liste confirme que NewStore joue un rôle de colonne opérationnelle intermédiaire entre les canaux, le stock, l'exécution, le client, la finance et certains flux IT.

Pour FLOW, cela signifie que remplacer NewStore ne consiste pas seulement à reprendre une fonctionnalité de suivi commande.

Il faut arbitrer, responsabilité par responsabilité, ce qui relève demain :

- du Case Management et du cycle de vie de la demande ;
- du Stock Unifié ;
- du Réseau d'Exécution ;
- du Product Agreement Catalog ou des règles d'affectation ;
- des systèmes d'engagement ;
- des systèmes d'exécution logistique ;
- de SAP FI/CO ou d'un système finance ;
- d'un service de paiement ;
- d'un service de fidélité ;
- d'un module SAV.

<div class="flow-conviction">
  <p>NewStore ne matérialise pas seulement un OMS.</p>
  <p>Il matérialise une zone de responsabilités que FLOW devra redistribuer proprement entre Demand, Stock, Réseau d'Exécution, Finance et systèmes conservés.</p>
</div>

## Planification, produit et données

Le paysage BRD mentionne plusieurs solutions autour de la planification, du produit et des données :

- SAP BPC / EPM — Business Planning and Consolidation ;
- Optimate / APS — Advanced Planning System ;
- PLM Centric — Product Life Management ;
- PIM & DAM — Product Information Management et Digital Asset Management ;
- Elastic — exposition, recherche ou usages catalogue selon les contextes.

À noter : BRD dispose déjà d'un PIM.

Cette précision est importante pour le positionnement de FLOW. Si le PIM est alimenté par le PLM et soutient la création des assortiments, des commercial agreements, des prix ou des contenus destinés aux canaux, alors il relève plutôt d'une zone de type `Design de l'engagement` ou `Offer / Assortment / Commercial Design`.

Dans cette lecture, le PIM n'est pas dans FLOW. Il soutient un processus amont de conception, d'enrichissement et de publication de l'offre.

FLOW ne doit donc pas être conçu, par défaut, comme un nouveau PIM ou comme un remplacement naturel du PIM.

### Recommandation d'architecture — PIM et FLOW

La recommandation d'architecture est de sortir le PIM du périmètre fonctionnel de FLOW, tout en reconnaissant que FLOW a besoin d'une vue produit d'exécution.

Le PIM doit rester positionné comme un système de design, d'enrichissement et de publication de l'offre, lorsqu'il soutient les processus PLM, assortiment, commercial agreement, prix, contenu ou engagement client.

FLOW doit disposer, en revanche, d'un référentiel produit d'exécution : une projection plus statique, plus simple et gouvernée des données produit nécessaires au fulfillment.

Ce référentiel produit d'exécution ne soutient pas le processus de création produit, de construction d'assortiment ou de négociation commerciale. Il fournit à FLOW les informations minimales nécessaires pour instruire une demande, promettre, allouer, orchestrer et exécuter.

Cette projection peut être alimentée par le PLM, le PIM, le pricing ou d'autres sources de référence, mais elle ne doit pas conduire FLOW à absorber la responsabilité de conception de l'offre.

```text
PLM / PIM / Pricing
        ↓
Design de l'offre et de l'engagement
        ↓
Produit publiable / vendable
        ↓
Référentiel produit d'exécution
        ↓
FLOW
```

Cette recommandation évite deux dérives :

- faire de FLOW un PIM bis ;
- sous-estimer le besoin d'une donnée produit stable et exploitable par le fulfillment.

Ces composants ne sont pas nécessairement à remplacer par FLOW.

Ils constituent plutôt des systèmes contributeurs, sources ou consommateurs selon les capacités concernées.

Ils alimentent les décisions relatives aux produits, saisons, prévisions, demandes planifiées, articles, attributs, contenus et assets.

## Collaboration fournisseur et sourcing

La vue BRD mentionne également :

- SNC — Supply Network Collaboration ;
- Fast — qualité fournisseur ;
- Vendor ;
- Purchase Request ;
- Order ;
- Planned Request.

Ces éléments indiquent que la chaîne BRD ne commence pas à la commande client.

Elle s'appuie sur des demandes planifiées, des demandes d'achat, des commandes, des fournisseurs et des mécanismes de collaboration amont.

Pour FLOW, cela pose une question importante : certaines demandes à orchestrer peuvent être amont, et pas uniquement aval ou client.

## Commerce et canaux

Le panorama BRD mentionne plusieurs systèmes et canaux :

- Salesforce Commerce Cloud ;
- Cegid Y2 ;
- retail ;
- B2C ;
- B2B ;
- Sales Order ;
- Commands.

Ces éléments montrent que BRD opère plusieurs canaux et parcours de vente.

Cegid Y2 porte notamment le stock magasin. Cette responsabilité est importante, car elle signifie que la vision de disponibilité utilisée par l'omnicanal ne peut pas être obtenue uniquement à partir de SAP.

FLOW ne doit pas être pensé comme une plateforme d'expérience qui remplacerait tous les points de contact.

Les expériences et canaux peuvent rester consommateurs de capacités FLOW.

## Stock, allocation et promesse

La vue BRD mentionne plusieurs notions autour du stock :

- stock magasin ;
- stock entrepôt ;
- stock disponible ;
- stock disponible magasin ;
- stock disponible entrepôt ;
- allocation / réservation ;
- promesse ATP — Available To Promise.

Ce point est central.

Le stock disponible apparaît à plusieurs endroits du paysage, ce qui confirme qu'il ne s'agit pas d'une simple donnée locale.

Le stock BRD n'a pas une source unique :

- SAP contient le stock entrepôt ;
- Cegid contient le stock magasin ;
- NewStore intègre les deux pour construire une vision exploitable par les parcours omnicanaux, la promesse et certaines décisions d'allocation ou de réservation.

Cette précision est structurante pour FLOW.

Inventory Visibility ne doit donc pas être compris comme une simple extraction du stock SAP. La capacité doit qualifier l'origine du stock, sa fraîcheur, son niveau de disponibilité, son statut de réservation ou d'allocation, et son usage possible dans une décision de promesse.

La disponibilité est une capacité distribuée, alimentée par plusieurs systèmes et mobilisée par plusieurs décisions.

Pour FLOW, cela prépare deux capacités majeures :

- Inventory Visibility ;
- Allocation & Promise.

Si FLOW remplace NewStore, il faudra décider si FLOW reprend directement ce rôle d'intégration du stock entrepôt et du stock magasin, ou si cette responsabilité doit être portée par une capacité dédiée d'Inventory Visibility consommée par FLOW.

## Logistique et exécution

Le panorama BRD mentionne plusieurs acteurs et systèmes d'exécution :

- Maersk 4PL ;
- C-Log ;
- C-Logistics ;
- Bleckmann UK ;
- WMS ;
- TMS Connex ;
- KTN ;
- gestion douane.

Ces composants relèvent de l'exécution logistique, du transport, de la douane et des opérations physiques.

Ils ne doivent pas être automatiquement placés dans le périmètre FLOW.

La question est plutôt de savoir quels événements, statuts, faits et documents ils doivent échanger avec FLOW pour permettre le suivi du Case et la prise de décision.

## Pilotage et performance

Le paysage mentionne également :

- BI Tableau ;
- OPM — Operational Performance Management.

Ces outils contribuent à l'observation et au pilotage de la performance.

Ils peuvent consommer les faits, événements et historiques produits par FLOW, mais ne sont pas nécessairement remplacés par FLOW.

## Synthèse applicative

| Zone | Applications / composants BRD | Lecture FLOW |
| --- | --- | --- |
| Transactionnel | SAP MM, SD, FI/CO, AFS, Inventory, Billing | Périmètre de remplacement initial ; SAP porte notamment le stock entrepôt |
| OMS / commandes | NewStore | Périmètre de remplacement initial ; cycle de vie commande, annulation, préparation, SFS, promesse, allocation, intégration des stocks, notifications, SAV, paiement et déclenchement de facturation à analyser responsabilité par responsabilité |
| Planification | SAP BPC, Optimate / APS | Sources ou contributeurs de demandes planifiées |
| Produit / contenu | PLM Centric, PIM, DAM, Elastic | Systèmes contributeurs de données produit et contenus ; le PIM relève plutôt du design de l'offre / engagement et ne doit pas être remplacé par FLOW par défaut |
| Fournisseurs | SNC, Fast, Vendor | Collaboration et qualité fournisseur ; contribution au contexte amont |
| Commerce | Salesforce Commerce Cloud, Cegid Y2, B2C, B2B, retail | Expériences ou systèmes consommateurs ; Cegid porte le stock magasin |
| Stock / promesse | stock magasin, stock entrepôt, ATP, allocation / réservation | Capacités candidates FLOW : Inventory Visibility, Allocation & Promise ; la source du stock doit être explicitement qualifiée |
| Produit d'exécution | Référentiel produit d'exécution alimenté par PLM / PIM / Pricing selon arbitrage | Projection statique et gouvernée nécessaire à FLOW pour le fulfillment ; ne porte pas le processus de création ou d'enrichissement de l'offre |
| Logistique | Maersk 4PL, C-Log, Bleckmann, WMS, TMS Connex, KTN | Systèmes d'exécution et sources d'événements |
| Pilotage | BI Tableau / OPM, AWS Stream | Observation, reporting, performance et notifications IT |

## Questions structurantes pour FLOW

Le panorama BRD conduit à plusieurs questions :

- Si FLOW remplace SAP et NewStore, quelles responsabilités de SAP sont réellement reprises par FLOW ?
- Quelles responsabilités actuellement portées par NewStore doivent être reprises, redistribuées ou laissées à des systèmes spécialisés ?
- Quelles responsabilités doivent rester dans Finance, notamment FI/CO ?
- FLOW doit-il porter les décisions d'allocation, ou seulement les orchestrer ?
- Inventory Visibility doit-elle consolider les stocks magasin, entrepôt, réservés et futurs ?
- Si NewStore disparaît, quel composant reprend l'intégration entre stock entrepôt SAP et stock magasin Cegid ?
- Les règles d'affectation du mode de préparation, notamment SFS, relèvent-elles du Case, du Stock Unifié, du Réseau d'Exécution ou d'un service de décision transverse ?
- Les déclenchements de facturation, paiement, fidélité et remboursement doivent-ils être portés par FLOW, orchestrés par FLOW ou laissés à des services spécialisés ?
- Les outils de planification comme Optimate ou BPC alimentent-ils FLOW en demandes, prévisions ou faits ?
- Le PIM existant soutient-il principalement le design de l'offre, les assortiments, les commercial agreements, les prix et les canaux d'engagement client ?
- Quelles données produit doivent être projetées dans un référentiel produit d'exécution consommable par FLOW ?
- Les systèmes logistiques restent-ils seulement exécutants ou deviennent-ils aussi contributeurs d'événements métier ?
- Quels composants doivent être remplacés, conservés, encapsulés ou simplement connectés ?
- Quelle grille d'urbanisme commune permettra de comparer le positionnement des applications BRD et GBM ?
- Dans quelle zone d'urbanisme cible faut-il positionner Cegid Y2 : Retail / Store Operations, Store Back-office, Inventory Visibility, ou combinaison de ces responsabilités ?

## À retenir

BRD n'est pas seulement un paysage SAP.

BRD est un écosystème articulé autour de SAP et NewStore, avec de nombreuses solutions spécialisées.

La vue BRD montre aussi que BRD possède déjà une manière de représenter son SI par blocs : Sourcing, PLM / Planning, Achat / Stock, E-commerce & B2B, Sustainability, WMS, Douanes et Cegid Y2. FLOW devra conserver cette richesse de lecture, tout en la traduisant dans une grille d'urbanisme commune avec GBM.

Le positionnement de Cegid Y2 est particulièrement révélateur : il porte une responsabilité structurante pour les stores et le stock magasin, mais il n'est pas naturellement placé dans un bloc d'urbanisme homogène. C'est un signal concret du travail que FLOW doit mener : passer d'une lecture applicative historique à une lecture par responsabilités comparables.

Le point de départ de FLOW est bien le remplacement de SAP et NewStore, mais l'analyse du panorama montre que cette décision ouvre immédiatement une question plus large :

> Quelles capacités transverses faut-il reprendre dans FLOW, et quels systèmes doivent rester contributeurs, consommateurs ou exécutants ?

Le cas du stock l'illustre bien : SAP porte le stock entrepôt, Cegid porte le stock magasin, et NewStore intègre aujourd'hui les deux. Remplacer SAP et NewStore ne suffit donc pas à répondre mécaniquement à la question de la visibilité de stock ; il faut décider où sera portée demain la capacité d'Inventory Visibility.

Le périmètre observé de NewStore renforce ce constat : NewStore porte aujourd'hui des responsabilités qui touchent à la commande, au stock, au Ship From Store, à l'annulation, au SAV, à la notification client, au paiement, à la fidélité, au déclenchement de facturation et aux entités fiscales. FLOW devra donc reprendre ce périmètre par capacités, et non par simple duplication applicative.

Le cas du PIM va dans le même sens : BRD dispose déjà d'un système qui peut soutenir le design de l'offre, les assortiments, les commercial agreements, les prix et les contenus d'engagement client. La recommandation d'architecture est donc de ne pas intégrer le PIM dans FLOW par défaut.

FLOW a en revanche besoin d'un référentiel produit d'exécution : une projection produit statique, gouvernée et limitée aux données nécessaires au fulfillment. Cette projection permet à FLOW de promettre, allouer, orchestrer et exécuter sans absorber la responsabilité de conception et d'enrichissement de l'offre.