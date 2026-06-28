# Fiche produit — Stock Unifié

## Intention

Le Stock Unifié rend le stock lisible, actionnable et gouvernable à l'échelle du groupe.

Il ne se limite pas à consolider des quantités.

Il doit permettre de calculer une disponibilité contextualisée, de réserver, d'allouer, de taguer une ressource à une finalité et de publier des faits stock exploitables par les Cases.

<div class="flow-conviction">
  <p>Le stock n'est pas seulement une donnée.</p>
  <p>C'est une capacité d'entreprise pour promettre, réserver, allouer et expliquer.</p>
</div>

## Responsabilités portées

- Consolider une vision opérationnelle du stock.
- Distinguer stock physique, stock disponible, stock réservé, stock alloué et stock promis.
- Calculer une disponibilité selon un contexte business.
- Gérer réservations et allocations / tagging.
- Consommer les mouvements de stock publiés par POS, WMS, partenaires ou systèmes logistiques.
- Publier des faits stock utilisables par les Cases et Vues 360.
- Permettre la réconciliation en cas d'écart.

## Ce que le produit ne porte pas

- Les opérations physiques de magasin, entrepôt ou transport.
- Les WMS, TMS ou POS.
- Les règles commerciales complètes de promesse si elles dépendent d'Agreements hors stock.
- La responsabilité comptable du stock.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Cases | Demander disponibilité, réservation ou allocation. |
| Engagement / canaux | Afficher une disponibilité contextualisée. |
| Supply / WMS / POS | Publier mouvements et corrections de stock. |
| Finance / contrôle | Consommer faits et écarts réconciliables. |
| Vues 360 | Afficher stock, réservations, anomalies et historique. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Stock physique observé | Fact | Projection FLOW |
| Stock disponible | Fact | Source ou dérivé FLOW |
| Réservation | Objet métier / Fact | Source FLOW |
| Allocation / tagging | Décision / Fact | Source FLOW |
| Mouvement de stock | Event | Projection consommée |
| Écart de stock | Fact | Source ou projection |
| Règle de disponibilité | Policy | Source ou projection selon gouvernance |

## Capacités candidates

- Consulter le stock disponible.
- Calculer une disponibilité contextualisée.
- Créer, confirmer, annuler ou expirer une réservation.
- Allouer / taguer du stock à une finalité.
- Consommer les mouvements de stock.
- Publier les changements de disponibilité.
- Réconcilier stock théorique et stock observé.
- Expliquer pourquoi un stock est ou n'est pas disponible.

## Interfaces candidates

- API AvailableToPromise / disponibilité.
- API ReserveStock.
- API AllocateStock / TagStock.
- API ReleaseReservation.
- Événements consommés : StockMoved, StockAdjusted, StockReceived, StockSold, StockReturned.
- Événements publiés : StockAvailabilityChanged, ReservationCreated, ReservationExpired, AllocationConfirmed.

## Premiers epics backlog

1. Définir le modèle de stock minimal.
2. Définir les sources de mouvements stock prioritaires.
3. Définir les statuts de réservation et allocation.
4. Implémenter un premier calcul de disponibilité contextualisée.
5. Exposer une API de consultation stock.
6. Exposer une API de réservation.
7. Publier les événements de disponibilité.
8. Définir les mécanismes de réconciliation.
9. Définir les exigences de fraîcheur par usage.
10. Définir les règles de preuve et auditabilité du stock.

## Questions ouvertes

- Le Stock Unifié est-il source de disponibilité ou seulement projection calculée ?
- Quelle fraîcheur minimale est nécessaire par cas d'usage ?
- Quels mouvements doivent être temps réel et lesquels peuvent rester batch ?
- Quelle frontière avec C-LOG, WMS, POS et NewStore / StoreLand pendant la transition ?
- Où placer la décision finale de promesse : Stock Unifié, Case ou service de décision ?
