# Agreement comme Pivot

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
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Constat

Les différences entre Achat, B2B, B2C, retail, wholesale ou marketplace ne proviennent pas principalement de la demande.

Elles proviennent du cadre d'engagement applicable.

Une commande peut rester relativement générique si son traitement est piloté par son contexte, par l'Agreement applicable et par des règles explicites.

## Agreement

Agreement représente notamment :

- contrat client ;
- accord fournisseur ;
- assortiment ;
- prix ;
- allocations ;
- SLA ;
- conditions de livraison ;
- droits ;
- priorités ;
- conditions de retour ou de remboursement ;
- contraintes commerciales ou opérationnelles.

## Pourquoi c'est central

Sans Agreement, la tentation est forte de décliner les commandes et les processus par canal, marque, type de client, type de vente ou modèle opérationnel.

On finit alors par multiplier les variantes :

```text
commande B2C
commande B2B
commande retail
commande wholesale
commande marketplace
commande fournisseur
commande premium
commande marque A
commande marque B
...
```

Cette approche rend le modèle rigide.

Chaque variation de règle devient une variation de processus.

Agreement propose une autre lecture.

Les commandes peuvent rester plus génériques si les différences de traitement sont portées par :

```text
contexte de la commande
    + Agreement applicable
    + référentiel de règles
    + moteur de règles
```

Le traitement devient alors dynamique.

La commande n'a pas besoin d'embarquer toutes les variantes de processus.

Elle peut être instruite selon les règles et conditions applicables à son contexte.

## Conséquence pour FLOW

La plateforme FLOW doit séparer :

```text
Agreement
    ↓
Demand
    ↓
Decision
    ↓
Execution
```

plutôt que d'encapsuler toutes les règles dans les demandes ou de spécialiser excessivement les commandes.

Agreement devient le lieu conceptuel où l'on rattache les conditions de traitement.

Les règles peuvent ensuite être externalisées dans un référentiel ou un moteur de règles, afin de piloter dynamiquement les variations.

## Insight

La valeur d'Agreement n'est pas seulement de représenter un contrat ou un accord commercial.

Sa valeur est de réduire la prolifération des processus et objets spécialisés.

FLOW peut alors traiter des commandes plus génériques, tout en adaptant leur comportement selon le contexte et les règles applicables.
