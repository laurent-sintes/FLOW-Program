# Référentiel des rôles

<!-- FLOW-READING-CARD:START -->
<div class="flow-reading-card">
  <div class="flow-reading-card__title">Repère de lecture</div>
  <div class="flow-reading-card__grid">
    <div>
      <span>Public cible</span>
      <strong>Mainteneur, Contributeur, Codex</strong>
    </div>
    <div>
      <span>Temps de lecture</span>
      <strong>2 min</strong>
    </div>
    <div>
      <span>Usage</span>
      <strong>Maintenir le référentiel, l'environnement local et les contrôles</strong>
    </div>
  </div>
</div>
<!-- FLOW-READING-CARD:END -->

Cette page définit les seuls rôles autorisés dans le champ `Public cible` des cartouches de lecture.

L'objectif est de garder les cartouches utiles et homogènes. Un cartouche doit aider le lecteur à savoir rapidement si la page le concerne.

## Rôles autorisés

| Rôle | Définition opérationnelle | Pages typiques |
| --- | --- | --- |
| Tous lecteurs | Lecteur général qui cherche à s'orienter, comprendre le vocabulaire ou consulter un repère transverse. | Accueil, glossaire, statistiques, index de section |
| Sponsor | Décideur qui doit comprendre la valeur, les risques, les arbitrages et les décisions à prendre. | Vision, hotspots, valeur attendue, notes de choix |
| Direction | Lecteur de niveau stratégique qui a besoin d'une synthèse courte et du positionnement global. | Abstract, vision synthétique, ambition |
| Architecte | Lecteur qui conçoit la cible, les principes, les responsabilités, les patterns et les frontières entre domaines. | Architecture cible, principes, patterns, hotspots |
| Métier | Lecteur qui porte les usages, règles, exceptions, arbitrages fonctionnels ou impacts opérationnels. | Contexte, hotspots, transformation, principes métier |
| Développeur | Lecteur qui doit comprendre les composants techniques, APIs, scripts, prototypes, moteurs ou choix d'implémentation. | Architecture technique, produits FLOW, administration, scripts |
| Delivery | Lecteur qui prépare la construction, l'intégration, le déploiement, l'exploitation ou la mise en œuvre. | Fiches produits, architecture cible, intégration, environnement |
| Change Manager | Lecteur qui prépare l'adoption, la communication, les changements de posture et l'accompagnement. | Transformation, valeur attendue, méthodologie, arbitrages, hotspots |
| PMO | Lecteur qui pilote la méthode, le cadrage, les livrables, les dépendances et la gouvernance projet. | Méthodologie Projet, processus de cadrage |
| Contributeur | Personne qui enrichit, corrige ou maintient le contenu du référentiel. | Administration, instructions Codex, statistiques |
| Mainteneur | Personne qui administre le site, les checks, GitHub Actions, l'environnement local ou la publication. | Administration du référentiel, environnement, workflows |
| Codex | Agent Codex ou consigne qui lui est destinée pour maintenir le référentiel de façon cohérente. | AGENTS.md, instructions Codex, environnement Codex |

## Règles d'utilisation

- Utiliser uniquement les libellés exacts listés ci-dessus.
- Mettre trois rôles maximum par cartouche.
- Ne pas créer de variantes au pluriel ou en minuscules.
- Ne pas utiliser `Product Owner` tant qu'il n'existe pas de pages dédiées à la gestion du backlog produit.
- Lorsqu'un rôle manque réellement, mettre à jour cette page avant de modifier les cartouches.
- Après toute modification de cette page ou d'une page documentaire, relancer `.\scripts\update-reading-metrics.ps1`, puis `.\scripts\check-site.ps1`.
