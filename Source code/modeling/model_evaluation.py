"""
model_evaluation.py
Génère le fichier de soumission Kaggle à partir du modèle entraîné.
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def predict_and_submit(model_path, X_test_path, test_csv_path, output_path):
    """Charge le modèle, prédit sur X_test, et sauvegarde la soumission."""
    model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    test_df = pd.read_csv(test_csv_path)
    predictions = model.predict(X_test)
    output = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': predictions})
    output.to_csv(output_path, index=False)
    print(f"Soumission sauvegardée dans {output_path}")

if __name__ == "__main__":
    # Chemins par défaut (à adapter si besoin)
    model_path = "model.joblib"
    X_test_path = "X_test.csv"
    test_csv_path = "titanic/test.csv"
    output_path = "submission.csv"
    predict_and_submit(model_path, X_test_path, test_csv_path, output_path)
