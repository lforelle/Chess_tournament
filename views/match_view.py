"""Display the matches."""


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
