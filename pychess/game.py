"""
Game class
"""

from typing import Tuple
from ticket import Ticket


class Game:
    def __init__(self, tickets: Tuple[Ticket, Ticket]):
        time = tickets[0].time
        self.timeLeft = (time, time)
