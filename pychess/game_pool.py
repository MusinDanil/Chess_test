"""
GamePool class
"""
from typing import Dict, Tuple
from ticket import Ticket
from game import Game, GameId
from history import History


class GamePool:
    current_games: Dict[GameId, Game]
    last_id: GameId

    def __init__(self, history: History):
        self.history = history
        self.current_games = dict()
        self.last_id = 0

    def start_game(self, tickets: Tuple[Ticket, Ticket]):
        new_game = Game(self.last_id, tickets)
        self.current_games[self.last_id] = new_game
        self.last_id += 1

        return id

    def end_game(self, game_id: GameId):
        ended_game = self.current_games.pop(game_id)
        self.history.save_replay(ended_game.replay)

    def get_game(self, game_id: GameId):
        return self.current_games[game_id]
