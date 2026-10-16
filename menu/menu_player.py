"""Menu used to act on player objects"""
from controllers.player_controller import PlayerController


def menu_player():
    lastname = input("Nom : ")
    firstname = input("Prénom : ")
    birthday = input("Date de naissance (JJ/MM/AAAA) : ")
    ranking = int(input("Classement : "))
    cnid = input("Identifiant national ('AB12345'): ")

    player_controller = PlayerController()
    player = player_controller.create_player(
        lastname,
        firstname,
        birthday,
        ranking,
        cnid,
    )

    print(f"\n--- Joueur créé ---\n{player}")
