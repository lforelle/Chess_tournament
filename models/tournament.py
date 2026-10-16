"""Define the tournament
Un fichier json contiendra les tournois, leurs joueurs, leurs tours, leurs matchs et leurs résultats
"""


class Tournament:
    """Represent a tournament, its name, location, start and end dates, description, number of rounds"""

    def __init__(self, name, location, start_date, end_date, description, number_of_rounds):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        # self.current_round_number = current_round_number
        # self.rounds = []
        # self.registered_players = []

    def __str__(self):
        return (
            f"\n--- Tournois {self.name} de {self.location} ---\n"
            f"Date début: {self.start_date}\n"
            f"Date fin : {self.end_date}\n"
            f"Nombre de tours: {self.number_of_rounds}\n"
            f"Description: {self.description}"
        )
