"""Tournament updating menu."""

from datetime import datetime


def menu_update_tournament(tournament_controller, tournament_view):
    """To modify the information of a tournament."""

    tournaments = tournament_controller.get_tournaments()

    if not tournaments:
        print("\nAucun tournoi n'est enregistré.")
        return

    tournament_view.display_tournaments(tournaments)

    try:
        selection = int(
            input("\nNuméro du tournoi à modifier (0 pour revenir) : ")
        )
    except ValueError:
        print("\nVeuillez saisir un numéro valide.")
        return

    if selection == 0:
        return

    if not 1 <= selection <= len(tournaments):
        print("\nNuméro de tournoi invalide.")
        return

    tournament = tournaments[selection - 1]

    print(f"\n--- Modification du tournoi : {tournament.name} ---")
    print("Appuyez sur Entrée pour conserver la valeur actuelle.\n")

    updates = {}

    name = input(f"Nom [{tournament.name}] : ").strip()
    if name:
        updates["name"] = name

    place = input(f"Lieu [{tournament.place}] : ").strip()
    if place:
        updates["place"] = place

    start_date = input(
        f"Date de début [{tournament.start_date.date()}] (JJ/MM/AAAA) : "
    ).strip()

    if start_date:
        try:
            updates["start_date"] = datetime.strptime(start_date, "%d/%m/%Y")
        except ValueError:
            print("\nFormat de date invalide.")
            return

    end_date = input(
        f"Date de fin [{tournament.end_date.date()}] (JJ/MM/AAAA) : "
    ).strip()

    if end_date:
        try:
            updates["end_date"] = datetime.strptime(end_date, "%d/%m/%Y")
        except ValueError:
            print("\nFormat de date invalide.")
            return

    description = input(
        f"Description [{tournament.description}] : "
    ).strip()

    if description:
        updates["description"] = description

    number_of_rounds = input(
        f"Nombre de tours [{tournament.number_of_rounds}] : "
    ).strip()

    if number_of_rounds:
        try:
            number_of_rounds = int(number_of_rounds)

            if number_of_rounds < 1:
                print("\nLe nombre de tours doit être supérieur à zéro.")
                return

            updates["number_of_rounds"] = number_of_rounds

        except ValueError:
            print("\nVeuillez saisir un nombre entier valide.")
            return

    if not updates:
        print("\nAucune modification demandée.")
        return

    try:
        tournament_controller.update_tournament(tournament, updates)
        print("\nLe tournoi a été modifié avec succès.")

    except ValueError as error:
        print(f"\nModification impossible : {error}")
