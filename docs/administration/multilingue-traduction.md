# Multilingue et traduction

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

Le référentiel FLOW est maintenu en français comme source de référence.

Le site publié est généré en deux langues :

- `/fr/` : version française, issue directement de `docs/` ;
- `/en/` : version anglaise générée à partir de la source française.

## Principe

Les contributeurs ne maintiennent pas deux arborescences documentaires à la main.

La commande de build produit une arborescence générée dans `.generated/i18n/`, puis construit les deux sites statiques dans `site/fr/` et `site/en/`.

Ces dossiers sont des artefacts locaux :

- `site/` ne doit pas être committé ;
- `.generated/` ne doit pas être committé ;
- `docs/` reste la source éditoriale.

## Sélecteur de langue

Le build multilingue génère une configuration MkDocs par langue.

Chaque configuration ajoute le sélecteur de langue Material via `extra.alternate`.

Le lecteur peut donc passer de la version française à la version anglaise depuis l'en-tête du site.

Un script léger ajuste le lien pour conserver le chemin courant : depuis `/fr/faq/`, le bouton `English` pointe vers `/en/faq/`.

## Traduction anglaise

La version anglaise est actuellement une version générée depuis le français avec un bandeau de traduction.

Ce choix permet de poser l'architecture multilingue sans créer immédiatement une dette de duplication manuelle.

La cible est d'ajouter ensuite un cache de traduction par page ou par fragment :

- hash de la source française ;
- glossaire contrôlé des termes FLOW ;
- régénération uniquement des pages modifiées ;
- contrôle `check-site` pour détecter les traductions obsolètes.

Les termes structurants doivent rester maîtrisés : `FLOW`, `Demand`, `Fulfillment`, `Supply`, `Case`, `Agreement`, `Source de référence`, `Projection`, `Decision`, `Promise`.

## Commandes

Build local :

```powershell
.\scripts\build-docs.ps1
```

Contrôle complet :

```powershell
.\scripts\check-site.ps1
```

GitHub Actions exécute également :

```powershell
python scripts/build_multilang.py
python scripts/check_site.py --external-links --external-timeout 10
```

Cette validation CI contrôle le build multilingue et les liens externes avec un accès réseau plus fiable que Codex.

Diagnostic environnement :

```powershell
.\scripts\doctor.ps1
```

## Garde-fous

Après toute évolution du multilingue :

- vérifier que `site/fr/` et `site/en/` sont générés ;
- vérifier que le sélecteur de langue apparaît dans l'en-tête ;
- vérifier que `.generated/` et `site/` ne sont pas suivis par Git ;
- relancer `.\scripts\check-site.ps1`.
