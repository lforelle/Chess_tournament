"""Display the matches and tournament ranking."""


class MatchView:
    def display_matches(self, matches):
        print("\n--- Liste des matchs ---")

        if not matches:
            print("Aucun match créé.")
            return

        number = 1
        for match in matches:
            print(f"{number} | ", end="")
            print(match)
            number += 1

    def display_ranking(self, ranking):
        """Display the tournament ranking."""

        print("\n=============== CLASSEMENT DU TOURNOI ================\n")

        if not ranking:
            print("Aucun joueur à afficher.")
            return

        print(f"{'Rang':<6}{'Nom':<20}{'Prénom':<20}{'Points':>8}")
        print("-" * 54)

        for rank, (player, points) in enumerate(ranking, start=1):
            print(
                f"{rank:<6}"
                f"{player.lastname:<20}"
                f"{player.firstname:<20}"
                f"{points:>8.1f}"
            )

        print("======================================================\n")

    def display_tournament_rounds(self, rounds):
        """Display all the rounds and their matches."""

        print("\n========== HISTORIQUE DU TOURNOI ==========")

        if not rounds:
            print("Aucun tour n'a encore été créé.")
            return

        for round_instance in rounds:
            print(f"\n--- {round_instance.name} ---")

            if round_instance.start_datetime is not None:
                print(
                    "Début : "
                    f"{round_instance.start_datetime.strftime('%d/%m/%Y %H:%M')}"
                )

            if round_instance.end_datetime is not None:
                print(
                    "Fin : "
                    f"{round_instance.end_datetime.strftime('%d/%m/%Y %H:%M')}"
                )
                print("Statut : Terminé")
            else:
                print("Statut : En cours")

            if round_instance.bye_player is not None:
                player = round_instance.bye_player
                print(
                    f"Joueur exempté : "
                    f"{player.firstname} {player.lastname}"
                )

            if not round_instance.matches:
                print("Aucune rencontre dans ce tour.")
                continue

            print("\nRencontres :")

            for number, match in enumerate(round_instance.matches, start=1):
                player1 = match.players[0][0]
                player2 = match.players[1][0]

                if match.result is None:
                    result = "Non joué"
                else:
                    result = match.result

                print(
                    f"  Match {number} : "
                    f"{player1.firstname} {player1.lastname} "
                    f"vs "
                    f"{player2.firstname} {player2.lastname} "
                    f"| Résultat : {result}"
                )
