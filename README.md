### Chess_tournament
Management of a chess tournament (rounds, matches list, players, scores,...)

## Project architecture

:open_file_folder: tournois_echec
    - :open_file_folder: main.py
        point d'entree du programme
        |__menu_player.py
        |__menu_tournament.py

    - :open_file_folder: models/
        |__player.py
        |__tournament.py

    - :open_file_folder: controllers/
        |__player_controller.py
        |__tournament_controller.py

    - :open_file_folder: data/
        |__player_data.json
        |__tournament_data.json

    - :open_file_folder: views/
        |__player_view.py
        |__tournament_view.py
    