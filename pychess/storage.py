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
