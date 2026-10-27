"""Match between two players."""


class Match:
    """A match between two players."""

    VALID_RESULTS = ("1-0", "0-1", "1/2-1/2")

    def __init__(self, player1, player2):
        self.players = [
            [player1, 0],
            [player2, 0],
        ]
        self.result = None

    def set_result(self, result):
        """Record the results and update the scores."""

        if result not in self.VALID_RESULTS:
            return False

        if result == "1-0":
            self.players[0][1] = 1
            self.players[1][1] = 0

        elif result == "0-1":
            self.players[0][1] = 0
            self.players[1][1] = 1

        else:
            self.players[0][1] = 0.5
            self.players[1][1] = 0.5

        self.result = result
        return True

    def to_dict(self):
        """Convert the match into a dictionary."""
        
        players_data = []

        for player_score in self.players:
            player_data = {
                "cnid": player_score[0].cnid,
                "score": player_score[1],
            }
            players_data.append(player_data)

        return {
            "players": players_data,
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data, players_by_cnid):
        """Rebuild a match from a dictionary."""

        player1_data = data["players"][0]
        player2_data = data["players"][1]

        player1 = players_by_cnid[player1_data["cnid"]]
        player2 = players_by_cnid[player2_data["cnid"]]

        match = cls(player1, player2)

        result = data.get("result")

        if result in cls.VALID_RESULTS:
            match.set_result(result)

        return match
