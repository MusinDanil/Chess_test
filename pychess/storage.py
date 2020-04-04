"""
Storage interface
"""
from typing import List, Dict, Optional
from replay import Replay, ReplayId
from user import User


class Storage:
    replays: Dict[ReplayId, Optional[Replay]]
    users: List[User]

    def __init__(self):
        self.users = []
        self.replays = []

    def save_replay(self, replay_id: ReplayId, replay: Optional[Replay]):
        self.replays[replay_id] = replay

    def get_replay(self, replay_id: ReplayId) -> Optional[Replay]:
        return self.replays[replay_id]

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id):
        return self.users[user_id]

    def edit_user(self, user_id, delta):  # todo annotated
        return self.users[user_id]

    def count_games(self) -> ReplayId:
        return len(self.replays)

    def delete_user(self, user_id):
        pass
