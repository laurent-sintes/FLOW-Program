# Overview de la plateforme FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Développeur, Delivery</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>8 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page propose un premier overview de la plateforme FLOW.

Elle ne cherche pas encore à détailler les flux, les APIs ou les choix techniques.

Elle cherche d'abord à montrer comment la vision de convergence peut se traduire en produits fonctionnels.

Le point de départ n'est pas : “quelle plateforme voulons-nous construire ?”.

Le point de départ est :

> Quelles responsabilités doivent devenir communes, gouvernées et transverses pour permettre la convergence, sans centraliser tout le SI ?

FLOW est ici décrit comme une plateforme Demand fédérée.

Elle est centrée sur les Cases, enrichie par des services partagés et des projections opérationnelles.

## Périmètre fonctionnel : quatre domaines

Le positionnement de FLOW se lit à travers quatre domaines.

![Positionnement de FLOW entre Engagement, Demand, Fulfillment et Supply](../assets/images/positionnement-flow-4-domaines.svg)

En lecture d'architecture fonctionnelle :

- <span class="flow-keyword">Engagement</span> capte l'intention et porte les parcours, interfaces, canaux et négociations.
- <span class="flow-keyword">Demand</span> qualifie la demande, porte le Case, le contexte, les statuts et la promesse à tenir.
- <span class="flow-keyword">Fulfillment</span> arbitre la promesse tenable, l'allocation, le sourcing, la priorisation et la trajectoire d'exécution.
- <span class="flow-keyword">Supply</span> expose les ressources, capacités, contraintes, SLA et événements d'exécution.

Le périmètre cœur de FLOW est <span class="flow-keyword">Demand + Fulfillment</span>.

Engagement et Supply restent adhérents : ils conservent leur autonomie, mais doivent être raccordés par des APIs, événements, statuts, projections, règles d'interaction et contrats de données.

## Deux niveaux de lecture du fonctionnement

Le "comment ça marche" doit rester lisible à deux niveaux.

Au niveau Vision, on explique le modèle mental : intention, Case, fait, événement, règle, décision, promesse, plan d'exécution et retours d'information.

Au niveau Architecture cible, on montre comment ces notions traversent les produits FLOW, les fonctionnalités attendues et les contrats d'information.

→ Niveau vision : [Modèle de fonctionnement de FLOW](../vision/modele-fonctionnement-flow.md).

→ Niveau architecture : [Flux fonctionnels FLOW](flux-fonctionnels-flow.md).

## Chronologie fonctionnelle

Le fonctionnement de FLOW doit aussi être lu dans le temps.

![Chronologie Engagement vers FLOW vers Supply](../assets/images/chronologie-engagement-supply-flow.svg)

Cette chronologie montre le cycle fonctionnel minimal :

- Engagement crée ou actualise une intention.
- FLOW porte la demande dans un Case.
- Demand enrichit la demande avec contexte, Agreement, priorité et promesse attendue.
- Fulfillment applique les règles, interroge les ressources et décide une promesse tenable.
- Supply exécute ou confirme selon le plan.
- Les faits, statuts et événements remontent vers FLOW.
- Le Case reste à jour et peut être réarbitré en cas d'exception.

→ Pour la lecture pédagogique complète, voir : [Modèle de fonctionnement de FLOW](../vision/modele-fonctionnement-flow.md).

## Schéma d'overview

![Overview de la plateforme FLOW](../assets/images/architecture-cible-flow-overview.svg)

## Produits FLOW à instruire

| Produit | Rôle |
| --- | --- |
| Plateforme de Case Management | Piloter les demandes dans la durée. Les Cases portent le contexte, les décisions métier, les promesses, les documents et les événements. |
| Stock Unifié | Rendre la disponibilité fiable et exploitable. Porter les réservations, l'allocation / tagging, les facts et événements stock. |
| Fulfillment Network / Réseau d'Exécution | Décrire les nœuds logistiques, partenaires, capacités, contraintes, services et conditions d'usage mobilisables pour servir une demande. |
| Supply Service Registry | Référencer les services Supply exposés : APIs, SLA, conditions d'accès, éligibilités et contraintes. |
| Product Agreement Catalog | Exposer les produits, assortiments et agreements utiles à la vente, à l'achat et à l'exécution. |
| Vues 360 | Agréger le contexte transverse autour du client, du fournisseur ou du Case. |

La gouvernance des données en transit reste une pratique transverse importante : elle encadre les contrats de données, les modes d'échange, les consommateurs, la fraîcheur, la qualité, la supervision et la réconciliation.

Elle n'est pas représentée comme un produit FLOW à instruire dans ce schéma.

## Logique de découpage des produits FLOW

Le découpage ne cherche pas à reproduire les grands blocs applicatifs existants.

Il isole les responsabilités qui doivent être gouvernées pour que FLOW puisse décider vite, expliquer ses décisions, promettre correctement et dialoguer avec les domaines d'exécution.

| Produit | Justification du découpage |
| --- | --- |
| Plateforme de Case Management | Ce n'est pas seulement une application de suivi. C'est un socle orienté PaaS : services techniques, runtime métier et framework de développement permettant aux équipes de construire en autonomie des Cases, règles, paramétrages, événements et extensions gouvernées. |
| Stock Unifié | Ce n'est pas seulement une consolidation de quantités. C'est une capacité d'Inventory Visibility enrichie de services d'action : réserver, allouer, taguer ou libérer du stock. Ces actions doivent ensuite produire des commandes ou instructions vers la logistique, les magasins ou les systèmes d'exécution qui prennent physiquement en compte l'information. |
| Fulfillment Network Configuration | Ce produit ne représente pas l'entreprise dans son ensemble. Il configure les nœuds, capacités, contraintes et services de la supply chain mobilisables pour répondre au fulfillment. La finance et les structures juridiques ne pilotent pas ce modèle : elles restent dans leur domaine. C'est une rupture avec l'ERP, où l'on paramètre souvent l'entreprise complète avant de développer les services. |
| Vues 360 | Aujourd'hui, les utilisateurs doivent souvent ouvrir plusieurs applications pour comprendre un client, une commande, un fournisseur, une usine ou une exception. Comme le Case Management devient un hub de Business Events et que FLOW porte des Shared Business Services transverses, les vues matérialisées 360 ont naturellement leur place dans FLOW. |
| Product Agreement Catalog | FLOW ne doit pas appeler le PLM, le PIM ou les outils de prix à chaque décision. La promesse croise produit, stock, agreement et réseau d'exécution ; elle doit pouvoir répondre en temps court, souvent en moins de 100 ms. Le catalogue est donc une projection d'exécution gouvernée, pensée pour la décision, pas un nouveau PLM ou PIM. |
| Supply Service Registry | Ce n'est pas seulement un catalogue d'APIs Supply réutilisables. Le registry doit décrire aussi les SLA, conditions d'appel, contraintes, éligibilités et engagements opérationnels de service du monde réel afin que les promesses FLOW restent compatibles avec ce que Supply peut réellement tenir. |

La conséquence est importante : FLOW ne remplace pas les domaines existants par un nouveau monolithe.

FLOW compose des produits de décision, de projection et de configuration qui rendent les responsabilités explicites, tout en laissant Engagement, Supply, Finance, PLM, PIM, WMS, POS ou partenaires porter leurs responsabilités propres.

## Lecture fonctionnelle

FLOW ne doit pas être lu comme un ERP, un OMS unique, un PIM, un CRM, un WMS ou un outil Finance.

FLOW doit être lu comme une plateforme de cohérence Demand.

Sa responsabilité est de rendre possible l'instruction, la décision métier, la promesse et l'orchestration de demandes transverses.

```text
Case
    → porte la demande dans la durée

Stock Unifié
    → fournit les facts stock et les réservations nécessaires

Fulfillment Network / Réseau d'Exécution
    → décrit les nœuds, capacités, contraintes et conditions d'usage mobilisables

Supply Service Registry
    → décrit les services Supply appelables

Product Agreement Catalog
    → donne le contexte produit / agreement nécessaire

Vues 360
    → donnent du contexte transverse et sont enrichies par les événements des Cases
```

## Colonne vertébrale du SI

FLOW réécrit la <span class="flow-keyword">colonne vertébrale opérationnelle</span> du SI.

Cela signifie qu'il porte les responsabilités qui doivent rester cohérentes à l'échelle du groupe : demandes, décisions métier, statuts, événements, stock, promesses, allocations, besoins d'exécution et vues transverses.

Cela ne signifie pas que tous les services existants doivent être réécrits.

Une bonne cible FLOW doit permettre de réintégrer des applications ou services existants lorsque leur valeur métier justifie leur maintien.

```text
Services spécialisés existants
    → CBS
    → SAV Client Sarenza
    → outils fournisseurs
    → systèmes logistiques spécialisés
    → domaines d'exécution ou de conformité

FLOW
    → colonne vertébrale Demand
    → cohérence des demandes, statuts, décisions métier, événements et projections
```

Ces services peuvent rester autour de FLOW comme consommateurs, contributeurs, sources d'événements ou domaines spécialisés.

La règle d'urbanisme est donc : ne pas réécrire ce qui porte une valeur métier spécifique, mais ne pas laisser ces services recréer chacun leur propre colonne vertébrale.

## Données en transit : des flux projet aux contrats gouvernés

FLOW doit aussi traiter la manière dont les informations circulent entre applications.

Aujourd'hui, beaucoup d'échanges naissent comme des flux projet : une application cible exprime un besoin, une application source est analysée, puis une équipe flux développe un batch ou une intégration spécifique.

Cette logique répond à des besoins concrets, mais elle produit un foisonnement de flux difficile à gouverner dans la durée.

L'architecture cible doit donc distinguer la publication d'une information de sa consommation.

L'idée de demi-flux déjà imaginée côté Beaumanoir constitue une première graine : elle sort du flux point-à-point et prépare une logique de publication / consommation découplées.

FLOW doit prolonger cette intuition vers des contrats de données gouvernés.

```text
Flux point-à-point
    ↓
Demi-flux
    ↓
Publication / consommation découplées
    ↓
Contrats de données gouvernés
```

Un contrat de données doit préciser au minimum : source de référence, consommateurs, mode d'échange, granularité, fraîcheur attendue, qualité attendue, supervision, reprise et réconciliation.

Cette capacité est transverse : elle soutient le Case Management, les projections, les Vues 360, le Stock Unifié et la réintégration des services existants.

## Point important : les Cases sont les objets actifs

La plateforme de Case Management fournit le runtime et les mécanismes nécessaires.

Mais l'objet actif n'est pas la plateforme elle-même.

Ce sont les Cases qui portent :

- le contexte ;
- les décisions métier ;
- les promesses ;
- les événements ;
- les documents ;
- les exceptions ;
- les interactions avec les autres produits FLOW.

Cette distinction est importante.

Elle évite de transformer la plateforme de Case Management en orchestrateur opaque.

Le Case reste l'unité métier d'orchestration.

## Nomenclature d'information appliquée

| Produit FLOW | Informations plutôt sources de référence dans FLOW | Informations plutôt projections dans FLOW |
| --- | --- | --- |
| Plateforme de Case Management | Case, décisions métier, événements FLOW, documents attachés | événements externes, documents externes, contexte projeté |
| Stock Unifié | stock disponible, réservations, allocations si calculées par FLOW | stock physique issu des systèmes sources, mouvements externes, statuts WMS / magasin |
| Fulfillment Network / Réseau d'Exécution | réseau, capacités, contraintes et conditions d'usage si gouvernés par FLOW | capacités ou contraintes issues de systèmes Supply |
| Supply Service Registry | éventuellement services normalisés FLOW | services, APIs, SLA exposés par Supply |
| Product Agreement Catalog | rarement source de référence au départ | product core, agreements vente / achat, assortiments, conditions |
| Vues 360 | rarement sources de référence ; plutôt dérivées FLOW | Customer 360, Supplier 360, historiques et signaux externes |

Les contrats de données, règles de publication et exigences de fraîcheur / qualité relèvent d'une pratique transverse de gouvernance. Ils soutiennent les produits FLOW sans constituer un produit fonctionnel autonome dans cette cartographie.

## Rupture de conception

Dans un ERP, les référentiels décrivent souvent l'entreprise telle qu'elle est.

Dans FLOW, les objets de configuration décrivent surtout ce qui permet de décider, promettre et exécuter.

Cette différence est structurante : FLOW ne cherche pas à reconstruire une master data globale.

FLOW cherche à définir les objets nécessaires pour traiter les demandes de manière fiable, explicable et optimisable.

## Ce que ce schéma ne dit pas encore

Cet overview ne détaille pas encore :

- les interfaces ;
- les flux unitaires ou de masse ;
- les événements publiés ou consommés ;
- les patterns d'intégration ;
- les choix de produits du marché ;
- la trajectoire de migration depuis StoreLand, Socloz, UR, SAP ou NewStore.

Ces éléments devront être traités dans des pages d'architecture fonctionnelle et de trajectoire.

## À retenir

FLOW est une réponse fédérée à un problème de convergence.

La plateforme Demand concentre les responsabilités qui doivent devenir communes — Case, décision métier, stock, réseau d'exécution, projections — sans chercher à absorber tout le SI.

FLOW n'a pas vocation à réécrire tous les organes spécialisés du SI.

Il doit reconstruire la colonne vertébrale commune qui permet à ces organes de fonctionner ensemble.

Il doit aussi remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.
