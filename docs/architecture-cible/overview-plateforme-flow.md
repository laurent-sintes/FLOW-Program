# Overview de la plateforme FLOW

## Intention

Cette page propose un premier overview de la plateforme FLOW.

Elle ne cherche pas encore à détailler les flux, les APIs ou les choix techniques.

Elle cherche d'abord à montrer comment la vision de convergence peut se traduire en produits fonctionnels.

Le point de départ n'est pas : “quelle plateforme voulons-nous construire ?”.

Le point de départ est :

> Quelles responsabilités doivent devenir communes, gouvernées et transverses pour permettre la convergence, sans centraliser tout le SI ?

FLOW est ici décrit comme une plateforme Demand fédérée.

Elle est centrée sur les Cases, enrichie par des services partagés et des projections opérationnelles.

## Schéma d'overview

![Overview de la plateforme FLOW](../assets/images/architecture-cible-flow-overview.svg)

## Produits FLOW candidats

| Produit | Rôle |
| --- | --- |
| Plateforme de Case Management | Piloter les demandes dans la durée. Les Cases portent le contexte, les décisions, les promesses, les documents et les événements. |
| Stock Unifié | Rendre la disponibilité fiable et exploitable. Porter les réservations, l'allocation / tagging, les facts et événements stock. |
| Fulfillment Network / Réseau d'Exécution | Décrire les nœuds logistiques, partenaires, capacités, contraintes, services et conditions d'usage mobilisables pour servir une demande. |
| Supply Service Registry | Référencer les services Supply exposés : APIs, SLA, conditions d'accès, éligibilités et contraintes. |
| Product Agreement Catalog | Exposer les produits, assortiments et agreements utiles à la vente, à l'achat et à l'exécution. |
| Vues 360 | Agréger le contexte transverse autour du client, du fournisseur ou du Case. |
| Diffusion et gouvernance opérationnelle des données | Gouverner les contrats de données, modes d'échange, consommateurs, fraîcheur, qualité, supervision et réconciliation des données en transit. |

## Lecture fonctionnelle

FLOW ne doit pas être lu comme un ERP, un OMS unique, un PIM, un CRM, un WMS ou un outil Finance.

FLOW doit être lu comme une plateforme de cohérence Demand.

Sa responsabilité est de rendre possible l'instruction, la décision, la promesse et l'orchestration de demandes transverses.

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

Diffusion et gouvernance opérationnelle des données
    → transforme les flux projet en contrats de données gouvernés
```

## Colonne vertébrale du SI

FLOW réécrit la <span class="flow-keyword">colonne vertébrale opérationnelle</span> du SI.

Cela signifie qu'il porte les responsabilités qui doivent rester cohérentes à l'échelle du groupe : demandes, décisions, statuts, événements, stock, promesses, allocations, besoins d'exécution et vues transverses.

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
    → cohérence des demandes, statuts, décisions, événements et projections
```

Ces services peuvent rester autour de FLOW comme consommateurs, contributeurs, sources d'événements ou domaines spécialisés.

La règle d'urbanisme est donc : ne pas réécrire ce qui porte une valeur métier spécifique, mais ne pas laisser ces services recréer chacun leur propre colonne vertébrale.

## Données en transit : des flux projet aux contrats gouvernés

FLOW doit aussi traiter la manière dont les données circulent entre applications.

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

Un contrat de données doit préciser au minimum : source, consommateurs, mode d'échange, granularité, fraîcheur attendue, qualité attendue, supervision, reprise et réconciliation.

Cette capacité est transverse : elle soutient le Case Management, les projections, les Vues 360, le Stock Unifié et la réintégration des services existants.

## Point important : les Cases sont les objets actifs

La plateforme de Case Management fournit le runtime et les mécanismes nécessaires.

Mais l'objet actif n'est pas la plateforme elle-même.

Ce sont les Cases qui portent :

- le contexte ;
- les décisions ;
- les promesses ;
- les événements ;
- les documents ;
- les exceptions ;
- les interactions avec les autres produits FLOW.

Cette distinction est importante.

Elle évite de transformer la plateforme de Case Management en orchestrateur opaque.

Le Case reste l'unité métier d'orchestration.

## Nomenclature d'information appliquée

| Produit FLOW | Informations plutôt Source dans FLOW | Informations plutôt Projection dans FLOW |
| --- | --- | --- |
| Plateforme de Case Management | Case, décisions, événements FLOW, documents attachés | événements externes, documents externes, contexte projeté |
| Stock Unifié | stock disponible, réservations, allocations si calculées par FLOW | stock physique source, mouvements externes, statuts WMS / magasin |
| Fulfillment Network / Réseau d'Exécution | réseau, capacités, contraintes et conditions d'usage si gouvernés par FLOW | capacités ou contraintes issues de systèmes Supply |
| Supply Service Registry | éventuellement services normalisés FLOW | services, APIs, SLA exposés par Supply |
| Product Agreement Catalog | rarement source au départ | product core, agreements vente / achat, assortiments, conditions |
| Vues 360 | Case 360 probablement source ou dérivée FLOW | Customer 360, Supplier 360, historiques et signaux externes |
| Diffusion et gouvernance opérationnelle des données | contrats de données, règles de publication, exigences de fraîcheur / qualité si gouvernés par FLOW | catalogues d'échanges existants, flux historiques, capacités d'intégration des domaines |

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

La plateforme Demand concentre les responsabilités qui doivent devenir communes — Case, décision, stock, réseau d'exécution, projections — sans chercher à absorber tout le SI.

FLOW n'a pas vocation à réécrire tous les organes spécialisés du SI.

Il doit reconstruire la colonne vertébrale commune qui permet à ces organes de fonctionner ensemble.

Il doit aussi remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.