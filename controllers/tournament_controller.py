from models.tournament import Tournament


class TournamentController:
    def create_tournament(self, name, location, start_date, end_date, description, number_of_rounds):
        tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            description,
            number_of_rounds,
        )

        # Plus tard :
        # self.repository.save_tournament_infos()

        return tournament
