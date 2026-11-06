"""Match creation menu."""


def menu_create_match(tournament, round_controller):
    """Create a round and display its matches."""

    # Only fetch the players registered in the tournament.
    players = tournament.players

    if len(players) < 2:
        print("\nErreur : il faut au moins deux joueurs inscrits "
              "à ce tournois.")
        return

    # Automatically generate the matches of the next round.
    round_instance = round_controller.generate_next_round(players)

    if round_instance is None:
        print(
            "\nImpossible de générer le tour.\n"
            "Vérifiez qu'aucun tour précédent n'est encore en cours,\n"
            "que le nombre maximal de tours n'est pas atteint\n"
            "et que les appairages sont possibles."
        )
        return

    print(f"\n--- {round_instance.name} généré ---")

    # Display the bye player if the number of players is odd.
    if round_instance.bye_player is not None:
        player = round_instance.bye_player
        print(
            f"\nJoueur exempté : {player.firstname} {player.lastname}"
        )
        print("Ce joueur reçoit 1 point.")

    # Display the matches and the white/black colors sorted.
    if not round_instance.matches:
        print("\nAucune rencontre n'a été créée.")
        return

    for index, match in enumerate(round_instance.matches, start=1):
        white = match.players[0][0]
        black = match.players[1][0]

        print(f"\nRencontre {index}")
        print(f"Blancs : {white.firstname} {white.lastname}")
        print(f"Noirs  : {black.firstname} {black.lastname}")
        print("Scores : 0 - 0")
