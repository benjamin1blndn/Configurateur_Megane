# Configurateur Renault MEGANE IV phase 2 (brochure janvier 2021)

Configurateur statique (HTML/JS, sans dépendance) reconstitué à partir de la brochure `2021_01.pdf`.
Choix : modèle (Berline/Estate), finition (Zen, SL Limited, Intens, R.S. Line), motorisation, couleur (10 teintes),
jantes, sellerie, options et packs, avec récapitulatif. La configuration est sauvegardée dans l'URL (#).

## Utiliser
- Local : `python3 -m http.server` puis http://localhost:8000
- GitHub Pages : poussez sur `main` (workflow `.github/workflows/pages.yml` inclus), puis Settings > Pages > Source : GitHub Actions.

## Régénérer les visuels depuis le PDF
`python extract_assets.py 2021_01.pdf` (nécessite `poppler-utils`).

## Rendus identiques à l'ancien configurateur
L'ancien configurateur affichait un rendu 3D par combinaison. La brochure n'en contient pas : l'appli affiche
la photo de la teinte choisie + les vignettes jantes/sellerie. Pour de vrais rendus, déposez-les dans
`assets/renders/` nommés `{body}_{trim}_{color}_{wheel}.jpg`, par ex. `berline_intens_cuivre-solar_allium-17.jpg`.
Ils sont utilisés automatiquement en priorité.
Valeurs : body = berline|estate ; trim = zen|limited|intens|rsline ;
color = blanc-glacier|blanc-nacre|gris-highland|gris-baltique|gris-titanium|noir-etoile|bleu-iron|bleu-cosmos|rouge-flamme|cuivre-solar ;
wheel = elliptik-16|limited-16|impulse-16|allium-17|hightek-18|montlhery-17|magny-cours-18.

Projet non officiel, visuels © Renault.
