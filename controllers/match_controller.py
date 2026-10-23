"""Define the match controller."""
import random

from models.match import Match
from models.round import Round


class MatchController:
    def __init__(self, repository=None, players=None):
        self.repository = repository
        self.rounds = (repository.load_all(players or []) if repository else [])

    def get_rounds(self):
        return self.rounds

    def get_player_points(self, player):
        total_points = 0

        for round_instance in self.rounds:
            # Points won in the matches
            for match in round_instance.matches:
                for player_score in match.players:
                    match_player = player_score[0]
                    score = player_score[1]

                    if match_player.cnid == player.cnid:
                        total_points += score

            # A player exempted from a match receive a point
            if (
                round_instance.bye_player is not None
                and round_instance.bye_player.cnid == player.cnid
            ):
                total_points += 1

        return total_points

    def get_previous_opponents(self, player):
        opponents = set()

        for round_instance in self.rounds:
            for match in round_instance.matches:
                player1 = match.players[0][0]
                player2 = match.players[1][0]

                if player1.cnid == player.cnid:
                    opponents.add(player2.cnid)
                elif player2.cnid == player.cnid:
                    opponents.add(player1.cnid)

        return opponents

    def has_received_bye(self, player):
        for round_instance in self.rounds:
            if (
                round_instance.bye_player is not None
                and round_instance.bye_player.cnid == player.cnid
            ):
                return True

        return False

    def rank_players(self, players):
        players_by_score = {}

        for player in players:
            points = self.get_player_points(player)

            if points not in players_by_score:
                players_by_score[points] = []

            players_by_score[points].append(player)

        ranked_players = []

        for points in sorted(players_by_score, reverse=True):
            tied_players = players_by_score[points]
            random.shuffle(tied_players)
            ranked_players.extend(tied_players)

        return ranked_players

    def _find_pairings(self, players, allow_rematches):
        """Find complete pairings, preferring opponents not yet faced."""
        if not players:
            return []

        first_player = players[0]
        previous_opponents = self.get_previous_opponents(first_player)

        candidates = players[1:]
        random.shuffle(candidates)

        # Try players not previously faced before considering matches
        candidates.sort(
            key=lambda player: player.cnid in previous_opponents
        )

        for opponent in candidates:
            is_rematch = opponent.cnid in previous_opponents

            if is_rematch and not allow_rematches:
                continue

            remaining_players = [
                player
                for player in players
                if player.cnid not in (
                    first_player.cnid,
                    opponent.cnid,
                )
            ]

            remaining_pairings = self._find_pairings(
                remaining_players,
                allow_rematches,
            )

            if remaining_pairings is not None:
                return [(first_player, opponent)] + remaining_pairings

        return None

    def find_valid_pairings(self, players):
        # First, require every pairing to be a new match
        pairings = self._find_pairings(players, allow_rematches=False)

        if pairings is not None:
            return pairings

        # Only if that is impossible, allow matches again
        return self._find_pairings(players, allow_rematches=True)

    def create_round(self):
        round_number = len(self.rounds) + 1
        round_instance = Round(f"Tour {round_number}")

        self.rounds.append(round_instance)
        self._save()

        return round_instance

    def create_match(self, round_index, player1, player2):
        if not 0 <= round_index < len(self.rounds):
            return None

        round_instance = self.rounds[round_index]

        if round_instance.end_datetime is not None:
            return None

        if player1.cnid == player2.cnid:
            return None

        # Each player can participate in only one match per round
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

        # The exempt player cannot also have a match
        if round_instance.bye_player is not None:
            bye_cnid = round_instance.bye_player.cnid

            if bye_cnid in (player1.cnid, player2.cnid):
                return None

        match = Match(player1, player2)
        round_instance.add_match(match)
        self._save()

        return match

    def update_score(self, round_index, match_index, player_index, score):
        if not 0 <= round_index < len(self.rounds):
            return False

        round_instance = self.rounds[round_index]

        if round_instance.end_datetime is not None:
            return False

        if not 0 <= match_index < len(round_instance.matches):
            return False

        match = round_instance.matches[match_index]

        if not match.update_score(player_index, score):
            return False

        self._save()
        return True

    def finish_round(self, round_index):
        if not 0 <= round_index < len(self.rounds):
            return False

        round_instance = self.rounds[round_index]

        if round_instance.end_datetime is not None:
            return False

        # All the macthes must have a result
        for match in round_instance.matches:
            if match.result is None:
                return False

        round_instance.finish()
        self._save()
        return True

    def generate_next_round(self, players):
        # The previous round must be finished first
        if self.rounds and self.rounds[-1].end_datetime is None:
            return None

        if len(players) < 2:
            return None

        # random draw on the first round
        if not self.rounds:
            ranked_players = list(players)
            random.shuffle(ranked_players)
        else:
            # On the next rounds, order by tournament points
            ranked_players = self.rank_players(players)

        bye_player = None

        if len(ranked_players) % 2 == 1:
            # Prefer a player not already having received a bye
            eligible_players = [
                player
                for player in ranked_players
                if not self.has_received_bye(player)
            ]

            if eligible_players:
                # The lowest-ranked eligible player gets the bye
                bye_player = eligible_players[-1]
            else:
                # Everyone has already received a bye
                bye_player = ranked_players[-1]

            ranked_players.remove(bye_player)

        pairings = self.find_valid_pairings(ranked_players)

        if pairings is None:
            return None

        round_instance = self.create_round()
        round_index = len(self.rounds) - 1

        if bye_player is not None:
            round_instance.set_bye_player(bye_player)

        for player1, player2 in pairings:
            # Randomly decide which player is White and which is Black
            if random.choice([True, False]):
                player1, player2 = player2, player1

            match = self.create_match(
                round_index,
                player1,
                player2,
            )

            if match is None:
                # do not leave a partially generated round
                self.rounds.pop()
                self._save()
                return None

        self._save()
        return round_instance

    def _save(self):
        if self.repository:
            self.repository.save_all(self.rounds)

    def record_result(self, round_index, match_index, result):
        """Record the match result of a round."""

        if not 0 <= round_index < len(self.rounds):
            return False

        round_instance = self.rounds[round_index]

        # A round finioshed cannot be modified
        if round_instance.end_datetime is not None:
            return False

        if not 0 <= match_index < len(round_instance.matches):
            return False

        match = round_instance.matches[match_index]

        if not match.set_result(result):
            return False

        self._save()
        return True

    def get_ranking(self, players):
        """Return the players ordered by decreasing points."""

        ranking = []

        for player in players:
            points = self.get_player_points(player)
            ranking.append((player, points))

        ranking.sort(
            key=lambda item: (
                -item[1],
                item[0].lastname.lower(),
                item[0].firstname.lower(),
            )
        )

        return ranking
