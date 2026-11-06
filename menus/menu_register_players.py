

def menu_register_players(tournament, player_controller, tournament_controller):
    """Permet d'inscrire des joueurs à un tournoi."""

    players = player_controller.get_players()

    if not players:
        print("\nAucun joueur n'est enregistré dans l'application.")
        return

    while True:
        # Récupérer les joueurs non inscrits
        available_players = [
            player for player in players
            if all(
                registered_player.cnid != player.cnid
                for registered_player in tournament.players
            )
        ]

        if not available_players:
            print("\nTous les joueurs sont déjà inscrits à ce tournoi.")
            return

        print(f"\n--- Inscription des joueurs : {tournament.name} ---")

        for index, player in enumerate(available_players, start=1):
            print(
                f"{index}. {player.firstname} {player.lastname} "
                f"({player.cnid})"
            )

        print("0. Retour")

        try:
            selection = int(input("\nNuméro du joueur à inscrire : "))
        except ValueError:
            print("\nVeuillez saisir un numéro valide.")
            continue

        if selection == 0:
            return

        if not 1 <= selection <= len(available_players):
            print("\nNuméro de joueur invalide.")
            continue

        selected_player = available_players[selection - 1]

        success = tournament_controller.register_player(
            tournament,
            selected_player,
        )

        if success:
            print(
                f"\n{selected_player.firstname} "
                f"{selected_player.lastname} "
                "a été inscrit au tournoi."
            )
