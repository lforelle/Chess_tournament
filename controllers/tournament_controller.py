"""Define the tournament controller."""
from models.tournament import Tournament


class TournamentController:
    """Manage the creation and the closure of tournaments."""

    def __init__(self, repository, player_controller):
        self.repository = repository
        self.player_controller = player_controller
        self.tournaments = self.repository.load_all(
            player_controller.get_players()
        )

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
        self.save_all()

        return tournament

    def get_tournaments(self):
        return tuple(self.tournaments)

    def register_player(self, tournament, player):
        """Register a player in the tournament."""

        if not player.active or not any(
            registered_player is player
            for registered_player in self.player_controller.get_players()
        ):
            return False

        # check if the player is already registered
        for registered_player in tournament.players:
            if registered_player.cnid == player.cnid:
                return False

        # Add the player in the tournament
        tournament.players.append(player)

        # Save the modifications
        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

        self.save_all()

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
        self.save_all()

        return tournament

    def validate_player_references(self):
        players = self.player_controller.get_players()
        players_by_cnid = {player.cnid: player for player in players}

        if len(players_by_cnid) != len(players):
            raise ValueError("Des CNID sont attribués à plusieurs joueurs.")

        for tournament in self.tournaments:
            references = list(tournament.players)

            for round_instance in tournament.rounds:
                if round_instance.bye_player is not None:
                    references.append(round_instance.bye_player)

                for match in round_instance.matches:
                    references.extend(
                        player_score[0] for player_score in match.players
                    )

            for player in references:
                if players_by_cnid.get(player.cnid) is not player:
                    raise ValueError(
                        f"Référence joueur invalide dans {tournament.name} : "
                        f"{player.cnid}"
                    )

    def save_all(self):
        self.validate_player_references()
        self.repository.save_all(self.tournaments)
