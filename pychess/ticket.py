from user import User


class Wishes:
    _wished_time: int
    _wished_side: str

    def __init__(self, wished_time, wished_side):
        self._wished_time = wished_time
        self._wished_side = wished_side


class Ticket:
    _user: User
    _wishes: Wishes
    _id: str