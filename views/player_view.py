"""Define the player view class and functions for displaying player information."""


def get_player_sort_key(player):
    return (
        player.lastname.casefold(),
        player.firstname.casefold(),
    )


def sort_players_by_name(players):
    return sorted(players, key=get_player_sort_key)


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
            f"{'Naissance':<11}| "
            f"{'CNID':<7}| Statut"
        )
        print("-" * 74)

        for number, player in enumerate(sort_players_by_name(players), start=1):
            print(
                f"{number:<3}| "
                f"{player.lastname:<16}| "
                f"{player.firstname:<16}| "
                f"{player.birthdate:<11}| "
                f"{player.cnid:<7}| "
                f"{'Actif' if player.active else 'Inactif'}"
            )

    def display_tournament_players(self, players):
        print("\n--- Joueurs inscrits au tournoi ---")

        if not players:
            print("Aucun joueur inscrit à ce tournoi.")
            return

        for number, player in enumerate(sort_players_by_name(players), start=1):
            print(
                f"{number:>3}. "
                f"{player.lastname} {player.firstname}"
            )
