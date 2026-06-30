# Pourquoi FLOW n'est-il pas structuré autour de J'achète / Je vends ?

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Tous lecteurs</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Lire et maintenir le référentiel FLOW</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Question

`J'achète` et `Je vends` sont deux repères très naturels pour lire l'entreprise.

Ils parlent aux métiers, aux processus, aux équipes et aux systèmes historiques.

Pourquoi FLOW ne reprend-il pas ce découpage comme axe structurant du cœur SI cible ?

## Réponse courte

`J'achète` et `Je vends` restent des parcours métier utiles.

Mais ils ne sont pas assez stables pour structurer le cœur de FLOW.

Ils mélangent plusieurs responsabilités qui n'ont pas les mêmes cycles de vie : engagement commercial, achat fournisseur, promesse client, disponibilité, allocation, exécution, documents, finance, conformité, retours et exceptions.

FLOW structure donc le cœur SI autour de responsabilités plus durables :

- Engagement : capter l'intention, le contexte commercial, les parcours et la relation ;
- Demand : qualifier la demande, porter le Case, les statuts, la promesse attendue et le fil métier ;
- Fulfillment : arbitrer une promesse tenable, réserver, allouer, choisir une trajectoire, splitter ou ouvrir une exception ;
- Supply : exposer les ressources, capacités, contraintes, services d'exécution et événements terrain ;
- Finance et référentiels spécialisés : porter leurs responsabilités propres sans être absorbés par FLOW.

Cette distinction vaut aussi pour le pilotage du programme.

Le programme FLOW peut décider de financer, coordonner ou livrer certaines applications côté Engagement ou Supply si elles sont nécessaires à la trajectoire. Mais cela ne change pas le périmètre de la plateforme FLOW : son cœur reste Demand + Fulfillment.

## Pourquoi J'achète / Je vends paraît naturel

Le découpage paraît naturel parce qu'il correspond à des verbes métier simples.

`Je vends` parle de l'engagement client, du canal, du panier, de la commande, de la promesse et de la livraison.

`J'achète` parle de fournisseur, de négociation, d'assortiment, de commande d'achat, d'approvisionnement, de réception, de documents et de finance.

Ce vocabulaire est donc très utile pour raconter les usages, organiser des ateliers, décrire des parcours ou expliquer une transformation.

Le problème apparaît lorsqu'on veut en faire l'architecture du cœur SI.

## Pourquoi ce découpage ne suffit pas au cœur SI

Une même responsabilité traverse souvent les deux verbes.

La promesse client dépend de la vente, mais aussi du stock, des capacités Supply, des lead times fournisseur, des Agreements, des contraintes transport et parfois de décisions d'achat ou de réassort.

Le stock peut être le résultat d'un achat, d'un retour, d'un transfert, d'une réception fournisseur, d'une correction d'inventaire ou d'une réservation client.

Une exception peut naître côté client, mais devoir mobiliser Supply, Finance, SAV, fournisseur, entrepôt ou magasin.

Si FLOW structure son cœur autour de `J'achète` et `Je vends`, il risque de recréer deux silos qui devront ensuite se synchroniser :

- un silo achat / approvisionnement ;
- un silo vente / commande client.

Or FLOW cherche précisément à éviter que la cohérence de la demande, de la promesse, du stock, des décisions et des statuts soit reconstruite après coup par intégration.

## La bonne place de J'achète / Je vends

`J'achète` et `Je vends` doivent rester visibles.

Mais ils doivent être lus comme :

- des parcours métier ;
- des familles d'usages ;
- des entrées de conduite du changement ;
- des regroupements de processus ;
- des manières de raconter la valeur aux équipes.

Ils ne doivent pas devenir la frontière profonde des responsabilités.

La frontière importante est donc double :

- frontière produit : ce qui appartient au cœur Demand + Fulfillment de FLOW ;
- frontière programme : ce que le programme FLOW prend en charge pour réussir la trajectoire, y compris éventuellement des applications Engagement ou Supply.

Une architecture cible peut donc continuer à dire :

```text
J'achète
    → engagement fournisseur
    → agreements
    → approvisionnement
    → collaboration fournisseur
    → documents et conformité

Je vends
    → engagement client
    → demande
    → promesse
    → fulfillment
    → service client
```

Mais le cœur FLOW doit ensuite découper ces usages par responsabilités :

```text
Engagement
    capte l'intention et le contexte

Demand
    porte la demande et le Case

Fulfillment
    arbitre la promesse et la trajectoire

Supply
    expose et exécute les capacités

Finance / référentiels
    portent leurs responsabilités propres
```

## Ce que cela change concrètement

Cela change le point de départ de la conception.

Au lieu de demander :

> Cette fonction appartient-elle à J'achète ou à Je vends ?

FLOW demande :

> Quelle responsabilité est portée ici, qui décide, quelle information fait référence, quelle projection est consommée, quel événement doit circuler et quel Case doit rester lisible ?

Cette bascule est déroutante, mais elle protège le modèle cible.

Elle évite de plaquer des macro-processus historiques sur une plateforme qui doit traiter des demandes longues, des promesses révisables, des stocks distribués, des décisions explicites, des exceptions et des événements multi-domaines.

## Exemple : commande d'achat et promesse client

Une commande d'achat peut sembler appartenir à `J'achète`.

Mais si elle représente une disponibilité future mobilisable pour promettre une demande client, elle devient aussi pertinente pour FLOW.

Cela ne veut pas dire que FLOW absorbe tout le processus achat.

Cela veut dire que FLOW doit consommer ou porter les informations nécessaires à la promesse :

- quel produit ou article sera disponible ;
- à quelle date ;
- via quel fournisseur, usine ou site de production ;
- selon quel Agreement ;
- avec quelle fiabilité ;
- sous quelle responsabilité de source de référence.

Le parcours reste `J'achète`, mais la responsabilité transverse est : rendre une disponibilité future exploitable pour Demand + Fulfillment.

## Lien avec ERP / OMS

Cette question prolonge la question ERP / OMS.

Un ERP legacy a tendance à mélanger achats, stock, documents, finance, commandes et statuts.

Un OMS a tendance à concentrer commande client, promesse, allocation, stock disponible, règles de sourcing et exceptions.

Si l'on structure FLOW autour de `J'achète` et `Je vends`, on risque de reproduire cette logique de blocs applicatifs.

FLOW cherche plutôt à établir un centre de décision cohérent pour les responsabilités transverses, sans recréer un monolithe.

## Rapprochement avec la solution FLOW

Le découpage FLOW est donc cohérent avec :

- la [note de choix stratégique](../vision/note-choix-strategique.md), qui place les premiers arbitrages sur le centre de gravité du SI ;
- le principe [Articuler Engagement, Demand, Fulfillment et Supply](../principes-directeurs/4-separer-demand-et-supply.md) ;
- le principe [La demande comme objet métier central d'orchestration](../principes-directeurs/6-demande-objet-metier-central-orchestration.md) ;
- la page experte [Supprimer ERP et OMS ? Une folie !](supprimer-erp-oms-folie.md) ;
- le pattern [Sources de référence, projections et vues](../architecture-cible/patterns/sources-reference-projections-vues.md).

## Références utiles

- [ASCM - SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) fournit un modèle de référence supply chain pour analyser et améliorer les processus de bout en bout. Cette lecture confirme qu'une chaîne opérationnelle moderne ne se réduit pas à `acheter` et `vendre` : elle sépare les responsabilités d'approvisionnement, commande, fulfillment, retour et orchestration.
- [OMG - Decision Model and Notation](https://www.omg.org/spec/DMN/) fournit un standard pour décrire les décisions métier indépendamment des processus ou applications qui les appellent.
- [OMG - Case Management Model and Notation](https://www.omg.org/spec/CMMN/) fournit un standard utile pour les situations où le traitement dépend du contexte, des événements et d'actions non totalement prévisibles.

## À retenir

`J'achète` et `Je vends` restent indispensables pour parler aux métiers.

Mais FLOW ne peut pas en faire les fondations de son cœur SI.

Le cœur cible doit être structuré par responsabilités stables : demande, promesse, décision, stock, ressources, événements, sources de référence, projections et exécution.

Le vocabulaire métier reste en surface de lecture.

Le modèle d'architecture doit descendre au niveau des responsabilités.
