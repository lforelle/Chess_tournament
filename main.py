"""Menu used to select the action to do in the program"""
from menu.menu_tournament import menu_tournament
from menu.menu_player import menu_player


def main():
    while True:
        print("\n### Tournois d'Echecs ###\n")
        print("   1. Créer un tournois")
        print("   2. Créer un joueur")
        print("   3. Créer les matchs")

        print("   4. Lister les tours du tournois")
        print("   5. Lister les joueurs enregistrés")

        print("\n   0. Quitter")
        choice = input("\nVotre choix : ")

        if choice == "1":
            menu_tournament()

        elif choice == "2":
            menu_player()

        elif choice == "3":
            pass
        
        elif choice == "4":
            pass
        
        elif choice == "5":
            pass
        
        elif choice == "0":
            print("\n====== Au revoir ! =======\n")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
