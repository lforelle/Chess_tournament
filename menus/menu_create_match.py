"""Match creation menu."""


def menu_create_match(player_controller, player_view, round_controller, match_view):
    """Create a round and display the matches."""

    players = player_controller.get_players()

    if len(players) < 2:
        print("\nErreur : il faut au moins deux joueurs pour créer un tour.")
        return

    # Générer automatiquement les rencontres du prochain tour.
    round_instance = round_controller.generate_next_round(players)

    if round_instance is None:
        print(
            "\nImpossible de générer le tour.\n"
            "Vérifiez qu'aucun tour précédent n'est encore en cours\n"
            "et que les rencontres peuvent être créées."
        )
        return

    print(f"\n--- {round_instance.name} généré ---")

    # Afficher le joueur exempt si le nombre de joueurs est impair.
    if round_instance.bye_player is not None:
        player = round_instance.bye_player
        print(
            f"\nJoueur exempt : {player.firstname} {player.lastname}"
        )
        print("Ce joueur reçoit 1 point.")

    # Afficher les rencontres et les couleurs tirées.
    if not round_instance.matches:
        print("\nAucune rencontre n'a été créée.")
        return

    for index, match in enumerate(round_instance.matches, start=1):
        white = match.players[0][0]
        black = match.players[1][0]

        print(f"\nRencontre {index}")
        print(
            f"Blancs : {white.firstname} {white.lastname}"
        )
        print(
            f"Noirs  : {black.firstname} {black.lastname}"
        )
        print("Scores : 0 - 0")
