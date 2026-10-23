"""Menu used to create a player objects."""
from datetime import datetime
import re


def ask_name(message):
    while True:
        name = input(message).strip().capitalize()
        if name and name.replace("-", "").replace(" ", "").isalpha():
            return name

        print("Erreur : utilisez uniquement des lettres, des espaces ou des tirets !")


def ask_birthdate():
    while True:
        date_input = input("Date de naissance (JJ/MM/AAAA) : ").strip()

        try:
            birthdate = datetime.strptime(date_input, "%d/%m/%Y")
            return birthdate

        except ValueError:
            print("Erreur : saisissez une date valide au format JJ/MM/AAAA !")


def ask_cnid():
    while True:
        cnid = input("Identifiant national ('AB12345'): ").strip().upper()

        if re.fullmatch(r"[A-Z]{2}[0-9]{5}", cnid):
            return cnid

        print("Erreur : saisissez 2 lettres suivies de 5 chiffres !")


def menu_create_player(player_controller, player_view):    
    lastname = ask_name("Nom : ")
    firstname = ask_name("Prénom : ")
    birthdate = ask_birthdate()
    cnid = ask_cnid()

    player = player_controller.create_player(
        lastname,
        firstname,
        birthdate,
        cnid,
    )

    print(f"\n--- Joueur créé ---\n{player}\n")
    player_view.display_players(player_controller.get_players())
