"""Define the player view."""


class PlayerView:
    def display_players(self, players):
        print("\n--- Liste des joueurs ---")

        if not players:
            print("Aucun joueur enregistré.")
            return

        number = 1
        print("Joueur n° | Nom | Prénom | Date Naissance | Classement | CNID")
        for player in players:
            print(f"{number} | ", end="")
            print(player)
            number += 1
