# Fiche produit — Socle Case Management

## Intention

Le Socle Case Management fournit le cœur applicatif permettant de modéliser, piloter et faire évoluer les demandes dans la durée.

Il ne s'agit pas seulement d'un moteur de workflow.

Le produit doit permettre de construire des objets métier de type Case, capables de porter une intention, un contexte, des décisions, des événements, des documents, des ressources mobilisées et un état courant.

<div class="flow-conviction">
  <p>Le Case est l'unité autonome de décision et d'orchestration.</p>
  <p>Le socle fournit le runtime, mais ce sont les Cases qui portent la logique métier.</p>
</div>

## Pourquoi un socle Case Management ?

Le Case Management répond à une limite des modèles classiques d'orchestration.

Dans un modèle <span class="flow-keyword">document-centric</span>, typique des grands ERP, le processus métier est implicite dans le graphe des documents et des transactions.

```text
Sales Order → Delivery → Invoice
```

Ce modèle est robuste pour la cohérence transactionnelle, mais il rend le processus d'entreprise structurellement difficile à modifier. Le périmètre de décision reste centré sur la transaction.

Dans un modèle <span class="flow-keyword">process-centric</span>, typique BPMN, le processus devient explicite et configurable.

```text
Initialiser → Vérifier disponibilité → Valider → Préparer → Livrer
```

Ce modèle rend l'organisation plus visible, mais le processus reste largement prédéfini. Il est configurable, mais il demeure fixe au moment de l'exécution.

Le modèle <span class="flow-keyword">case-centric</span> introduit une rupture : le processus n'est plus le point de départ. Il émerge des décisions prises sur une demande, au regard de son contexte, des faits observés, des règles métier et des événements d'exécution.

<div class="flow-conviction">
  <p>Le processus émerge des décisions prises sur le Case.</p>
  <p>L'exécution de la demande influence la décision et adapte continuellement le plan d'exécution.</p>
</div>

## Modèles d'orchestration comparés

| Modèle | Point de départ | Processus | Périmètre de décision | Limite principale |
| --- | --- | --- | --- | --- |
| Document-centric | Document / transaction | Implicite dans le graphe documentaire | Transaction | Processus structurellement difficile à modifier. |
| Process-centric | Processus BPMN | Explicite et configurable | Processus | Processus visible mais fixé par conception. |
| Case-centric | Demande / Case | Émergent et adaptable | Environnement de la demande | Nécessite une gouvernance forte des décisions, événements et règles. |

Cette comparaison est structurante pour FLOW.

FLOW ne cherche pas seulement à remplacer un OMS ou un ERP par un autre outil. Il déplace le centre de gravité de l'orchestration vers la <span class="flow-keyword">Demande</span>.

## Boucle opérationnelle du Case

Un Case doit pouvoir apprendre de ce qui se passe pendant son exécution.

La boucle cible peut être exprimée ainsi :

```text
J'observe
    ↓
Je comprends
    ↓
Je décide
    ↓
Je planifie
    ↓
J'agis
    ↓
J'apprends
```

Cette boucle articule plusieurs composants :

- les événements qui décrivent ce qui s'est passé ;
- les faits qui rendent la situation exploitable pour décider ;
- les policies et règles qui guident la décision ;
- le plan d'orchestration qui organise l'action ;
- les systèmes d'exécution qui réalisent les opérations ;
- les retours d'exécution qui adaptent le Case.

## Modèle conceptuel minimal d'un Case

Un Case représente une demande à instruire dans la durée.

Il doit porter au minimum :

| Élément | Rôle |
| --- | --- |
| Request | Expression de la demande, proche d'une user story métier. |
| Requester | Personne, système, client, fournisseur ou organisation qui demande. |
| Goal | Résultat attendu. |
| Intent | Intention ou raison métier de la demande. |
| Policy model | Ensemble des règles, contraintes et politiques applicables. |
| State | État courant de la demande. |
| Event log | Historique immuable de ce qui s'est passé. |
| Attachments | Documents attachés : facture, bon de livraison, preuve, justificatif, échange client. |
| Aggregate views / Vues 360 | Lectures agrégées utiles autour du Case, du client, de la commande ou du fournisseur. |
| Statistics | Indicateurs d'exécution, durée, exceptions, qualité ou performance. |

Ce modèle doit rester générique : le Case peut représenter une commande client, un retour, un litige SAV, une demande fournisseur, une exception stock ou une demande d'achat.

## Responsabilités portées

- Modéliser les types de demandes / Cases.
- Porter le cycle de vie d'une demande dans la durée.
- Enregistrer les décisions, événements, statuts, documents et faits associés.
- Orchestrer les interactions avec les produits FLOW et les systèmes externes.
- Supporter les transactions longues, exceptions, retours, SAV, commandes et demandes fournisseur.
- Permettre la traçabilité et l'explicabilité d'une demande.
- Fournir un cadre contrôlé pour développer de nouveaux types de Case.
- Adapter le plan d'exécution au fil des événements et des faits observés.
- Déléguer l'organisation opérationnelle à des API, systèmes d'exécution, IAM / IDP et applications satellites.

## Ce que le produit ne porte pas

- Les expériences client ou interfaces d'engagement.
- Les opérations physiques de stock, entrepôt, magasin ou transport.
- La comptabilité et les écritures financières.
- Le PLM, le PIM complet ou le CRM.
- Les règles métier globales lorsqu'elles appartiennent à un domaine spécialisé hors FLOW.
- Les systèmes spécialisés qui exécutent une tâche opérationnelle mais ne portent pas la demande.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Canaux d'engagement | Créer ou suivre une demande. |
| Services client / SAV | Piloter litiges, retours, remboursements ou exceptions. |
| Produits FLOW | Fournir décisions, stock, promesse, réseau d'exécution ou projections. |
| Supply | Recevoir des besoins d'exécution et publier des événements. |
| Finance | Consommer faits, statuts, documents ou références nécessaires à la comptabilité. |
| IAM / IDP / API Gateway | Sécuriser délégations, accès et interactions externes. |
| PO / équipes domaine | Développer de nouveaux types de Case selon un cadre contrôlé. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Case | Objet métier | Source FLOW |
| Request | Command / Objet métier | Source consommateur, traitée par FLOW |
| Requester | Projection / Objet métier selon domaine | Source externe ou projection FLOW |
| Goal / Intent | Fact / Policy selon usage | Source FLOW |
| Command de création / action | Command | Source consommateur, traitée par FLOW |
| Événement de Case | Event | Source FLOW |
| Event log | Event | Source FLOW |
| Fact de situation | Fact | Dérivé FLOW ou projection consommée |
| Décision de Case | Decision / Fact | Source FLOW ou projection |
| Policy model | Policy | Source FLOW ou projection selon gouvernance |
| Document attaché | Document | Source ou projection selon origine |
| Statut de Case | Fact / Nomenclature | Source FLOW |
| Contexte client / fournisseur / produit | Projection | Projection FLOW |
| Vue 360 | Projection | Dérivé FLOW |

## Décision, événement et fait

Le Case Management doit distinguer explicitement trois notions.

| Notion | Définition opérationnelle | Exemple |
| --- | --- | --- |
| Event | Quelque chose qui s'est passé, immuable, horodaté et explicite. | ShippingConfirmed, StockReserved, PaymentCaptured. |
| Fact | Information exploitable pour prendre une décision, souvent dérivée d'un ou plusieurs événements. | Le stock disponible est insuffisant ; le client est prioritaire ; la livraison est en retard. |
| Decision | Choix effectué dans un contexte donné, guidé par des policies, règles ou contraintes. | Choisir SFS plutôt que entrepôt ; annuler une ligne ; déclencher un remboursement. |

Cette distinction évite de coder la logique métier directement dans un processus figé.

La décision est guidée par la <span class="flow-keyword">Business Policy</span> plutôt que codée dans les enchaînements de tâches.

## Capacités candidates

- Définir un type de Case.
- Créer un Case.
- Piloter son cycle de vie.
- Attacher un document.
- Enregistrer une décision.
- Générer ou consommer des faits de situation.
- Publier un événement de changement d'état.
- Adapter le plan d'exécution en fonction des événements.
- Corréler un Case avec une commande, un client, un fournisseur ou une exécution.
- Rejouer ou reconstruire l'histoire d'un Case.
- Exposer une lecture Case 360.
- Gérer les exceptions et escalades.
- Déléguer des tâches à des systèmes d'exécution via API.

## Interfaces candidates

- API de création de Case.
- API de consultation de Case.
- API d'action sur Case.
- API de publication ou réception de documents.
- API d'explication de décision.
- Événements publiés : CaseCreated, CaseUpdated, CaseDecisionTaken, CaseStatusChanged, CasePlanAdapted, CaseClosed.
- Événements consommés : stock movement, allocation result, supply status, shipping confirmation, document received, payment / finance status, customer notification status.
- Intégration avec moteur de règles, workflow, CEP, IAM / IDP, API Gateway et produits FLOW.

## Architecture candidate du socle

Le socle peut combiner plusieurs composants spécialisés.

| Composant | Rôle probable |
| --- | --- |
| Framework de développement de Case | Permettre de créer des objets métier Case robustes, extensibles et gouvernés. |
| Moteur de règles | Évaluer policies, règles, conditions et décisions métier. |
| CEP / Situation Engine | Transformer événements et signaux en faits exploitables par les décisions. |
| Moteur de workflow / orchestration | Piloter les tâches longues, compensations, attentes et interactions systèmes. |
| Event log | Historiser l'exécution et permettre audit, reconstruction et explication. |
| API sécurisées | Exposer les actions de Case aux domaines consommateurs et applications satellites. |
| Vues 360 | Agréger l'information autour du Case, du client, de la commande ou du fournisseur. |

Cette architecture doit éviter une confusion : le moteur de workflow n'est qu'un composant du socle. Il ne doit pas redevenir le centre du modèle.

<div class="flow-conviction">
  <p>Le workflow exécute une partie du plan.</p>
  <p>Le Case porte la demande, le contexte, les décisions et l'histoire.</p>
</div>

## Impacts produit pour FLOW

Le Socle Case Management doit permettre de traiter toutes les demandes métier, au-delà de la seule vente.

Exemples de familles de Case candidates :

- commande client ;
- retour ;
- litige SAV ;
- remboursement ;
- annulation pour rupture ;
- demande d'achat ;
- exception stock ;
- demande fournisseur ;
- demande de réallocation ou de priorisation.

Chaque demande doit être traitée comme un petit projet : elle a un objectif, un contexte, des décisions, des événements, des documents, des acteurs, un plan d'action et une histoire.

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
11. Prototyper la boucle observer / comprendre / décider / agir sur un cas réel.
12. Définir le Situation Engine minimal permettant de produire des faits à partir d'événements.
13. Définir les contrats entre Case, moteur de règles, workflow et systèmes d'exécution.
14. Définir les règles d'explication : pourquoi telle décision a été prise, sur quels faits et selon quelles policies.

## Questions ouvertes

- Quels types de Case doivent être pilotes : commande, retour, SAV, commande d'achat, exception stock ?
- Quel niveau de standardisation du cycle de vie est acceptable ?
- Comment séparer la logique Case du moteur de workflow ?
- Où sont exécutées les règles : dans le Case, dans un service de décision ou dans les domaines ?
- Quelles responsabilités restent dans les systèmes existants réintégrés ?
- Jusqu'où le Case doit-il porter le plan d'exécution, et où commence le rôle des systèmes Supply ?
- Quel modèle d'auditabilité faut-il pour réconcilier Case Management, DataHub, finance et Vues 360 ?
- Comment sécuriser la délégation aux applications satellites sans recréer des silos ?
- Quel niveau d'autonomie donner aux domaines pour créer de nouveaux types de Case ?