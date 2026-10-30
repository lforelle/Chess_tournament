from menus.menu_record_scores import get_last_round


def menu_update_scores(match_controller):
    """Modify the results of the matches in the last round."""

    round_index, round_instance = get_last_round(match_controller)

    if round_instance is None:
        return

    # Affichage des rencontres
    # on affiche le matches du tour en liste avec index pour chaque match
    for match_index, match in enumerate(round_instance.matches, start=1):
        white = match.players[0][0]
        black = match.players[1][0]

        print(f"\nRencontre {match_index}")
        print(f"Blancs : {white.firstname} {white.lastname}")
        print(f"Noirs  : {black.firstname} {black.lastname}")
        print(f"Résultat actuel : {match.result}")

    # Sélection de la rencontre
    while True:
        try:
            choice = int(input(
                f"\nIndex de la rencontre à modifier (1 à {len(round_instance.matches)}) ou 0 pour annuler : "
            ).strip())

            if choice == 0:
                return

            if 1 <= choice <= len(round_instance.matches):
                break

            print("Index invalide !")

        except ValueError:
            print("Valeur non numérique saisie !")

    # Récupération de la rencontre sélectionnée
    match_index = choice - 1

    # Saisie du nouveau résultat
    print("\n1. Victoire des blancs (1-0)")
    print("2. Match nul (1/2-1/2)")
    print("3. Victoire des noirs (0-1)")

    results = {
        "1": "1-0",
        "2": "1/2-1/2",
        "3": "0-1",
    }

    result_choice = input("Nouveau résultat : ").strip()
    result = results.get(result_choice)

    if result is None:
        print("Choix invalide. Résultat non modifié.")
        return

    success = match_controller.record_result(
        round_index,
        match_index,
        result,
    )

    if success:
        print(f"\nNouveau résultat enregistré : {result}")
    else:
        print("Erreur lors de la modification du résultat.")
