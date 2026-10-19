"""Menu used to select the action to do in the program"""
from menu.menu_create_player import menu_create_player
from controllers.player_controller import PlayerController
from menu.menu_update_player import menu_update_player
from views.player_view import PlayerView
from repositories.player_repository import PlayerRepository
from menu.menu_remove_player import menu_remove_player


def main():
    repository = PlayerRepository()
    player_controller = PlayerController(repository)
    player_view = PlayerView()

    while True:
        print("\n### Tournois d'Echecs ###\n")
        print("   ---------Joueurs----------")
        print("   1. Créer un joueur")
        print("   2. Modifier un joueur")
        print("   3. Supprimer un joueur")
        print("   4. Afficher les joueurs")
        print("   ---------Matchs-----------")
        print("   5. Créer un match")
        print("   6. Modifier un match")
        print("   7. Supprimer un match")
        print("   8. Afficher les matchs")
        print("   ---------Tours------------")
        print("   9. Créer un tour")
        print("   10. Modifier un tour")
        print("   11. Supprimer un tour")
        print("   12. Afficher les tours")
        print("   ---------Tournois---------")
        print("   13. Créer un tournois")
        print("   14. Modifier un tournois")
        print("   15. Modifier un tournois")
        print("   16. Afficher les tournois")

        print("\n   0. Quitter")
        choice = input("\nVotre choix : ")

        if choice == "1":
            menu_create_player(player_controller)

        elif choice == "2":
            menu_update_player(player_controller, player_view)

        elif choice == "3":
            menu_remove_player(player_controller, player_view)

        elif choice == "4":
            players = player_controller.get_players()
            player_view.display_players(players)

        elif choice == "5":
            pass

        elif choice == "6":
            pass

        elif choice == "7":
            pass

        elif choice == "8":
            pass

        elif choice == "9":
            pass

        elif choice == "10":
            pass

        elif choice == "11":
            pass

        elif choice == "12":
            pass

        elif choice == "13":
            pass

        elif choice == "0":
            print("\n====== Au revoir ! =======\n")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
