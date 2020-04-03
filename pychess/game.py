"""
Game class
"""

from typing import Tuple
from ticket import Ticket
from engine import GameState


class Game:
    def __init__(self, tickets: Tuple[Ticket, Ticket]):
        time = tickets[0].wishes.time

        self.record = tickets
        self.timeLeft = (time, time)
        self.gameState = GameState()
