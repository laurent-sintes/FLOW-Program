# Principe 2 — FLOW comme plateforme d'entreprise

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
      <strong>6 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Guider les décisions de conception et vérifier la cohérence des arbitrages</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Introduction

Les premières discussions autour de FLOW étaient largement structurées autour du remplacement d'applications existantes :

- StoreLand ;
- Socloz ;
- SAP ;
- NewStore.

Les ateliers et interviews ont progressivement montré que cette approche était insuffisante pour décrire la cible.

Les besoins exprimés dépassent largement le périmètre d'un OMS, d'un ERP ou d'une application particulière.

FLOW n'est pas un projet de remplacement applicatif.

FLOW est un projet de plateforme d'entreprise.

---

## Principe

> FLOW n'est pas une application.
>
> FLOW est une plateforme d'entreprise.

FLOW fournit des capacités mutualisées permettant à plusieurs marques, canaux, partenaires et business models de partager les mêmes ressources métier, techniques et de gouvernance.

Cette plateforme ne doit pas être comprise comme une couche supplémentaire placée entre ERP et OMS.

Elle vise au contraire à réconcilier dans un même socle les responsabilités de Demand & Fulfillment qui sont aujourd'hui dispersées entre plusieurs systèmes : demande, commande, stock, promesse, allocation, exécution, retour, exception, documents et événements.

---

## Une plateforme gouverne des ressources centralisées

Une plateforme d'entreprise n'est pas seulement un ensemble d'API ou une collection de composants techniques.

C'est une entité autonome qui possède un périmètre de responsabilité, une gouvernance, un cycle de vie et des ressources qu'elle maintient dans la durée.

Dans FLOW, ces ressources centralisées peuvent être :

- des objets métier de demande et de Case ;
- des règles, politiques et décisions ;
- le Stock Unifié ;
- le Fulfillment Network ;
- les capacités d'allocation, réservation, promesse et orchestration ;
- les événements, faits, documents et vues nécessaires à la traçabilité ;
- les standards d'interface et d'extension.

Ces ressources ne sont pas centralisées pour tout contrôler depuis un centre unique.

Elles sont centralisées parce que leur dispersion crée de l'incohérence, des arbitrages contradictoires, des coûts d'intégration et une perte de capacité d'optimisation.

---

## Une plateforme reste ouverte

Une plateforme ne doit pas devenir un monolithe fermé.

Son rôle est aussi de permettre à des acteurs externes à la plateforme de contribuer à son fonctionnement, sans fragiliser le socle commun.

Cette ouverture doit être contrôlée.

FLOW doit donc proposer des processus explicites pour :

- configurer le réseau d'exécution : nœuds, capacités, services, contraintes, SLA ;
- développer de nouveaux types de Case ou de demandes métier ;
- définir, versionner, tester et publier des règles ;
- construire ou faire évoluer des décisions métier ;
- publier et consommer des événements selon des contrats gouvernés ;
- exposer des extensions sans créer de dette locale non maîtrisée.

```text
Plateforme
    ↓
Ressources centralisées et gouvernées
    +
Processus contrôlés de configuration et d'extension
```

C'est cette combinaison qui distingue une plateforme d'une application centralisée classique.

Une application centralisée cherche surtout à faire faire.

Une plateforme cherche aussi à permettre à d'autres de configurer, étendre et consommer ses capacités dans un cadre maîtrisé.

---

## Ce que nous avons observé chez GBM

Au fil du temps, le système d'information de GBM s'est enrichi de nombreuses solutions :

- StoreLand ;
- UR ;
- OMS C-LOG ;
- Salesforce ;
- Socloz ;
- Elastic ;
- Optimate ;
- Talend.

La valeur ne réside plus dans une application unique.

Elle réside dans la capacité à coordonner plusieurs responsabilités et plusieurs domaines.

L'apparition de UR montre que certaines responsabilités dépassent naturellement le périmètre d'une marque ou d'une application.

---

## Ce que nous avons observé chez BRD

Boardriders a déjà engagé une démarche de convergence autour de plusieurs solutions :

- SAP ;
- NewStore ;
- Maersk ;
- partenaires logistiques ;
- applications spécialisées.

Cette trajectoire montre que certaines capacités doivent être mutualisées à l'échelle du groupe.

Cependant, la coexistence de plusieurs moteurs de décision et de plusieurs périmètres de responsabilité montre également que la mutualisation ne suffit pas.

Une plateforme doit également clarifier les responsabilités et les règles de gouvernance.

---

## FLOW n'est pas un ERP

L'un des principes fondateurs des ERP est souvent résumé par l'adage :

> Adopt > Adapt

L'entreprise adopte le modèle du progiciel plutôt que d'adapter le progiciel à l'entreprise.

Cette approche vise à :

- standardiser les processus ;
- réduire les développements spécifiques ;
- améliorer la gouvernance ;
- faciliter les audits ;
- renforcer la transparence.

FLOW poursuit un objectif différent.

Les ERP recherchent souvent la convergence par la standardisation des processus.

FLOW recherche la convergence par la mutualisation des capacités et la réunification des responsabilités transverses.

### Vision ERP

Organisation
↓
Progiciel
↓
Processus

### Vision FLOW

Responsabilités
↓
Capacités
↓
Produits

Dans un ERP, l'organisation s'aligne souvent sur les modules du progiciel.

Dans FLOW, les capacités s'organisent autour de responsabilités métier plus stables.

Les business models, les organisations et les applications restent libres de consommer ces capacités selon leurs propres besoins.

---

## FLOW n'est pas une simple séparation ERP / OMS

Dire que FLOW n'est ni un ERP ni un OMS ne signifie pas que FLOW doit ajouter une nouvelle frontière dans le SI.

L'ambition est plus forte : réunifier les responsabilités qui rendent possible l'exécution d'une demande sans dépendre de transferts permanents entre un ERP, un OMS et plusieurs systèmes périphériques.

```text
Demande / Case
        ↓
Décisions
        ↓
Stock, promesse, allocation, exécution, exceptions
        ↓
Événements, documents, vision 360
```

Les systèmes spécialisés peuvent rester nécessaires : finance, WMS, transport, conformité, engagement client, catalogue riche, collaboration fournisseur ou applications partenaires.

Mais FLOW doit devenir le lieu de cohérence des responsabilités transverses du Demand & Fulfillment lorsque leur dispersion crée de la dette opérationnelle ou architecturale.

---

## Les caractéristiques d'une plateforme d'entreprise

Une plateforme d'entreprise ne se limite pas à un ensemble d'applications partagées.

Elle combine des capacités métier, techniques et organisationnelles permettant à plusieurs domaines de collaborer tout en conservant leur autonomie.

### 1. Elle mutualise des capacités

#### Capacités métier

- Agreement
- Demand
- Decision
- Inventory Visibility
- Supply
- Execution

#### Capacités techniques

- API Management
- Event Backbone
- Data Platform
- Rule Engine
- Case Management
- Observability

#### Capacités de développement

- CI/CD
- SDK
- Templates
- Developer Portal

#### Capacités de gouvernance

- Architecture
- Change Management
- Lifecycle Management
- Standards

### 2. Elle gouverne ses ressources centrales

FLOW doit posséder une gouvernance propre sur les ressources dont la cohérence est critique.

Cela implique :

- des owners identifiés ;
- des règles d'évolution ;
- des contrôles de qualité ;
- une gestion du cycle de vie ;
- des mécanismes d'arbitrage ;
- une observabilité opérationnelle.

### 3. Elle est ouverte et extensible

FLOW expose ses capacités au travers de :

- APIs unitaires ;
- APIs de masse ;
- événements ;
- projections d'informations ;
- flux analytiques.

Mais l'ouverture ne se limite pas à la consommation.

Elle doit aussi permettre à des domaines externes de configurer et d'étendre la plateforme selon des processus gouvernés.

De nouvelles capacités, règles, décisions, types de Case ou services peuvent être intégrés sans remettre en cause l'ensemble de la plateforme.

### 4. Elle préserve l'autonomie des consommateurs

FLOW ne cherche pas à imposer :

- une expérience utilisateur ;
- une technologie ;
- une organisation ;
- un canal.

> FLOW fournit les capacités.
>
> Les consommateurs construisent les expériences.

### 5. Elle porte sa propre gouvernance

Une plateforme est un actif partagé.

Elle nécessite :

- une gouvernance ;
- une gestion du changement ;
- une gestion du cycle de vie ;
- des standards ;
- des mécanismes d'arbitrage.

---

## À retenir

FLOW n'est ni un ERP, ni un OMS, ni une plateforme d'intégration.

FLOW est une plateforme d'entreprise composée de capacités métier, techniques et de gouvernance partagées au service des marques, des canaux, des partenaires et des business models du groupe.

FLOW ne juxtapose pas ERP et OMS : il cherche à réconcilier les responsabilités de Demand & Fulfillment dans un socle cohérent.

FLOW gouverne des ressources centralisées lorsque leur dispersion crée de l'incohérence.

FLOW reste ouvert grâce à des processus contrôlés de configuration, d'extension et de consommation.

FLOW n'est pas une recherche du progiciel idéal.

FLOW est une recherche du bon niveau de mutualisation des capacités et du bon lieu de vérité pour les responsabilités transverses.
