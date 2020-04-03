"""
GamePool class
"""
from typing import List, Tuple
from ticket import Ticket
from game import Game


class GamePool:
    games: List[Game]

    def __init__(self):
        self.games = []

    def new_game(self, tickets: Tuple[Ticket, Ticket]):
        self.games.append(Game(tickets))
