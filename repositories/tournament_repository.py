import json
from pathlib import Path
from models.tournament import Tournament
from datetime import datetime


class TournamentRepository:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        self.file_path = project_root / "data" / "tournaments_data" / "tournaments.json"

    def load_all(self):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            tournaments_data = json.load(file)

        tournaments = []

        for data in tournaments_data:
            tournament = Tournament(
                data["name"],
                data["place"],
                datetime.strptime(data["start_date"], "%Y-%m-%dT%H:%M:%S"),
                datetime.strptime(data["end_date"], "%Y-%m-%dT%H:%M:%S"),
                data["description"],
                data["number_of_rounds"],
            )
            tournaments.append(tournament)

        return tournaments

    def save_all(self, tournaments):
        tournaments_data = []

        for tournament in tournaments:
            tournament_data = tournament.to_dict()
            tournaments_data.append(tournament_data)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                tournaments_data,
                file,
                ensure_ascii=False,
                indent=4,
            )
