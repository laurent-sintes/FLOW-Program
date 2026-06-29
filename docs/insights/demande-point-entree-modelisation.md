# La demande comme point d’entrée de la modélisation FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecture, sponsors, contributeurs</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Le point de départ

Dans un programme SAP classique, le modèle métier est largement préexistant.

```text
Business Process
        ↓
SAP Model
        ↓
Configuration
```

Les objets, les catégories et les questions sont déjà connus : Customer, Vendor, Material, Sales Order, Delivery, Invoice, Purchase Order, Plant ou Storage Location.

La question principale devient alors : comment renseigner et configurer le modèle fourni par SAP ?

FLOW se situe dans une situation différente.

```text
Pas de modèle préexistant
        ↓
Pas de liste de questions préétablie
        ↓
Pas de taxonomie imposée
```

La première difficulté n’est donc pas l’intégration. Elle consiste à découvrir où commence le modèle.

## Changer le point d’entrée

Les approches habituelles démarrent volontiers par les objets de référence :

```text
Customer
Product
Stock
Supplier
Warehouse
Transporter
```

FLOW peut partir d’une autre question :

> Quelle est la demande à instruire ?

Par exemple, lorsqu’un client souhaite acheter un produit, le point d’entrée n’est pas nécessairement une liste de données Customer, Product, Price et Stock.

```text
Customer Request
        ↓
Qui demande ?
        ↓
Customer

Quoi ?
        ↓
Product

Peut-on le faire ?
        ↓
Stock et capacité

Comment ?
        ↓
Transport et exécution
```

La hiérarchie devient :

```text
Demande
        ↓
Décisions
        ↓
Données nécessaires
```

et non :

```text
Master Data
        ↓
Processus
        ↓
Décisions
```

## La demande donne du sens aux données

Dans FLOW, toutes les données ne jouent pas le même rôle.

### Objet métier central

La demande ou le Case porte l’intention à traiter, son contexte, son cycle de vie et les engagements associés.

Exemples :

- Customer Request ;
- Case ;
- demande de retour ;
- demande de transfert ;
- demande d’achat ;
- demande de changement interne.

### Données de décision

Elles sont mobilisées pour instruire la demande et prendre une décision.

Exemples :

- stock ;
- capacité ;
- prix ;
- contrat ;
- client ;
- produit ;
- disponibilité fournisseur.

### Données de support

Elles qualifient les objets et les décisions sans organiser directement le modèle.

Exemples :

- code postal ;
- couleur ;
- poids ;
- dimensions.

## Repenser les Master Data

Dans un système distribué, Master Data ne doit pas simplement désigner les catégories héritées d’un ERP.

Une donnée partagée est une donnée dont :

- la responsabilité est clairement attribuée ;
- la qualité est gouvernée ;
- la définition est vérifiée ;
- la disponibilité est assurée pour plusieurs domaines ;
- l’usage est justifié par les décisions qu’elle permet de prendre.

La question n’est donc pas seulement : quelles sont les Master Data ?

La question devient :

> Quel est l’objet métier central à partir duquel les autres données prennent leur sens ?

## Les principes qui peuvent émerger

Cet insight ne constitue pas encore un principe unique. Il fait apparaître plusieurs candidats à confirmer :

1. la demande ou le Case comme unité d’orchestration transverse ;
2. les données partagées et gouvernées au service des décisions ;
3. les décisions comme capacités explicites, traçables et gouvernées ;
4. les processus comme conséquences de décisions et non comme point de départ de la modélisation.

## À retenir

FLOW ne commence pas par inventorier les données de référence.

FLOW commence par identifier la demande à instruire, les décisions qu’elle requiert et les données nécessaires à ces décisions.

La demande constitue ainsi un point d’entrée possible pour découvrir et structurer le modèle de l’entreprise.
