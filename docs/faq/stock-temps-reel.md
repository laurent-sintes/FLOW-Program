# À quoi ça sert un stock temps réel ?

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Tous lecteurs</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>7 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Lire et maintenir le référentiel FLOW</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Question

Étant donné qu'un magasin propose du Ship From Store et que le POS envoie un événement dès qu'une vente est faite, on ne pourra pas garantir le stock disponible sur le site eCommerce.

Il faut du temps pour que l'événement soit consommé par le Stock Unifié et que le site eCommerce soit renotifié de la diminution du stock. Quelques secondes peut-être. Aujourd'hui, les synchronisations batch peuvent durer 30 minutes.

Mais si le client a déjà mis un article dans son panier, retirer l'article du catalogue ne servira à rien et on aura encore des demandes non satisfaites.

Le problème semble insoluble et le temps réel, ou asynchrone court, ne va pas nécessairement résoudre le problème.

## Réponse courte

La question est juste : un stock temps réel ne garantit jamais une disponibilité parfaite.

Si l'objectif est de garantir qu'aucune demande non satisfaite ne se produira jamais, le problème est insoluble.

Mais ce n'est pas le bon objectif.

L'objectif de FLOW n'est pas de prétendre à une vérité instantanée parfaite. L'objectif est de réduire fortement l'incertitude, de la rendre gouvernable, et de donner au Fulfillment les moyens de promettre, réserver, arbitrer, expliquer et réagir.

Sans stock temps réel, FLOW promet sur une photo ancienne.

Avec un Stock Unifié temps réel, FLOW promet sur une vision fraîche, qualifiée et réconciliable.

C'est imparfait, mais c'est précisément ce qui transforme un problème subi en problème gouvernable.

## Ce que le temps réel ne résout pas

Le temps réel ne supprime pas :

- la concurrence sur le dernier article ;
- les ventes simultanées entre magasin, eCommerce, marketplace et service client ;
- les articles déjà dans un panier avant la mise à jour du stock ;
- les écarts terrain : casse, vol, article mal rangé, oubli de scan, inventaire faux ;
- les retards ou pertes d'événements ;
- les périodes offline en magasin ;
- les décisions de priorité entre clients, canaux ou promesses.

Retirer un article du catalogue après une vente magasin ne suffit pas si un client a déjà placé l'article dans son panier.

Le vrai point de contrôle n'est donc pas seulement l'affichage catalogue. Il se situe dans la décision de promesse, la réservation et la confirmation de commande.

## Ce que le temps réel améliore fortement

Passer d'un batch de 30 minutes à un asynchrone court ne rend pas le système parfait.

Mais cela change l'ordre de grandeur du problème.

Avec des batchs de 30 minutes, le site eCommerce peut vendre pendant longtemps sur une disponibilité dépassée. Avec des événements consommés en quelques secondes, la fenêtre de risque devient beaucoup plus courte, les erreurs se concentrent sur les situations réellement concurrentes, et les écarts deviennent observables.

Le Stock Unifié sert donc à :

- réduire le délai entre un mouvement physique et une disponibilité exploitable ;
- distinguer stock physique, stock disponible, stock réservé, stock alloué et stock promettable ;
- exposer une disponibilité contextualisée selon canal, promesse, pays, client ou priorité ;
- permettre une réservation courte avant confirmation ;
- calculer une promesse avec un niveau de confiance ;
- détecter les événements manquants, en retard ou incohérents ;
- réconcilier les écarts entre stock théorique et stock observé ;
- expliquer pourquoi une demande a été acceptée, refusée, splitée, substituée ou réorientée.

Le temps réel est donc un moyen.

La vraie capacité cible est l'<span class="flow-keyword">Inventory Visibility</span> gouvernée : fraîcheur, cohérence, confiance, réservation, allocation, observabilité et réconciliation.

## Rapprochement avec les hotspots et insights

Cette question est directement liée au hotspot [Stock temps réel : obtenir les mouvements à la source](../hotspots/stock-temps-reel.md).

Elle confirme aussi l'insight [Inventory Visibility est une capacité d'entreprise](../insights/inventory-visibility-capacite-d-entreprise.md) : la visibilité stock ne doit pas être seulement une fonctionnalité d'OMS ou de site eCommerce. Elle sert aussi l'allocation, la réallocation, le B2B, le SAV, la marketplace, le pilotage réseau et la promesse.

Elle rejoint enfin l'insight [Cohérence de l'information : fraîcheur, DataHub et CEP](../insights/coherence-donnees-fraicheur-datahub-cep.md) : la fraîcheur seule ne suffit pas. Une information fraîche mais incohérente reste dangereuse. FLOW doit maîtriser le triptyque fraîcheur, cohérence et observabilité.

## Rapprochement avec la solution FLOW

La réponse FLOW est portée par la fiche produit [Stock Unifié](../architecture-cible/produits/stock-unifie.md) et par le pattern [Operational DataHub](../architecture-cible/patterns/operational-datahub.md).

Le Stock Unifié ne doit pas être conçu comme une simple copie centrale du stock.

Il doit maintenir :

- un ledger ou historique des mouvements ;
- des projections de disponibilité prêtes à lire ;
- des règles de disponibilité et de promesse ;
- des réservations avec expiration ;
- des allocations ou tags de stock par finalité ;
- des indicateurs de fraîcheur et de confiance ;
- des mécanismes de réconciliation ;
- des événements publiés vers les canaux et les Cases.

Dans cette lecture, le site eCommerce n'est pas le lieu qui garantit seul la disponibilité.

Il affiche une promesse probable, puis FLOW vérifie, réserve ou réarbitre au moment où la demande devient engageante.

## Pratiques à mettre en place

Pour réduire les problèmes résiduels, FLOW devra combiner plusieurs pratiques.

| Pratique | Effet attendu | Limite |
| --- | --- | --- |
| Réservation courte au panier | Bloquer temporairement une quantité lorsqu'un client manifeste une intention forte. | Risque de bloquer trop de stock si les paniers sont abandonnés ; nécessite un TTL court et une expiration fiable. |
| Réservation ferme au checkout | Vérifier et réserver au moment où la commande devient engageante. | Peut encore échouer si le stock a bougé entre panier et paiement. |
| Stock de sécurité par canal ou magasin | Masquer une petite quantité pour absorber les écarts terrain et ventes simultanées. | Réduit la disponibilité affichée et peut diminuer le chiffre d'affaires si trop conservateur. |
| Disponibilité avec niveau de confiance | Afficher ou utiliser une disponibilité différente selon fraîcheur, source et historique d'écarts. | Demande une gouvernance métier des seuils de confiance. |
| Dégradation contrôlée | Basculer vers click and collect, livraison plus longue, autre magasin, substitution ou backorder. | Nécessite des règles de promesse et une communication claire au client. |
| Revalidation à chaque étape critique | Recontrôler le stock au panier, checkout, paiement, préparation et expédition. | Ajoute des appels et doit rester ergonomique. |
| Événements idempotents et rejouables | Éviter qu'un retard, doublon ou événement perdu crée une incohérence durable. | Nécessite une vraie discipline d'intégration. |
| Réconciliation opérationnelle | Détecter et corriger les écarts entre stock théorique et stock terrain. | Ne supprime pas les écarts, mais les rend pilotables. |

La réservation au panier doit être utilisée avec prudence.

Elle est pertinente pour les produits rares, les derniers articles, les opérations commerciales, les paniers qualifiés ou les clients connectés. Elle est moins pertinente si elle bloque massivement du stock sur des paniers abandonnés.

La bonne approche est donc souvent graduée :

```text
Affichage catalogue
    -> disponibilité probable

Ajout panier
    -> option de réservation courte selon contexte

Checkout
    -> réservation ferme ou promesse engageante

Préparation / expédition
    -> confirmation, exception ou réarbitrage
```

## Expériences et références externes

Les solutions du marché vont dans le même sens : elles ne vendent pas le temps réel seul, mais un ensemble disponibilité + réservation + promesse + réconciliation.

- [Microsoft Dynamics 365 Inventory Visibility](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility) met en avant la visibilité temps réel, les réservations souples pour éviter la survente, l'ATP et l'allocation. La documentation précise aussi que l'agrégation peut se refléter immédiatement, à la seconde ou à la minute selon l'intervalle de publication des données : c'est donc bien un temps réel opérationnel, pas une vérité magique.
- [Microsoft Dynamics 365 Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) décrit le cas de plusieurs systèmes qui prennent des commandes en parallèle et la nécessité d'une source unique de disponibilité réservable pour éviter le double-booking du dernier article.
- [Adobe Commerce Inventory Management](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations) combine stock salable, source selection algorithm et réservations. La documentation montre aussi les risques résiduels : les files de messages doivent tourner en continu et des réservations peuvent rester bloquées si elles ne sont pas compensées correctement.
- [Shopify Inventory States](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states) distingue `On hand`, `Available`, `Committed`, `Unavailable` et `Incoming`. Cette séparation confirme qu'un stock exploitable n'est pas seulement une quantité physique.
- [Google Merchant Center - Availability](https://support.google.com/merchants/answer/6324448) exige la cohérence entre disponibilité publiée, page produit et checkout. Google peut désapprouver des produits si l'information est incohérente, ce qui illustre le coût business d'une disponibilité mal maîtrisée.
- [Vogue Business - RFID et visibilité stock dans la mode](https://www.vogue.com/article/the-tech-shaking-up-fashions-inventory-load) cite des usages positifs de RFID pour améliorer la visibilité stock, le Ship From Store et le Click & Collect. L'article mentionne notamment une hausse d'exactitude stock observée chez Ganni après déploiement RFID.
- [Inventory record inaccuracy in grocery retailing](https://arxiv.org/abs/2506.05357) rappelle l'autre côté du problème : même avec de meilleurs flux, l'écart entre stock système et stock réel reste un sujet terrain. L'étude analyse environ 24 000 SKU dans 11 magasins et montre que les audits de stock peuvent produire un effet business significatif.

## À retenir

Le stock temps réel ne garantit pas qu'aucune commande ne sera jamais impossible à servir.

Il sert à réduire massivement la fenêtre d'erreur, rendre la disponibilité exploitable par les décisions de Fulfillment, permettre des réservations, exposer la fraîcheur et la confiance, détecter les anomalies et réarbitrer plus vite.

La promesse FLOW n'est pas l'infaillibilité.

La promesse FLOW est de rendre la disponibilité gouvernable, explicable et réconciliable.
