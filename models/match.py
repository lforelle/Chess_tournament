"""Match between two players."""


class Match:
    """A match and the scores of its two players."""

    def __init__(self, player1, player2, score1=0, score2=0, result=None):
        self.players = ([player1, score1], [player2, score2])
        self.result = result

    def to_dict(self):
        """Return a JSON-serializable representation of the match.

        Players are identified by their CNID so the player information remains
        stored in a single place: ``data/players_data/players.json``.
        """
        return {
            "player1_cnid": self.players[0][0].cnid,
            "player2_cnid": self.players[1][0].cnid,
            "score1": self.players[0][1],
            "score2": self.players[1][1],
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data, players_by_cnid):
        """Recreate a match from JSON using the already loaded players."""
        try:
            player1 = players_by_cnid[data["player1_cnid"]]
            player2 = players_by_cnid[data["player2_cnid"]]
        except KeyError as error:
            raise ValueError(
                "Le match référence un joueur introuvable : "
                f"{error.args[0]}"
            ) from error

        return cls(
            player1,
            player2,
            data.get("score1", 0),
            data.get("score2", 0),
            data.get("result"),
        )

    def __str__(self):
        result = self.result if self.result is not None else "Non joué"
        player1 = self.players[0][0]
        player2 = self.players[1][0]
        return (
            f"{player1.firstname} {player1.lastname} "
            f"contre {player2.firstname} {player2.lastname} "
            f"- Résultat : {result}"
        )
