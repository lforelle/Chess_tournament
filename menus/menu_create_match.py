"""Match creation menu."""


def menu_create_match(player_controller, player_view, match_controller, match_view):
    players = player_controller.get_players()
    player_view.display_players(players)

    if len(players) < 2:
        print("\nErreur : il faut au moins deux joueurs pour créer un match.")
        return

    try:
        player1_number = int(input("\nNuméro du premier joueur : "))
        player2_number = int(input("Numéro du second joueur : "))
    except ValueError:
        print("Erreur : saisissez des numéros valides.")
        return

    player1_index = player1_number - 1
    player2_index = player2_number - 1

    if not (
        0 <= player1_index < len(players)
        and 0 <= player2_index < len(players)
    ):
        print("Erreur : un des numéros de joueur n'existe pas.")
        return

    if player1_index == player2_index:
        print("Erreur : un joueur ne peut pas jouer contre lui-même.")
        return

    match = match_controller.create_match(
        players[player1_index],
        players[player2_index],
    )

    print(f"\n--- Match créé ---\n{match}")
    match_view.display_matches(match_controller.get_matches())
