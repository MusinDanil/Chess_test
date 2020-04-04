"""
User class
"""

from users_handler import UsersHandler


class User:
    user_id: int
    rating: int

    def __init__(self, user_info: dict):
        self.user_id = user_info['user_id']
        self.rating = user_info['rating']
