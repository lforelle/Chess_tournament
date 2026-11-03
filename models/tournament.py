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
        number_of_rounds=4
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds

        self.current_round = 0
        self.rounds = []
        self.players = []

    def __str__(self):
        return (
            f"{self.name:<15} |"
            f"{self.place:<12} |"
            f"{self.start_date:<10} |"
            f"{self.end_date:<10} |"
            f" {self.number_of_rounds:<8} |"
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
        }
