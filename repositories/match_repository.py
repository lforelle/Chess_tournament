"""Persistence of matches in a JSON file."""

import json
from pathlib import Path

from models.match import Match


class MatchRepository:
    """Read and write matches in ``data/matches_data/matches.json``."""

    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = project_root / "data" / "matches_data" / "matches.json"

    def load_all(self, players):
        """Load matches and associate their CNIDs with loaded Player objects."""
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            matches_data = json.load(file)

        if not isinstance(matches_data, list):
            raise ValueError("Le fichier des matchs doit contenir une liste JSON.")

        players_by_cnid = {player.cnid: player for player in players}
        return [Match.from_dict(data, players_by_cnid) for data in matches_data]

    def save_all(self, matches):
        """Save every match as JSON, creating the data directory if required."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                [match.to_dict() for match in matches],
                file,
                ensure_ascii=False,
                indent=4,
            )
