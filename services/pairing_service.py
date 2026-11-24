"""Services gathering the business logic algorithms."""
import random


class PairingService:
    """Manage the players pairing and the byes."""

    def __init__(self, rounds):
        self.rounds = rounds

    def get_previous_opponents(self, player):
        """Return the opponents already matched by a player."""
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
        """Check if a player has already had a bye."""
        for round_instance in self.rounds:
            if (
                round_instance.bye_player is not None
                and round_instance.bye_player.cnid == player.cnid
            ):
                return True

        return False

    def _find_pairings(self, players, allow_rematches):
        """Search for complete pairings avoiding revenges if possible.
        Each element in that list represent a combination to explore.
        We start with all the players and no matches created."""

        combinations_to_check = [(players, [])]

        while combinations_to_check:
            remaining_players, pairings = combinations_to_check.pop()

            if not remaining_players:
                return pairings

            first_player = remaining_players[0]

            previous_opponents = self.get_previous_opponents(first_player)

            candidates = remaining_players[1:]
            random.shuffle(candidates)

            # Favour the players who has not faced off.
            candidates.sort(
                key=lambda player: player.cnid in previous_opponents
            )

            for opponent in candidates:
                is_rematch = opponent.cnid in previous_opponents

                if is_rematch and not allow_rematches:
                    continue

                new_remaining_players = []

                for player in remaining_players:
                    if (
                        player.cnid != first_player.cnid
                        and player.cnid != opponent.cnid
                    ):
                        new_remaining_players.append(player)

                new_pairings = pairings + [(first_player, opponent)]

                combinations_to_check.append(
                    (new_remaining_players, new_pairings)
                )

        return None

    def find_valid_pairings(self, players):
        """Avoid revenge, except if unavoidable."""

        pairings = self._find_pairings(
            players,
            allow_rematches=False,
        )

        if pairings is not None:
            return pairings

        return self._find_pairings(
            players,
            allow_rematches=True,
        )
