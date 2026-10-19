"""Update players data."""

from menu.menu_create_player import (
    ask_name,
    ask_birthdate,
    ask_ranking,
    ask_cnid,
)


def menu_update_player(player_controller, player_view):
    players = player_controller.get_players()
    player_view.display_players(players)

    if not players:
        return

    try:
        player_index_number = int(
            input("\nQuel est le numéro du joueur à modifier : ")
        )
    except ValueError:
        print("Erreur : saisissez un numéro.")
        return

    index = player_index_number - 1

    if not 0 <= index < len(players):
        print("Erreur : ce numéro de joueur n'existe pas.")
        return

    print("\n--- Nouvelles informations ---")
    lastname = ask_name("Nom : ")
    firstname = ask_name("Prénom : ")
    birthdate = ask_birthdate()
    ranking = ask_ranking()
    cnid = ask_cnid()

    is_updated = player_controller.update_player(
        index,
        lastname,
        firstname,
        birthdate,
        ranking,
        cnid,
    )

    if is_updated:
        print("\nJoueur modifié avec succès.")