# Outils de tests

Cette page decrit comment executer et superviser la suite de tests de Fancy Tools.

## Vue d ensemble

La suite couvre tous les modules publics du paquet `fancy_tools` et s appuie sur Pytest ainsi que pytest-cov pour la couverture. Les tests se trouvent dans le dossier `tests/` et reproduisent la structure du code source.

## Preparation

- Activer l environnement virtuel :
  ```bash
  source .venv/bin/activate
  ```
- Installer les dependances de developpement si necessaire :
  ```bash
  uv sync --dev
  # ou
  pip install -e ".[dev]"
  ```

## Lancer les tests

```bash
# Suite complete
pytest tests/

# Mode verbeux
pytest tests/ -v

# Fichier specifique
pytest tests/unit_tests/test_markdown/test_renderer.py

# Test precis
pytest tests/unit_tests/test_markdown/test_renderer.py::test_read_markdown_file_success
```

## Couverture de code

```bash
# Rapport terminal
pytest tests/ --cov=fancy_tools --cov-report=term-missing

# Rapport HTML
pytest tests/ --cov=fancy_tools --cov-report=html

# Deux formats en meme temps
pytest tests/ --cov=fancy_tools --cov-report=term-missing --cov-report=html
```

Les rapports HTML sont generes dans `htmlcov/`. Ouvrir `htmlcov/index.html` dans un navigateur pour une analyse detaillee.

## Resultats actuels

- Couverture globale : **72 %**
- `fancy_tools.markdown.renderer` : 71 %
- `fancy_tools.pdf.converter` : 54 % (dependances optionnelles requises pour des scenarios complets)
- `fancy_tools.project.to_file` : 77 %
- `fancy_tools.templates_and_cheatsheets.validator` : 90 %
- `fancy_tools.web.favicon` : 71 %

## Fixtures principales

Les fixtures communes se trouvent dans `tests/conftest.py` :

- `temp_dir` : repertoire temporaire par test
- `sample_markdown_content` : contenu Markdown de reference
- `sample_markdown_file` : fichier Markdown temporaire
- `sample_project_structure` : petite arborescence de projet
- `runner` : instance `CliRunner` pour tester les commandes Click

## Bonnes pratiques

1. Cibler toutes les branches de code (chemins heureux et erreurs).
2. Mutualiser la preparation via des fixtures pour simplifier les cas de test.
3. Isoler chaque test pour le rendre deterministe et reproductible.
4. Simuler les dependances externes (fichier, reseau, bibliotheques optionnelles).
5. Mettre a jour la documentation des tests (`tests/README_TESTS.md`) en cas de modification structurelle.

## Resolution de problemes

| Situation | Actions suggerees |
|-----------|------------------|
| ImportError | Verifier l activation de l environnement et lancer `uv sync`. |
| Couverture faible | Identifier les lignes manquantes via `pytest --cov-report=term-missing`. |
| Tests instables | Utiliser `pytest --maxfail=1 --lf` pour reexecuter uniquement les echecs recents. |
| Erreurs de permissions | Verifier les droits sur les fichiers temporaires, surtout sur macOS/Linux. |

## Ressources complementaires

- Documentation detaillee de la suite : `tests/README_TESTS.md`
- Guide Pytest : https://docs.pytest.org/
- Guide pytest-cov : https://pytest-cov.readthedocs.io/
