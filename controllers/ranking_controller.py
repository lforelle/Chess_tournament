import random


class RankingController:
    """Gère les points et le classement des joueurs."""

    def __init__(self, rounds):
        self.rounds = rounds

    def get_player_points(self, player):
        """Calcule le total des points d'un joueur."""
        total_points = 0

        for round_instance in self.rounds:
            for match in round_instance.matches:
                for player_score in match.players:
                    match_player = player_score[0]
                    score = player_score[1]

                    if match_player.cnid == player.cnid:
                        total_points += score

            # Un joueur exempté reçoit un point.
            if (
                round_instance.bye_player is not None
                and round_instance.bye_player.cnid == player.cnid
            ):
                total_points += 1

        return total_points

    def rank_players(self, players):
        """Trie les joueurs par points, avec un ordre aléatoire en cas d'égalité."""
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
        """Renvoie les joueurs et leurs points, triés par points puis par ordre alphabétique."""
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
