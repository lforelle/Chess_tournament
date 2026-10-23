"""Remove players from data."""


def menu_remove_player(player_controller, player_view):
    players = player_controller.get_players()
    player_view.display_players(players)

    if not players:
        print("Erreur: Aucun joueur à supprimer.")
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
        "Etes-vous certain de vouloir supprimer ce joueur (o/n) : "
        ).strip().lower()
    if confirmation != "o":
        print(f"Suppression du joueur n°{index_to_remove} annulée.")
        return

    is_removed = player_controller.remove_player(index_to_remove)
    if is_removed:
        print(f"\nJoueur n°{index_to_remove} supprimé.\n")
        player_view.display_players(player_controller.get_players())
    else:
        print("\nErreur : la suppression du joueur a échoué.")

