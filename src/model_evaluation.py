from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    """
    Évalue les performances du modèle (Précision et Rapport détaillé). [cite: 52]
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    
    print(f"--- Évaluation du Modèle ---")
    print(f"Précision : {accuracy:.2%}")
    print("Rapport détaillé :\n", report)
    
    return accuracy