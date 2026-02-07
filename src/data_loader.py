import pandas as pd
import os


def load_titanic_data():
    """Charge les données train et test depuis le dossier data."""
    # On définit le chemin relatif vers le dossier data
    base_path = os.path.join(os.path.dirname(__file__), "..", "data")

    train_path = os.path.join(base_path, "train.csv")
    test_path = os.path.join(base_path, "test.csv")

    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    print("Données chargées avec succès !")
    return train_data, test_data


if __name__ == "__main__":
    train, test = load_titanic_data()
    print(f"Nombre de lignes dans Train : {len(train)}")
