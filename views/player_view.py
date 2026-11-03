"""Define the player view."""


class PlayerView:
    def display_players(self, players):
        print("\n--- Liste des joueurs ---")

        if not players:
            print("Aucun joueur enregistré.")
            return

        print(
            f"{'N°':<3}| "
            f"{'Nom':<16}| "
            f"{'Prénom':<16}| "
            f"{'Naissance':<11}| CNID"
        )
        print("-" * 61)

        for number, player in enumerate(players, start=1):
            print(
                f"{number:<3}| "
                f"{player.lastname:<16}| "
                f"{player.firstname:<16}| "
                f"{player.birthdate:<11}| "
                f"{player.cnid:<7}"
            )
