# Solution : une plateforme pour fédérer les demandes, opérations et décisions

FLOW est une <span class="flow-keyword">plateforme</span> de fédération des demandes de l'entreprise.

Elle n'a pas vocation à remplacer tout le SI.

Elle porte le cœur commun qui permet de traiter les demandes, gouverner les décisions et mobiliser les ressources d'exécution.

## Plateforme : autonomie de gouvernance et ouverture contrôlée

Une plateforme n'est pas seulement un assemblage de composants techniques.

C'est une entité autonome qui gère et gouverne un ensemble de ressources centralisées.

Dans FLOW, ces ressources sont notamment :

- Les objets de demande et leur cycle de vie.
- Les règles, décisions et politiques de traitement.
- Le <span class="flow-keyword">Stock Unifié</span>.
- Le <span class="flow-keyword">Fulfillment Network</span>.
- Les capacités d'allocation, de réservation, de promesse et d'orchestration.
- Les événements, faits, documents et vues nécessaires à la traçabilité.

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

FLOW doit être compris comme la <span class="flow-keyword">colonne vertébrale opérationnelle</span> du SI, pas comme la totalité du SI.

Il donne une structure commune aux demandes, décisions, statuts, événements, promesses, stocks et besoins d'exécution.

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

L'enjeu est d'éviter que chaque application reconstruise sa propre logique de demande, de statut, de stock, d'événement ou de décision.

<div class="flow-conviction">
  <p>FLOW ne remplace pas tous les organes du SI.</p>
  <p>FLOW reconstruit la colonne vertébrale qui leur permet de fonctionner ensemble.</p>
</div>

## Composants structurants

Ses composants structurants sont :

- Une plateforme de Case Management pour modéliser et piloter les demandes dans la durée.
- Un Stock Unifié exposé par API, capable de gérer disponibilité, réservation, allocation et calcul du stock disponible selon un contexte business.
- Un référentiel Fulfillment Network, décrivant les nœuds logistiques, leurs capacités, leurs contraintes, leurs services et leurs conditions d'usage.
- Un système de décision fondé sur des règles, contraintes et capacités d'optimisation, potentiellement augmenté par l'IA là où cela crée de la valeur.
- Un réseau d'exécution Supply connecté en continu à la demande.
- Des Vues 360 pour rendre les activités, statuts, événements et exceptions plus lisibles.
- Des intégrations avec les services existants, lorsque leur valeur métier justifie leur maintien.

## Fulfillment Network : décrire ce que le réseau sait faire

Le <span class="flow-keyword">Fulfillment Network</span> est essentiel : il ne décrit pas seulement des lieux.

Il décrit ce que le réseau sait faire.

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
    + décisions
    = traitement adapté
```

La variation métier ne doit plus augmenter mécaniquement la complexité du SI.

L'uniformisation cesse alors d'être une contrainte IT.

Elle devient un choix métier : on uniformise lorsque cela crée de la valeur, on différencie lorsque le business l'exige.

## Silos : décloisonner sans nier les organisations

FLOW doit opérer un décloisonnement fort.

Les silos B2B, B2C, retail, wholesale, marques, groupes ou canaux peuvent rester pertinents dans l'organisation, dans les expériences, dans les offres, dans les équipes et dans les pratiques business.

Ils ne doivent pas structurer le cœur de la plateforme.

Dans FLOW, une demande reste une demande.

Elle peut provenir d'un client B2C, d'un client B2B, d'un magasin, d'une marketplace, d'un service client, d'un fournisseur, d'une marque ou d'une entité du groupe.

Ce qui change, c'est le contexte, l'Agreement, les règles, les droits, les engagements, les priorités et le réseau d'exécution mobilisable.

<div class="flow-conviction">
  <p>Les consommateurs peuvent être différenciés.</p>
  <p>La plateforme doit être décloisonnée.</p>
</div>

C'est un écart majeur avec une approche ERP classique, où les variations de canal, d'organisation ou de modèle business finissent souvent par produire des modules, processus ou flux spécialisés.

FLOW doit éviter cette fragmentation.

## Périmètre : ce que FLOW n'est pas

FLOW n'est pas un ERP bis.

FLOW n'est pas seulement un OMS.

FLOW n'est pas un PIM, un CRM, un WMS, un TMS ou un outil Finance.

FLOW n'a pas vocation à absorber tout le SI.

Les expériences client, les outils métier spécialisés, les systèmes d'exécution physique, la finance, la conception produit ou les systèmes partenaires peuvent rester autonomes.

Mais FLOW doit empêcher que ces autonomies redeviennent des silos au cœur du traitement de la demande.

---

← Page précédente : [Ruptures](2-ruptures-structurantes.md) · → Page suivante : [Hotspots](4-hotspots.md)