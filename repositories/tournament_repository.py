"""Repository for managing tournament data in a JSON file."""

import json
from pathlib import Path

from models.tournament import Tournament


class TournamentRepository:
    """Read and write tournaments in JSON."""

    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = project_root / "data" / "tournaments" / "tournaments.json"
        self.tournaments = []

    def load_all(self, players):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            tournaments_data = json.load(file)

        if not isinstance(tournaments_data, list):
            raise ValueError("Le fichier doit contenir une liste JSON de tournois.")

        players_by_cnid = {
            player.cnid: player
            for player in players
        }

        tournaments = []

        for data in tournaments_data:
            tournament = Tournament.from_dict(data, players_by_cnid)
            tournaments.append(tournament)

        return tournaments

    def save_all(self, tournaments):
        """Save all the tournaments."""

        self.tournaments = tournaments
        self._write_file()

    def save_tournament(self, tournament):
        """Save a single tournament."""

        if tournament not in self.tournaments:
            self.tournaments.append(tournament)

        self._write_file()

    def _write_file(self):
        """Write the tournaments data in the JSON file."""

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        tournaments_data = [
            tournament.to_dict()
            for tournament in self.tournaments
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                tournaments_data,
                file,
                ensure_ascii=False,
                indent=4,
            )
