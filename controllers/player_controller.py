"""Define the player controller."""
from models.player import Player


class PlayerController:
    def __init__(self, repository):
        self.repository = repository
        self.players = self.repository.load_all()

    def create_player(self, lastname, firstname, birthdate, ranking, cnid):
        player = Player(
            lastname,
            firstname,
            birthdate,
            ranking,
            cnid,
        )

        self.repository.save(player)
        self.players.append(player)

        return player

    def get_players(self):
        return self.players

    def update_player(self, index, lastname, firstname, birthdate, ranking, cnid):
        if not 0 <= index < len(self.players):
            return False

        player = self.players[index]
        player.lastname = lastname
        player.firstname = firstname
        player.birthdate = birthdate
        player.ranking = ranking
        player.cnid = cnid

        self.repository.save_all(self.players)
        return True

    def remove_player(self, index):
        if not 0 <= index < len(self.players):
            return False

        updated_players = self.players.copy()
        del updated_players[index]

        self.repository.save_all(updated_players)
        self.players = updated_players
        return True
