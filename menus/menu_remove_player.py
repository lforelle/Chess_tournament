"""Remove players from data."""


def menu_remove_player(player_controller, player_view):
    players = player_controller.get_players()
    player_view.display_players(players)

    if not players:
        return

    try:
        player_index_number = int(
            input("\nQuel est le numéro du joueur à supprimer : ")
        )
    except ValueError:
        print("Erreur : saisissez un numéro.")
        return

    index = player_index_number - 1

    if not 0 <= index < len(players):
        print("Erreur : ce numéro de joueur n'existe pas.")
        return

    print("\n--- Ligne à supprimer ---")
    player_removing_ok = input("Etes-vous certain de vouloir supprimer ce joueur (o/n) : ")
    if player_removing_ok.lower() != "o":
        return

    is_removed = player_controller.remove_player(index)
    if is_removed:
        print("\nJoueur supprimé.")
        player_view.display_players(player_controller.get_players())
