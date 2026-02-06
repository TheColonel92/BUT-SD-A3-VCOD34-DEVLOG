"""
model_training.py
Entraîne un modèle RandomForest sur les données Titanic.
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save(X_train_path, y_train_path, model_out_path):
    """Charge les données, entraîne le modèle et le sauvegarde."""
    X_train = pd.read_csv(X_train_path)
    y_train = pd.read_csv(y_train_path).squeeze()
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)
    joblib.dump(model, model_out_path)
    print(f"Modèle sauvegardé dans {model_out_path}")

if __name__ == "__main__":
    # Chemins par défaut (à adapter si besoin)
    X_train_path = "X_train.csv"
    y_train_path = "y_train.csv"
    model_out_path = "model.joblib"
    train_and_save(X_train_path, y_train_path, model_out_path)
