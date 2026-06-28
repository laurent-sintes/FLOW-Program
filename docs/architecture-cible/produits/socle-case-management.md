# Fiche produit — Socle Case Management

## Intention

Le Socle Case Management fournit le cœur applicatif permettant de modéliser, piloter et faire évoluer les demandes dans la durée.

Il ne s'agit pas seulement d'un moteur de workflow.

Le produit doit permettre de construire des objets métier de type Case, capables de porter une intention, un contexte, des décisions, des événements, des documents, des ressources mobilisées et un état courant.

<div class="flow-conviction">
  <p>Le Case est l'unité autonome de décision et d'orchestration.</p>
  <p>Le socle fournit le runtime, mais ce sont les Cases qui portent la logique métier.</p>
</div>

## Responsabilités portées

- Modéliser les types de demandes / Cases.
- Porter le cycle de vie d'une demande dans la durée.
- Enregistrer les décisions, événements, statuts, documents et faits associés.
- Orchestrer les interactions avec les produits FLOW et les systèmes externes.
- Supporter les transactions longues, exceptions, retours, SAV, commandes et demandes fournisseur.
- Permettre la traçabilité et l'explicabilité d'une demande.
- Fournir un cadre contrôlé pour développer de nouveaux types de Case.

## Ce que le produit ne porte pas

- Les expériences client ou interfaces d'engagement.
- Les opérations physiques de stock, entrepôt, magasin ou transport.
- La comptabilité et les écritures financières.
- Le PLM, le PIM complet ou le CRM.
- Les règles métier globales lorsqu'elles appartiennent à un domaine spécialisé hors FLOW.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Canaux d'engagement | Créer ou suivre une demande. |
| Services client / SAV | Piloter litiges, retours, remboursements ou exceptions. |
| Produits FLOW | Fournir décisions, stock, promesse, réseau d'exécution ou projections. |
| Supply | Recevoir des besoins d'exécution et publier des événements. |
| Finance | Consommer faits, statuts, documents ou références nécessaires à la comptabilité. |
| PO / équipes domaine | Développer de nouveaux types de Case selon un cadre contrôlé. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Case | Objet métier | Source FLOW |
| Command de création / action | Command | Source consommateur, traitée par FLOW |
| Événement de Case | Event | Source FLOW |
| Décision de Case | Policy / Fact selon usage | Source FLOW ou projection |
| Document attaché | Document | Source ou projection selon origine |
| Statut de Case | Fact / Nomenclature | Source FLOW |
| Contexte client / fournisseur / produit | Projection | Projection FLOW |

## Capacités candidates

- Définir un type de Case.
- Créer un Case.
- Piloter son cycle de vie.
- Attacher un document.
- Enregistrer une décision.
- Publier un événement de changement d'état.
- Corréler un Case avec une commande, un client, un fournisseur ou une exécution.
- Rejouer ou reconstruire l'histoire d'un Case.
- Exposer une lecture Case 360.
- Gérer les exceptions et escalades.

## Interfaces candidates

- API de création de Case.
- API de consultation de Case.
- API d'action sur Case.
- Événements publiés : CaseCreated, CaseUpdated, CaseDecisionTaken, CaseStatusChanged, CaseClosed.
- Événements consommés : stock movement, allocation result, supply status, document received, payment / finance status.
- Intégration avec moteur de règles, workflow, CEP et produits FLOW.

## Premiers epics backlog

1. Définir le modèle minimal de Case.
2. Définir le cycle de vie standard d'un Case.
3. Créer un premier type de Case pilote.
4. Gérer documents et pièces attachées.
5. Publier les événements de Case.
6. Consommer une décision de stock / promesse.
7. Exposer une vue de suivi opérationnel du Case.
8. Définir les mécanismes de corrélation avec systèmes externes.
9. Poser les règles d'auditabilité et d'historisation.
10. Définir le cadre d'extension par les domaines consommateurs.

## Questions ouvertes

- Quels types de Case doivent être pilotes : commande, retour, SAV, commande d'achat, exception stock ?
- Quel niveau de standardisation du cycle de vie est acceptable ?
- Comment séparer la logique Case du moteur de workflow ?
- Où sont exécutées les règles : dans le Case, dans un service de décision ou dans les domaines ?
- Quelles responsabilités restent dans les systèmes existants réintégrés ?
