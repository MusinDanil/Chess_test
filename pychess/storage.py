"""
Storage interface
"""
from typing import List
from replay import Replay, ReplayId
from user import User


class Storage:
    replays: List[Replay]
    users: List[User]

    def __init__(self):
        self.users = []
        self.replays = []

    def save_replay(self, replay: Replay):
        self.replays.append(replay)

    def get_replay(self, replay_id: ReplayId) -> Replay:
        return self.replays[replay_id]

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id):
        return self.users[user_id]

    def edit_user(self, user_id, delta): # todo annotated
        return self.users[user_id]
    
    def delete_user(self, user_id):
        pass
