"""Update players data."""

from menus.menu_create_player import (
    ask_name,
    ask_birthdate,
    ask_cnid,
)


def menu_update_player(player_controller, tournament_controller, player_view):
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

    if player_controller.cnid_is_used(cnid, exclude_index=index):
        print("Erreur : ce CNID est déjà attribué à un autre joueur.")
        return

    is_updated = player_controller.update_player(
        index,
        lastname,
        firstname,
        birthdate,
        cnid,
        persist=False,
    )

    if is_updated:
        print("\nJoueur modifié avec succès.")
        tournament_controller.validate_player_references()
        player_controller.save_all()
        tournament_controller.save_all()
        player_view.display_players(player_controller.get_players())
    else:
        print("\nErreur : la modification du joueur a échoué.")
