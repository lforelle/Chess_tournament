"""App global menu."""

from menus.menu_create_tournament import menu_create_tournament
from menus.menu_update_tournament import menu_update_tournament
from menus.menu_tournament import menu_tournament

from menus.menu_create_player import menu_create_player
from menus.menu_update_player import menu_update_player
from menus.menu_remove_player import menu_remove_player
from views.tournament_view import sort_tournaments_by_date


def menu_global(
    tournament_controller,
    tournament_view,
    player_controller,
    player_view,
):
    while True:
        print("\n######### Tournois d'Echecs #########\n")
        print("   --------- Tournois ----------")
        print("   1. Créer un tournoi")
        print("   2. Modifier un tournoi")
        print("   3. Afficher les tournois")
        print("   4. Sélectionner un tournoi")

        print("\n   --------- Joueurs ----------")
        print("   5. Créer un joueur")
        print("   6. Modifier un joueur")
        print("   7. Désactiver un joueur")
        print("   8. Afficher les joueurs")

        print("\n   0. Quitter")

        choice = input("\nVotre choix : ").strip()

        if choice == "1":
            menu_create_tournament(tournament_controller, tournament_view)

        elif choice == "2":
            menu_update_tournament(tournament_controller, tournament_view)

        elif choice == "3":
            tournaments = tournament_controller.get_tournaments()
            if not tournaments:
                print("\nAucun tournoi n'est enregistré.")

            else:
                tournament_view.display_tournaments(tournaments)

        elif choice == "4":
            tournaments = sort_tournaments_by_date(
                tournament_controller.get_tournaments()
            )

            if not tournaments:
                print("\nAucun tournoi n'est enregistré.")
                continue

            tournament_view.display_tournaments(tournaments)

            try:
                selection = int(
                    input("\nNuméro du tournoi à sélectionner : ")
                )
            except ValueError:
                print("\nVeuillez saisir un numéro valide.")
                continue

            if not 1 <= selection <= len(tournaments):
                print("\nNuméro de tournoi invalide.")
                continue

            selected_tournament = tournaments[selection - 1]

            menu_tournament(
                selected_tournament,
                tournament_repository=tournament_controller.repository,
                player_controller=player_controller,
                tournament_controller=tournament_controller,
                player_view=player_view,
                match_view=None,
            )

        elif choice == "5":
            menu_create_player(player_controller, player_view)

        elif choice == "6":
            menu_update_player(player_controller, tournament_controller, player_view)

        elif choice == "7":
            menu_remove_player(player_controller, player_view)

        elif choice == "8":
            players = player_controller.get_players()
            player_view.display_players(players)

        elif choice == "0":
            print("\n========== Au revoir ! ===========\n")
            break

        else:
            print("Choix invalide.")
