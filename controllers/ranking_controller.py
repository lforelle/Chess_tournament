import random


class RankingController:
    """Manage the points and the ranking of players."""

    def __init__(self, rounds):
        self.rounds = rounds

    def get_player_points(self, player):
        """Calculate the global points of a player."""

        total_points = 0

        for round_instance in self.rounds:
            for match in round_instance.matches:
                for player_score in match.players:
                    match_player = player_score[0]
                    score = player_score[1]

                    if match_player.cnid == player.cnid:
                        total_points += score

            # A bye player receive 1 point.
            if (
                round_instance.bye_player is not None
                and round_instance.bye_player.cnid == player.cnid
            ):
                total_points += 1

        return total_points

    def rank_players(self, players):
        """Prepare the coupling of the next round
        Sort the players by points, with a random order if equal."""

        players_by_score = {}

        for player in players:
            points = self.get_player_points(player)

            if points not in players_by_score:
                players_by_score[points] = []

            players_by_score[points].append(player)

        ranked_players = []

        for points in sorted(players_by_score, reverse=True):
            tied_players = players_by_score[points]
            random.shuffle(tied_players)
            ranked_players.extend(tied_players)

        return ranked_players

    def get_ranking(self, players):
        """Return the players and their points, sorted by points then by alphabetical order."""

        ranking = []

        for player in players:
            points = self.get_player_points(player)
            ranking.append((player, points))

        ranking.sort(
            key=lambda item: (
                -item[1],
                item[0].lastname.lower(),
                item[0].firstname.lower(),
            )
        )

        return ranking
