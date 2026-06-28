# Gouverner les données en transit

## Insight

Dans le SI actuel, beaucoup d'échanges de données naissent comme des réponses projet.

Lorsqu'une application a besoin d'une donnée, l'équipe responsable analyse l'application source, rédige une spécification, puis sollicite une équipe flux pour développer un batch ou une intégration technique.

Cette logique existe notamment autour de Talend côté Beaumanoir et de Tibco côté Boardriders.

Elle répond à des besoins réels.

Mais elle produit progressivement un foisonnement de flux difficile à gouverner dans la durée.

## Le problème observé

Le flux est souvent conçu comme une solution entre deux applications, dans le budget et le calendrier d'un projet.

```text
Besoin applicatif local
    ↓
Analyse d'une application source
    ↓
Spécification projet
    ↓
Développement d'un flux
    ↓
Consommation par une application cible
```

Cette approche rend plus difficile la maîtrise d'entreprise :

- Qui publie réellement la donnée ?
- Quelle source fait foi pour quel usage ?
- Quelle fraîcheur est attendue ?
- Quelle qualité est garantie ?
- Quels consommateurs dépendent de cette donnée ?
- Comment diagnostique-t-on un écart ?
- Comment fait-on évoluer l'échange sans casser l'écosystème ?

Le résultat n'est pas seulement technique.

Il touche la gouvernance IT : les flux s'accumulent plus vite qu'ils ne s'inscrivent dans une trajectoire durable.

## La graine du demi-flux

Une intuition intéressante a déjà émergé côté Beaumanoir autour de la notion de <span class="flow-keyword">demi-flux</span>.

Cette idée introduit une séparation utile entre la publication d'une information et sa consommation.

```text
Flux point-à-point
    Application A → flux spécifique → Application B

Demi-flux
    Application A → publication normalisée
    Application B → consommation adaptée
```

Ce n'est pas encore une gouvernance complète de la donnée en transit.

Mais c'est une petite graine architecturale importante.

Elle permet de sortir d'une logique purement point-à-point et prépare une trajectoire plus durable :

```text
Flux point-à-point
    ↓
Demi-flux
    ↓
Publication / consommation découplées
    ↓
Contrats de données gouvernés
    ↓
Capacités de données d'entreprise
```

## Ce que FLOW doit prolonger

FLOW doit prolonger cette intuition.

La cible n'est pas seulement de moderniser les outils d'intégration.

La cible est de passer d'une logique de flux projet à une logique de <span class="flow-keyword">contrats de données gouvernés</span>.

Un échange de données doit préciser :

- la donnée publiée ;
- sa source responsable ;
- ses consommateurs ;
- sa fraîcheur attendue ;
- sa qualité attendue ;
- son mode d'échange : événement, API, query, synchronisation, stream ou batch ;
- sa granularité : unitaire ou masse ;
- ses règles de supervision ;
- ses mécanismes de reprise et de réconciliation.

<div class="flow-conviction">
  <p>FLOW ne doit pas seulement remplacer des applications.</p>
  <p>Il doit remplacer la logique de tuyauterie projet par une logique de contrats de données gouvernés.</p>
</div>

## Conséquence architecture

Cet insight doit se traduire dans l'architecture cible.

FLOW ne peut pas être seulement une plateforme de Case Management, de stock et de décisions.

Il doit aussi s'appuyer sur une capacité transverse de diffusion et gouvernance opérationnelle des données.

Cette capacité n'est pas forcément un composant applicatif unique.

Elle décrit plutôt une responsabilité d'architecture : rendre les échanges durables, explicites, observables et gouvernés.

Elle est directement liée :

- à la qualification Source / Projection ;
- aux modes d'échange ;
- aux événements ;
- aux APIs ;
- aux systèmes réintégrés ;
- à la colonne vertébrale opérationnelle ;
- à la capacité du CTO à produire une roadmap consolidée au-delà des roadmaps projet.

## À retenir

Le demi-flux montre qu'une partie de l'intuition existe déjà dans l'organisation.

FLOW doit la porter au niveau d'un principe d'architecture d'entreprise.

La donnée en transit ne doit plus être seulement une affaire de flux techniques.

Elle doit devenir une capacité durable, gouvernée et observable du SI.