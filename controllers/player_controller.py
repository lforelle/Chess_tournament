"""Define the player controller."""
from models.player import Player


class PlayerController:
    def __init__(self, repository):
        self.repository = repository
        self.players = self.repository.load_all()

    def create_player(self, lastname, firstname, birthdate, cnid):
        player = Player(
            lastname,
            firstname,
            birthdate,
            cnid,
        )

        self.players.append(player)
        self.repository.save_all(self.players)

        return player

    def get_players(self):
        return self.players

    def update_player(self, index, lastname, firstname, birthdate, cnid):
        if not 0 <= index < len(self.players):
            return False

        player = self.players[index]
        player.lastname = lastname
        player.firstname = firstname
        player.birthdate = birthdate
        player.cnid = cnid

        self.repository.save_all(self.players)
        return True

    def remove_player(self, index):
        if not 0 <= index < len(self.players):
            return False

        del self.players[index]
        self.repository.save_all(self.players)

        return True
