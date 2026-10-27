"""Gère la création des rencontres et leurs résultats."""

from models.match import Match


class MatchController:
    def __init__(self, repository=None, players=None):
        self.repository = repository
        self.rounds = (
            repository.load_all(players or [])
            if repository
            else []
        )

    def get_rounds(self):
        return self.rounds

    def create_match(self, round_index, player1, player2):
        """Crée une rencontre dans un tour."""

        if not 0 <= round_index < len(self.rounds):
            return None

        round_instance = self.rounds[round_index]

        if round_instance.end_datetime is not None:
            return None

        if player1.cnid == player2.cnid:
            return None

        # Un joueur ne peut participer qu'à une rencontre par tour.
        for match in round_instance.matches:
            match_cnids = {
                match.players[0][0].cnid,
                match.players[1][0].cnid,
            }

            if (
                player1.cnid in match_cnids
                or player2.cnid in match_cnids
            ):
                return None

        # Un joueur exempté ne peut pas participer à une rencontre.
        if round_instance.bye_player is not None:
            bye_cnid = round_instance.bye_player.cnid

            if bye_cnid in (player1.cnid, player2.cnid):
                return None

        match = Match(player1, player2)
        round_instance.add_match(match)
        self._save()

        return match

    def record_result(self, round_index, match_index, result):
        """Enregistre le résultat d'une rencontre."""

        if not 0 <= round_index < len(self.rounds):
            return False

        round_instance = self.rounds[round_index]

        # Un tour terminé ne peut plus être modifié.
        if round_instance.end_datetime is not None:
            return False

        if not 0 <= match_index < len(round_instance.matches):
            return False

        match = round_instance.matches[match_index]

        if not match.set_result(result):
            return False

        self._save()
        return True

    def _save(self):
        """Sauvegarde les tours dans le dépôt."""
        if self.repository:
            self.repository.save_all(self.rounds)
