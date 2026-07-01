# Pattern — Sources de référence, projections et vues

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
      <strong>5 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Ce pattern décrit comment cartographier les informations dans un SI distribué sans retomber dans le fourre-tout `Master Data`.

L'idée centrale est simple :

> Cartographier les informations par leur source de référence, pas par les vues, copies ou agrégats où elles sont visibles.

Une information devient fiable pour FLOW lorsqu'elle est créée, validée ou maintenue dans un domaine responsable, avec un minimum de qualité contrôlé par un processus.

## Définitions

| Concept | Définition |
| --- | --- |
| Source de référence | Application, service ou domaine où une information est créée, validée ou maintenue par un processus responsable, avec un niveau de qualité suffisant pour faire référence pour un usage donné. |
| Projection | Représentation dérivée d'une ou plusieurs sources de référence, adaptée à un usage de lecture, de décision ou d'intégration. Une projection peut devenir source de référence seulement si cette responsabilité est explicitement gouvernée. |
| Vue | Lecture organisée pour un utilisateur, un processus ou une API ; elle peut agréger plusieurs projections ou sources. |
| Vue 360 | Vue transverse autour d'un acteur, d'un objet ou d'un Case ; elle facilite la compréhension mais ne remplace pas les sources de référence. |
| Agrégat de lecture | Assemblage technique ou fonctionnel optimisé pour consulter, rechercher, calculer ou décider. |

## Règle de conception

Une information ne doit pas être considérée comme référence parce qu'elle est visible quelque part.

Elle fait référence parce qu'un domaine :

- crée ou valide l'information ;
- contrôle les règles de qualité minimales ;
- sait qui peut la modifier ;
- conserve son cycle de vie ou son historique utile ;
- publie l'information ou ses changements aux consommateurs ;
- assume les écarts, corrections et arbitrages associés.

## Différence avec les notions MDM

Le concept est proche de `System of Record` ou `Source of Record` dans le vocabulaire MDM.

FLOW retient volontairement l'expression **source de référence**, plus lisible dans les ateliers métier.

La source de référence n'est pas nécessairement :

- une base unique ;
- un MDM central ;
- une source de vérité absolue ;
- le premier endroit où l'information a été saisie ;
- la vue la plus complète.

Elle est le lieu où l'information est suffisamment contrôlée pour faire foi dans un contexte donné.

## Références externes

Ce vocabulaire FLOW s'appuie sur plusieurs notions reconnues en data management et MDM.

| Référence | Apport pour FLOW |
| --- | --- |
| [Master Data Management — Gartner](https://www.gartner.com/en/data-analytics/topics/master-data-management) | Positionne le MDM comme une discipline de gouvernance, qualité et gestion des données critiques, pas seulement comme un référentiel technique. |
| [Master Data Management — Informatica](https://www.informatica.com/resources/articles/what-is-master-data-management.html) | Explique les notions de master record, golden record, vue fiable et information gouvernée entre plusieurs applications. |
| [System of Record](https://en.wikipedia.org/wiki/System_of_record) | Donne le vocabulaire courant de système ou source faisant autorité pour une information donnée. |
| [Golden Record](https://en.wikipedia.org/wiki/Golden_record_%28informatics%29) | Rappelle la notion de version consolidée ou validée d'un enregistrement dans une démarche MDM. |
| DAMA-DMBOK — *Data Management Body of Knowledge* | Cadre de référence de la discipline data management : gouvernance, qualité, architecture, MDM, reference data, metadata et responsabilités data. |
| ISO 8000 — Data quality / Master data | Référence normative autour de la qualité des données et des échanges de master data, utile pour ancrer les notions de qualité, provenance et données maîtrisées. |

FLOW ne reprend pas directement l'expression `System of Record`, car elle est trop applicative et peut laisser croire qu'une information n'a qu'un seul maître absolu.

L'expression **source de référence** est retenue pour les ateliers parce qu'elle est plus lisible et qu'elle met l'accent sur le processus qui contrôle l'information.

## Application dans FLOW

Pour chaque information importante, FLOW doit identifier :

| Question | Exemple |
| --- | --- |
| Quelle information ? | Usine associée à une commande d'achat |
| Quelle nature ? | Objet métier, relation, fact ou policy |
| Quelle source de référence ? | SRM, CBS, PLM, Finance, Supply ou autre domaine responsable |
| Quelle projection FLOW consomme-t-il ? | Projection fournisseur / usine / Agreement utile au Case Management |
| Quel usage ? | Calculer une date de promesse, contrôler une habilitation, produire un document |
| Quelle qualité minimale ? | Validité, complétude, fraîcheur, traçabilité, droits de modification |

Cette méthode permet de distinguer :

- l'information qui fait référence ;
- la projection utile à FLOW ;
- la vue qui aide un utilisateur ;
- le contrat de données qui encadre la circulation.

## Exemple fournisseur / usine / Agreement

Dans le hotspot BRD, le sujet n'est pas seulement de savoir où les fournisseurs sont visibles.

Il faut savoir où les informations deviennent références :

| Information | Question de source de référence |
| --- | --- |
| Fournisseur | Est-il recensé d'abord dans SRM, CBS, Finance ou un référentiel tiers ? |
| Usine / site de production | Est-ce SRM, CBS ou Supply qui contrôle l'existence et la validité ? |
| Agreement | Est-il négocié dans le PLM, porté par Négoce, exposé par Product Agreement Catalog ou qualifié ailleurs ? |
| Entité de facturation | Finance est-elle source de référence ? |
| Document réglementaire fournisseur | CBS est-il source de référence pour le document produit par le fournisseur ? |
| Date de promesse | FLOW calcule-t-il une information de référence à partir de projections gouvernées ? |

## Anti-patterns

### Source par visibilité

Considérer qu'une application est source parce que tout le monde consulte ses écrans.

### Vue 360 comme référentiel

Transformer une vue transverse en référentiel implicite alors qu'elle agrège des informations maîtrisées ailleurs.

### MDM magique

Créer un référentiel central sans clarifier les processus qui créent, valident, corrigent et publient l'information.

### Copie devenue maître par accident

Laisser une projection, une vue, un export, un cache ou un agrégat devenir l'endroit où les corrections sont faites, faute d'avoir identifié et gouverné la vraie source de référence.

Ce glissement est dangereux parce qu'il transforme un consommateur en maître opérationnel sans processus de contrôle, sans responsabilité claire et sans contrat de réconciliation.

## Lien avec les autres patterns

| Pattern | Articulation |
| --- | --- |
| CQRS et projections | Les projections sont des modèles de lecture ; elles ne sont pas automatiquement sources de référence. |
| Operational DataHub | Le hub construit une vérité opérationnelle consommable, mais doit expliciter ses sources de référence. |
| Event-Driven Architecture | Les événements publient des changements issus de sources de référence ou de projections gouvernées. |
| Event Sourcing / Ledger | Le ledger peut devenir source de référence pour certains faits ou mouvements s'il porte le processus de contrôle associé. |
| Rôles, relations et policies | Les rôles et relations doivent avoir une source de référence avant d'être résolus par policy. |
| Projection locale de décision | La projection locale rend la décision rapide et autonome, sans devenir source de référence par accident. |

## À retenir

Une source de référence n'est pas le plus gros référentiel.

C'est le lieu applicatif ou domaine où une information est contrôlée par un processus responsable et devient fiable pour un usage donné.

FLOW doit donc cartographier les sources de référence avant de concevoir les projections, vues 360, data hubs ou contrats de données qui les consomment.
