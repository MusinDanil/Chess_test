"""
User class
"""

from users_handler import UsersHandler


class User:
    user_id: int
    rating: int
    users_handler: UsersHandler

    def __init__(self, users_handler: UsersHandler, user_id):
        self.users_handler = users_handler
        self.users_handler.get_user(user_id)
