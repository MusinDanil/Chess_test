"""
History module
"""

from storage import Storage
from replay import Replay, ReplayId


class History:
    def __init__(self, storage: Storage):
        self._storage = storage

    def save_replay(self, replay: Replay):
        self._storage.save_replay(replay)

    def get_replay(self, replay_id: ReplayId) -> Replay:
        return self._storage.get_replay(replay_id)
