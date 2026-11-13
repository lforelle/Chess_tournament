"""Menu used to create a player objects."""
from datetime import datetime
import re


def ask_name(message, default=None):
    while True:
        name = input(message).strip()
        if not name and default is not None:
            return default

        name = name.capitalize()
        if name and name.replace("-", "").replace(" ", "").isalpha():
            return name

        print("Erreur : utilisez uniquement des lettres, des espaces ou des tirets !")


def ask_birthdate(default=None):
    while True:
        prompt = "Date de naissance"
        if default is not None:
            prompt += f" [{default}]"
        date_input = input(f"{prompt} (JJ/MM/AAAA) : ").strip()

        if not date_input and default is not None:
            return default

        try:
            birthdate = datetime.strptime(date_input, "%d/%m/%Y")
            return birthdate

        except ValueError:
            print("Erreur : saisissez une date valide au format JJ/MM/AAAA !")


def ask_cnid(default=None):
    while True:
        if default is None:
            prompt = "Identifiant national ('AB12345'): "
        else:
            prompt = (
                f"Identifiant national [{default}] ('AB12345') : "
            )
        cnid = input(prompt).strip().upper()

        if not cnid and default is not None:
            return default

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

    if player is None:
        print("Erreur : ce CNID est déjà attribué à un autre joueur.")
        return

    print(f"\n--- Joueur créé ---\n{player}\n")
    player_view.display_players(player_controller.get_players())
