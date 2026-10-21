"""Define the match controller."""

from models.match import Match


class MatchController:
    def __init__(self, repository=None, players=None):
        self.repository = repository
        self.matches = repository.load_all(players or []) if repository else []

    def create_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)
        self._save()
        return match

    def update_score(self, match_index, player_index, score):
        """Update one score and persist the match.

        ``match_index`` and ``player_index`` are zero-based.  Returns ``False``
        when either index is invalid.
        """
        if not 0 <= match_index < len(self.matches) or not 0 <= player_index < 2:
            return False

        match = self.matches[match_index]
        match.players[player_index][1] = score
        match.result = f"{match.players[0][1]}-{match.players[1][1]}"
        self._save()
        return True

    def get_matches(self):
        return self.matches

    def _save(self):
        if self.repository:
            self.repository.save_all(self.matches)
