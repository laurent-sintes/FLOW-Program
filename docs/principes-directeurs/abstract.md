# Abstract des principes directeurs

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Métier, Sponsor</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Les principes directeurs de FLOW servent à éviter que chaque décision soit rejouée de zéro.

Ils forment une doctrine simple : FLOW ne cherche pas à remplacer une application par une autre, ni à uniformiser tous les modèles du groupe. FLOW cherche à construire une plateforme de cohérence autour des demandes, des décisions, des promesses, des ressources mobilisables et des informations qui circulent entre domaines.

## Message en une minute

FLOW doit créer du commun là où l'incohérence coûte cher.

Ce commun ne se construit pas en imposant un processus unique ou un monolithe applicatif.

Il se construit en clarifiant les responsabilités durables, en rendant les décisions explicites, en traitant la demande comme objet central, et en gouvernant les informations selon leur rôle réel : source de référence, projection ou information en transit.

## Les sept principes en synthèse

| Principe | Règle courte | Ce que cela protège |
| --- | --- | --- |
| [01 — Construire le bon niveau de commun](1-converger-c-est-federer.md) | Rendre commun ce qui doit être cohérent, préserver ce qui différencie réellement. | Éviter à la fois la prolifération de silos et l'uniformisation inutile. |
| [02 — FLOW comme plateforme d'entreprise](2-flow-comme-plateforme-d-entreprise.md) | FLOW est une plateforme de capacités partagées, pas une application de plus. | Éviter de réduire FLOW à un remplacement d'OMS, d'ERP ou d'outil existant. |
| [03 — Les domaines avant les structures](3-domaines-avant-les-structures.md) | Les domaines métier sont plus durables que les organisations, applications et processus. | Concevoir autour des responsabilités stables plutôt qu'autour de l'existant. |
| [04 — Articuler Engagement, Demand, Fulfillment et Supply](4-separer-demand-et-supply.md) | Engagement capte l'intention, Demand qualifie la demande, Fulfillment arbitre, Supply expose les ressources. | Ne pas mélanger parcours, intention qualifiée, décision et exécution dans le même modèle. |
| [05 — Le processus émerge des décisions métier](5-le-processus-emerge-des-decisions.md) | Les décisions métier doivent être conçues avant les variantes de workflow. | Rendre visibles les règles, priorités, exceptions et arbitrages réels. |
| [06 — La demande comme objet métier central d'orchestration](6-demande-objet-metier-central-orchestration.md) | Le Case porte la demande, son contexte, son historique, ses décisions et ses engagements. | Garder un fil métier cohérent malgré les canaux, domaines et systèmes traversés. |
| [07 — Master Data : des objets maîtres aux sources gouvernées](7-qualifier-les-informations-plutot-que-master-data.md) | Faire du MDM, c'est passer d'un modèle d'objets, attributs et cardinalités à une cartographie des sources de référence, projections, contrats et responsabilités de gouvernance. | Éviter le piège `MDM = inventaire des objets "maîtres" de l'entreprise` et le foisonnement de flux projet. |

## Lecture d'ensemble

Les principes s'enchaînent comme une logique de conception.

```text
Bon niveau de commun
        ↓
Plateforme d'entreprise
        ↓
Domaines durables
        ↓
Engagement + Demand + Fulfillment + Supply
        ↓
Décisions métier explicites
        ↓
Case comme objet central
        ↓
Informations qualifiées et contractualisées
```

Cette chaîne permet de passer d'une ambition de convergence à une architecture gouvernable.

## Ce qu'il faut retenir pour arbitrer

Quand une décision est difficile, les principes posent quelques réflexes.

Ne pas demander d'abord : quelle application doit porter le sujet ?

Demander plutôt :

- quelle responsabilité durable est concernée ;
- quel niveau de commun est réellement nécessaire ;
- quelle demande ou quel Case doit être piloté ;
- quelle décision métier doit être rendue explicite ;
- quelle promesse doit être tenue ;
- quelle ressource Supply est mobilisée ;
- quelle information fait référence pour cet usage ;
- quel contrat de données permet de raccorder les domaines.

## Risques évités

Ces principes évitent plusieurs dérives fréquentes :

- construire un nouveau monolithe au nom de la convergence ;
- transformer FLOW en simple couche d'intégration ;
- confondre ERP, OMS, plateforme et domaine métier ;
- figer les processus alors que les décisions changent selon le contexte ;
- importer le vocabulaire `Master Data` sans clarifier les responsabilités ;
- multiplier les flux point-à-point sans gouvernance durable.

## À lire ensuite

Pour la vision globale, commencer par [l'abstract FLOW](../vision/abstract.md).

Pour comprendre le périmètre de FLOW, lire [Positionnement de FLOW](../vision/positionnement-flow.md).

Pour traduire les principes en produits et flux, lire [Overview de la plateforme FLOW](../architecture-cible/overview-plateforme-flow.md) puis [Flux fonctionnels FLOW](../architecture-cible/flux-fonctionnels-flow.md).
