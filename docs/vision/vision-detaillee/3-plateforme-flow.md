# Solution : une plateforme pour fédérer les demandes, opérations et décisions métier

<div class="flow-conviction">
  <p>FLOW ne déplace pas tout dans une nouvelle application centrale.</p>
  <p>FLOW porte ce qui doit rester cohérent, et ne porte pas ce qui relève de domaines spécialisés.</p>
</div>

FLOW est une <span class="flow-keyword">plateforme</span> de fédération des demandes de l'entreprise.

Elle n'a pas vocation à remplacer tout le SI.

Elle porte le cœur commun qui permet de traiter les demandes, gouverner les décisions métier et mobiliser les ressources d'exécution.

## Lecture synthétique : ce que FLOW porte, ce que FLOW ne porte pas

<div class="flow-conviction">
  <p>FLOW n'est pas le nouveau contenant de tout le SI.</p>
  <p>FLOW est le lieu où les demandes, les décisions métier et les ressources critiques deviennent cohérentes.</p>
</div>

| FLOW porte | FLOW ne porte pas |
| --- | --- |
| Les <span class="flow-keyword">demandes</span> et leur cycle de vie | Les expériences client, interfaces et parcours d'engagement |
| Les <span class="flow-keyword">décisions métier</span>, règles, policies et choix de traitement liés à la demande | La totalité des règles locales ou métiers lorsqu'elles relèvent d'un domaine spécialisé |
| Le <span class="flow-keyword">Stock Unifié</span>, la promesse, la réservation et l'allocation | Les opérations physiques de magasin, entrepôt, transport ou douane |
| Le <span class="flow-keyword">Fulfillment Network</span> et les capacités mobilisables | Les WMS, TMS, POS, outils fournisseurs ou systèmes d'exécution spécialisés |
| Les <span class="flow-keyword">événements</span>, statuts, documents et faits nécessaires à la traçabilité du Case | La Finance, le PLM, le PIM complet, le CRM ou les outils de conception produit |
| Les <span class="flow-keyword">contrats de données</span> et la gouvernance des échanges critiques | Les applications satellites lorsqu'elles portent une valeur métier spécifique |

Cette lecture est essentielle.

FLOW est central là où la cohérence est critique.

FLOW reste ouvert là où les domaines doivent continuer à agir, configurer, contribuer ou exécuter.

## Modèle plateforme : un cœur gouverné, des extensions ouvertes

<div class="flow-conviction">
  <p>Une plateforme n'est pas seulement un produit central.</p>
  <p>C'est un cœur gouverné qui expose des capacités contrôlées aux produits qui l'étendent.</p>
</div>

Une plateforme n'est pas seulement un assemblage de composants techniques.

C'est une entité autonome qui gère et gouverne un ensemble de ressources centralisées.

Dans FLOW, ces ressources sont notamment :

- Les objets de <span class="flow-keyword">demande</span> et leur cycle de vie.
- Les <span class="flow-keyword">décisions métier</span>, règles et politiques de traitement.
- Le <span class="flow-keyword">Stock Unifié</span>.
- Le <span class="flow-keyword">Fulfillment Network</span>.
- Les capacités d'allocation, de réservation, de promesse et d'orchestration.
- Les événements, faits, documents et vues nécessaires à la traçabilité.
- Les contrats de données qui encadrent la publication, la consommation, la fraîcheur, la qualité et la supervision des données en transit.

Mais une plateforme ne doit pas devenir un bloc fermé.

Elle doit être ouverte par conception.

Cette ouverture ne signifie pas que chacun modifie librement le cœur de la plateforme.

Elle signifie que FLOW doit proposer des processus contrôlés permettant à des acteurs externes à la plateforme de contribuer à son fonctionnement.

Par exemple :

- Configurer des éléments du réseau d'exécution : nœuds, capacités, services, contraintes, SLA.
- Développer de nouveaux types de Case ou de demandes métier.
- Définir, versionner et tester des règles.
- Construire des décisions métier contrôlées.
- Publier ou consommer des événements selon des contrats explicites.
- Publier ou consommer des données selon des contrats gouvernés.
- Exposer des extensions sans fragiliser le socle commun.

```text
Plateforme FLOW
    ↓
Gouverne des ressources centralisées
    +
Ouvre des processus contrôlés de configuration et d'extension
```

C'est ce double mouvement qui permet à FLOW d'être à la fois centralisée là où la cohérence est critique, et ouverte là où les domaines doivent conserver leur capacité d'action.

## Colonne vertébrale : réintégrer sans tout réécrire

<div class="flow-conviction">
  <p>FLOW ne remplace pas tous les organes du SI.</p>
  <p>FLOW reconstruit la colonne vertébrale qui leur permet de fonctionner ensemble.</p>
</div>

FLOW doit être compris comme la <span class="flow-keyword">colonne vertébrale opérationnelle</span> du SI, pas comme la totalité du SI.

Il donne une structure commune aux demandes, décisions métier, statuts, événements, promesses, stocks et besoins d'exécution.

Mais il ne remplace pas par principe tous les services, applications ou domaines spécialisés existants.

Les services existants qui portent une valeur métier spécifique doivent pouvoir être réintégrés autour de FLOW lorsqu'ils restent pertinents.

C'est le cas, par exemple, de CBS pour certains processus fournisseur spécialisés ou du SAV Client développé par Sarenza pour certaines demandes de service client.

Ces services peuvent rester :

- consommateurs de FLOW ;
- contributeurs de faits, documents ou événements ;
- sources spécialisées ;
- extensions métier ;
- domaines autonomes connectés à la colonne vertébrale Demand.

L'enjeu n'est donc pas de tout réécrire.

L'enjeu est d'éviter que chaque application reconstruise sa propre logique de demande, de statut, de stock, d'événement ou de décision métier.

## Données en transit : sortir de la tuyauterie projet

<div class="flow-conviction">
  <p>FLOW ne doit pas seulement remplacer des applications.</p>
  <p>Il doit remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.</p>
</div>

FLOW doit également transformer la manière dont les données circulent entre applications.

Aujourd'hui, un besoin de donnée produit souvent un flux spécifique : analyse d'une application source, spécification, développement par une équipe flux, puis consommation par une application cible.

Cette approche est efficace pour répondre à un projet, mais elle fragilise la gouvernance d'entreprise lorsque les flux se multiplient.

L'idée de demi-flux déjà imaginée côté Beaumanoir est une intuition utile : elle distingue la publication d'une donnée de sa consommation.

FLOW doit prolonger cette graine vers une logique de contrats de données gouvernés.

```text
Flux projet
    → réponse ponctuelle entre deux applications

Contrat de données
    → publication durable, consommateurs identifiés, fraîcheur, qualité, supervision et réconciliation
```

## Composants structurants

<div class="flow-conviction">
  <p>La solution FLOW n'est pas un module unique.</p>
  <p>C'est un ensemble de produits cohérents autour de la demande, du stock, du réseau d'exécution et de la décision métier.</p>
</div>

Ses composants structurants sont :

- Une plateforme de <span class="flow-keyword">Case Management</span> pour modéliser et piloter les demandes dans la durée.
- Un <span class="flow-keyword">Stock Unifié</span> exposé par API, capable de gérer disponibilité, réservation, allocation et calcul du stock disponible selon un contexte business.
- Un référentiel <span class="flow-keyword">Fulfillment Network</span>, décrivant les nœuds logistiques, leurs capacités, leurs contraintes, leurs services et leurs conditions d'usage.
- Un système de <span class="flow-keyword">décision métier</span> fondé sur des règles, contraintes et capacités d'optimisation, potentiellement augmenté par l'IA là où cela crée de la valeur.
- Un réseau d'exécution <span class="flow-keyword">Supply</span> connecté en continu à la demande.
- Des <span class="flow-keyword">Vues 360</span> pour rendre les activités, statuts, événements et exceptions plus lisibles.
- Une capacité de diffusion et gouvernance opérationnelle des données pour encadrer les contrats de données, modes d'échange, consommateurs, qualité, fraîcheur et réconciliation.
- Des intégrations avec les services existants, lorsque leur valeur métier justifie leur maintien.

## Fulfillment Network : décrire des capacités plutôt qu'une réalité physique

<div class="flow-conviction">
  <p>Le Fulfillment Network ne décrit pas seulement où sont les ressources.</p>
  <p>Il décrit ce que le réseau est capable de faire.</p>
</div>

Le <span class="flow-keyword">Fulfillment Network</span> est essentiel parce qu'il ne décrit pas seulement une réalité physique : entrepôts, magasins, partenaires ou transporteurs.

Il décrit une capacité d'exécution mobilisable par FLOW : ce que chaque nœud sait faire, dans quelles conditions, avec quelles contraintes et avec quel niveau de service.

```text
Nœud logistique
    ↓
Capacités disponibles
    ↓
Contraintes
    ↓
Services exposés
    ↓
Conditions d'usage
```

Cette approche permet à FLOW de raisonner sur la capacité réelle d'exécution, et pas seulement sur une liste d'entrepôts, de magasins ou de partenaires.

## Variation métier : maîtriser sans rigidifier

<div class="flow-conviction">
  <p>La variation métier ne doit plus créer mécaniquement de la complexité SI.</p>
  <p>Elle doit être pilotée par le contexte, les agreements, les règles et les décisions métier.</p>
</div>

Le groupe n'a pas besoin d'un modèle rigide qui impose l'uniformisation partout.

Il n'a pas non plus besoin d'un SI où chaque variation métier crée un nouveau processus, un nouveau flux, un nouveau statut ou une nouvelle application.

FLOW doit rendre possible une autre voie : un système adaptatif.

La variation de traitement doit être pilotée par :

- Le contexte de la demande.
- L'<span class="flow-keyword">Agreement</span> applicable.
- Les règles métier.
- Les politiques de priorité.
- Les contraintes de stock et d'exécution.
- Les droits et engagements du client, partenaire, fournisseur ou canal.

Cela suppose un référentiel de règles et un moteur de règles capables de piloter dynamiquement les variations.

```text
Commande ou demande générique
    + contexte
    + Agreement
    + règles
    + décisions métier
    = traitement adapté
```

L'uniformisation cesse alors d'être une contrainte IT.

Elle devient un choix métier : on uniformise lorsque cela crée de la valeur, on différencie lorsque le business l'exige.

## Silos : décloisonner sans nier les organisations

<div class="flow-conviction">
  <p>Les consommateurs peuvent être différenciés.</p>
  <p>La plateforme doit être décloisonnée.</p>
</div>

FLOW doit opérer un décloisonnement fort.

Les silos B2B, B2C, retail, wholesale, marques, groupes ou canaux peuvent rester pertinents dans l'organisation, dans les expériences, dans les offres, dans les équipes et dans les pratiques business.

Ils ne doivent pas structurer le cœur de la plateforme.

Dans FLOW, une demande reste une demande.

Elle peut provenir d'un client B2C, d'un client B2B, d'un magasin, d'une marketplace, d'un service client, d'un fournisseur, d'une marque ou d'une entité du groupe.

Ce qui change, c'est le contexte, l'Agreement, les règles, les droits, les engagements, les priorités et le réseau d'exécution mobilisable.

C'est un écart majeur avec une approche ERP classique, où les variations de canal, d'organisation ou de modèle business finissent souvent par produire des modules, processus ou flux spécialisés.

FLOW doit éviter cette fragmentation.

## Périmètre : ce que FLOW n'est pas

<div class="flow-conviction">
  <p>FLOW n'est ni un ERP bis, ni un OMS élargi, ni un outil qui absorbe tout.</p>
  <p>FLOW est la plateforme qui empêche les autonomies nécessaires de redevenir des silos.</p>
</div>

FLOW n'est pas un ERP bis.

FLOW n'est pas seulement un OMS.

FLOW n'est pas un PIM, un CRM, un WMS, un TMS ou un outil Finance.

FLOW n'a pas vocation à absorber tout le SI.

Les expériences client, les outils métier spécialisés, les systèmes d'exécution physique, la finance, la conception produit ou les systèmes partenaires peuvent rester autonomes.

Mais FLOW doit empêcher que ces autonomies redeviennent des silos au cœur du traitement de la demande.

---

← Page précédente : [Ruptures](2-ruptures-structurantes.md) · → Page suivante : [Hotspots](4-hotspots.md)
