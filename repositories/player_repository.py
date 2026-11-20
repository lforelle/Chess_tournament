"""Repository for managing player data in a JSON file."""

import json
from pathlib import Path
from models.player import Player


class PlayerRepository:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = project_root / "data" / "tournaments" / "players.json"

    def load_all(self):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            players_data = json.load(file)

        players = [
            Player.from_dict(player_data)
            for player_data in players_data
        ]

        return players

    def save_all(self, players):
        players_data = []

        for player in players:
            player_data = player.to_dict()
            players_data.append(player_data)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                players_data,
                file,
                ensure_ascii=False,
                indent=4,
            )
