# Fiche produit — Gouvernance des données en transit

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
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Relier les concepts FLOW aux produits, patterns et responsabilités cible</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Intention

La Gouvernance des données en transit transforme les échanges entre applications en contrats durables.

Le produit ne vise pas seulement à créer des flux.

Il vise à gouverner ce qui est publié, consommé, supervisé, réconcilié et maintenu dans la durée.

<div class="flow-conviction">
  <p>Une donnée en transit n'est pas un tuyau technique.</p>
  <p>C'est un contrat durable entre source de référence, consommateurs et responsabilité métier.</p>
</div>

## Responsabilités portées

- Décrire les contrats de données critiques.
- Distinguer publication et consommation.
- Documenter nature d'information, source de référence / projection, mode d'échange et granularité.
- Définir fraîcheur, qualité, supervision, reprise et réconciliation.
- Réduire le foisonnement de flux projet.
- Soutenir la réintégration des systèmes existants autour de FLOW.

## Ce que le produit ne porte pas

- Tous les flux techniques du SI.
- L'implémentation détaillée de chaque connecteur.
- Le MDM complet.
- Le monitoring infrastructure pur.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Architecture / intégration | Gouverner les échanges. |
| Produits FLOW | Publier ou consommer événements, facts, documents, nomenclatures. |
| Systèmes existants | S'aligner sur des contrats explicites. |
| Data / observabilité | Suivre fraîcheur, qualité et réconciliation. |
| PO / PM | Identifier les échanges nécessaires à leur produit. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Contrat de données | Document / Policy | Source de référence FLOW |
| Information publiée | Command / Event / Fact / Policy / Objet métier / Document / Nomenclature | Selon contrat |
| Producteur | Nomenclature / Objet | Source de référence gouvernée |
| Consommateur | Nomenclature / Objet | Source de référence gouvernée |
| Mode d'échange | Nomenclature | Source de référence FLOW |
| Fraîcheur / qualité attendue | Policy | Source de référence FLOW |
| Écart de réconciliation | Fact | Source de référence ou projection |

## Capacités candidates

- Définir un contrat de données.
- Identifier producteurs et consommateurs.
- Décrire le mode d'échange : API, event, stream, batch, query.
- Décrire la granularité : unitaire ou masse.
- Définir fraîcheur et qualité attendues.
- Suivre la supervision et les incidents.
- Définir les mécanismes de reprise et réconciliation.
- Cartographier les flux remplacés ou rationalisés.

## Interfaces candidates

- Catalogue des contrats de données.
- API de consultation des contrats.
- Événements de changement de contrat.
- Dashboard de fraîcheur / qualité / incidents.
- Liens vers observabilité technique et métier.

## Premiers epics backlog

1. Définir le modèle de contrat de données FLOW.
2. Recenser les échanges critiques autour du Case, stock, catalogue et Supply.
3. Définir les modes d'échange autorisés.
4. Définir les règles de granularité unitaire vs masse.
5. Définir les exigences de fraîcheur par usage.
6. Définir la supervision minimale.
7. Définir les mécanismes de reprise et réconciliation.
8. Transformer un premier flux projet en contrat gouverné.
9. Documenter l'idée de demi-flux comme trajectoire intermédiaire.
10. Intégrer les contrats au processus d'architecture.

## Questions ouvertes

- Ce produit est-il un produit FLOW ou un standard d'architecture transverse ?
- Quelle frontière avec les outils d'intégration existants : Talend, Tibco, EAI ?
- Quels contrats doivent être obligatoires dès le MVP ?
- Comment articuler contrats de données et ownership produit ?
- Quelle gouvernance pour refuser un nouveau flux point-à-point ?
