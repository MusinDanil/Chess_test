"""
Ticket class
"""

from user import User

class Ticket:
    def __init__(self, user: User, wish: Wishlist):
        self.wish = wish
        self.user = user
