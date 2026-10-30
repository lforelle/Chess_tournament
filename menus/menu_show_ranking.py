def menu_show_ranking(player_controller, ranking_controller, match_view):
    players = player_controller.get_players()

    if not players:
        print("\nAucun joueur n'est enregistré.")
        return

    ranking = ranking_controller.get_ranking(players)
    match_view.display_ranking(ranking)
