# FAQ FLOW

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
      <strong>4 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Lire et maintenir le référentiel FLOW</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette FAQ répond aux questions qui reviennent lorsqu'on découvre FLOW rapidement.

Elle ne remplace pas la vision, les principes ou l'architecture cible. Elle sert de raccourci pour lever les malentendus les plus fréquents.

## FLOW, c'est quoi en une phrase ?

FLOW est une plateforme de cohérence Demand + Fulfillment qui permet de piloter les demandes, les décisions métier, les promesses, les ressources mobilisables, les statuts et les événements transverses.

## FLOW est-il un OMS ?

Pas exactement.

FLOW couvre certaines responsabilités qu'un OMS peut porter : orchestration, allocation, promesse, suivi d'exécution, statut de commande.

Mais FLOW est pensé plus largement comme une plateforme de Demand Management et de Fulfillment, capable de traiter plusieurs types de demandes, plusieurs canaux, plusieurs modèles économiques et plusieurs domaines adhérents.

## FLOW remplace-t-il SAP, StoreLand, Socloz ou NewStore ?

FLOW ne se définit pas comme un remplacement applicatif un pour un.

Il reprend ou gouverne les responsabilités transverses qui doivent devenir cohérentes à l'échelle du groupe.

Certaines applications pourront être remplacées, d'autres conservées, raccordées ou réintégrées selon leur valeur métier et leur capacité à exposer leurs responsabilités proprement.

## Pourquoi ne pas simplement uniformiser tout le groupe ?

Parce que la convergence utile ne consiste pas à effacer les singularités.

Le groupe doit construire du commun là où l'incohérence coûte cher : demande, stock disponible, promesse, décision, statuts, événements, contrats de données.

Les marques, canaux, parcours et modèles économiques doivent pouvoir conserver ce qui crée réellement de la valeur.

## Quel est le cœur de FLOW ?

Le cœur de FLOW est <span class="flow-keyword">Demand + Fulfillment</span>.

Demand qualifie la demande, porte le Case, le contexte, les priorités et la promesse à tenir.

Fulfillment arbitre une promesse tenable et une trajectoire d'exécution à partir des règles, des priorités, du stock, des capacités et des contraintes Supply.

## Engagement et Supply sont-ils dans FLOW ?

Engagement et Supply sont adhérents à FLOW.

Engagement capte l'intention et porte les parcours, interfaces, canaux ou négociations.

Supply expose les ressources, capacités, contraintes, services et événements d'exécution.

Ils ne sont pas absorbés par FLOW, mais ils doivent être raccordés par des APIs, événements, statuts, projections, règles d'interaction et contrats de données.

## Pourquoi parler de Case ?

Parce qu'une demande réelle vit dans la durée.

Elle peut changer, recevoir des événements, être réarbitrée, produire des documents, ouvrir une exception ou traverser plusieurs systèmes.

Le Case conserve le fil métier : intention, contexte, décisions, promesses, statuts, événements, documents et historique.

## Pourquoi dit-on que le processus émerge des décisions métier ?

Dans les situations simples, un workflow suffit.

Dans FLOW, beaucoup de situations dépendent du contexte : stock disponible, priorités, allocation, précommande, retard, capacité fournisseur, canal, pays ou client.

Le comportement réel doit donc être piloté par des règles, événements et décisions explicites. Le processus observé devient la conséquence de ces décisions.

## Pourquoi le Fulfillment est-il central ?

Parce que c'est le lieu de décision entre une demande à servir et des ressources limitées.

Fulfillment répond à des questions concrètes : peut-on promettre, depuis où servir, quel stock réserver, faut-il splitter, substituer, reporter, prioriser ou ouvrir une exception ?

## Pourquoi ne pas parler simplement de Master Data ?

Parce que le terme mélange trop de choses : objets ERP, données de référence, discipline MDM, projections, paramètres, règles, faits, documents.

FLOW préfère qualifier les informations avec deux questions simples :

- quelle est la nature de cette information ;
- pour cet usage, est-elle source de référence ou projection ?

## Qu'est-ce qu'une source de référence ?

Une source de référence est le domaine, l'application ou le service qui crée, valide ou maintient une information avec un processus de contrôle identifié pour un usage donné.

Elle n'est pas forcément unique pour tous les usages.

Par exemple, le PLM peut faire référence pour la conception produit, tandis qu'une projection produit d'exécution peut faire référence pour le Fulfillment.

## Pourquoi les contrats de données sont-ils importants ?

Parce qu'un flux critique n'est pas seulement un tuyau technique.

Il doit préciser l'information publiée, sa source de référence, ses consommateurs, sa fraîcheur attendue, sa qualité, son mode d'échange, sa supervision, sa reprise et sa réconciliation.

Sans cela, le SI accumule des flux projet difficiles à maintenir.

## Quels documents lire si j'ai peu de temps ?

Lire dans cet ordre :

1. [Abstract FLOW](vision/abstract.md)
2. [Positionnement de FLOW](vision/positionnement-flow.md)
3. [Abstract des principes directeurs](principes-directeurs/abstract.md)
4. [Overview de la plateforme FLOW](architecture-cible/overview-plateforme-flow.md)
5. [Glossaire](glossaire.md)

## Où trouver le vocabulaire partagé ?

Le vocabulaire stabilisé se trouve dans le [Glossaire](glossaire.md).

Les mots les plus structurants sont aussi expliqués dans [Concepts clés du programme FLOW](vision/concepts-cles.md).

## Comment contribuer sans casser la cohérence ?

Commencer par qualifier l'information ajoutée : fait observé, insight, question ouverte, principe, hotspot, concept, produit ou règle de contribution.

Puis vérifier les impacts sur la vision, les principes, l'architecture cible, le glossaire, les cartouches et les métriques.

Le [Guide de contribution éditoriale](administration/guide-contribution-contenu.md) donne la procédure complète.
