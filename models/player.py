"""Define the player"""

from datetime import date, datetime


class Player:
    """A player has a lastname, a firstname, a birthdate, a chess ranking and a Chess National ID
    (format: 'AB12345') that is manually entered on registration.
    """

    def __init__(self, lastname, firstname, birthdate, ranking, cnid):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.ranking = ranking
        self.cnid = cnid

    def __str__(self):
        return (
            f"{self.lastname} | {self.firstname} | {self.birthdate} | "
            f"{self.ranking} | {self.cnid}"
        )

    def to_dict(self):
        if isinstance(self.birthdate, (date, datetime)):
            self.birthdate = self.birthdate.strftime("%d/%m/%Y")

        return {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "ranking": self.ranking,
            "cnid": self.cnid,
        }
