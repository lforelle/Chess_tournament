"""Define the player controller."""
from models.player import Player


class PlayerController:
    def __init__(self, repository):
        self.repository = repository
        self.players = self.repository.load_all()

    def create_player(self, lastname, firstname, birthdate, cnid):
        cnid = cnid.strip().upper()
        if self.cnid_is_used(cnid):
            return None

        player = Player(
            lastname,
            firstname,
            birthdate,
            cnid,
        )

        self.players.append(player)
        self.repository.save_all(self.players)

        return player

    def cnid_is_used(self, cnid, exclude_index=None):
        """Check whether another player already has this CNID."""
        cnid = cnid.strip().upper()

        return any(
            index != exclude_index and player.cnid == cnid
            for index, player in enumerate(self.players)
        )

    def get_players(self):
        return tuple(self.players)

    def save_all(self):
        self.repository.save_all(self.players)

    def update_player(
        self,
        index,
        lastname,
        firstname,
        birthdate,
        cnid,
        *,
        persist=True,
    ):
        if not 0 <= index < len(self.players):
            return False

        cnid = cnid.strip().upper()
        # If another player already owns that CNID, abort the update.
        if self.cnid_is_used(cnid, exclude_index=index):
            return False

        player = self.players[index]
        player.lastname = lastname
        player.firstname = firstname
        player.birthdate = birthdate
        player.cnid = cnid

        if persist:
            self.save_all()

        return True

    def get_active_players(self):
        return tuple(player for player in self.players if player.active)

    def deactivate_player(self, cnid):
        player = next(
            (player for player in self.players if player.cnid == cnid),
            None,
        )
        if player is None or not player.active:
            return False

        player.active = False
        self.save_all()
        return True
