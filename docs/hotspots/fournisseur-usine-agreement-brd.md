# Fournisseur, usine et Agreement BRD

## Intention

Cette page documente un hotspot issu de l'atelier Boardriders du 29 juin 2026.

Le sujet n'est pas seulement la création des fournisseurs dans SAP.

Le sujet est la manière dont BRD mélange ou distingue, dans son existant, plusieurs réalités qui ne relèvent pas forcément du même domaine cible :

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

Ce décalage est structurant.

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
| Données utiles au PLM | Projection amont consommée par le PLM, sans faire du PLM la source de tous les rôles |

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
| SRM | SRM est-il réellement la source officielle, et pour quels objets : fournisseur, usine, relation commerciale, site de production ? |
| Synchronisation | Faut-il mettre en place une synchronisation SRM vers SAP, PLM ou FLOW, ou reconstruire une projection cible ? |
| Usine vs fournisseur | FLOW doit-il distinguer systématiquement le fournisseur, l'usine, l'agent et l'entité de facturation ? |
| Agreement | Un Agreement doit-il être associé au fournisseur, à l'usine, à la relation fournisseur-usine, ou au contexte d'achat ? |
| Lead time | Le lead time relève-t-il de la fiche fournisseur, de l'usine, du service Supply ou d'une policy d'exécution ? |
| PLM | Le PLM doit-il recevoir une projection enrichie des rôles fournisseurs, ou rester consommateur d'un sous-ensemble utile à la conception ? |
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
