# Projet Titanic - BUT SD

Ce projet vise à prédire la survie des passagers du Titanic en utilisant des techniques d'apprentissage automatique (Machine Learning). Il a été structuré selon les principes du génie logiciel pour assurer sa modularité et sa reproductibilité.

## 🚀 Structure du Projet

- `data/` : Contient les fichiers bruts (`train.csv`, `test.csv`).
- `notebooks/` : Explorations initiales et tutoriels.
- `src/` : Scripts sources modulaires :
  - `data_loader.py` : Chargement automatique des données.
  - `preprocessing.py` : Nettoyage, sélection des features et encodage.
  - `model.py` : Entraînement du modèle Random Forest et évaluation.
- `requirements.txt` : Liste des dépendances Python nécessaires.
- `.gitignore` : Protection contre l'envoi de fichiers inutiles (venv, caches).

## 🛠️ Installation et Utilisation

1. **Créer l'environnement virtuel :**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   Installer les dépendances :

PowerShell
pip install -r requirements.txt
Lancer l'entraînement et l'évaluation :

PowerShell
python src/model.py
📊 Résultats
Le modèle actuel (Random Forest) obtient une précision d'environ 76% sur les données de validation internes.