"""Define the tournament view class and related functions for displaying tournament information."""


def get_tournament_sort_key(tournament):
    return (
        tournament.start_date is None,
        tournament.start_date,
    )


def sort_tournaments_by_date(tournaments):
    return sorted(tournaments, key=get_tournament_sort_key)


class TournamentView:
    def display_tournaments(self, tournaments):
        print("\n--- Liste des tournois ---")

        if not tournaments:
            print("Aucun tournoi enregistré.")
            return

        print(
            f"{'N°':<4}| "
            f"{'Nom':<20}| "
            f"{'Lieu':<15}| "
            f"{'Date début':<11}| "
            f"{'Date fin':<11}| "
            f"{'Nb tours':<9}| "
            f"{'Tour EC':<8}| "
            "Description"
        )
        print("-" * 130)

        for number, tournament in enumerate(sort_tournaments_by_date(tournaments), start=1):
            start_date = (
                tournament.start_date.strftime("%d/%m/%Y")
                if tournament.start_date else ""
            )

            end_date = (
                tournament.end_date.strftime("%d/%m/%Y")
                if tournament.end_date else ""
            )

            print(
                f"{number:<4}| "
                f"{tournament.name:<20}| "
                f"{tournament.place:<15}| "
                f"{start_date:<11}| "
                f"{end_date:<11}| "
                f"{tournament.number_of_rounds:^9}| "
                f"{tournament.current_round:^8}| "
                f"{tournament.description}"
            )
