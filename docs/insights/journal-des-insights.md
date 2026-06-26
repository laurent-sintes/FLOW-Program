# Journal des Insights

## Intention

Ce journal conserve les insights du programme FLOW sous une forme courte.

Les numéros permettent de garder la trace chronologique d'apparition des idées.

Le classement permet de retrouver les insights par famille de réflexion.

Un même insight peut nourrir plusieurs articles, principes ou décisions d'architecture, mais il est rangé ici dans sa famille principale.

## Positionnement de FLOW

### Insight 001 — FLOW n'est probablement pas un OMS
Le problème dépasse l'omnicanalité Vente. FLOW doit traiter les demandes, les engagements, les décisions et l'exécution.

### Insight 010 — FLOW est devenu un programme d'entreprise
FLOW dépasse désormais le simple cadre d'un projet SI.

### Insight 011 — FLOW n'est pas une plateforme d'engagement
Les métiers souhaitent conserver Salesforce, SFCC, Elastic et les autres outils de relation client. FLOW doit exposer des APIs, des décisions et des capacités réutilisables plutôt que remplacer les canaux d'engagement.

### Insight 012 — FLOW est une plateforme d'orchestration des demandes
La plateforme reçoit des demandes provenant des domaines d'engagement puis coordonne la décision et l'exécution. FLOW se positionne davantage comme une Demand Orchestration Platform que comme une Customer Engagement Platform.

### Insight 013 — Le périmètre de FLOW ne peut pas être défini par le remplacement d'applications
L'objectif initial de remplacement de Storeland, SoCloz, SAP ou NewStore s'est révélé insuffisant. Le véritable périmètre est défini par les responsabilités métier que la plateforme doit porter et mutualiser.

### Insight 020 — FLOW réconcilie ERP et OMS dans une plateforme Demand
La séparation ERP / OMS crée des transferts, doublons et zones grises de responsabilité. FLOW cherche à reconstruire une cohérence unique autour du Case, du stock, de la promesse, de l'allocation et de l'orchestration.

### Insight 027 — FLOW devient le moteur de la convergence
La plateforme FLOW, et le programme qui la gouverne, deviennent le moteur de la convergence : pratiques business, responsabilités métier, capacités partagées, règles de décision, données opérationnelles, trajectoires applicatives et autonomie locale.

## Modèle conceptuel

### Insight 002 — Les demandes sont plus stables que les processus
Les organisations changent, les processus évoluent, les demandes restent.

### Insight 003 — Agreement est le pivot métier
Les différences B2B, B2C ou Achat proviennent principalement des engagements applicables.

### Insight 014 — Agreement évite de multiplier les variantes de commandes
Agreement apporte les règles et conditions de traitement applicables à une commande. Une commande peut rester plus générique si son contexte, l'Agreement et un référentiel de règles pilotent dynamiquement les variations de traitement. FLOW doit donc éviter de décliner une même commande en dizaines de variantes de processus lorsque les différences peuvent être gouvernées par des règles explicites.

### Insight 018 — Les organisations consomment la plateforme, elles ne la structurent pas
B2B, B2C, retail, wholesale ou achat sont des organisations, canaux ou contextes de consommation. Ils doivent consommer FLOW, tandis que la plateforme doit être urbanisée selon des responsabilités plus durables.

### Insight 019 — Demand / Supply remplace les oppositions achat / vente
La conception ne doit pas partir de “j'achète” ou “je vends”, ni de B2C ou B2B. Elle doit distinguer la demande à instruire, décider et promettre, du réseau d'exécution à mobiliser.

## Convergence, fédération et gouvernance

### Insight 007 — Une plateforme doit fédérer autant qu'elle mutualise
FLOW ne doit pas devenir un nouveau monolithe.

### Insight 008 — Le tenant est une notion de gouvernance
Le tenant permet la différenciation maîtrisée.

### Insight 015 — La convergence est IT et business model
Le point de départ n'est pas seulement une convergence de systèmes. FLOW doit aussi traiter les différences de business models, de pratiques business, de modes d'engagement, d'achat, de vente et d'exploitation des marques.

### Insight 016 — BRD et GBM ont des centres de gravité inverses
GBM est historiquement un SI retail ouvert ensuite au e-commerce puis au B2B. BRD est plutôt issu d'un socle B2B / wholesale ensuite adapté au retail. FLOW doit créer une couche commune au-dessus de ces héritages différents.

### Insight 017 — La convergence est aussi intra-GBM
La convergence ne concerne pas seulement BRD et GBM. Elle concerne aussi les marques GBM entre elles, notamment lorsque certaines disposent de processus outillés et d'autres de pratiques plus manuelles ou dispersées.

## Opérations, décision et données

### Insight 004 — Le stock est une vue avant d'être un système
Le besoin réel est une visibilité fiable et explicable.

### Insight 005 — Inventory Visibility est une Shared Business Capability
Cette capacité doit être mutualisée au niveau plateforme.

### Insight 006 — Decision Services est une Shared Business Capability
ATP, allocation, sourcing et promesse relèvent d'une même famille de décisions.

### Insight 009 — L'observabilité est un sujet métier
La confiance dépend de la capacité à expliquer les données et les décisions.

### Insight 023 — Le PIM n'est pas naturellement dans FLOW
Si le PIM soutient le design de l'offre, les assortiments, les commercial agreements, les prix ou les contenus d'engagement client, il doit rester hors FLOW. FLOW a besoin d'une projection produit d'exécution, pas d'un PIM bis.

### Insight 024 — Les données doivent être qualifiées plutôt que rangées dans “Master Data”
FLOW doit distinguer les natures d'information — Command, Event, Fact, Policy, Objet Métier, Document, Nomenclature — et leur statut — Source ou Projection. La notion de Master Data est trop large pour guider l'architecture.

### Insight 026 — C-LOG doit être lu comme un acteur Supply, pas comme un simple EAI
C-LOG ne doit pas être réduit à une brique d'intégration. Il peut porter ou agréger des responsabilités logistiques, entrepôt, transport, stock et événements d'exécution.

## Finance et adhérences externes

### Insight 021 — Le fulfillment précède les documents
Une conception orientée ERP part souvent de la commande, de la facture, du bon de livraison ou des écritures. FLOW doit partir de la demande à satisfaire, puis intégrer les documents et la finance au bon moment.

### Insight 022 — La finance doit rester un domaine séparé
FLOW peut produire ou consommer des faits, documents, événements économiques et références nécessaires à la comptabilité. Mais FLOW ne remplace pas la comptabilité, la fiscalité ou le contrôle de gestion.

### Insight 025 — CBS est un domaine spécialisé contributeur et consommateur de FLOW
CBS porte des processus fournisseurs spécialisés : packing list, conformité documentaire, livraison amont, collaboration fournisseur. Certaines responsabilités qu'il manipule — commande, cycle de vie, statuts, événements, vision 360 — peuvent toutefois relever de FLOW.

## Vue chronologique synthétique

| Insight | Famille principale | Résumé |
| --- | --- | --- |
| 001 | Positionnement | FLOW n'est probablement pas un OMS. |
| 002 | Modèle conceptuel | Les demandes sont plus stables que les processus. |
| 003 | Modèle conceptuel | Agreement est le pivot métier. |
| 004 | Opérations, décision et données | Le stock est une vue avant d'être un système. |
| 005 | Opérations, décision et données | Inventory Visibility est une Shared Business Capability. |
| 006 | Opérations, décision et données | Decision Services est une Shared Business Capability. |
| 007 | Convergence, fédération et gouvernance | Une plateforme doit fédérer autant qu'elle mutualise. |
| 008 | Convergence, fédération et gouvernance | Le tenant est une notion de gouvernance. |
| 009 | Opérations, décision et données | L'observabilité est un sujet métier. |
| 010 | Positionnement | FLOW est devenu un programme d'entreprise. |
| 011 | Positionnement | FLOW n'est pas une plateforme d'engagement. |
| 012 | Positionnement | FLOW est une plateforme d'orchestration des demandes. |
| 013 | Positionnement | Le périmètre de FLOW ne peut pas être défini par le remplacement d'applications. |
| 014 | Modèle conceptuel | Agreement évite de multiplier les variantes de commandes. |
| 015 | Convergence, fédération et gouvernance | La convergence est IT et business model. |
| 016 | Convergence, fédération et gouvernance | BRD et GBM ont des centres de gravité inverses. |
| 017 | Convergence, fédération et gouvernance | La convergence est aussi intra-GBM. |
| 018 | Modèle conceptuel | Les organisations consomment la plateforme, elles ne la structurent pas. |
| 019 | Modèle conceptuel | Demand / Supply remplace les oppositions achat / vente. |
| 020 | Positionnement | FLOW réconcilie ERP et OMS dans une plateforme Demand. |
| 021 | Finance et adhérences externes | Le fulfillment précède les documents. |
| 022 | Finance et adhérences externes | La finance doit rester un domaine séparé. |
| 023 | Opérations, décision et données | Le PIM n'est pas naturellement dans FLOW. |
| 024 | Opérations, décision et données | Les données doivent être qualifiées plutôt que rangées dans “Master Data”. |
| 025 | Finance et adhérences externes | CBS est un domaine spécialisé contributeur et consommateur de FLOW. |
| 026 | Opérations, décision et données | C-LOG doit être lu comme un acteur Supply, pas comme un simple EAI. |
| 027 | Positionnement | FLOW devient le moteur de la convergence. |
