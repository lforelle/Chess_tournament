"""Define the Tournament."""


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
