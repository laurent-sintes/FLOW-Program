# Ébauche de la plateforme FLOW

## Intention

Cette page propose une première ébauche de la plateforme FLOW.

Elle ne constitue pas encore une architecture cible détaillée.

Elle sert à clarifier :

- ce qui pourrait appartenir à FLOW ;
- ce qui doit rester en dehors de FLOW ;
- les principales capacités à faire émerger ;
- la manière dont FLOW se positionne entre les demandes, les ressources, les décisions, les systèmes consommateurs et les systèmes d'exécution.

## Principe de positionnement

FLOW n'est pas un ERP.

FLOW n'est pas un OMS unique.

FLOW n'est pas une plateforme d'engagement client.

FLOW est une plateforme fédérée de capacités d'entreprise.

Elle porte les capacités transverses qui permettent d'instruire, décider, orchestrer et suivre des demandes traversant plusieurs domaines, applications, marques, canaux ou partenaires.

## Schéma simple

```text
Expériences et systèmes consommateurs
(eCommerce, magasins, B2B, wholesale, service client, applications métier)
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│                         FLOW                                │
│                                                             │
│  Demand / Case Management                                  │
│  Agreement & Engagement Context                            │
│  Decision Services / Rules                                 │
│  Allocation & Promise                                      │
│  Inventory Visibility                                      │
│  Supply orchestration                                      │
│  Event & Fact management                                   │
│  Documents opérationnels liés au Case                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
Systèmes d'exécution et systèmes de référence
(ERP, Finance, WMS, TMS, POS, PLM, PIM, CRM, partenaires logistiques)
```

Ce schéma exprime une idée simple : FLOW ne remplace pas tous les systèmes.

FLOW fournit un niveau transverse de compréhension, décision et orchestration.

Les expériences consomment les capacités FLOW.

Les systèmes d'exécution réalisent les opérations physiques, comptables, commerciales ou documentaires relevant de leur responsabilité.

## Ce qui est dans FLOW

### Demand / Case Management

FLOW porte le Case comme unité de pilotage d'une demande dans la durée.

Le Case conserve :

- l'intention ;
- le contexte ;
- les parties concernées ;
- les engagements ;
- les décisions ;
- les événements ;
- les documents associés ;
- l'état courant ;
- l'historique.

Cette capacité permet de traiter les transactions longues et transverses sans les enfermer dans un seul processus ou une seule application.

### Agreement & Engagement Context

FLOW doit pouvoir comprendre le cadre d'engagement dans lequel une demande est instruite.

Ce cadre peut dépendre :

- d'un client ;
- d'un contrat ;
- d'un canal ;
- d'une marque ;
- d'une saison ;
- d'un SLA ;
- d'une règle commerciale ;
- d'une condition de prix ou de remise.

Agreement ne remplace pas nécessairement les contrats ou référentiels existants.

Il fournit le contexte nécessaire pour décider correctement.

### Decision Services / Rules

FLOW doit rendre explicites les décisions qui font progresser une demande.

Cela implique de gouverner :

- les règles métier ;
- les critères d'arbitrage ;
- les priorités ;
- les politiques de décision ;
- les conditions d'application ;
- les traces de décision.

Les règles ne sont pas seulement des prédicats techniques.

Elles décrivent le comportement attendu de l'entreprise dans une situation donnée.

### Allocation & Promise

L'allocation est un cas emblématique de décision transverse.

Elle relie :

- une demande ;
- un engagement ;
- une ressource disponible ou future ;
- des règles de priorité ;
- des contraintes opérationnelles ;
- des événements ;
- une promesse ou une action d'exécution.

FLOW doit permettre de comprendre, tracer, simuler ou gouverner ces décisions.

Cela ne signifie pas forcément que tous les calculs d'allocation doivent être physiquement exécutés dans FLOW dès le départ.

Mais leur responsabilité doit être rendue explicite.

### Inventory Visibility

FLOW a besoin d'une visibilité cohérente des ressources.

Inventory Visibility ne se limite pas au stock disponible à l'instant T.

Elle doit pouvoir qualifier :

- les stocks physiques ;
- les stocks logiques ;
- les stocks réservés ;
- les stocks futurs ;
- les commandes d'achat ;
- les réceptions attendues ;
- les ressources mobilisables ;
- les contraintes d'usage.

Cette capacité est nécessaire pour décider, promettre, allouer ou réallouer.

### Supply orchestration

FLOW doit articuler la demande avec la disponibilité et la mobilisation des ressources.

Supply orchestration ne remplace pas les systèmes logistiques.

Elle permet de coordonner les décisions qui mobilisent les ressources nécessaires au traitement d'une demande.

### Event & Fact management

FLOW doit s'appuyer sur des faits et des événements.

Un fait décrit une réalité métier observée.

Un événement signale qu'une évolution significative s'est produite.

Ces éléments alimentent les décisions, déclenchent des réévaluations et permettent d'observer le cycle de vie d'un Case.

### Documents opérationnels liés au Case

FLOW doit référencer les documents utiles au traitement d'une demande :

- facture ;
- bon de livraison ;
- bon de retour ;
- avoir ;
- contrat ;
- preuve de remise ;
- document fournisseur ;
- document de transport.

FLOW ne devient pas pour autant le domaine Finance ni un coffre documentaire universel.

Il doit relier les documents au Case pour assurer la continuité opérationnelle, la traçabilité et l'intégration avec les domaines concernés.

## Ce qui reste en dehors de FLOW

### Les expériences utilisateur

FLOW ne porte pas les expériences différenciantes.

Les sites eCommerce, applications magasin, portails B2B, outils service client ou interfaces métier peuvent consommer FLOW sans être absorbés par FLOW.

```text
FLOW fournit les capacités.
Les consommateurs construisent les expériences.
```

### Les systèmes d'exécution physique

Les WMS, TMS, systèmes magasin, partenaires logistiques et outils opérationnels conservent leurs responsabilités d'exécution.

FLOW peut instruire, décider, orchestrer ou suivre.

Mais l'exécution physique reste portée par les systèmes compétents.

### Finance et comptabilité

Finance conserve ses responsabilités comptables, fiscales et de contrôle.

FLOW peut transmettre des événements économiques, référencer des documents, ou fournir le contexte opérationnel d'une demande.

Mais FLOW ne remplace pas SAP Finance, FI/CO, la comptabilisation ou le contrôle de gestion.

### Les référentiels source

FLOW ne doit pas devenir par défaut le propriétaire de toutes les données de référence.

PLM, PIM, CRM, ERP, Finance ou autres domaines peuvent rester propriétaires de certaines données.

FLOW doit plutôt distinguer :

- les données nécessaires à la décision ;
- les données partagées à gouverner ;
- les données de support ;
- les projections nécessaires aux consommateurs.

### Les outils spécialisés

Certains outils spécialisés peuvent rester en dehors de FLOW lorsqu'ils portent une expertise locale ou différenciante.

FLOW doit alors clarifier leur rôle : consommateur, contributeur, système d'exécution, source de données ou partenaire de processus.

## Première cartographie des capacités

| Capacité | Rôle dans FLOW | Statut à ce stade |
| --- | --- | --- |
| Demand / Case Management | Porter la demande dans la durée | Centrale |
| Agreement & Engagement Context | Donner le cadre d'engagement de la demande | À formaliser |
| Decision Services / Rules | Rendre les décisions explicites et gouvernées | Centrale |
| Allocation & Promise | Décider l'affectation d'une ressource à une demande | Cas emblématique |
| Inventory Visibility | Qualifier les ressources disponibles, futures ou réservables | Centrale |
| Supply orchestration | Articuler demande et mobilisation des ressources | À préciser |
| Event & Fact management | Alimenter les décisions et observer les changements | Transverse |
| Document linkage | Relier les documents opérationnels et financiers au Case | À cadrer |
| API / Event exposure | Exposer les capacités aux consommateurs | Technique transverse |
| Observability | Suivre les décisions, événements et processus émergents | Technique transverse |

## Questions ouvertes

Cette ébauche soulève plusieurs questions qui devront être instruites progressivement :

- Quelles décisions doivent être réellement prises dans FLOW, et lesquelles restent dans les systèmes existants ?
- Quel est le bon périmètre produit pour Allocation & Promise ?
- Inventory Visibility est-elle un produit FLOW autonome ou une capacité portée par un produit Supply plus large ?
- Agreement doit-il être un produit, une capacité ou un modèle partagé ?
- Quels événements opérationnels FLOW doit-il produire pour Finance ?
- Quels documents doivent être conservés dans FLOW, référencés par FLOW ou simplement liés au Case ?
- Où placer la frontière entre orchestration FLOW et exécution logistique ?
- Comment faire coexister les moteurs existants de SAP, Storeland, OMS ou WMS avec les capacités FLOW ?

## À retenir

FLOW doit être pensé comme une couche de capacités fédérées, pas comme un remplacement global du paysage applicatif.

Sa valeur tient dans sa capacité à rendre explicites les demandes, les décisions, les engagements, les ressources et les événements qui traversent les systèmes.

La cible ne doit donc pas être formulée comme :

```text
Quel outil remplace quel outil ?
```

mais comme :

```text
Quelle capacité transverse doit être gouvernée par FLOW,
et quels systèmes restent consommateurs, contributeurs ou exécutants ?
```
