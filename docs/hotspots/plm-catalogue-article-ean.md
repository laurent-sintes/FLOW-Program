# PLM, catalogue, Article / EAN

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsor, Architecte, Métier</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Pourquoi c'est un hotspot

Le Groupe Beaumanoir dispose d'un PLM structurant pour gérer les collections au cours des saisons.

Historiquement, ce PLM a été construit, configuré et standardisé pour des activités de conception de collection et de gestion de contrat avec les fournisseurs et façonniers.

Cette logique est cohérente avec le modèle historique : concevoir un produit sans vérifier très tôt qu'il peut être produit en quantité, à un prix cible et selon des contraintes industrielles maîtrisées n'a pas de sens.

Le PLM Beaumanoir prend donc en compte la dimension industrielle très tôt dans la préparation de saison.

Il gère notamment :

- les processus de conception et d'affinage avec les fournisseurs ;
- les fiches produits ;
- les grilles taille / couleur ;
- les engagements de prix sur volume ;
- les nomenclatures de taille et de couleur ;
- l'initialisation de saison ;
- la détermination des codes-barres EAN ;
- la transmission des informations au fabricant pour intégration sur l'étiquette produit.

Dans ce modèle, la fiche produit porte une structure riche : style, tailles, couleurs, variantes, volumes, conditions industrielles et informations nécessaires à la fabrication.

## Une autre stratégie de collection apparaît

Une autre logique existe avec Sarenza, notamment sur la chaussure, et avec certaines collections Boardriders.

Dans ces cas, l'entreprise n'achète pas toujours des produits conçus dans son propre processus de collection.

Elle peut acheter des références déjà designées par les fournisseurs.

Les fournisseurs ne transmettent pas nécessairement un catalogue construit sous forme de fiche produit avec matrice taille / couleur / style.

Ils peuvent fournir directement un catalogue de variantes produit, où chaque ligne porte déjà :

- un EAN ;
- une référence fournisseur ;
- une taille ;
- une couleur ;
- des caractéristiques parfois non alignées avec les nomenclatures historiques Beaumanoir.

Cette situation met en tension le modèle PLM historique.

Les nomenclatures taille / couleur rationalisées pour les activités de conception ne couvrent pas nécessairement toutes les formes d'achat de produits déjà conçus.

## Le problème posé à FLOW

FLOW devra pouvoir gérer les achats et les ventes de deux familles de produits :

- des <span class="flow-keyword">produits conçus</span>, issus d'un processus PLM structuré ;
- des <span class="flow-keyword">produits importés</span>, déjà designés par des fournisseurs et fournis au niveau variante / EAN.

Le risque serait de faire dépendre FLOW trop fortement de la structure du PLM historique.

Dans ce cas, chaque variation de stratégie de collection, de fournisseur ou de nomenclature amont pourrait se propager dans la plateforme Demand.

À l'inverse, si FLOW se place à un niveau trop pauvre, il peut perdre les informations nécessaires pour acheter, vendre, promettre, allouer ou expliquer une demande.

## Vente et achat : le même niveau de catalogue ne suffit peut-être pas

Pour les demandes afférentes à la vente, un catalogue d'articles, ou Product Variant, est très probablement suffisant.

La vente a principalement besoin d'un objet exécutable et identifiable : Article, EAN, caractéristiques utiles, disponibilité, prix ou conditions applicables, promesse, allocation et exécution.

À ce niveau, FLOW peut raisonnablement chercher à rester découplé du modèle PLM.

Pour les achats, la situation est plus délicate.

Les règles industrielles, les engagements fournisseurs, les conditions de volume, les contraintes de fabrication et les informations de préparation de saison sont parfois tellement intégrées dans la fiche produit que le simple niveau Article / EAN pourrait être insuffisant.

FLOW pourrait alors avoir besoin d'un <span class="flow-keyword">catalogue Produit d'achat</span>, distinct du catalogue d'articles utilisé pour la vente.

Ce serait une duplication partielle du référentiel produit.

Elle serait dommageable si elle reconstitue deux vérités concurrentes.

Mais elle peut devenir nécessaire si les responsabilités d'achat ne peuvent pas être correctement portées par un catalogue Article / EAN.

L'arbitrage est donc ouvert :

```text
Demandes de vente
    Catalogue Article / EAN probablement suffisant

Demandes d'achat
    Catalogue Article / EAN peut-être insuffisant
    Catalogue Produit d'achat à étudier
```

Le sujet doit être analysé en profondeur avant de stabiliser la cible.

## Question d'architecture

La question centrale est donc :

> FLOW doit-il connaître la structure du PLM, consommer un catalogue d'exécution au niveau Article / EAN, ou introduire un catalogue Produit d'achat pour couvrir les règles et engagements propres aux achats ?

Cette question est structurante car elle touche directement :

- la frontière entre conception produit et exécution ;
- le rôle du Product Agreement Catalog ;
- la granularité minimale nécessaire au fulfillment ;
- la capacité à vendre et acheter des produits conçus comme des produits importés ;
- la gouvernance des nomenclatures taille / couleur ;
- la capacité de FLOW à rester indépendant des variations de processus amont ;
- le risque de duplication de référentiel produit entre vente et achat.

## Hypothèse de travail

L'hypothèse à instruire est que FLOW ne doit pas reproduire la structure complète du PLM.

Pour la vente, FLOW devrait plutôt consommer une projection d'exécution, suffisamment riche pour traiter les demandes, mais découplée du processus de conception.

Cette projection pourrait être portée par le Product Agreement Catalog, au niveau Article / EAN, avec les informations nécessaires pour :

- vendre ;
- promettre ;
- allouer ;
- réserver ;
- exécuter ;
- expliquer les engagements et conditions applicables.

Pour l'achat, l'hypothèse doit rester ouverte.

Il faut étudier si les responsabilités d'achat peuvent s'appuyer sur la même projection Article / EAN enrichie par les Agreements, ou si un catalogue Produit d'achat distinct est nécessaire pour porter les règles, conditions et informations issues de la fiche produit.

Le PLM resterait alors responsable de la conception produit, de l'affinage avec les fournisseurs et des nomenclatures nécessaires à son propre processus.

FLOW consommerait ce qui est nécessaire à l'exécution, sans absorber toute la complexité du design de collection.

## Ce que FLOW doit clarifier

| Sujet | Question à instruire |
| --- | --- |
| Granularité produit vente | Le niveau Article / EAN suffit-il pour vendre, promettre, allouer et exécuter ? |
| Granularité produit achat | Les achats peuvent-ils s'appuyer sur Article / EAN ou nécessitent-ils un catalogue Produit d'achat ? |
| Produits conçus vs produits importés | Comment représenter les deux stratégies sans imposer un modèle unique ? |
| Nomenclatures taille / couleur | Quelles nomenclatures doivent être gouvernées par le PLM, lesquelles doivent être projetées vers FLOW ? |
| Product Agreement Catalog | Porte-t-il uniquement une projection d'exécution ou devient-il un référentiel métier plus large ? |
| Duplication produit | Comment éviter deux référentiels produit concurrents si un catalogue Produit d'achat est nécessaire ? |
| Achats et ventes | Les achats et ventes peuvent-ils s'appuyer sur la même projection enrichie par les Agreements ? |
| Découplage amont / aval | Comment éviter que les variations de conception de saison deviennent une complexité FLOW ? |

## À retenir

Ce hotspot n'oppose pas PLM et FLOW.

Il cherche à clarifier leur frontière.

Le PLM conçoit et prépare la collection.

FLOW doit traiter les demandes, achats, ventes et engagements sur des objets suffisamment stabilisés pour l'exécution.

Pour la vente, le niveau Article / EAN semble probablement suffisant.

Pour les achats, ce niveau doit être challengé : si les règles sont trop intégrées dans la fiche produit, un catalogue Produit d'achat pourrait être nécessaire.

Ce serait une duplication à éviter si possible, mais une contrainte à assumer si elle protège mieux les responsabilités métier.
