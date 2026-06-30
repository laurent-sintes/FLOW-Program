# Rôles, relations et policies plutôt que cardinalités figées

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
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Ce pattern décrit une manière de modéliser les relations métier lorsque les cardinalités peuvent évoluer selon les contextes commerciaux, juridiques, industriels ou logistiques.

L'idée centrale est simple :

> Ne pas figer dans le cœur du modèle une cardinalité qui relève en réalité d'une règle métier variable.

FLOW doit éviter de transformer une relation observée à un instant donné en structure rigide du modèle cible.

## Le problème

Un modèle paraît souvent simple au départ :

```text
Fournisseur
    1 → 1
Usine
```

Puis le métier évolue ou l'analyse révèle une réalité plus riche :

```text
1 fournisseur → N usines
1 usine → N fournisseurs
1 agent → N fournisseurs / N usines
1 usine → plusieurs entités de facturation
1 fournisseur → plusieurs rôles selon pays, marque, canal ou saison
```

Si le modèle cœur a été figé en `1-1`, l'évolution conduit à :

- dupliquer des lignes ;
- surcharger des champs ;
- créer des exceptions ;
- coder des cas particuliers ;
- perdre l'explication de la décision ;
- mélanger identité, rôle, relation, Agreement, finance et exécution.

Le problème n'est pas seulement technique.

Il devient un problème métier : le modèle empêche de représenter correctement les variations commerciales ou opérationnelles.

## Pattern

Modéliser séparément :

- les parties ;
- les rôles ;
- les relations ;
- les Agreements ;
- les policies ;
- le contexte d'application ;
- les périodes de validité ;
- les priorités ou règles de résolution.

Puis laisser la décision métier résoudre la relation applicable dans un contexte donné.

```text
Party
    → peut jouer plusieurs rôles

Role
    → fournisseur, usine, agent, entité de facturation, adresse de commande

Relationship
    → relie des parties dans un contexte donné

Agreement
    → porte les conditions applicables

Policy / Specification
    → détermine ce qui s'applique pour une demande donnée

Context
    → marque, pays, saison, canal, produit, type de demande, période
```

Le moteur de règles ne doit pas masquer le modèle.

Il doit résoudre des relations explicites, typées, gouvernées et observables.

## Filiation et références

Ce pattern n'est pas un standard nommé de façon unique.

Il assemble plusieurs patterns reconnus qui convergent vers la même idée : ne pas enfermer des rôles, relations et règles variables dans des cardinalités physiques trop précoces.

- **Knowledge Level** — Eric Evans décrit un niveau d'objets séparé pour représenter les règles, rôles et relations qui contraignent le modèle concret. C'est la référence la plus directe lorsque la complexité vient de règles de composition variables.
- **Specification** — Eric Evans et Martin Fowler isolent le critère d'applicabilité dans un objet séparé, testable et combinable. Dans FLOW, une policy ou specification décide quelle relation, quel Agreement ou quel service est applicable à une demande.
- **Accountability / Typed Relationship** — Martin Fowler modélise une relation entre parties comme un objet de domaine à part entière, typé selon la nature du lien. Cela justifie de ne pas réduire fournisseur / usine / agent / facturé à des clés étrangères figées.
- **Role Object** — Dirk Bäumer, Dirk Riehle, Wolf Siberski et Martina Wulf représentent les rôles comme des objets attachés dynamiquement à une entité selon le contexte. C'est utile pour éviter qu'une même partie soit dupliquée parce qu'elle joue fournisseur ici, usine là, entité de facturation ailleurs.

Dans FLOW, cette filiation se traduit par une règle de conception :

> La relation doit être explicite ; son applicabilité doit être gouvernée par policy ou specification.

Références :

- [DDD Reference — Eric Evans](https://www.domainlanguage.com/ddd/reference/)
- [Specification — Eric Evans & Martin Fowler](https://www.martinfowler.com/apsupp/spec.pdf)
- [Accountability — Martin Fowler](https://martinfowler.com/apsupp/accountability.pdf)
- [Role Object — Bäumer, Riehle, Siberski & Wulf](https://www.riehle.org/computer-science/research/1997/plop-1997-role-object.html)

## Exemple BRD : fournisseur, usine et entité de facturation

L'atelier Boardriders du 29 juin 2026 illustre bien le pattern.

Dans le modèle BRD, une commande peut être passée à une usine, tandis que l'entité à facturer, l'adresse de commande, le fournisseur, l'agent ou l'intermédiaire sont portés par des partner functions.

Exemple :

```text
Fabrication
    → Afrique du Sud

Facturation
    → Corée du Sud
```

Un modèle `fournisseur 1-1 usine` ne suffit pas.

Il faut représenter les rôles et relations :

```text
Party A
    joue le rôle : usine

Party B
    joue le rôle : entité de facturation

Party C
    joue le rôle : agent

Relationship
    relie A, B et C dans un contexte d'achat donné

Agreement
    définit les conditions applicables

Policy
    choisit la relation pertinente selon produit, pays, saison ou marque
```

## Application dans FLOW

Ce pattern s'applique notamment à :

- fournisseur / usine / agent / entité de facturation ;
- client / centrale / franchisé / livré / facturé ;
- marque / tenant / pays / canal ;
- entrepôt / service Supply / transporteur ;
- Agreement / condition / produit / saison ;
- PLM / Product Agreement Catalog / Supply Service Registry.

Il protège FLOW contre une tentation classique : importer dans le modèle cible les cardinalités accidentelles d'un ERP ou d'un outil existant.

## Règles de conception

### 1. Ne pas figer trop tôt une cardinalité métier

Une cardinalité `1-1` ne doit être inscrite dans le cœur que si elle correspond à une invariance métier durable.

Si elle dépend d'un pays, d'une marque, d'un canal, d'une saison, d'un type de demande ou d'une pratique commerciale, elle doit probablement devenir une relation gouvernée.

### 2. Typifier les relations

Une relation souple ne doit pas devenir un graphe amorphe.

Chaque relation doit avoir :

- un type ;
- des parties ;
- des rôles ;
- une période de validité ;
- un contexte ;
- une source ;
- une règle de priorité ou d'arbitrage si nécessaire.

### 3. Externaliser l'applicabilité

La question n'est pas seulement :

> Quelle relation existe ?

La question est :

> Quelle relation s'applique à cette demande, dans ce contexte ?

Cette applicabilité doit être portée par des policies, specifications ou règles métier explicites.

### 4. Rendre la résolution explicable

FLOW doit pouvoir expliquer pourquoi il a retenu :

- telle usine ;
- tel fournisseur ;
- telle entité de facturation ;
- tel Agreement ;
- tel lead time ;
- telle zone de transport.

La souplesse de cardinalité ne doit pas réduire l'observabilité.

### 5. Séparer la relation de l'exécution

Une relation fournisseur / usine / agent ne doit pas être confondue avec le service Supply effectivement mobilisable.

Le Supply Service Registry et le Fulfillment Network décrivent les services, capacités, SLA et contraintes d'exécution.

Les relations métier décrivent qui joue quel rôle dans quel contexte.

## Anti-patterns

### Fiche monolithique

Tout concentrer dans une fiche fournisseur, client ou article : identité, rôles, facturation, transport, conditions, lead times, capacité, finance et PLM.

Cela rend l'information difficile à gouverner et pousse FLOW à reproduire le monolithe existant.

### Cardinalité cachée dans les lignes

Dupliquer des lignes pour simuler une relation `1-N` ou `N-N` alors que le modèle physique impose du `1-1`.

Cela crée des ambiguïtés de source, de qualité et de décision.

### Moteur de règles opaque

Déplacer toute la complexité dans un moteur de règles sans modéliser les rôles et relations.

La règle devient alors impossible à expliquer, tester ou gouverner.

## Produits FLOW concernés

| Produit | Impact |
| --- | --- |
| Socle Case Management | Résoudre les parties prenantes et rôles applicables à une demande |
| Product Agreement Catalog | Exposer les Agreements et conditions selon rôles, relations et contexte |
| Supply Service Registry | Distinguer relation métier et service Supply mobilisable |
| Fulfillment Network Configuration | Décrire lieux, contraintes, services et capacités d'exécution |
| Vues 360 | Expliquer les relations entre parties, demandes, Agreements et exécutions |
| Gouvernance des données en transit | Publier des contrats de données explicites sur les relations et leur applicabilité |

## À retenir

Ce pattern ne dit pas que toutes les relations doivent être `N-N`.

Il dit que FLOW doit éviter de confondre une cardinalité observée avec une invariance métier.

La bonne pratique consiste à représenter explicitement les rôles et relations, puis à gouverner leur applicabilité par policies ou specifications.

Cela permet de rester fidèle au réel métier sans recréer un paramétrage monolithique.
