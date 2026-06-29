# Sortie progressive de SAP ECC : découper les responsabilités

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Sponsors, architecture, métiers concernés</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Préparer les arbitrages sur les points sensibles de convergence</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

## Pourquoi c'est un hotspot

Le périmètre BRD s'appuie fortement sur SAP ECC.

La nature monolithique de cette solution rend une migration progressive vers FLOW plus difficile qu'un remplacement par lots fonctionnels simples.

Ce sujet concentre plusieurs tensions :

- périmètre applicatif initial de FLOW ;
- adhérences entre finance, stock, commandes et exécution ;
- découpage des responsabilités entre SAP, FLOW et les systèmes spécialisés ;
- trajectoire de migration ;
- risque de bascule trop large ou trop risquée.

## Risque principal

Le risque est de confondre sortie applicative et clarification des responsabilités.

Sortir une responsabilité de SAP ECC suppose de comprendre précisément ce qu'elle porte aujourd'hui : transaction, document, stock, finance, commande, statut, événement, règle ou intégration.

Sans cette clarification, FLOW risque soit de reprendre trop large, soit de laisser des adhérences cachées dans SAP.

## Ce que FLOW doit clarifier

FLOW doit notamment clarifier :

- quelles responsabilités doivent sortir de SAP ECC ;
- lesquelles doivent rester articulées avec SAP Finance ;
- quelles données et documents doivent continuer à alimenter FI/CO ;
- quelles responsabilités relèvent de Demand, de Supply, de Finance ou d'un système spécialisé ;
- dans quel ordre une trajectoire de sortie peut être sécurisée.

## À retenir

SAP ECC n'est pas seulement un système à remplacer.

C'est un nœud d'adhérences qui oblige FLOW à préciser sa trajectoire de migration, ses frontières avec Finance et le découpage réel des responsabilités.
