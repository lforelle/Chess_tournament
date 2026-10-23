"""Menu used to select the action to do in the program"""
from repositories.player_repository import PlayerRepository
from repositories.match_repository import MatchRepository

from controllers.player_controller import PlayerController
from controllers.match_controller import MatchController

from views.player_view import PlayerView
from views.match_view import MatchView

from menus.menu_global import menu_global

def main():
    player_repository = PlayerRepository()
    player_controller = PlayerController(player_repository)
    
    match_repository = MatchRepository()
    match_controller = MatchController(
        match_repository,
        player_controller.get_players(),
    )
    
    player_view = PlayerView()
    match_view = MatchView()

    menu_global(
        player_controller, 
        player_view, 
        match_controller, 
        match_view
        )


if __name__ == "__main__":
    main()
