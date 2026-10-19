import json
from pathlib import Path
from models.player import Player


class PlayerRepository:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = project_root / "data" / "players_data" / "players.json"

    def load_all(self):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            players_data = json.load(file)

        players = []

        for data in players_data:
            player = Player(
                data["lastname"],
                data["firstname"],
                data["birthdate"],
                data["ranking"],
                data["cnid"],
            )
            players.append(player)

        return players

    def save(self, player):
        players = self.load_all()
        players.append(player)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                [saved_player.to_dict() for saved_player in players],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def save_all(self, players):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                [player.to_dict() for player in players],
                file,
                ensure_ascii=False,
                indent=4,
            )
