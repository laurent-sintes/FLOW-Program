# SI CBS

## Intention

Cette page documente le SI CBS, qui n'apparaît pas dans la cartographie applicative GBM visible mais qui porte des responsabilités importantes autour des commandes d'achat fournisseur, du support achat et de la livraison amont.

CBS est important pour FLOW car il se situe à la frontière entre :

- les commandes d'achat fournisseur ;
- les processus de collaboration fournisseur ;
- la livraison jusqu'à l'entrepôt ;
- la conformité documentaire ;
- la visibilité transverse ;
- les responsabilités candidates à FLOW comme la commande, le cycle de vie et la vision 360.

## Description générale

Le SI CBS est composé de plusieurs modules développés sur mesure en .NET.

Son objectif est de rendre visible l'ensemble des commandes d'achat fournisseur et d'implémenter les processus support à l'achat et à la livraison jusque dans l'entrepôt.

CBS ne doit donc pas être lu comme un simple outil périphérique.

Il porte une partie de la relation opérationnelle entre l'entreprise, ses fournisseurs fabricants, le transport et l'entrepôt.

```text
CBS
    → modules .NET sur mesure
    → visibilité commandes d'achat fournisseur
    → processus support achat / livraison
    → suivi jusqu'à l'entrepôt
    → documents fournisseur
    → conformité transport / taxes / identification objets
```

## Exemple : packing list fournisseur

Un exemple significatif est le service qui permet au fournisseur fabricant de publier une packing list.

Cette packing list est nécessaire à la transparence du transport.

Elle permet notamment d'assurer :

- l'identification des objets transportés ;
- la bonne documentation des marchandises ;
- la conformité avec la loi du pays de réception ;
- les informations nécessaires aux taxes, contrôles ou obligations réglementaires ;
- la continuité entre fournisseur, transport et entrepôt.

Ce type de fonctionnalité montre que CBS porte des processus spécialisés de collaboration fournisseur et de conformité amont.

## Lecture d'architecture

CBS doit être considéré, en première lecture, comme un domaine consommateur de FLOW.

Il porte des processus spécialisés autour de :

- la collaboration fournisseur ;
- le support achat ;
- la livraison amont ;
- la conformité documentaire ;
- la transparence transport ;
- l'identification des objets ;
- la préparation de l'arrivée entrepôt.

Ces processus ne doivent pas être absorbés par FLOW par défaut.

En revanche, CBS porte ou manipule certaines responsabilités plus génériques qui peuvent être candidates à FLOW.

## Responsabilités candidates FLOW

Certaines responsabilités actuellement présentes ou visibles via CBS doivent être évaluées comme candidates à FLOW :

- la commande d'achat ;
- le cycle de vie de la commande ;
- les statuts ;
- les événements ;
- les jalons d'avancement ;
- la vision 360 d'une commande ou d'un engagement fournisseur ;
- la disponibilité future ;
- le rattachement à une demande, un engagement ou une promesse.

La question n'est donc pas de décider que CBS entre ou sort entièrement de FLOW.

La question est de séparer les responsabilités :

```text
CBS — domaine consommateur
    → processus fournisseur spécialisés
    → packing list
    → conformité transport / douane / taxes
    → documentation légale
    → collaboration fournisseur

FLOW — responsabilités candidates
    → commande d'achat
    → cycle de vie
    → statuts / événements
    → vision 360
    → orchestration transverse
```

## Recommandation d'architecture — CBS et FLOW

CBS doit être considéré comme un domaine consommateur de FLOW.

FLOW ne doit pas absorber par défaut les processus spécialisés de collaboration fournisseur, packing list, conformité transport ou documentation réglementaire.

En revanche, les responsabilités génériques de commande, cycle de vie, statuts, événements et vision 360 doivent être évaluées comme candidates à FLOW.

Cette recommandation permet de poser une frontière saine :

- CBS conserve les processus fournisseur spécialisés ;
- FLOW peut devenir le socle transverse de visibilité, de cycle de vie et d'orchestration ;
- CBS consomme les informations ou événements exposés par FLOW ;
- FLOW peut consommer certains faits produits par CBS.

## Questions structurantes pour FLOW

Le SI CBS conduit à plusieurs questions :

- CBS doit-il rester un domaine spécialisé consommateur de FLOW ?
- Quelles responsabilités de CBS relèvent réellement de la collaboration fournisseur et de la conformité ?
- Quelles responsabilités de CBS relèvent plutôt d'une capacité transverse FLOW ?
- La commande d'achat fournisseur doit-elle être portée par FLOW, par l'ERP, ou par un domaine spécialisé ?
- Où doit vivre le cycle de vie transverse d'une commande d'achat ?
- La vision 360 d'une commande fournisseur doit-elle être exposée par FLOW ?
- Quels événements CBS doit-il publier à FLOW ?
- Quels événements ou statuts FLOW doit-il exposer à CBS ?
- Comment éviter de disperser les statuts, jalons et événements entre CBS, ERP, logistique et FLOW ?

## À retenir

CBS est un composant important du paysage GBM même s'il n'apparaît pas dans la cartographie visible.

Il porte des processus spécialisés autour de la commande d'achat fournisseur, de la collaboration fournisseur, de la livraison amont, de la packing list et de la conformité documentaire.

CBS doit être lu comme un domaine consommateur de FLOW.

Mais certaines responsabilités qu'il porte ou manipule — commande, cycle de vie, statuts, événements, vision 360 — peuvent relever d'une capacité transverse FLOW.

La bonne frontière n'est donc pas applicative. Elle doit être posée par responsabilité.
