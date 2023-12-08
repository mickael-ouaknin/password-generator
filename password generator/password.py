import re
import hashlib

def is_password_secure(password):
    """Vérifie si un mot de passe respecte les critères de sécurité."""
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

def get_secure_password():
    """Demande à l'utilisateur de choisir un mot de passe sécurisé."""
    while True:
        password = input("Veuillez entrer un mot de passe sécurisé: ")
        if is_password_secure(password):
            return password
        else:
            print("Le mot de passe que vous avez entré ne respecte pas les critères de sécurité, choisissez en un avec les critères suivants : @,!,0-9,Aa")

def hash_password(password):
    """Crypte un mot de passe en utilisant l'algorithme de hachage SHA-256."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Exécution du programme
print("Bienvenue! Veuillez choisir un mot de passe sécurisé.")
password = get_secure_password()
print("Le mot de passe que vous avez choisi est: ", hash_password(password))