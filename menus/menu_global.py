"""App global menu."""

from menus.menu_create_tournament import menu_create_tournament
from menus.menu_update_tournament import menu_update_tournament

from menus.menu_create_player import menu_create_player
from menus.menu_update_player import menu_update_player
from menus.menu_remove_player import menu_remove_player

from menus.menu_create_match import menu_create_match
from menus.menu_record_scores import menu_record_scores
from menus.menu_update_scores import menu_update_scores
from menus.menu_show_ranking import menu_show_ranking


def menu_global(
    tournament_controller,
    tournament_view,
    player_controller,
    player_view,
    match_controller,
    match_view,
    round_controller,
    ranking_controller,
):
    while True:
        print("\n######### Tournois d'Echecs #########\n")
        print("   --------- Tournois ----------")
        print("   1. Créer un tournoi")
        print("   2. Modifier un tournoi")
        print("   3. Afficher les infos du tournoi")
        print("\n   --------- Joueurs ----------")
        print("   4. Créer un joueur")
        print("   5. Modifier un joueur")
        print("   6. Supprimer un joueur")
        print("   7. Afficher les joueurs")
        print("\n   --------- Matches ----------")
        print("   8. Générer un tour et ses rencontres")
        print("   9. Saisir les résultats du dernier tour")
        print("   10. Modifier les résultats du dernier tour")
        print("   11. Terminer le dernier tour")
        print("   12. Afficher le classement")
        print("\n   0. Quitter")

        choice = input("\nVotre choix : ").strip()

        if choice == "1":
            menu_create_tournament(tournament_controller, tournament_view)

        elif choice == "2":
            menu_update_tournament(tournament_controller, tournament_view)

        elif choice == "3":
            tournaments = tournament_controller.get_tournaments()
            tournament_view.display_tournaments(tournaments)

        elif choice == "4":
            menu_create_player(player_controller, player_view)

        elif choice == "5":
            menu_update_player(player_controller, player_view)

        elif choice == "6":
            menu_remove_player(player_controller, player_view)

        elif choice == "7":
            players = player_controller.get_players()
            player_view.display_players(players)

        elif choice == "8":
            menu_create_match(player_controller, round_controller)

        elif choice == "9":
            menu_record_scores(match_controller)

        elif choice == "10":
            menu_update_scores(match_controller)

        elif choice == "11":
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

        elif choice == "12":
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
