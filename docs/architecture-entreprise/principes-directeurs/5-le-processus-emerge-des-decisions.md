# Principe 5 — Le processus émerge des décisions

## Introduction

Les systèmes d'information traditionnels sont généralement construits autour de processus.

L'objectif consiste à définir à l'avance :

* les étapes ;
* les enchaînements ;
* les documents ;
* les validations ;
* les exceptions.

Cette approche fonctionne efficacement lorsque les processus sont relativement stables et prévisibles.

Les travaux menés chez GBM et BRD montrent cependant que de nombreuses situations ne suivent pas un chemin unique.

Les ressources évoluent.

Les priorités changent.

Les contraintes apparaissent et disparaissent.

Les décisions doivent être réévaluées.

FLOW considère que dans ces contextes, le processus ne doit pas constituer le point de départ de la conception.

---

## Ce que ce principe ne signifie pas

FLOW ne remet pas en cause l'existence des processus.

FLOW ne prétend pas que les processus n'existent pas.

FLOW ne cherche pas à remplacer tous les workflows de l'entreprise.

Les processus demeurent observables.

Les processus demeurent pilotables.

Les processus demeurent mesurables.

---

## Ce que nous avons observé

### BRD

Les mécanismes de :

* précommande ;
* allocation ;
* réallocation ;
* recalcul de promesse ;

créent de nombreuses variantes de traitement.

Le processus nominal existe.

Mais les variations réelles dépendent :

* des stocks ;
* des allocations ;
* des disponibilités ;
* des arbitrages métier.

Une partie importante de cette logique est aujourd'hui dispersée dans :

* les batchs ;
* les règles locales ;
* les applications spécialisées.

---

### GBM

Les problématiques liées à :

* Ship From Store ;
* sourcing ;
* stock unifié ;
* orchestration logistique ;

montrent également que les décisions sont souvent plus importantes que le chemin théorique du processus.

Le scénario réellement exécuté dépend du contexte opérationnel observé au moment de la décision.

---

### Étude Synvance

L'étude Synvance a également mis en visibilité l'allocation comme un sujet particulièrement saillant.

Dans les besoins cibles, l'allocation apparaît comme un ensemble de règles, de priorités, de simulations, de réservations, de stocks futurs, d'événements et de réallocations.

Cela confirme que certaines problématiques ne peuvent pas être comprises uniquement comme des étapes de processus.

Elles doivent être conçues comme des décisions successives prises à partir d'un contexte métier évolutif.

---

## L'approche ERP

Les ERP modélisent généralement un macro-processus.

Par exemple :

```text
Commande
    ↓
Livraison
    ↓
Facturation
```

ou :

```text
Demande d'achat
    ↓
Commande fournisseur
    ↓
Réception
    ↓
Facturation
```

Le processus principal est visible dans le modèle.

Les objets métier possèdent :

* des états ;
* des transitions ;
* des liens.

---

## Les limites de cette approche

Lorsque les variations deviennent nombreuses, la logique finit souvent par être répartie dans :

* le paramétrage ;
* le code ;
* les interfaces ;
* les batchs ;
* les traitements spécifiques.

Le processus reste visible.

Les décisions deviennent invisibles.

---

## L'approche FLOW

FLOW considère que les décisions constituent un objet de conception de premier ordre.

Plutôt que de modéliser toutes les variantes de processus, FLOW cherche à modéliser :

* les états ;
* les événements ;
* les règles ;
* les décisions ;
* les contraintes.

Le processus devient alors une conséquence de leur interaction.

---

## Une demande évolue par décisions successives

Une demande possède un cycle de vie.

```text
Créée
    ↓
Évaluée
    ↓
Promise
    ↓
Sourcée
    ↓
Exécutée
    ↓
Résolue
```

Chaque transition résulte d'une décision prise à partir :

* des règles ;
* des événements ;
* du contexte ;
* des ressources disponibles.

---

## Les décisions deviennent explicites

FLOW cherche à rendre visibles :

* les règles métier ;
* les critères d'arbitrage ;
* les politiques de décision ;
* les événements déclencheurs ;
* les raisons ayant conduit à une décision.

Une décision doit pouvoir être :

* comprise ;
* tracée ;
* auditée ;
* modifiée ;
* simulée.

---

## Pourquoi est-ce important ?

Parce qu'une même demande peut donner naissance à plusieurs parcours différents.

Par exemple :

```text
Commande eCommerce
```

peut être :

* expédiée depuis un entrepôt ;
* expédiée depuis un magasin ;
* fractionnée ;
* réallouée ;
* mise en attente ;
* annulée.

Le modèle de demande reste identique.

Les décisions changent.

Le processus qui en résulte change également.

---

## L'allocation comme exemple

L'allocation montre concrètement pourquoi le processus émerge des décisions.

Une même demande peut être :

* préallouée ;
* allouée fermement ;
* partiellement allouée ;
* réallouée ;
* désallouée ;
* mise en attente ;
* substituée ;
* libérée pour exécution.

Ces transitions ne suivent pas toujours un workflow unique.

Elles résultent de décisions prises à partir de stocks, de priorités, d'engagements, de règles commerciales, de contraintes logistiques et d'événements opérationnels.

---

## Conséquences architecturales

Cette approche conduit naturellement à privilégier :

```text
États
    +
Événements
    +
Règles
    +
Décisions
```

plutôt que :

```text
Workflow
    +
Exceptions
    +
Sous-processus
    +
Variantes codées
```

---

## Le rôle du Case

Dans FLOW, le Case constitue le support de la demande.

Le Case :

* conserve l'état courant ;
* conserve l'historique ;
* reçoit les événements ;
* expose le contexte de décision.

Les décisions prises sur le Case déterminent son évolution.

Le processus observé est la conséquence de ces décisions successives.

---

## Les processus demeurent visibles

FLOW ne cherche pas à supprimer la notion de processus.

Les processus restent observables :

* dans la BI ;
* dans le Process Mining ;
* dans les journaux d'événements ;
* dans les indicateurs opérationnels.

Mais ils ne constituent plus l'élément central de conception.

Ils deviennent une vue de lecture du comportement du système.

---

## Insights associés

- [L'allocation révèle la vraie nature de la convergence](../../insights/allocation-point-saillant-de-la-convergence.md)
- [La demande comme point d’entrée de la modélisation FLOW](../../insights/demande-point-entree-modelisation.md)

## À retenir

Les ERP modélisent principalement des processus et des documents.

FLOW modélise principalement des demandes, des règles, des événements et des décisions.

Le processus n'est pas défini à l'avance dans toutes ses variantes.

Il émerge des décisions prises sur le Case.

Les processus s'observent.

Les décisions se conçoivent.

