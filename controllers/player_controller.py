from models.player import Player


class PlayerController:
    def create_player(self, lastname, firstname, birthday, ranking, cnid):
        player = Player(
            lastname,
            firstname,
            birthday,
            ranking,
            cnid,
        )

        # Plus tard :
        # self.repository.save_player_infos(player)

        return player
