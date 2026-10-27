from datetime import datetime
from models.match import Match


class Round:
    """A tournament round containing matches and an optional bye in case a player has no opponent.
    For instance if the number of players, engaged in the tournament, is odd"""

    def __init__(self, name, matches=None, bye_player=None):
        self.name = name
        self.matches = matches if matches is not None else []
        self.bye_player = bye_player

        self.start_datetime = datetime.now()
        self.end_datetime = None

    def add_match(self, match):
        self.matches.append(match)

    def set_bye_player(self, player):
        self.bye_player = player

    def finish(self):
        if self.end_datetime is None:
            self.end_datetime = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat()
                if self.end_datetime is not None
                else None
            ),
            "bye_player_cnid": (
                self.bye_player.cnid
                if self.bye_player is not None
                else None
            ),
            "matches": [
                match.to_dict()
                for match in self.matches
            ],
        }

    @classmethod
    def from_dict(cls, data, players_by_cnid):
        matches = []

        for match_data in data["matches"]:
            match = Match.from_dict(match_data, players_by_cnid)
            matches.append(match)

        bye_cnid = data.get("bye_player_cnid")
        bye_player = (
            players_by_cnid.get(bye_cnid)
            if bye_cnid is not None
            else None
        )

        round_instance = cls(
            data["name"],
            matches,
            bye_player,
        )

        round_instance.start_datetime = datetime.fromisoformat(
            data["start_datetime"]
        )

        end_datetime = data.get("end_datetime")
        if end_datetime is not None:
            round_instance.end_datetime = datetime.fromisoformat(
                end_datetime
            )

        return round_instance
