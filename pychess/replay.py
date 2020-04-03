"""
Replay class
"""

from typing import List, Tuple
from move import Move
from ticket import Ticket

ReplayId = int


class Replay:
    def __init__(self, replay_id: ReplayId, tickets: Tuple[Ticket, Ticket]):
        self.moves: List[Move] = []
        self.tickets = tickets
        self.id = replay_id
