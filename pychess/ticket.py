from user import User


class Wishes:
    wished_time: int
    wished_side: str

    def __init__(self, wished_time, wished_side):
        self._wished_time = wished_time
        self._wished_side = wished_side


class Ticket:
    user: User
    wishes: Wishes
    id: str
