"""Define the player"""


class Player:
    """A player has a lastname, a firstname, a birthday, a chess ranking and a Chess National ID
    (format: 'AB12345') that is manually entered on registration.
    """

    def __init__(self, lastname, firstname, birthday, ranking, cnid):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.ranking = ranking
        self.cnid = cnid

    def __str__(self):
        return (
            f"{self.lastname} {self.firstname}\n"
            f"Classement: {self.ranking}\n"
            f"ID: '{self.cnid}'"
        )
