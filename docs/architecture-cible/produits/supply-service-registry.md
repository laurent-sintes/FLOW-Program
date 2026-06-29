# Fiche produit — Supply Service Registry

## Intention

Le Supply Service Registry référence les services Supply que FLOW peut mobiliser.

Il décrit les APIs, événements, SLA, conditions d'appel, contraintes et responsabilités des services d'exécution.

Il permet aux Cases de dialoguer avec Supply sans connaître directement toutes les implémentations locales.

<div class="flow-conviction">
  <p>FLOW ne doit pas connaître toute l'exécution en détail.</p>
  <p>Il doit connaître les services Supply mobilisables et leurs contrats.</p>
</div>

## Responsabilités portées

- Référencer les services Supply consommables.
- Décrire leurs contrats d'interface.
- Documenter SLA, contraintes, périmètres et conditions d'appel.
- Clarifier les événements attendus en retour.
- Supporter la réintégration de services existants : C-LOG, CBS, WMS, transporteurs, outils fournisseurs.

## Ce que le produit ne porte pas

- L'exécution physique des opérations.
- Le monitoring technique complet des systèmes externes.
- Les règles métier internes des systèmes Supply.
- La gouvernance contractuelle juridique avec les partenaires.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Cases | Identifier et appeler un service Supply. |
| Supply / C-LOG / CBS / WMS | Publier leurs capacités et contrats. |
| Architecture / intégration | Gouverner les interfaces et contrats. |
| Observabilité | Suivre disponibilité, SLA et incidents. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Service Supply | Objet métier / Nomenclature | Source FLOW ou projection Supply |
| API exposée | Nomenclature / Document | Source FLOW |
| SLA | Policy | Source ou projection |
| Contrat d'événement | Document / Policy | Source FLOW |
| Éligibilité service | Policy | Source ou projection |
| Statut de service | Fact | Projection |

## Capacités candidates

- Déclarer un service Supply.
- Décrire ses interfaces.
- Décrire les événements qu'il publie ou consomme.
- Décrire ses SLA et conditions d'appel.
- Rechercher un service éligible.
- Versionner un contrat de service.
- Suivre les dépendances entre Case et service Supply.

## Interfaces candidates

- API de consultation registry.
- API de publication / modification contrôlée de service.
- Événements publiés : SupplyServiceRegistered, SupplyServiceUpdated, SupplyContractChanged.
- Événements consommés : service unavailable, SLA degraded, contract updated.

## Premiers epics backlog

1. Définir le modèle minimal d'un service Supply.
2. Référencer les premiers services candidats : C-LOG, CBS, WMS, transport.
3. Définir les métadonnées d'API et d'événements.
4. Définir les SLA et contraintes minimales.
5. Exposer la recherche de services éligibles.
6. Gérer le versioning des contrats.
7. Définir le processus d'onboarding d'un service existant.
8. Connecter le registry au Case Management.
9. Mettre en place une première lecture d'observabilité.
10. Définir les critères conserver / encapsuler / remplacer.

## Questions ouvertes

- Le registry est-il un produit FLOW autonome ou une partie du Fulfillment Network ?
- Qui maintient les contrats : FLOW, Supply, architecture, intégration ?
- Les usines BRD et leurs lead times doivent-ils être modélisés comme services Supply, comme capacités de fabrication ou comme projections issues d'un référentiel spécialisé ?
- Quels services doivent être obligatoirement event-driven ?
- Quels systèmes existants ne peuvent pas être réintégrés sans évolution technique ?
