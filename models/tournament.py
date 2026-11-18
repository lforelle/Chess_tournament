"""Define the Tournament."""

from datetime import datetime
from models.round import Round


class Tournament:
    """A Chess tournament must contain informations like name, place or
    number of rounds to roll down in the competition.
    """
    def __init__(
        self,
        name,
        place,
        start_date,
        end_date,
        description,
        number_of_rounds=4,
        current_round=0,
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds = []
        self.players = []

    def __str__(self):
        return (
            f"{self.name:<15} |"
            f"{self.place:<12} |"
            f"{self.start_date.strftime('%d/%m/%Y'):<10} |"
            f"{self.end_date.strftime('%d/%m/%Y'):<10} |"
            f"{self.number_of_rounds:<8} |"
            f"{self.current_round:<11} |"
            f"{self.description:<45}"
        )

    def to_dict(self):
        """Convert the tournament into a dictionary."""

        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": [player.cnid for player in self.players],
            "rounds": [round_instance.to_dict()
                       for round_instance in self.rounds],
        }

    @classmethod
    def from_dict(cls, data, players_by_cnid):
        tournament = cls(
            name=data["name"],
            place=data["place"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(data["end_date"]),
            description=data["description"],
            number_of_rounds=data["number_of_rounds"],
            current_round=data["current_round"],
        )

        tournament.players = [
            players_by_cnid[cnid]
            for cnid in data.get("players", [])
        ]

        tournament.rounds = [
            Round.from_dict(round_data, players_by_cnid)
            for round_data in data.get("rounds", [])
        ]

        return tournament
