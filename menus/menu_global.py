"""Menu global de l'application."""

from menus.menu_create_player import menu_create_player
from menus.menu_update_player import menu_update_player
from menus.menu_remove_player import menu_remove_player

from menus.menu_create_match import menu_create_match
from menus.menu_record_scores import menu_record_scores
from menus.menu_show_ranking import menu_show_ranking


def menu_global(
    player_controller,
    player_view,
    match_controller,
    match_view,
    round_controller,
    ranking_controller,
):
    while True:
        print("\n######### Tournois d'Echecs #########\n")
        print("   --------- Joueurs ----------")
        print("   1. Créer un joueur")
        print("   2. Modifier un joueur")
        print("   3. Supprimer un joueur")
        print("   4. Afficher les joueurs")
        print("\n   --------- Matches ----------")
        print("   5. Générer un tour et ses rencontres")
        print("   6. Saisir les résultats du dernier tour")
        print("   7. Terminer le dernier tour")
        print("   8. Afficher le classement")
        print("\n   0. Quitter")

        choice = input("\nVotre choix : ").strip()

        if choice == "1":
            menu_create_player(player_controller, player_view)

        elif choice == "2":
            menu_update_player(player_controller, player_view)

        elif choice == "3":
            menu_remove_player(player_controller, player_view)

        elif choice == "4":
            players = player_controller.get_players()
            player_view.display_players(players)

        elif choice == "5":
            menu_create_match(
                player_controller,
                player_view,
                round_controller,
                match_view,
            )

        elif choice == "6":
            menu_record_scores(match_controller)

        elif choice == "7":
            rounds = round_controller.get_rounds()

            if not rounds:
                print("\nAucun tour n'a été créé.")
            else:
                last_round_index = len(rounds) - 1

                if round_controller.finish_round(last_round_index):
                    print(f"\nLe {rounds[-1].name} est terminé.")
                else:
                    print(
                        "\nImpossible de terminer ce tour. "
                        "Vérifiez que toutes les rencontres ont un résultat."
                    )

        elif choice == "8":
            menu_show_ranking(
                player_controller,
                ranking_controller,
                match_view,
            )

        elif choice == "0":
            print("\n========== Au revoir ! ===========\n")
            break

        else:
            print("Choix invalide.")
