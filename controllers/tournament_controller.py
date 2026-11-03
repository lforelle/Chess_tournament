"""Define the tournament controller."""
from models.tournament import Tournament


class TournamentController:
    """Manage the creation and the closure of tournaments."""

    def __init__(self, repository):
        self.repository = repository
        self.tournaments = self.repository.load_all()

    def create_tournament(self, name, place, start_date, end_date, description, number_of_rounds=4):
        tournament = Tournament(
            name=name,
            place=place,
            start_date=start_date,
            end_date=end_date,
            description=description,
            number_of_rounds=number_of_rounds
        )
        self.tournaments.append(tournament)
        self.repository.save_all(self.tournaments)

        return tournament

    def get_tournaments(self):
        return self.tournaments
