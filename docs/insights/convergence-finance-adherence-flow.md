# La convergence Finance constitue une adhérence forte pour FLOW

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecture, sponsors, contributeurs</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Contexte

Chez GBM comme chez BRD, la facturation et l'intégration comptable reposent fortement sur SAP.

Les deux groupes disposent de SAP FI/CO pour la comptabilité et le contrôle de gestion.

Ils disposent également de SAP SD afin de faciliter l'intégration des orders, des factures et des événements économiques dans FI/CO.

## Ce que nous avons observé

### B2C

En B2C, la facture est généralement produite par le système d'engagement client ou de vente :

- site eCommerce ;
- marketplace ;
- POS retail.

Les commandes et les factures sont ensuite intégrées dans SAP afin d'alimenter :

- la comptabilité ;
- le contrôle de gestion ;
- les mécanismes de reporting financier.

Dans ce modèle, SAP SD joue un rôle de support d'intégration vers SAP FI/CO.

### B2B

En B2B, la facture est produite directement par SAP SD.

SAP SD est utilisé pour :

- déterminer quand la facture doit être émise ;
- appliquer les règles documentaires ;
- sélectionner le modèle de facture ;
- assurer l'intégration native avec SAP FI/CO.

## Constat

La production de facture est aujourd'hui éparpillée.

Elle dépend :

- du canal ;
- du business model ;
- du type de client ;
- du système qui porte l'expérience ou la vente.

Néanmoins, les deux groupes convergent vers une même logique cible :

```text
SAP SD
    ↓
SAP FI/CO
```

comme socle commun de facturation B2B, de comptabilité et de contrôle de gestion.

## Arbitrage structurant

Le programme SAP Finance / migration S/4HANA, hors périmètre FLOW, a arbitré la conservation de SAP SD/FI/CO comme socle de :

- facturation B2B ;
- comptabilité ;
- contrôle de gestion.

Cette trajectoire constitue un arbitrage structurant déjà engagé.

## Insight

Toutes les capacités de convergence ne convergent pas dans FLOW.

La convergence Finance autour de SAP existe déjà.

Elle n'est pas dans le périmètre de FLOW, mais elle constitue une adhérence forte pour FLOW.

FLOW doit donc se concevoir en tenant compte :

- des responsabilités conservées dans SAP ;
- des événements attendus par SAP ;
- des contraintes de facturation ;
- des besoins de contrôle de gestion ;
- des choix structurants du programme S/4HANA.

## Conséquence pour FLOW

La question n'est pas :

> FLOW doit-il remplacer SAP SD ou SAP FI/CO ?

La question est plutôt :

> Quels événements opérationnels et économiques FLOW doit-il transmettre au domaine Finance afin de permettre la facturation, la comptabilité et le contrôle de gestion ?

FLOW doit donc clarifier son articulation avec la Finance autour :

- des orders ;
- des factures ;
- des événements économiques ;
- des écritures comptables ;
- des comptes rendus d'événements.

## À retenir

La convergence Finance est portée par SAP.

FLOW ne remet pas en cause cette trajectoire.

FLOW doit cependant s'intégrer proprement avec elle.

Cette adhérence est structurante pour l'urbanisme cible, car elle rappelle que FLOW n'est pas le futur ERP unique mais une plateforme d'entreprise qui coexiste avec d'autres socles de responsabilité.
