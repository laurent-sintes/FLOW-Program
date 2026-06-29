# Fournisseur, usine et Agreement : séparer les rôles

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsors, architecture, métiers concernés</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>8 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

Cette page documente un hotspot issu de l'atelier Boardriders du 29 juin 2026.

Le sujet n'est pas seulement la création des fournisseurs dans SAP.

Le sujet est la manière dont l'existant BRD articule plusieurs réalités qui ne relèvent pas forcément du même domaine cible :

- fournisseur ;
- usine ;
- intermédiaire ou agent ;
- entité de facturation ;
- adresse de commande ;
- zone de transport ;
- lead time ;
- conditions d'achat ;
- responsabilité juridique ;
- relation avec le PLM et SAP.

## Constat terrain

Aujourd'hui, les fournisseurs sont créés manuellement par l'équipe Finance.

La fiche fournisseur porte notamment :

- la `Transportation Zone` ;
- des `partner functions`, par exemple ordering address, vendor et invoicing party ;
- les informations permettant de gérer des intermédiaires, des agents et des chaînes commerciales complexes ;
- les usines, avec des informations comme les lead times.

Cette fiche fournisseur pousse certaines informations dans le PLM.

Le PLM repousse ensuite la donnée complète dans SAP, afin que les informations produit, fournisseur, usine et conditions associées restent cohérentes dans le socle SAP.

Le référentiel officiel est SRM, mais il n'existe pas aujourd'hui de mécanisme de synchronisation opérationnel. C'est ce qui explique la saisie manuelle.

La suite de l'atelier ajoute un autre point d'attention : l'intégration SRM / PLM ne concerne pas seulement la donnée. Elle conditionne aussi les habilitations des fournisseurs, agents ou responsables d'usine lorsqu'ils se connectent à la SRM.

## Le point de tension

Le SRM est orienté usine plutôt que fournisseur.

Cela ouvre une question de compatibilité avec le modèle Beaumanoir, dans lequel l'ERP associe des Agreements à des fournisseurs.

La tension peut se formuler simplement :

```text
GBM
    on passe une commande à un fournisseur
    l'Agreement est associé à ce fournisseur

BRD
    on passe une commande à une usine
    les partner functions permettent de retrouver les autres rôles
```

Ce décalage ne doit pas être tranché comme une préférence abstraite entre deux modèles.

Le vrai sujet est architectural : faut-il reconduire un paramétrage monolithique, où fournisseur, usine, facturation, PLM, transport, lead time et habilitations sont concentrés dans un même objet, ou distribuer cette configuration dans les domaines responsables ?

Dans une configuration distribuée par domaine, les usages peuvent varier sans devenir structurants pour tout le modèle :

- parfois le fournisseur orchestre les opérations vers l'usine, et la PO peut légitimement ne décrire que le fournisseur ;
- parfois l'exécution exige de cibler l'usine pour passer la commande opérationnelle ;
- parfois les accès SRM doivent être donnés à des interlocuteurs différents selon leur rôle dans la relation.

Le point le plus important reste le calcul des dates de promesse.

Le modèle fournisseur / usine / Agreement / SRM / PLM n'a de valeur que s'il permet de calculer une date fiable : quand peut-on réellement promettre la mise à disposition, la fabrication, l'expédition ou la livraison, compte tenu du rôle opérationnel concerné, du lead time, des conditions d'achat, du transport et des contraintes d'exécution ?

Si FLOW reprend mécaniquement le modèle SAP BRD, il risque de reconduire un objet fournisseur trop chargé.

S'il reprend mécaniquement le modèle GBM, il risque de perdre la précision opérationnelle du modèle usine / partner functions.

## Lecture d'architecture

SAP fonctionne ici comme un monolithe de paramétrage.

Des notions utiles pour plusieurs domaines y sont concentrées dans une même fiche ou dans un même modèle de paramétrage :

- stock et disponibilité ;
- SLA ou lead time ;
- conditions de prix ;
- responsabilité juridique ;
- adresse ou rôle de commande ;
- entité de facturation ;
- relation fournisseur / usine / agent ;
- données nécessaires au PLM et à SAP.

Dans l'architecture FLOW, il n'est pas évident que ces informations doivent rester concentrées au même endroit.

L'hypothèse cible est plutôt de séparer les responsabilités par domaine.

| Responsabilité | Lecture cible possible |
| --- | --- |
| Identité du fournisseur ou partenaire | Domaine tiers / référentiel spécialisé, probablement projection dans FLOW |
| Usine et capacité de fabrication | Domaine Supply amont ou service Supply spécialisé |
| Lead time usine | Policy ou SLA rattaché à une capacité de fabrication ou à un service Supply |
| Conditions d'achat, prix, engagement | Agreement ou Product Agreement Catalog |
| Entité de facturation | Finance / référentiel tiers / projection nécessaire aux documents |
| Transportation Zone | Fulfillment Network, transport ou Supply Service Registry |
| Adresse de commande | Rôle de partie prenante ou partner function |
| Habilitations SRM | Règles d'accès fondées sur les rôles, relations et périmètres de responsabilité |
| Données utiles au PLM | Projection amont consommée par le PLM, sans faire du PLM la source de tous les rôles |

## Cartographie data et flux

Ce hotspot n'est pas un problème infranchissable.

Il implique surtout un travail sérieux de cartographie des données, des flux et des sources de référence : qui paramètre quoi, qui contrôle quelle information, et quelle projection FLOW ou Case Management doit consommer pour calculer une décision.

La décision portée par le Case Management ne s'appuie pas sur une donnée unique.

Elle combine potentiellement :

| Source ou domaine | Informations utiles à la décision | Point d'attention |
| --- | --- | --- |
| SRM | Agreement, fournisseur, usine / site de production, relation fournisseur-usine, habilitations | Le terme `plant` doit probablement être renommé en français métier : usine, site de production ou capacité de fabrication selon l'usage réel. |
| CBS | Commandes d'achat, suivi amont, documents réglementaires fournisseur, événements de livraison | À instruire : CBS est-il la SRM cible du groupe, le premier lieu de recensement fournisseur / usine, ou un domaine spécialisé consommateur d'une source de référence externe ? |
| PLM | Contrats ou éléments d'Agreement négociés pendant la conception et la préparation produit | Le PLM peut contribuer à l'Agreement sans devenir la source unique des rôles fournisseur / usine. |
| Module Négoce | Conditions commerciales, commandes d'achat, contexte d'assortiment ou d'approvisionnement | Certaines responsabilités peuvent relever de l'engagement commercial, d'autres de la Demand ou de la Supply. |
| Finance | Règles de facturation, entités juridiques, contraintes documentaires ou processus de facturation | FLOW doit consommer les règles utiles à la décision sans absorber la comptabilité. |
| Supply / exécution | Lead times, capacités, contraintes transport, disponibilité future | Ces informations alimentent directement le calcul des dates de promesse. |

La question n'est donc pas : où mettre toute la donnée ?

La question est : quelle donnée est autorisée par quel domaine, avec quelle fraîcheur, quelle traçabilité et quelle responsabilité de mise à jour ?

## Exemple métier

L'exemple donné en atelier illustre la complexité :

> Fabrication en Afrique du Sud, mais entité à facturer en Corée du Sud.

Cette situation montre qu'une même opération peut impliquer plusieurs rôles :

- un lieu de fabrication ;
- une entité juridique ou financière ;
- un intermédiaire commercial ;
- une adresse ou un rôle de commande ;
- des conditions d'achat ou d'exécution.

Le modèle cible ne doit donc pas écraser ces rôles dans une notion unique de fournisseur.

## Questions ouvertes

| Sujet | Question à instruire |
| --- | --- |
| Standard SAP ou héritage BRD | Le modèle observé est-il standard SAP, ou a-t-il été adapté pour reprendre la logique de l'ancien système ? |
| SRM | SRM est-il réellement la source de référence, et pour quels objets : fournisseur, usine, relation commerciale, site de production ? |
| CBS / SRM cible | CBS doit-il devenir la SRM cible du Groupe Beaumanoir, ou rester un domaine de suivi achat, collaboration fournisseur et conformité documentaire ? |
| Premier recensement | Le premier recensement des fournisseurs, usines et sites de production doit-il être fait dans CBS, SRM, Finance, PLM ou un référentiel spécialisé ? |
| Synchronisation | Faut-il mettre en place une synchronisation SRM vers SAP, PLM ou FLOW, ou reconstruire une projection cible ? |
| Usine vs fournisseur | FLOW doit-il distinguer systématiquement le fournisseur, l'usine, l'agent et l'entité de facturation ? |
| Agreement | Un Agreement doit-il être associé au fournisseur, à l'usine, à la relation fournisseur-usine, ou au contexte d'achat ? |
| Lead time | Le lead time relève-t-il de la fiche fournisseur, de l'usine, du service Supply ou d'une policy d'exécution ? |
| Date de promesse | Quelles données et quelles règles doivent être combinées pour calculer une date de promesse fiable selon que la PO cible le fournisseur ou l'usine ? |
| Source de référence | Qui est source de référence de chaque donnée : SRM, PLM, Négoce, Finance, Supply, FLOW ou une projection intermédiaire ? |
| Flux | Quels flux doivent être synchrones, événementiels, batch ou simplement reconstruits en projection pour la décision ? |
| PLM | Le PLM doit-il recevoir une projection enrichie des rôles fournisseurs, ou rester consommateur d'un sous-ensemble utile à la conception ? |
| Habilitations | Quels droits donner aux fournisseurs, responsables d'usine, agents ou intermédiaires selon le rôle qu'ils jouent dans une relation donnée ? |
| Convergence BRD / GBM | Comment rendre compatibles un modèle BRD orienté usine et un modèle GBM orienté fournisseur ? |

## Hypothèse de travail

FLOW ne devrait pas chercher à définir une nouvelle fiche fournisseur monolithique.

Il devrait plutôt consommer ou exposer des projections séparées, gouvernées par domaine :

```text
Party / fournisseur / agent
    → identité, rôle, relation commerciale

Usine / site de production
    → capacité, lead time, contraintes industrielles

Agreement
    → conditions, prix, droits, priorités, contexte d'achat

Finance
    → entité de facturation, responsabilité juridique, documents

Fulfillment / Supply
    → zone de transport, SLA, service mobilisable

PLM
    → données nécessaires à la conception et à la préparation produit
```

Le modèle cible doit donc éviter de transformer un choix d'usage local en contrainte globale.

Si l'usage dit que la PO s'adresse au fournisseur dans un cas et à l'usine dans un autre, cela ne doit pas avoir d'importance structurelle pour FLOW. La plateforme doit pouvoir résoudre le bon interlocuteur, le bon Agreement, la bonne projection PLM, les bonnes habilitations SRM et surtout la bonne date de promesse selon le contexte, à partir des configurations distribuées dans les bons domaines.

Cette séparation est cohérente avec les principes FLOW :

- ne pas importer le modèle SAP sans le challenger ;
- qualifier les informations plutôt que parler indistinctement de Master Data ;
- séparer Demand, Supply, Finance et conception produit ;
- utiliser l'Agreement pour piloter les variations métier sans multiplier les processus ;
- construire le bon niveau de commun sans effacer les spécificités BRD.

Elle s'appuie aussi sur un pattern d'architecture plus général : [Rôles, relations et policies plutôt que cardinalités figées](../architecture-cible/patterns/roles-relations-policies.md).

## À retenir

Ce hotspot ne dit pas que le modèle BRD est mauvais.

Il dit que le modèle SAP BRD révèle une complexité réelle : une commande peut être passée à une usine, facturée par une autre entité, portée par un fournisseur ou un agent, et dépendre de conditions et lead times spécifiques.

FLOW doit préserver cette richesse métier sans la reconduire sous forme d'un paramétrage monolithique.

Le bon niveau de commun sera probablement un modèle de rôles, relations, Agreements et services Supply, plutôt qu'une fiche fournisseur unique.
