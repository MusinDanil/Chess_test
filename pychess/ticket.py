"""
Ticket class
"""

from user import User
from wishes import Wishes


class Ticket:
    def __init__(self, user: User, wishes: Wishes):
        self.wishes = wishes
        self.user = user
