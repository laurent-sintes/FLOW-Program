# La facturation n'est pas un domaine, c'est un assemblage de responsabilités

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Sponsor, Contributeur</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Contexte

Les échanges autour de SAP SD, SAP FI/CO et de la convergence Finance ont mis en évidence une question fondamentale :

> À qui appartient réellement la responsabilité de facturer ?

L'analyse montre que le terme « facturation » recouvre en réalité plusieurs responsabilités distinctes.

## Le biais des applications

Les organisations ont tendance à attribuer une responsabilité au système qui la porte aujourd'hui.

Ainsi :

```text
Facturation = SAP SD
```

Cette lecture est pratique mais masque la réalité du problème métier.

SAP SD agrège aujourd'hui plusieurs responsabilités différentes.

## Décider qu'une facture doit être émise

Cette décision dépend :

- de l'état de la demande ;
- du contrat ;
- du canal ;
- du client ;
- du contexte réglementaire.

Par exemple :

```text
Commande expédiée
    ↓
Facture autorisée
```

ou :

```text
Paiement reçu
    ↓
Facture autorisée
```

Cette responsabilité relève principalement de la gestion des engagements et des demandes.

Elle appartient naturellement au domaine Demand.

## Produire le document

Une fois la décision prise, il faut produire un document.

Cette capacité consiste à transformer :

```text
Informations
+
Template
↓
Document
```

Elle s'applique à :

- factures ;
- avoirs ;
- bons de livraison ;
- confirmations de commande ;
- contrats ;
- documents réglementaires.

Cette responsabilité ressemble davantage à une capacité documentaire transverse qu'à une responsabilité Finance.

## Comptabiliser l'événement économique

Une fois le document produit, l'événement économique doit être enregistré.

Cette responsabilité couvre :

- les écritures comptables ;
- la TVA ;
- les comptes comptables ;
- les centres de coûts ;
- le contrôle de gestion.

Cette responsabilité appartient naturellement au domaine Finance.

## Insight

La facturation n'est probablement pas un domaine métier autonome.

Elle correspond à l'assemblage de plusieurs responsabilités appartenant à des domaines différents.

```text
Demand
    └─ Décider qu'une facture est exigible

Document Management
    └─ Produire le document

Finance
    └─ Comptabiliser l'événement économique
```

## Enseignement pour FLOW

L'analyse des domaines ne doit pas partir des applications existantes.

Elle doit partir des responsabilités durables de l'entreprise.

Une capacité peut être portée aujourd'hui par un ERP sans pour autant appartenir au domaine fonctionnel que cet ERP représente historiquement.

## À retenir

Les domaines avant les applications.

La facturation n'est pas une responsabilité unique.

Elle combine :

- une décision ;
- une production documentaire ;
- une comptabilisation.

Ces responsabilités peuvent appartenir à des domaines différents tout en étant aujourd'hui implémentées dans le même produit.
