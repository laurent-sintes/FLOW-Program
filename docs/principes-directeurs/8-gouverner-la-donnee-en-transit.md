# Principe 8 — Gouverner la donnée en transit

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

## Intention

FLOW ne doit pas seulement qualifier les informations au repos.

Il doit aussi gouverner les informations lorsqu'elles circulent entre domaines, applications, plateformes et services spécialisés.

Dans le SI actuel, beaucoup d'échanges sont nés comme des flux projet : une application cible exprime un besoin, une application source est analysée, puis une équipe flux développe un batch ou une intégration.

Cette logique a permis de répondre à des besoins concrets.

Mais elle crée aussi un foisonnement de flux, souvent difficiles à gouverner dans la durée.

## Principe

> Une donnée en transit n'est pas un simple flux technique entre deux applications.
>
> C'est un contrat durable entre une source de référence, des consommateurs et une responsabilité métier.

FLOW doit donc traiter les échanges de données comme des capacités d'entreprise.

Un échange important doit être conçu, documenté, supervisé et gouverné comme un actif durable du SI.

## Ce que le principe change

La logique historique est souvent la suivante :

```text
Besoin projet
    ↓
Mapping source / cible
    ↓
Flux batch ou intégration spécifique
    ↓
Consommation locale
```

FLOW doit promouvoir une logique différente :

```text
Donnée publiée
    ↓
Contrat de données
    ↓
Modes d'échange adaptés
    ↓
Consommateurs identifiés
    ↓
Supervision, qualité et réconciliation
```

Le sujet n'est donc pas seulement de choisir entre batch, API, événement ou stream.

Le sujet est de définir ce que l'entreprise publie durablement, pour qui, avec quelle qualité, quelle fraîcheur et quelle responsabilité.

## Le demi-flux comme graine architecturale

L'idée de demi-flux observée côté Beaumanoir est une intuition importante.

Elle distingue la publication d'une information de sa consommation.

```text
Flux point-à-point
    Application A → flux spécifique → Application B

Demi-flux
    Application A → publication normalisée
    Application B → consommation adaptée
```

Ce n'est pas encore une gouvernance complète.

Mais c'est une première séparation entre publier et consommer.

FLOW doit prolonger cette intuition vers des contrats de données gouvernés.

## Contrat de données

Un contrat de données précise au minimum :

- l'information publiée ;
- sa nature : command, event, fact, policy, objet métier, document ou nomenclature ;
- son statut pour le domaine qui la publie : source de référence ou projection ;
- la source de référence pour l'usage ;
- les consommateurs connus ;
- le mode d'échange : event, API, query, synchronisation, stream ou batch ;
- la granularité : unitaire ou masse ;
- la fraîcheur attendue ;
- la qualité attendue ;
- les règles de sécurité et d'accès ;
- les mécanismes de supervision, reprise et réconciliation.

Ce contrat ne doit pas être une documentation morte.

Il doit devenir un élément gouverné de l'architecture.

## Lien avec Source de référence / Projection

Le principe 7 qualifie les informations par nature et par statut Source de référence / Projection.

Le présent principe ajoute une dimension complémentaire : que se passe-t-il lorsque cette information circule ?

```text
Information au repos
    → nature
    → source de référence ou projection

Information en transit
    → contrat de données
    → mode d'échange
    → granularité
    → fraîcheur
    → consommateurs
    → supervision
```

Les deux principes sont donc complémentaires.

Le premier évite le fourre-tout `Master Data`.

Le second évite le foisonnement de flux projet.

## Conséquences pour FLOW

Ce principe conduit FLOW à :

- éviter les flux point-à-point créés uniquement par opportunité projet ;
- distinguer publication et consommation ;
- favoriser des données publiées selon des contrats durables ;
- choisir le mode d'échange selon l'usage, et non selon l'habitude technique ;
- rendre visibles les consommateurs d'une donnée ;
- expliciter la fraîcheur attendue et la qualité promise ;
- superviser les échanges critiques ;
- prévoir les mécanismes de reprise et de réconciliation ;
- inscrire les échanges importants dans une roadmap IT consolidée, au-delà des roadmaps projet.

## À retenir

FLOW ne doit pas seulement remplacer des applications.

Il doit remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.

C'est une condition pour construire un SI fédéré, observable et durable.
