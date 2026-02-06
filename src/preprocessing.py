import pandas as pd

def preprocess_data(df):
    """Nettoie et prépare les données du Titanic."""
    
    # 1. Sélection des colonnes utiles (on enlève le nom, le ticket, etc.)
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    
    # 2. Transformation du texte en chiffres (One-Hot Encoding)
    # Convertit 'Sex' en colonnes numériques (0 ou 1)
    X = pd.get_dummies(df[features])
    
    # 3. On récupère la cible (Survived) si elle existe dans le DataFrame
    y = df["Survived"] if "Survived" in df.columns else None
    
    return X, y

if __name__ == "__main__":
    # Petit test rapide
    from data_loader import load_titanic_data
    train, _ = load_titanic_data()
    X, y = preprocess_data(train)
    print("Colonnes après préparation :", X.columns.tolist())
    print("Aperçu des données :\n", X.head())