"""
Game class
"""

from typing import Tuple
from ticket import Ticket
from engine import GameState
from replay import Replay, ReplayId

GameId = ReplayId


class Game:
    def __init__(self, replay_id: ReplayId, tickets: Tuple[Ticket, Ticket]):
        time = tickets[0].wishes.time

        self.record = Replay(replay_id, tickets)
        self.timeLeft = (time, time)
        self.gameState = GameState()
