Titanic Survival Prediction - Industrialisation & Qualité Logicielle
 
Présentation du Projet :
Ce projet a été réalisé dans le cadre du cours d'Ingénierie Logicielle appliquée à la Data Science (BUT VCOD). L'objectif principal est de transformer un notebook exploratoire sur le dataset Titanic en une solution logicielle modulaire, robuste et industrialisable.

Nous avons appliqué les bonnes pratiques de développement : refactorisation modulaire, tests unitaires, respect des normes PEP 8, et mise en place d'une pipeline CI/CD.

Équipe (BUT-SD-VCOD34)
```
-Léo Jean UNITE
-Romain SALMERON
-Baye-Badou DIENG
-Diego CASAS
```

Architecture du Projet
Le projet suit une structure modulaire pour séparer les responsabilités:

```
── .github/workflows/  # Configuration de la Pipeline CI/CD
── data/               # Données brutes et traitées
── docs/               # Documentation du projet
── models/             # Modèles entraînés
── notebooks/          # Code source
   ── data loader       # Chargement des données
   ── data preprocessing # Nettoyage et encodage (Sex, Pclass)
   ── model training    # Entraînement du modèle
   ── model evaluation  # Évaluation des performances
── requirements.txt    # Dépendances du projet
── pyproject.toml      # Configuration des outils (Black, Flake8)
```

Installation et Utilisation
1. Prérequis
Python 3.10+ 

2. Installation
Bash
# Clonage du dépôt
git clone https://github.com/TheColonel92/BUT-SD-A3-VCOD34-DEVLOG
cd BUT-SD-A3-VCOD34-DEVLOG

# Création et activation de l'environnement virtuel
python -m venv .venv
source .venv/bin/activate 

# Installation des dépendances
pip install -r requirements.txt


3. Exécution des tests
Pour valider le bon fonctionnement des modules de prétraitement:

Bash
pytest

Qualité Logicielle & CI/CD
Normes de code
Nous utilisons des outils automatisés pour garantir la propreté du code:

```
Black : Formatage automatique du code.
Flake8 : Linting pour vérifier la conformité PEP 8.
Docstrings : Documentation systématique des fonctions.
```

Pipeline CI/CD (GitHub Actions)
À chaque push sur la branche main, une pipeline automatique s'exécute pour:

```
Installer les dépendances.
Vérifier le formatage (Black).
Linter le code (Flake8).
Lancer les tests unitaires (Pytest).
```

Note technique : Nous avons résolu des problèmes de compatibilité inter-plateformes (Windows/Linux) en purgeant les dépendances spécifiques à l'OS (comme pywinpty) du fichier requirements.txt.

Résultats du Modèle
Le modèle Random Forest implémenté atteint une précision de 76% sur le jeu de test. L'accent a été mis sur la reproductibilité du pipeline d'entraînement plutôt que sur la seule optimisation du score.
