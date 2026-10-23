"""Update players data."""

from menus.menu_create_player import (
    ask_name,
    ask_birthdate,
    ask_cnid,
)


def menu_update_player(player_controller, player_view):
    players_to_update = player_controller.get_players()
    player_view.display_players(players_to_update)

    if not players_to_update:
        print("Aucun joueur à modifier.")
        return

    try:
        player_index_number = int(
            input("\nQuel est le numéro du joueur à modifier : ").strip()
        )
    except ValueError:
        print("Erreur : saisissez un numéro valide.")
        return

    index = player_index_number - 1

    if not 0 <= index < len(players_to_update):
        print("Erreur : ce numéro de joueur n'existe pas.")
        return

    print("\n--- Nouvelles informations ---")
    lastname = ask_name("Nom : ")
    firstname = ask_name("Prénom : ")
    birthdate = ask_birthdate()
    cnid = ask_cnid()

    is_updated = player_controller.update_player(
        index,
        lastname,
        firstname,
        birthdate,
        cnid,
    )

    if is_updated:
        print("\nJoueur modifié avec succès.")
        player_view.display_players(player_controller.get_players())
    else:
        print("\nErreur : la modification du joueur a échoué.")