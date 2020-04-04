"""
GamePool class
"""
from typing import Dict, Tuple
from ticket import Ticket
from game import Game, GameId
from history import History


class GamePool:

    def __init__(self, history: History):
        self._history = history
        self._current_games: Dict[GameId, Game] = dict()

    def start_game(self, tickets: Tuple[Ticket, Ticket]):
        last_id = self._history.register_game()
        new_game = Game(last_id, tickets)
        self._current_games[last_id] = new_game

        return id

    def end_game(self, game_id: GameId):
        ended_game = self._current_games.pop(game_id)
        self._history.save_replay(ended_game.replay)

    def get_game(self, game_id: GameId):
        return self._current_games[game_id]
