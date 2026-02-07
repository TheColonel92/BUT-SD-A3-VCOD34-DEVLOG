from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from src.data_loader import load_titanic_data
from src.data_preprocessing import preprocess_data


def train_and_evaluate():
    """
    Entraîne le modèle Random Forest sur les données fournies. [cite: 37]

    Args:
        X_train: Features d'entraînement.
        y_train: Cible d'entraînement.

    Returns:
        model: Le modèle entraîné.
    """
    # 1. Chargement des données
    train_df, _ = load_titanic_data()

    # 2. Nettoyage
    X, y = preprocess_data(train_df)

    # 3. Séparation pour test interne (80% entraînement, 20% validation)
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    # 4. Création et entraînement du modèle (Random Forest)
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)

    # 5. Calcul du score
    score = model.score(X_val, y_val)
    print(f"--- Modèle entraîné ---")
    print(f"Précision du modèle sur les données de validation : {score:.2%}")

    return model


if __name__ == "__main__":
    train_and_evaluate()
