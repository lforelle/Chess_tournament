"""Display the matches."""


class MatchView:
    def display_matches(self, matches):
        print("\n--- Liste des matchs ---")

        if not matches:
            print("Aucun match créé.")
            return

        # for number, match in enumerate(matches, start=1):
        #     print(f"{number}. {match}")

        number = 1
        for match in matches:
            print(f"{number} | ", end="")
            print(match)
            number += 1
