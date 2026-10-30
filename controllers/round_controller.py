import random
from models.round import Round


class RoundController:
    """Gère la création et la clôture des tours."""

    def __init__(
        self,
        rounds,
        ranking_controller,
        pairing_service,
        match_controller,
        repository=None,
    ):
        self.rounds = rounds
        self.ranking_controller = ranking_controller
        self.pairing_service = pairing_service
        self.match_controller = match_controller
        self.repository = repository

    def get_rounds(self):
        return self.rounds

    def _save(self):
        if self.repository:
            self.repository.save_all(self.rounds)

    def create_round(self):
        round_number = len(self.rounds) + 1
        round_instance = Round(f"Tour {round_number}")

        self.rounds.append(round_instance)
        self._save()

        return round_instance

    def finish_round(self, round_index):
        if not 0 <= round_index < len(self.rounds):
            return False

        round_instance = self.rounds[round_index]

        if round_instance.end_datetime is not None:
            return False

        for match in round_instance.matches:
            if match.result is None:
                return False

        round_instance.finish()
        self._save()
        return True

    def generate_next_round(self, players):
        # Le tour précédent doit être terminé.
        if self.rounds and self.rounds[-1].end_datetime is None:
            return None

        if len(players) < 2:
            return None

        # Tirage aléatoire au premier tour.
        if not self.rounds:
            ranked_players = list(players)
            random.shuffle(ranked_players)
        else:
            ranked_players = self.ranking_controller.rank_players(players)

        bye_player = None

        # Si le nombre de joueurs est impair, choisir un exempté.
        if len(ranked_players) % 2 == 1:
            eligible_players = [
                player
                for player in ranked_players
                if not self.pairing_service.has_received_bye(player)
            ]

            if eligible_players:
                bye_player = eligible_players[-1]
            else:
                bye_player = ranked_players[-1]

            ranked_players.remove(bye_player)

        pairings = self.pairing_service.find_valid_pairings(
            ranked_players
        )

        if not pairings:
            return None

        round_instance = self.create_round()
        round_index = len(self.rounds) - 1

        if bye_player is not None:
            round_instance.set_bye_player(bye_player)

        for player1, player2 in pairings:
            # Déterminer aléatoirement les blancs (1ere position) et les noirs.
            if random.choice([True, False]):
                player1, player2 = player2, player1

            match = self.match_controller.create_match(
                round_index,
                player1,
                player2,
            )

            if match is None:
                # Annuler le tour si une rencontre échoue.
                self.rounds.pop()
                self._save()
                return None

        self._save()
        return round_instance
