"""Deck module"""

from collections import UserList
from random import shuffle as random_shuffle
from typing import List

from .card import Card, RANKS, SUITS


class Deck(UserList):
    """Deck of cards"""

    def __init__(self, data_cards: "List[Card]" = None):

        if data_cards is not None:
            super().__init__(data_cards)
            # self.data = data
        else:
            self.data_cards = []

            for rank in RANKS:
                for suit in SUITS:
                    card = Card(suit, rank)
                    self.data_cards.append(card)

            super().__init__(self.data_cards)
            self.shuffle()

    def shuffle(self):
        """Shuffle the cards"""
        random_shuffle(self.data)

    def draw_card(self):
        """A draw of cards"""
        try:
            return self.data.pop()
        except IndexError:
            return None
