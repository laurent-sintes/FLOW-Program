# Fiche produit — Vues 360

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

Les Vues 360 agrègent les informations nécessaires pour comprendre une activité, un client, un fournisseur, une commande ou un Case.

Elles ne sont pas la source de référence de toutes les données.

Elles fournissent une lecture transverse, principalement en consultation, alimentée par les événements, faits, documents, statuts et décisions.

Leur positionnement est renforcé par le rôle du Case Management : si FLOW devient un hub de Business Events et de Shared Business Services, il devient aussi le lieu naturel où matérialiser des vues transverses utiles aux opérations.

<div class="flow-conviction">
  <p>Une Vue 360 ne remplace pas les sources de référence.</p>
  <p>Elle rend l'activité lisible autour d'un objet ou d'un acteur.</p>
</div>

## Responsabilités portées

- Agréger les données autour d'un Case, d'un client, d'un fournisseur ou d'une commande.
- Exposer une lecture transverse des statuts, événements, décisions et documents.
- Aider les opérations, le service client, la finance et les métiers à comprendre une situation.
- Contribuer à l'observabilité métier.
- Réduire le besoin de naviguer entre plusieurs applications pour retrouver une vérité opérationnelle.

## Ce que le produit ne porte pas

- La création ou validation des données métier comme sources de référence.
- Les règles de décision qui font évoluer un Case.
- La responsabilité complète CRM ou MDM.
- Les interfaces d'expérience client complètes.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Opérations | Comprendre l'état d'une demande ou exécution. |
| SAV / service client | Expliquer une situation client. |
| Finance / contrôle | Retrouver faits, documents et statuts. |
| PO / PM | Identifier les données manquantes et les besoins de projection. |
| Sources de référence | Publier événements, faits ou documents. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Case 360 | Projection / Vue | Dérivée FLOW |
| Customer 360 | Projection | Projection multi-sources |
| Supplier 360 | Projection | Projection multi-sources |
| Order / Case 360 | Projection | Dérivée Case + sources de référence externes |
| Historique événements | Event | Projection agrégée |
| Documents associés | Document | Projection ou référence |
| Décisions et statuts | Fact / Event | Projection agrégée |

## Capacités candidates

- Rechercher une Vue 360 par identifiant.
- Agréger événements et statuts autour d'un Case.
- Agréger documents et références.
- Exposer une chronologie métier.
- Identifier les écarts ou incohérences visibles.
- Restituer les décisions et règles appliquées lorsqu'elles sont disponibles.
- Fournir une vue lecture seule aux consommateurs.

## Interfaces candidates

- API Case 360.
- API Customer 360.
- API Supplier 360.
- API timeline / historique.
- Événements consommés : Case events, stock events, supply events, document events, finance events.
- Événements publiés éventuels : ViewRefreshed, InconsistencyDetected.

## Premiers epics backlog

1. Définir les premières Vues 360 prioritaires.
2. Définir le modèle de timeline transverse.
3. Définir les sources de référence et projections nécessaires.
4. Exposer une première Case 360.
5. Intégrer les documents associés.
6. Intégrer les décisions et statuts.
7. Ajouter les événements Supply et stock.
8. Définir les règles d'accès et confidentialité.
9. Définir les alertes d'incohérence visibles.
10. Tester la valeur sur un cas SAV ou litige.

## Questions ouvertes

- Case 360 et Order 360 sont-ils une même vue avec plusieurs alias métier ?
- Quelles vues sont prioritaires : client, fournisseur, Case, commande ?
- Quelle fraîcheur est attendue par usage ?
- Les Vues 360 doivent-elles seulement lire ou aussi déclencher des actions ?
- Quel niveau de détail est nécessaire pour Finance et audit ?
