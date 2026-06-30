# Histoire de FLOW

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
      <strong>6 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## 1. Le point de départ n'est pas FLOW

Le point de départ est un programme de convergence entre Boardriders et le Groupe Beaumanoir.

Cette convergence n'est pas seulement IT.

Elle concerne aussi les business models, les pratiques business, les modes d'engagement client, les pratiques d'achat, les modèles de vente, les organisations et les façons d'opérer les marques.

Il est vrai que les discussions traitent beaucoup du SI, car les écarts applicatifs rendent les différences visibles.

Mais le sujet de fond est plus large : comment rapprocher deux patrimoines IT et business ayant des histoires, des modèles opérationnels et des pratiques différentes ?

À ce stade, les discussions portent essentiellement sur les ERP, les OMS, les intégrations, la logistique et le stock.

Le risque initial est donc de réduire trop vite la convergence à une convergence applicative, alors que le programme doit aussi traiter la convergence des pratiques et des modèles métier.

## 2. Deux histoires SI très différentes

### Boardriders

Boardriders a suivi une logique relativement centralisatrice autour de SAP.

Autour du cœur SAP gravitent Salesforce, NewStore, Elastic et plusieurs solutions spécialisées.

L'idée dominante est : un cœur commun et des satellites spécialisés.

### Marques Historiques Beaumanoir

Les marques historiques ont suivi une logique plus fédérale.

Chaque marque dispose historiquement de son propre Storeland et de ses spécificités.

Pour coordonner l'ensemble est apparu UR, qui centralise certaines demandes et leur cycle de vie.

## 3. L'étude Synvance

En 2025, une étude est commandée au cabinet de conseil Synvance.

Son objectif est d'objectiver les disparités entre Boardriders et les marques historiques du Groupe Beaumanoir.

L'étude doit permettre de constater les écarts entre les deux patrimoines SI, les modes de fonctionnement, les applications et les processus.

Elle sert également à éclairer le type de solution dont le groupe a besoin pour accompagner la convergence.

À ce stade, la question reste encore formulée de manière assez classique : quel type de solution cible permettrait de rapprocher BRD et GBM ?

Cette étude constitue un jalon important : elle met en visibilité les différences à traiter et prépare le terrain des réflexions qui conduiront progressivement à FLOW.

## 4. Première découverte

Lorsque l'on compare BRD et GBM, les outils diffèrent mais les problèmes sont souvent identiques :

- visibilité stock ;
- promesse ;
- orchestration ;
- allocation ;
- fulfillment ;
- omnicanalité ;
- gouvernance.

## 5. Le rôle révélateur de l'allocation

Dans les discussions issues de l'étude Synvance, l'allocation apparaît comme un sujet particulièrement saillant.

Elle revient dans les besoins cibles, les comparaisons ERP, les règles de priorisation, les précommandes, les stocks futurs, les simulations et les scénarios d'exécution.

Dans une lecture initiale, l'allocation est traitée comme une fonctionnalité à couvrir par un ERP ou un OMS.

Mais elle révèle progressivement une question plus profonde :

> Comment décider qu'une ressource doit être affectée à une demande, dans un cadre d'engagement donné, selon des règles explicites ?

L'allocation devient ainsi l'un des premiers indices que la convergence ne peut pas être réduite au choix d'une solution.

Elle met en tension la demande, le stock, les engagements, les règles, les priorités commerciales, les événements et l'exécution.

Elle prépare donc le basculement d'une logique de core model ERP vers une logique de capacités transverses de décision et d'orchestration.

## 6. Le débat OMS

La réflexion tourne initialement autour de la recherche d'un OMS cible.

Puis une gêne apparaît progressivement.

## 7. Le constat

Le terme OMS regroupe historiquement :

- ATP ;
- sourcing ;
- allocation ;
- orchestration ;
- visibilité stock ;
- transport ;
- retours ;
- ship-from-store ;
- click & collect.

OMS devient progressivement un mot-valise.

## 8. Le tournant

Une idée apparaît : nous ne cherchons peut-être pas un OMS.

Nous cherchons peut-être à comprendre quelles responsabilités les OMS ont agrégées historiquement.

## 9. Décomposition de l'OMS

Les responsabilités sont progressivement isolées :

- Inventory Visibility ;
- Fulfillment Network Configuration ;
- Decision Services ;
- Case Management.

## 10. Deuxième découverte

Les commandes ne sont peut-être pas le bon objet d'urbanisation.

Les mêmes mécanismes apparaissent dans l'achat, le B2B, le B2C, les retours et les transferts.

## 11. Passage à Demand

La réflexion évolue progressivement de l'Order Management vers le Demand Management.

La demande devient l'objet principal.

## 12. Troisième découverte

Ce qui différencie réellement les situations n'est pas la demande mais le cadre d'engagement.

## 13. Agreement devient un concept central

Les différences entre B2B, B2C, Achat, retail, wholesale ou marketplace ne doivent pas nécessairement conduire à décliner des dizaines de variantes de commandes ou de processus.

Une commande peut rester plus générique si son contexte est interprété au regard d'un cadre d'engagement explicite.

Agreement devient central parce qu'il porte ou référence les règles et conditions de traitement applicables :

- prix ;
- assortiment ;
- conditions commerciales ;
- SLA ;
- priorités ;
- droits ;
- contraintes ;
- règles d'allocation ;
- conditions de livraison ;
- règles de retour ou de remboursement.

Le contexte de la commande, appuyé par un référentiel de règles et un moteur de règles, peut alors piloter dynamiquement les variations de traitement.

La variation n'est plus encodée dans une multiplication de processus spécialisés.

Elle est portée par la combinaison :

```text
Commande générique
    + contexte
    + Agreement
    + règles
    = traitement adapté
```

Cet insight change profondément la conception : FLOW doit éviter de multiplier les objets et processus par canal lorsque les variations peuvent être gouvernées par Agreement et par des règles explicites.

## 14. Le modèle conceptuel FLOW

Party → Agreement → Demand → Decision → Execution

Ce modèle devient progressivement le socle conceptuel de FLOW.

## 15. La question de l'organisation

Le découpage Achat / Vente B2B / Vente B2C est remis en question.

Ces découpages correspondent davantage à des organisations, canaux, pratiques ou contextes de consommation qu'à la structure profonde de la plateforme.

Les organisations comme B2B, B2C, retail, wholesale ou achat consommeront la plateforme.

La plateforme, elle, doit être urbanisée selon un découpage plus durable :

```text
Demand
    ↓
Supply
```

Demand porte l'instruction, la décision, la promesse, l'allocation, le Case et les règles qui permettent de traiter la demande.

Supply porte les ressources, lieux, partenaires, capacités et événements d'exécution.

## 16. Quatrième découverte

Ce qui semble réellement mutualisable est :

- Agreement ;
- Demand ;
- Inventory Visibility ;
- Fulfillment Network Configuration ;
- Decision Services.

## 17. FLOW devient une plateforme

Le projet cesse progressivement d'être un projet OMS ou ERP.

Il devient une plateforme fédérale de capacités partagées.

## 18. Le COPIL de juin

FLOW est progressivement pensé comme une plateforme capable d'intégrer naturellement les futures acquisitions du groupe.

Les notions de fédération, de plateforme d'entreprise et de multi-tenant deviennent centrales.

## 19. FLOW devient le moteur de la convergence

FLOW n'est plus seulement un projet de convergence SI.

La plateforme FLOW, et le programme qui la gouverne, deviennent progressivement le moteur de la convergence.

Cette convergence ne consiste pas seulement à rapprocher des applications.

Elle consiste à organiser la manière dont le groupe fait converger :

- ses pratiques business ;
- ses business models ;
- ses responsabilités métier ;
- ses capacités partagées ;
- ses règles de décision ;
- ses informations opérationnelles ;
- ses trajectoires applicatives ;
- ses niveaux d'autonomie locale.

FLOW devient donc un programme d'entreprise visant à construire une plateforme fédérale conciliant :

- autonomie locale ;
- gouvernance globale ;
- mutualisation ;
- différenciation ;
- croissance externe ;
- transformation continue.
