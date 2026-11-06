from repositories.tournament_repository import TournamentRepository
from repositories.player_repository import PlayerRepository

from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController

from views.tournament_view import TournamentView
from views.player_view import PlayerView

from menus.menu_global import menu_global


def main():
    player_repository = PlayerRepository()
    player_controller = PlayerController(player_repository)

    players = player_controller.get_players()

    # Tournaments management
    tournament_repository = TournamentRepository()
    tournament_controller = TournamentController(
        tournament_repository,
        players
    )

    # Views
    player_view = PlayerView()
    tournament_view = TournamentView()

    # Main menu
    menu_global(
        tournament_controller,
        tournament_view,
        player_controller,
        player_view,
    )


if __name__ == "__main__":
    main()
