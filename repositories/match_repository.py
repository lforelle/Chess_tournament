"""Persistence of matches in a JSON file."""

import json
from pathlib import Path
from models.round import Round


class MatchRepository:
    """Read and write rounds and their matches in JSON."""

    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = (
            project_root
            / "data"
            / "matches_data"
            / "matches.json"
        )

    def load_all(self, players):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            rounds_data = json.load(file)

        if not isinstance(rounds_data, list):
            raise ValueError("Le fichier doit contenir une liste JSON de tours.")

        players_by_cnid = {}

        for player in players:
            players_by_cnid[player.cnid] = player

        rounds = []

        for round_data in rounds_data:
            round_instance = Round.from_dict(
                round_data,
                players_by_cnid,
            )
            rounds.append(round_instance)

        return rounds

    def save_all(self, rounds):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                [round_instance.to_dict() for round_instance in rounds],
                file,
                ensure_ascii=False,
                indent=4,
            )
