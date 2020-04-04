"""
History module
"""

from typing import Optional
from storage import Storage
from replay import Replay, ReplayId


class History:
    def __init__(self, storage: Storage):
        self._storage = storage

    def register_game(self) -> ReplayId:
        last_gameid = self._storage.count_games()
        self._storage.save_replay(last_gameid, None)
        return last_gameid

    def save_replay(self, replay: Replay):
        self._storage.save_replay(replay.replay_id, replay)

    def get_replay(self, replay_id: ReplayId) -> Optional[Replay]:
        return self._storage.get_replay(replay_id)
