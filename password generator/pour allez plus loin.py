import hashlib
import json
import os

PASSWORDS_FILE = "passwords.json"

def get_password():
    """Demande à l'utilisateur de saisir un mot de passe."""
    return input("Veuillez entrer un mot de passe: ")

def get_username():
    """Demande à l'utilisateur de saisir un nom d'utilisateur."""
    return input("Veuillez entrer un nom d'utilisateur: ")

def hash_password(password):
    """Crypte un mot de passe en utilisant l'algorithme de hachage SHA-256."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def add_password():
    """Ajoute un nouveau mot de passe haché à la liste des mots de passe."""
    username = get_username()
    password = get_password()
    hashed_password = hash_password(password)

    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    passwords[username] = hashed_password

    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords, file)

    print("Le mot de passe a été ajouté avec succès.")

def display_passwords():
    """Affiche la liste des mots de passe."""
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r") as file:
            passwords = json.load(file)
        for username, hashed_password in passwords.items():
            print(f"Nom d'utilisateur: {username}, Mot de passe: {hashed_password}")
    else:
        print("Aucun mot de passe enregistré.")

def menu():
    """Affiche le menu de l'application."""
    print("Bienvenue! Veuillez choisir une option:")
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Quitter")

    while True:
        try:
            choice = int(input("Veuillez entrer le numéro de l'option: "))
            if choice == 1:
                add_password()
            elif choice == 2:
                display_passwords()
            elif choice == 3:
                break
            else:
                print("Option invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

menu()