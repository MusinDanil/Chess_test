"""
Module lobby
"""

from typing import Dict

from ticket import Ticket
from game_pool import GamePool


class Lobby:
    _game_pool: GamePool
    _pending_tickets: Dict[int, Ticket]

    def _check_pairs(self):
        for _first_ticket in self._pending_tickets.keys():
            for _second_ticket in self._pending_tickets.keys():
                if _first_ticket != _second_ticket:
                    first_ticket = self._pending_tickets[_first_ticket]
                    second_ticket = self._pending_tickets[_second_ticket]
                    if (first_ticket._wishes._wished_side != second_ticket._wishes._wished_side) and \
                            (first_ticket._wishes._wished_time == second_ticket._wishes._wished_time):
                        self._game_pool.start_game(first_ticket, second_ticket)
                        self._game_pool.pop(_first_ticket)
                        self._game_pool.pop(_second_ticket)
                        self._check_pairs()
                        return

    def get_tickets(self):
        return self._pending_tickets.values()

    def change_ticket(self, ticket: Ticket, new_ticket: Ticket):
        if ticket._user.user_id in self._pending_tickets.keys():
            self._pending_tickets[ticket._user.user_id] = new_ticket
            self._check_pairs()

    def add_ticket(self, ticket: Ticket):
        if ticket._user.user_id in self._pending_tickets.keys():
            self._pending_tickets[ticket._user.user_id] = ticket
            self._check_pairs()

    def remove_ticket(self, ticket: Ticket):
        if ticket._user.user_id in self._pending_tickets.keys():
            self._pending_tickets.pop(ticket._user.user_id)

    def __init__(self, game_pool: GamePool):
        self._game_pool = game_pool
        self._pending_tickets = dict()
