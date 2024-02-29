"""Module Player"""


from collections import UserList
from typing import List

from .card import Card

class Hand(UserList):
    """The hand of the player"""

    def __init__(self, other: "List[Card]" = None):

        if other is None:
            super().__init__()
        elif isinstance(other, list):
            check_list_card = [isinstance(x, Card) for x in other]
            if False in check_list_card:
                raise ValueError(
                    "Only objects of type Card is accepted, please check your objects list !"
                )
            else:
                super().__init__(other)
        else:
            raise ValueError("Only List objects of <Card> is accepted !")

    def append(self, item: "Card"):
        """Append new card"""

        if isinstance(item, Card):
            self.data.append(item)
        else:
            raise ValueError("You can only add a Card object !")

    def extend(self, other):
        """Extend an existing list of cards"""

        if isinstance(other, Card):
            self.data.extend(other)
        elif isinstance(other, list):
            check_list_card = [isinstance(x, Card) for x in other]
            if False in check_list_card:
                raise ValueError("Only objects of type Card is accepted !")
            else:
                self.data.extend(other)
        else:
            raise ValueError("Only objects of type Card is accepted !")

class Player:

    def __init__(self, name, hand: "List[Hand]" = None):
        self.name = name
        self.hand = hand or Hand()

    """ def __str__(self):
        return f"List cards of {self.name}: {self.hand}"

    def __repr__(self):
        return str(self) """