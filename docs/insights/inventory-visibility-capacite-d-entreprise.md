# Inventory Visibility est une capacité d'entreprise

## Contexte

Chez BRD comme chez GBM, les stocks physiques sont répartis entre plusieurs systèmes.

### BRD

- stock entrepôt dans les systèmes logistiques ;
- stock magasin dans Cegid ;
- vision unifiée principalement reconstituée dans NewStore.

### GBM

- stock entrepôt dans l'écosystème C-LOG ;
- stock magasin dans Storeland ;
- vision unifiée principalement reconstituée dans SoCloz.

## Constat

Dans les deux groupes, la première vision consolidée du stock apparaît aujourd'hui dans l'OMS omnicanal.

Cette situation est pratique pour les besoins de vente :

- Ship From Store ;
- Click & Collect ;
- sourcing omnicanal ;
- promesse client.

Mais elle présente une limite importante.

L'OMS est un consommateur du stock.

Il n'est pas naturellement le propriétaire du référentiel.

## Insight

La visibilité stock unifiée constitue une responsabilité d'entreprise.

Elle ne doit pas dépendre d'un produit spécialisé dans la vente ou le fulfillment omnicanal.

## Pourquoi ?

Le stock unifié est nécessaire pour bien plus que la vente :

- achat ;
- allocation ;
- réallocation ;
- transfert ;
- planification ;
- marketplace ;
- pilotage réseau ;
- optimisation logistique ;
- reporting groupe.

Ces usages dépassent largement le périmètre d'un OMS.

## Conséquence architecturale

Inventory Visibility doit devenir une capacité autonome de la plateforme.

Store
  \
   \
Warehouse ---> Inventory Visibility
   /
  /
Partners

L'OMS consomme cette capacité.

Il ne la porte pas.

## Observation intéressante

BRD et GBM sont partis d'histoires différentes.

Pourtant les deux organisations convergent vers la même conclusion.

Le stock unifié doit devenir un référentiel d'entreprise.

Cette convergence renforce fortement la légitimité d'Inventory Visibility comme Shared Business Capability de FLOW.

## À retenir

L'OMS aide à prendre des décisions de fulfillment.

Inventory Visibility fournit la vision unifiée des ressources.

Ce sont deux responsabilités différentes.