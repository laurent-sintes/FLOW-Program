# Engagements, Soft Allocation et Priorisation Commerciale

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Architecte, Sponsor, Contributeur</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>3 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Retrouver la mémoire de raisonnement et les hypothèses stabilisées</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Contexte

Les discussions entre BRD et GBM ont mis en évidence deux philosophies très différentes de gestion des engagements B2B.

Cette différence ne porte pas uniquement sur les processus ou les outils.

Elle porte sur la nature même de l'engagement commercial.

## Modèle GBM

Chez Groupe Beaumanoir, un principe historique est souvent résumé par l'adage :

> Premier arrivé, premier servi.

Une fois la commande confirmée et le stock alloué, l'engagement est considéré comme relativement protégé.

Le système privilégie :

- l'équité ;
- la prévisibilité ;
- la stabilité des engagements ;
- la confiance des clients.

Les commandes B2B sont généralement fermes, même si certaines options peuvent exister avant confirmation.

## Modèle BRD

Chez Boardriders, environ 50 % du chiffre d'affaires est réalisé en Wholesale.

Les engagements de début de saison ne sont pas toujours considérés comme totalement fermes.

Lorsqu'un client stratégique, comme un grand distributeur, passe une commande importante, l'entreprise peut décider de réallouer le stock disponible.

Cette réallocation peut conduire à :

- repousser des dates de livraison ;
- réduire certaines allocations ;
- modifier des promesses déjà accordées à d'autres clients.

Des traitements batchs nocturnes sont utilisés pour recalculer les engagements selon des règles de priorisation.

Un irritant majeur a été identifié côté BRD : le moteur de repriorisation des promesses de Sales Orders, utilisé lorsqu'une grosse commande Wholesale arrive pour un grand distributeur stratégique, repose sur un batch SQL nocturne.

Ce batch orchestre plusieurs dizaines de règles.

Le programme est devenu tellement complexe que sa maintenance est perçue comme risquée : les équipes n'osent plus le modifier sans craindre des effets de bord sur les promesses, allocations et dates futures.

Ce cas rend visible le problème central : la priorisation commerciale est légitime, mais lorsqu'elle est enfouie dans un traitement opaque, elle devient une dette de variabilité.

## Soft Allocation

Ce fonctionnement est très proche d'une logique de Soft Allocation.

Les allocations existent mais peuvent être révisées ultérieurement selon :

- la valeur stratégique du client ;
- le potentiel commercial ;
- les priorités métier ;
- les règles de gouvernance.

## Une décision peut remettre en cause des décisions déjà prises

Cet aspect est particulièrement important.

Une nouvelle demande ne déclenche pas uniquement une nouvelle décision.

Elle peut également conduire à réévaluer et modifier des décisions déjà prises.

Le moteur de décision doit alors être capable de :

- recalculer les engagements ;
- réallouer le stock ;
- republier les promesses ;
- gérer les impacts en chaîne.

Le cas du batch SQL BRD montre que cette capacité ne doit pas seulement exister techniquement.

Elle doit être explicite, testable, simulable et gouvernée.

Sinon, la richesse du modèle Wholesale se transforme en complexité conditionnelle non maîtrisée.

## Le portefeuille de demandes devient pilotable

Le référentiel de demandes ne doit plus être considéré comme uniquement transactionnel.

Il devient un objet de pilotage.

Les demandes existantes peuvent être analysées, replanifiées ou modifiées dans le cadre de décisions globales.

## Conséquence pour FLOW

FLOW doit être capable de supporter :

- des décisions unitaires en temps réel ;
- des traitements massifs ;
- des simulations ;
- des campagnes de réallocation ;
- des mises à jour batch du portefeuille de demandes.

La capacité d'accéder au référentiel de demandes pour le recalculer ou le modifier en masse constitue donc une exigence métier légitime.

Mais cette capacité ne doit pas être reconstruite comme un batch monolithique intouchable.

Elle doit s'appuyer sur des règles, contraintes, critères de priorité, simulations et traces de décision gouvernés.

## Insight majeur

Deux entreprises peuvent gérer exactement la même demande avec exactement le même stock et prendre des décisions opposées simplement parce qu'elles n'ont pas la même politique d'engagement.

Cette observation renforce l'importance du concept Agreement dans le modèle FLOW.

Ce qui différencie réellement les comportements n'est pas la demande elle-même mais les règles d'engagement qui lui sont associées.

Elle renforce aussi le [principe 8](../principes-directeurs/8-preserver-richesse-business-sans-complexite-si.md) : une variabilité business légitime doit être gouvernée, pas enfouie dans une complexité technique que plus personne n'ose faire évoluer.
