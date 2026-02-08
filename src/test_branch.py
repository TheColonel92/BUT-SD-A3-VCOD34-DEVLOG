# Script de test pour la branche test-branch
# Simple test pour vérifier que tout fonctionne correctement

def greet(name):
    """Fonction simple de salutation"""
    return f"Bonjour {name}, ceci est un test de branche!"

def add(a, b):
    """Fonction pour additionner deux nombres"""
    return a + b

def multiply(a, b):
    """Fonction pour multiplier deux nombres"""
    return a * b

if __name__ == "__main__":
    # Tests simples
    print(greet("Développeur"))
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Multiplication: 4 * 7 = {multiply(4, 7)}")
    print("\n Tests de branche réussis!")
