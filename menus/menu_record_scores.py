
def get_last_round(match_controller):
    """Retrieve and check the last round."""

    rounds = match_controller.get_rounds()

    if not rounds:
        print("\nAucun tour n'a été créé.")
        return None, None

    round_index = len(rounds) - 1
    round_instance = rounds[round_index]

    print(f"\n----- {round_instance.name} -----")

    if round_instance.end_datetime is not None:
        print("\nCe tour est déjà terminé.")
        return None, None

    if not round_instance.matches:
        print("\nCe tour ne contient aucune rencontre.")
        return None, None

    return round_index, round_instance


def menu_record_scores(match_controller):
    """Enter the results of the matches in the last round."""

    round_index, round_instance = get_last_round(match_controller)

    if round_instance is None:
        return

    for match_index, match in enumerate(round_instance.matches):
        white = match.players[0][0]
        black = match.players[1][0]

        print(f"\nRencontre {match_index + 1}")
        print(f"Blancs : {white.firstname} {white.lastname}")
        print(f"Noirs  : {black.firstname} {black.lastname}")

        if match.result is not None:
            print(f"Résultat enregistré : {match.result}")
            continue

        print("1. Victoire des blancs (1-0)")
        print("2. Match nul (1/2-1/2)")
        print("3. Victoire des noirs (0-1)")

        choice = input("Résultat : ").strip()

        results = {
            "1": "1-0",
            "2": "1/2-1/2",
            "3": "0-1",
        }

        result = results.get(choice)

        if result is None:
            print("Choix invalide. Résultat non enregistré.")
            continue

        success = match_controller.record_result(
            round_index,
            match_index,
            result,
        )

        if success:
            print(f"Résultat enregistré : {result}")
        else:
            print("Erreur lors de l'enregistrement du résultat.")
