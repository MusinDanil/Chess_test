"""
GamePool class
"""
from typing import List
from game import Game


class GamePool:
    games: List[Game]

    def __init__(self):
        self.games = []

    def new_game(self, tickets: (Ticket, Ticket)):
        self.games.append(Game(tickets))
