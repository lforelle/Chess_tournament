def menu_show_ranking(tournament, ranking_controller, match_view):
    players = tournament.players

    if not players:
        print("\nAucun joueur n'est enregistré.")
        return

    ranking = ranking_controller.get_ranking(players)
    match_view.display_ranking(ranking)
