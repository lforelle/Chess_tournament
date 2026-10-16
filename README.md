### Chess_tournament
Management of a chess tournament (rounds, matches list, players, scores,...)

## Project architecture

    📂 tournois_echec
        |_ 📂 main.py        > point d'entree du programme
        |        |__menu_player.py
        |        |__menu_tournament.py
        |
        |_ 📂 models/
        |        |__player.py
        |        |__tournament.py
        |
        |_ 📂 controllers/
        |        |__player_controller.py
        |        |__tournament_controller.py
        |
        |_ 📂 data/
        |        |__player_data.json
        |        |__tournament_data.json
        |
        |_ 📂 views/
                |__player_view.py
                |__tournament_view.py
    
