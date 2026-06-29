# Questions pour les nouveaux

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
      <strong>6 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Lire et maintenir le référentiel FLOW</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page répond aux questions qui reviennent lorsqu'on découvre FLOW rapidement.

Elle ne remplace pas la vision, les principes ou l'architecture cible. Elle sert de raccourci pour lever les malentendus les plus fréquents.

### FLOW, c'est quoi en une phrase ?

FLOW est une plateforme de cohérence Demand + Fulfillment qui permet de piloter les demandes, les décisions métier, les promesses, les ressources mobilisables, les statuts et les événements transverses.

À lire ensuite : [Abstract FLOW](../vision/abstract.md) et [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md).

### FLOW est-il un OMS ?

Pas exactement.

FLOW couvre certaines responsabilités qu'un OMS peut porter : orchestration, allocation, promesse, suivi d'exécution, statut de commande.

Mais FLOW est pensé plus largement comme une plateforme de Demand Management et de Fulfillment, capable de traiter plusieurs types de demandes, plusieurs canaux, plusieurs modèles économiques et plusieurs domaines adhérents.

À lire ensuite : [De l'OMS au Demand Management](../insights/oms-vers-demand-management.md) et [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md).

### FLOW remplace-t-il SAP, StoreLand, Socloz ou NewStore ?

FLOW ne se définit pas comme un remplacement applicatif un pour un.

Il reprend ou gouverne les responsabilités transverses qui doivent devenir cohérentes à l'échelle du groupe.

Certaines applications pourront être remplacées, d'autres conservées, raccordées ou réintégrées selon leur valeur métier et leur capacité à exposer leurs responsabilités proprement.

À lire ensuite : [Vision FLOW](../vision/vision.md) et [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md).

### Supprimer ERP et OMS, c'est une folie ?

Ce serait une folie si l'objectif était de recréer un gros monolithe qui porterait à la fois ERP, OMS, canaux, finance, stock, promesse, règles et exécution.

Ce n'est pas l'objectif de FLOW.

FLOW cherche plutôt à clarifier les responsabilités : l'ERP garde ce qui relève du cœur transactionnel, financier ou référentiel ; les canaux portent l'engagement ; Supply porte les capacités et l'exécution ; FLOW porte Demand + Fulfillment, c'est-à-dire les demandes, promesses, décisions et événements transverses.

Le vrai problème n'est pas seulement de séparer ERP et OMS. C'est que chacun peut devenir un système complet avec ses propres règles, décisions, orchestrations et statuts, sans partager le modèle cible Demand / Fulfillment / Supply.

→ Réponse pour les experts : [Supprimer ERP et OMS ? Une folie !](supprimer-erp-oms-folie.md)

À lire ensuite : [ERP + OMS : séparation utile ou dette architecturale ?](../insights/erp-oms-separation-ou-plateforme-integree.md).

### Pourquoi ne pas simplement uniformiser tout le groupe ?

Parce que la convergence utile ne consiste pas à effacer les singularités.

Le groupe doit construire du commun là où l'incohérence coûte cher : demande, stock disponible, promesse, décision, statuts, événements, contrats de données.

Les marques, canaux, parcours et modèles économiques doivent pouvoir conserver ce qui crée réellement de la valeur.

À lire ensuite : [Construire le bon niveau de commun](../principes-directeurs/1-converger-c-est-federer.md) et [Convergence et bon niveau de commun](../insights/convergence-federation-uniformisation.md).

### Quel est le cœur de FLOW ?

Le cœur de FLOW est <span class="flow-keyword">Demand + Fulfillment</span>.

Demand qualifie la demande, porte le Case, le contexte, les priorités et la promesse à tenir.

Fulfillment arbitre une promesse tenable et une trajectoire d'exécution à partir des règles, des priorités, du stock, des capacités et des contraintes Supply.

À lire ensuite : [Positionnement de FLOW](../vision/positionnement-flow.md) et [Articuler Demand, Fulfillment et Supply](../principes-directeurs/4-separer-demand-et-supply.md).

### Engagement et Supply sont-ils dans FLOW ?

Engagement et Supply sont adhérents à FLOW.

Engagement capte l'intention et porte les parcours, interfaces, canaux ou négociations.

Supply expose les ressources, capacités, contraintes, services et événements d'exécution.

Ils ne sont pas absorbés par FLOW, mais ils doivent être raccordés par des APIs, événements, statuts, projections, règles d'interaction et contrats de données.

À lire ensuite : [Modèle de fonctionnement de FLOW](../vision/modele-fonctionnement-flow.md) et [Flux fonctionnels FLOW](../architecture-cible/flux-fonctionnels-flow.md).

### Pourquoi parler de Case ?

Parce qu'une demande réelle vit dans la durée.

Elle peut changer, recevoir des événements, être réarbitrée, produire des documents, ouvrir une exception ou traverser plusieurs systèmes.

Le Case conserve le fil métier : intention, contexte, décisions, promesses, statuts, événements, documents et historique.

À lire ensuite : [La demande comme objet métier central d'orchestration](../principes-directeurs/6-demande-objet-metier-central-orchestration.md) et [Socle Case Management](../architecture-cible/produits/socle-case-management.md).

### Pourquoi dit-on que le processus émerge des décisions métier ?

Dans les situations simples, un workflow suffit.

Dans FLOW, beaucoup de situations dépendent du contexte : stock disponible, priorités, allocation, précommande, retard, capacité fournisseur, canal, pays ou client.

Le comportement réel doit donc être piloté par des règles, événements et décisions explicites. Le processus observé devient la conséquence de ces décisions.

À lire ensuite : [Le processus émerge des décisions métier](../principes-directeurs/5-le-processus-emerge-des-decisions.md) et [Case-centric orchestration](../architecture-cible/patterns/case-centric-orchestration.md).

### Pourquoi le Fulfillment est-il central ?

Parce que c'est le lieu de décision entre une demande à servir et des ressources limitées.

Fulfillment répond à des questions concrètes : peut-on promettre, depuis où servir, quel stock réserver, faut-il splitter, substituer, reporter, prioriser ou ouvrir une exception ?

À lire ensuite : [Articuler Demand, Fulfillment et Supply](../principes-directeurs/4-separer-demand-et-supply.md) et [Flux fonctionnels FLOW](../architecture-cible/flux-fonctionnels-flow.md).

### À quoi ça sert un stock temps réel ?

Le stock temps réel ne garantit pas qu'aucune commande ne sera jamais impossible à servir.

Il sert à réduire fortement la fenêtre d'erreur, rendre la disponibilité exploitable par les décisions de Fulfillment, permettre des réservations, exposer la fraîcheur et la confiance, détecter les anomalies et réarbitrer plus vite.

→ Réponse pour les experts : [À quoi ça sert un stock temps réel ?](stock-temps-reel.md)

À lire ensuite : [Stock Unifié](../architecture-cible/produits/stock-unifie.md).

### Pourquoi ne pas parler simplement de Master Data ?

Parce que le terme mélange trop de choses : objets ERP, données de référence, discipline MDM, projections, paramètres, règles, faits, documents.

FLOW préfère qualifier les informations avec deux questions simples :

- quelle est la nature de cette information ;
- pour cet usage, est-elle source de référence ou projection ?

À lire ensuite : [Qualifier les informations plutôt que parler de Master Data](../principes-directeurs/7-qualifier-les-informations-plutot-que-master-data.md) et [Sources de référence, projections et vues](../architecture-cible/patterns/sources-reference-projections-vues.md).

### Qu'est-ce qu'une source de référence ?

Une source de référence est le domaine, l'application ou le service qui crée, valide ou maintient une information avec un processus de contrôle identifié pour un usage donné.

Elle n'est pas forcément unique pour tous les usages.

Par exemple, le PLM peut faire référence pour la conception produit, tandis qu'une projection produit d'exécution peut faire référence pour le Fulfillment.

À lire ensuite : [Sources de référence, projections et vues](../architecture-cible/patterns/sources-reference-projections-vues.md) et [Glossaire](../glossaire.md).

### Pourquoi les contrats de données sont-ils importants ?

Parce qu'un flux critique n'est pas seulement un tuyau technique.

Il doit préciser l'information publiée, sa source de référence, ses consommateurs, sa fraîcheur attendue, sa qualité, son mode d'échange, sa supervision, sa reprise et sa réconciliation.

Sans cela, le SI accumule des flux projet difficiles à maintenir.

À lire ensuite : [Gouverner la donnée en transit](../principes-directeurs/8-gouverner-la-donnee-en-transit.md) et [Gouvernance des données en transit](../architecture-cible/produits/gouvernance-donnees-transit.md).

## Quels documents lire si j'ai peu de temps ?

Lire dans cet ordre :

1. [Abstract FLOW](../vision/abstract.md)
2. [Positionnement de FLOW](../vision/positionnement-flow.md)
3. [Abstract des principes directeurs](../principes-directeurs/abstract.md)
4. [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md)
5. [Glossaire](../glossaire.md)

## Où trouver le vocabulaire partagé ?

Le vocabulaire stabilisé se trouve dans le [Glossaire](../glossaire.md).

Les mots les plus structurants sont aussi expliqués dans [Concepts clés du programme FLOW](../vision/concepts-cles.md).

## Comment contribuer sans casser la cohérence ?

Commencer par qualifier l'information ajoutée : fait observé, insight, question ouverte, principe, hotspot, concept, produit ou règle de contribution.

Puis vérifier les impacts sur la vision, les principes, l'architecture cible, le glossaire, les cartouches et les métriques.

Le [Guide de contribution éditoriale](../administration/guide-contribution-contenu.md) donne la procédure complète.
