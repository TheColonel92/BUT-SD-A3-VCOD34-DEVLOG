import pytest
import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data_columns():
    """Vérifie que le prétraitement génère les bonnes colonnes numériques."""
    # On simule un petit tableau de données Titanic
    df_test = pd.DataFrame({
        'Pclass': [3, 1],
        'Sex': ['male', 'female'],
        'SibSp': [1, 0],
        'Parch': [0, 0],
        'Survived': [0, 1]
    })
    
    X, y = preprocess_data(df_test)
    
    # Test 1 : Vérifier que Sex a été transformé en colonnes dummies
    assert 'Sex_female' in X.columns
    assert 'Sex_male' in X.columns
    
    # Test 2 : Vérifier qu'on a bien récupéré la cible 'y'
    assert y is not None
    assert len(y) == 2