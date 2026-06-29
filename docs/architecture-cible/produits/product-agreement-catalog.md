# Fiche produit — Product Agreement Catalog

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecture, product owners, delivery</strong>
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

Le Product Agreement Catalog met à disposition de FLOW les informations produit, assortiment, conditions commerciales et agreements nécessaires pour traiter une demande.

Il ne remplace pas le PLM, le PIM ou les outils de design commercial.

Il fournit une projection d'exécution suffisamment stable pour vendre, acheter, promettre, réserver, allouer et exécuter.

<div class="flow-conviction">
  <p>FLOW n'a pas besoin d'un PIM bis.</p>
  <p>FLOW a besoin d'un catalogue d'exécution exploitable par les demandes.</p>
</div>

## Responsabilités portées

- Exposer les produits / articles utiles à l'exécution.
- Exposer les assortiments et agreements applicables.
- Fournir le contexte nécessaire aux décisions de promesse, allocation, achat et fulfillment.
- Découpler FLOW des variations de PLM, PIM, outils de prix ou design commercial.
- Permettre la coexistence des produits conçus et des produits importés.

## Ce que le produit ne porte pas

- La conception produit complète.
- L'enrichissement marketing produit.
- La gouvernance complète du PLM ou du PIM.
- La négociation commerciale complète si elle appartient à l'Engagement.
- La publication vers les canaux d'expérience.

## Consommateurs et contributeurs

| Acteur | Usage attendu |
| --- | --- |
| Cases | Comprendre le produit demandé et son agreement applicable. |
| Stock Unifié | Relier stock et article / variante. |
| Engagement / canaux | Fournir ou consommer assortiment et conditions utiles. |
| PLM / PIM / pricing | Alimenter les projections. |
| Achats / fournisseurs | Contribuer aux conditions d'achat ou données nécessaires. |

## Informations clés

| Information | Nature | Statut probable |
| --- | --- | --- |
| Article / Product Variant / EAN | Objet métier / Projection | Projection FLOW |
| Produit | Projection | Projection FLOW |
| Assortiment | Policy / Projection | Projection FLOW |
| Agreement | Policy / Objet métier | Projection ou source de référence selon périmètre |
| Prix / condition | Policy / Fact | Projection FLOW |
| Nomenclature taille / couleur | Nomenclature | Projection ou source de référence selon gouvernance |

## Capacités candidates

- Exposer un article / EAN utilisable par FLOW.
- Exposer les attributs nécessaires au fulfillment.
- Exposer les agreements applicables à une demande.
- Exposer les assortiments autorisés par canal, marque ou client.
- Gérer produits conçus et produits importés.
- Signaler les changements significatifs de catalogue.
- Tracer la source et la fraîcheur des projections.

## Interfaces candidates

- API de consultation article / variant.
- API de consultation agreement.
- API d'éligibilité produit / assortiment.
- Événements consommés : ProductPublished, ProductVariantUpdated, AgreementUpdated, AssortmentChanged.
- Événements publiés : ExecutionCatalogUpdated, AgreementProjectionUpdated.

## Premiers epics backlog

1. Définir le modèle minimal Article / EAN pour FLOW.
2. Définir les attributs nécessaires à la vente et à l'exécution.
3. Définir les attributs nécessaires à l'achat.
4. Clarifier la frontière PLM / PIM / Product Agreement Catalog.
5. Gérer produits conçus et produits importés.
6. Exposer les agreements applicables à une demande.
7. Définir les règles de fraîcheur et de qualité.
8. Construire une première projection catalogue pilote.
9. Connecter le catalogue aux décisions de promesse / allocation.
10. Identifier les doublons ou écarts de référentiel.

## Questions ouvertes

- Un catalogue Article / EAN suffit-il pour la vente ?
- Faut-il un catalogue Produit d'achat distinct ?
- Quels agreements doivent être sources dans FLOW et lesquels restent hors FLOW ?
- Comment représenter les Agreements lorsque BRD passe commande à une usine, alors que GBM associe plutôt ses Agreements à un fournisseur ?
- Comment éviter une duplication excessive du référentiel produit ?
- Quelle gouvernance pour les produits importés qui ne respectent pas les nomenclatures historiques ?
