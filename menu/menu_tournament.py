"""Menu used to act on tournament objects"""
from controllers.tournament_controller import TournamentController


def menu_tournament():
    name = input("Nom du tournois : ")
    location = input("Lieu d'organisation : ")
    start_date = input("Date de début : ")
    end_date = input("Date de fin : ")
    number_of_rounds = input("Nombre de tours (4 par defaut): ")
    description = input("Description : ")

    tournament_controller = TournamentController()
    tournament = tournament_controller.create_tournament(
        name,
        location,
        start_date,
        end_date,
        description,
        number_of_rounds,
    )

    print(f"\n{tournament}")
