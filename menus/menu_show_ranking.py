
def menu_show_ranking(player_controller, match_controller, match_view):
    """Fetch and display the tournament rankings."""

    players = player_controller.get_players()

    if not players:
        print("\nAucun joueur n'est enregistré.")
        return

    ranking = match_controller.get_ranking(players)
    match_view.display_ranking(ranking)
