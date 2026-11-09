"""Management of the selected tournament."""

from controllers.match_controller import MatchController
from controllers.round_controller import RoundController
from controllers.ranking_controller import RankingController

from services.pairing_service import PairingService

from views.match_view import MatchView

from menus.menu_register_players import menu_register_players
from menus.menu_create_match import menu_create_match
from menus.menu_record_scores import menu_record_scores
from menus.menu_update_scores import menu_update_scores
from menus.menu_show_ranking import menu_show_ranking


def menu_tournament(
    tournament,
    tournament_repository,
    player_controller,
    tournament_controller,
    player_view,
    match_view=None,
):
    # The rounds specific to this tournament.
    rounds = tournament.rounds

    # Creation of the components specific to the tournament.
    match_controller = MatchController(
        tournament=tournament,
        repository=tournament_repository,
    )

    ranking_controller = RankingController(rounds)

    pairing_service = PairingService(rounds)

    round_controller = RoundController(
        tournament=tournament,
        ranking_controller=ranking_controller,
        pairing_service=pairing_service,
        match_controller=match_controller,
        repository=tournament_repository,
    )

    if match_view is None:
        match_view = MatchView()

    while True:
        print(f"\n######### {tournament.name} #########")
        print("\n   --------- Gestion du tournoi ----------")
        print("   1. Inscrire des joueurs au tournoi")
        print("   2. Générer un tour et ses rencontres")
        print("   3. Saisir les résultats")
        print("   4. Modifier les résultats")
        print("   5. Terminer le dernier tour")
        print("   6. Afficher les joueurs inscrits au tournoi")
        print("   7. Afficher le classement")
        print("   8. Afficher tous les tours et leurs rencontres")
        print("\n   0. Retour au menu principal")

        choice = input("\nVotre choix : ").strip()

        if choice == "1":
            menu_register_players(
                tournament,
                player_controller,
                tournament_controller,
            )

        elif choice == "2":
            menu_create_match(tournament, round_controller)

        elif choice == "3":
            menu_record_scores(match_controller)

        elif choice == "4":
            menu_update_scores(match_controller)

        elif choice == "5":
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

        elif choice == "6":
            player_view.display_tournament_players(tournament.players)

        elif choice == "7":
            menu_show_ranking(
                tournament,
                ranking_controller,
                match_view,
            )

        elif choice == "8":
            match_view.display_tournament_rounds(rounds)

        elif choice == "0":
            print("\nRetour au menu principal.")
            break

        else:
            print("\nChoix invalide.")
