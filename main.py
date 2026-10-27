from repositories.player_repository import PlayerRepository
from repositories.match_repository import MatchRepository

from controllers.player_controller import PlayerController
from controllers.match_controller import MatchController
from controllers.round_controller import RoundController
from controllers.ranking_controller import RankingController

from services.pairing_service import PairingService

from views.player_view import PlayerView
from views.match_view import MatchView

from menus.menu_global import menu_global


def main():
    player_repository = PlayerRepository()
    player_controller = PlayerController(player_repository)

    match_repository = MatchRepository()

    # Charge les tours une seule fois.
    match_controller = MatchController(
        match_repository,
        player_controller.get_players(),
    )

    # Tous les composants partagent la même liste de tours.
    rounds = match_controller.get_rounds()

    ranking_controller = RankingController(rounds)
    pairing_service = PairingService(rounds)

    round_controller = RoundController(
        rounds=rounds,
        ranking_controller=ranking_controller,
        pairing_service=pairing_service,
        match_controller=match_controller,
        repository=match_repository,
    )

    player_view = PlayerView()
    match_view = MatchView()

    menu_global(
        player_controller,
        player_view,
        match_controller,
        match_view,
        round_controller,
        ranking_controller,
    )


if __name__ == "__main__":
    main()
