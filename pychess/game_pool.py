"""
GamePool class
"""
from typing import List, Tuple
from ticket import Ticket
from game import Game, GameId
from history import History


class GamePool:
    current_games: List[Game]
    last_id: int

    def __init__(self, history: History):
        self.history = history
        self.current_games = []
        self.last_id = 0

    def start_game(self, tickets: Tuple[Ticket, Ticket]):
        new_game = Game(self.last_id, tickets)
        self.current_games.append(new_game)
        self.last_id += 1

        return id

    def end_game(self):
        ended_game = self.current_games.pop()
        self.history.save_replay(ended_game.replay)

    def get_game(self, game_id: GameId):
        return self.current_games[game_id]
