# Fiche produit — Fulfillment Network Configuration

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
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Fulfillment Network Configuration décrit le réseau d'exécution mobilisable par FLOW.

Il ne s'agit pas seulement d'une liste d'entrepôts, de magasins ou de partenaires.

Le produit décrit ce que chaque nœud sait faire, dans quelles conditions, avec quelles contraintes, quels services et quel niveau de service.

<div class="flow-conviction">
  <p>Le réseau d'exécution ne décrit pas seulement une réalité physique.</p>
  <p>Il décrit des capacités d'action mobilisables pour satisfaire une demande.</p>
</div>

## Responsabilités portées

- Référencer les nœuds du réseau d'exécution.
- Décrire les capacités associées aux nœuds.
- Décrire les services exposés : préparation, expédition, retour, réassort, click & collect, dropship, etc.
- Porter contraintes, SLA, conditions d'usage et périmètres d'éligibilité.
- Alimenter les décisions de promesse, sourcing, allocation et orchestration.
- Fournir une configuration gouvernée mais ouverte à contribution contrôlée.

## Ce que le produit ne porte pas

- L'exécution physique elle-même.
- Le WMS, TMS, POS ou transport opérationnel.
- Les contrats juridiques complets avec partenaires.
- Le calcul final de décision si celui-ci dépend du Case, du stock et des Agreements.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Cases | Identifier les options d'exécution possibles. |
| Stock Unifié | Contextualiser la disponibilité par nœud ou service. |
| Supply / C-LOG / partenaires | Déclarer capacités, contraintes, SLA et événements. |
| Engagement | Comprendre les services disponibles par contexte. |
| Architecture / PM | Gouverner le découpage du réseau cible. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Nœud d'exécution | Objet métier / Nomenclature | Source de référence FLOW si gouverné par FLOW |
| Capacité d'exécution | Policy / Nomenclature | Source de référence FLOW |
| Service Supply | Objet métier / Nomenclature | Source de référence ou projection |
| Contrainte d'usage | Policy | Source de référence FLOW ou projection Supply |
| SLA | Policy / Fact | Projection ou source de référence selon gouvernance |
| Zone de couverture | Nomenclature / Policy | Source de référence ou projection |

## Capacités candidates

- Créer et maintenir un nœud d'exécution.
- Déclarer les capacités d'un nœud.
- Déclarer les services disponibles.
- Configurer contraintes, SLA, jours d'ouverture, cut-off, zones et restrictions.
- Exposer les capacités disponibles pour une demande.
- Versionner la configuration.
- Auditer les changements de configuration.

## Interfaces candidates

- API de consultation du réseau.
- API de recherche de nœuds éligibles.
- API de configuration contrôlée.
- Événements publiés : FulfillmentNodeUpdated, CapabilityChanged, ServiceAvailabilityChanged.
- Événements consommés : service indisponible, contrainte logistique, fermeture exceptionnelle.

## Premiers epics backlog

1. Définir le modèle de nœud d'exécution.
2. Définir la nomenclature des capacités.
3. Définir la nomenclature des services Supply.
4. Configurer un premier réseau pilote.
5. Exposer une API de recherche de capacités.
6. Définir la gouvernance de modification du réseau.
7. Versionner et auditer les configurations.
8. Connecter le réseau à la décision de promesse.
9. Définir les événements de changement de capacité.
10. Clarifier les responsabilités C-LOG / WMS / partenaires.

## Questions ouvertes

- Qui est owner de la configuration du réseau : FLOW, Supply, C-LOG, marques ?
- Quels éléments sont sources de référence dans FLOW et lesquels sont projections Supply ?
- Comment gérer les capacités temporaires ou saisonnières ?
- Quelle granularité de nœud : entrepôt, zone, magasin, partenaire, service ?
- Comment éviter que la configuration réseau devienne un nouveau fourre-tout applicatif ?
