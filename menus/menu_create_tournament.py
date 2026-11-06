"""Tournament creation menu."""
from datetime import datetime


def menu_create_tournament(tournament_controller, tournament_view):
    """Create a tournament."""

    name = input("Nom du tournoi: ").strip()
    place = input("Lieu d'organisation du tournoi: ").strip()

    # Input the start date of the tournament
    while True:
        try:
            start_date_input = input("Date de debut du tournoi (JJ/MM/AAAA): ").strip()
            start_date = datetime.strptime(start_date_input, "%d/%m/%Y")
            break

        except ValueError:
            print("Erreur : saisissez une date valide au format JJ/MM/AAAA !")

    # Input the end date of the tournament
    while True:
        try:
            end_date_input = input("Date de fin du tournoi (JJ/MM/AAAA): ").strip()
            end_date = datetime.strptime(end_date_input, "%d/%m/%Y")
            if end_date >= start_date:
                break

            else:
                print(f"\nLa date de fin du tournois saisie ({end_date_input}")
                print("doit impérativement être postérieure ou égale à la date")
                print(f"de debut du tournois ({start_date_input}) !\n")

        except ValueError:
            print("Erreur : saisissez une date valide au format JJ/MM/AAAA !")

    # Input the number of rounds needed for the tournament
    while True:
        number_of_rounds_input = input("Nombre de tours (défaut = 4) : ").strip()
        if not number_of_rounds_input:
            number_of_rounds = 4
            break

        try:
            number_of_rounds = int(number_of_rounds_input)
            if number_of_rounds > 0:
                break
            print("Le nombre de tours doit être supérieur à zéro.")

        except ValueError:
            print("Erreur : saisissez un nombre entier !")

    # Optional description
    description = input("Description : ").strip()

    # Tournament object creation
    tournament = tournament_controller.create_tournament(
        name=name,
        place=place,
        start_date=start_date,
        end_date=end_date,
        description=description,
        number_of_rounds=number_of_rounds,
    )

    if tournament is None:
        print("\nErreur : le tournoi n'a pas pu être créé.")
        return

    print(f"\n--- Tournoi {tournament.name} créé ---")

    tournament_view.display_tournaments(tournament_controller.get_tournaments())
