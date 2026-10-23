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
        return {
            "players": [
                {
                    "cnid": player_score[0].cnid,
                    "score": player_score[1],
                }
                for player_score in self.players
            ],
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data, players_by_cnid):
        player1_data = data["players"][0]
        player2_data = data["players"][1]

        player1 = players_by_cnid[player1_data["cnid"]]
        player2 = players_by_cnid[player2_data["cnid"]]

        match = cls(player1, player2)

        result = data.get("result")

        if result in cls.VALID_RESULTS:
            match.set_result(result)
        else:
            # Compatibility with the previous JSON data.
            match.players[0][1] = player1_data["score"]
            match.players[1][1] = player2_data["score"]

        return match
