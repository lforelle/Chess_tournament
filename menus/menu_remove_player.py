"""Remove players from data."""

from views.player_view import sort_players_by_name


def menu_remove_player(player_controller, player_view):
    players = sort_players_by_name(player_controller.get_active_players())
    player_view.display_players(players)

    if not players:
        print("Erreur : aucun joueur actif à désactiver.")
        return

    try:
        player_number = int(
            input("\nQuel est le numéro du joueur à supprimer : ").strip()
        )
    except ValueError:
        print("Erreur : saisissez un numéro de joueur valide.")
        return

    index_to_remove = player_number - 1

    if not 0 <= index_to_remove < len(players):
        print("Erreur : ce numéro de joueur n'existe pas.")
        return

    print("\n--- Ligne à supprimer ---")
    confirmation = input(
        "Etes-vous certain de vouloir désactiver ce joueur (o/n) : "
        ).strip().lower()
    if confirmation != "o":
        print(f"Désactivation du joueur n°{player_number} annulée.")
        return

    player = players[index_to_remove]
    is_deactivated = player_controller.deactivate_player(player.cnid)
    if is_deactivated:
        print(f"\nJoueur n°{player_number} désactivé.\n")
        player_view.display_players(player_controller.get_players())
    else:
        print("\nErreur : la désactivation du joueur a échoué.")
