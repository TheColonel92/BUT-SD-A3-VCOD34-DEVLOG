"""
data_preprocessing.py
Prépare les données Titanic pour l'entraînement du modèle.
"""
import pandas as pd

def load_and_show(train_path, test_path):
    """Charge les CSV et affiche les 5 premières lignes de train et test."""
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    print("Aperçu train.csv :")
    print(train_data.head())
    print("\nAperçu test.csv :")
    print(test_data.head())
    return train_data, test_data

def prepare_features(train_data, test_data):
    """Prépare les features pour l'entraînement du modèle."""
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X_train = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])
    y_train = train_data["Survived"]
    return X_train, X_test, y_train

if __name__ == "__main__":
    # Chemins par défaut (à adapter si besoin)
    train_path = "titanic/train.csv"
    test_path = "titanic/test.csv"
    
    train_data, test_data = load_and_show(train_path, test_path)
    X_train, X_test, y_train = prepare_features(train_data, test_data)
    # Sauvegarde les fichiers pour l'étape suivante
    X_train.to_csv("X_train.csv", index=False)
    X_test.to_csv("X_test.csv", index=False)
    y_train.to_csv("y_train.csv", index=False)
    print("\nFichiers X_train.csv, X_test.csv et y_train.csv sauvegardés.")
