"""Define the tournament controller."""
from models.tournament import Tournament


class TournamentController:
    """Manage the creation and the closure of tournaments."""

    def __init__(self, repository, players):
        self.repository = repository
        self.players = players
        self.tournaments = self.repository.load_all(players)

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

    def register_player(self, tournament, player):
        """Register a player in the tournament."""

        # check if the player is already registered
        for registered_player in tournament.players:
            if registered_player.cnid == player.cnid:
                return False

        # Add the player in the tournament
        tournament.players.append(player)

        # Save the modifications
        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

        self.repository.save_all(self.tournaments)

        return True

    def update_tournament(self, tournament, updates):
        """Update the informations of a tournament."""

        new_start_date = updates.get("start_date", tournament.start_date)
        new_end_date = updates.get("end_date", tournament.end_date)
        new_number_of_rounds = updates.get(
            "number_of_rounds",
            tournament.number_of_rounds,
        )

        # Check the consistency in dates
        if new_start_date > new_end_date:
            raise ValueError(
                "La date de début doit être antérieure à la date de fin."
            )

        # Do not bring down the number of rounds below the one previously created
        if new_number_of_rounds < len(tournament.rounds):
            raise ValueError(
                "Le nombre de tours ne peut pas être inférieur "
                "au nombre de tours déjà créés."
            )

        # Apply modifications
        for field, value in updates.items():
            setattr(tournament, field, value)

        # Save all the tournaments
        self.repository.save_all(self.tournaments)

        return tournament
