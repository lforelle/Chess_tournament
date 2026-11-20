"""Define the player"""

from datetime import date, datetime


class Player:
    """A player has a lastname, a firstname, a birthdate and a Chess National ID
    (format: 'AB12345') that is manually entered on registration.
    """

    def __init__(self, lastname, firstname, birthdate, cnid, active=True):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.cnid = cnid
        self.active = active

    def __str__(self):
        return (
            f"{self.lastname} "
            f"{self.firstname}"
        )

    def to_dict(self):
        birthdate = self.birthdate

        if isinstance(birthdate, (date, datetime)):
            birthdate = birthdate.strftime("%d/%m/%Y")

        return {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": birthdate,
            "cnid": self.cnid,
            "active": self.active,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            lastname=data["lastname"],
            firstname=data["firstname"],
            birthdate=datetime.strptime(data["birthdate"], "%d/%m/%Y"),
            cnid=data["cnid"],
            active=data.get("active", True),
        )
