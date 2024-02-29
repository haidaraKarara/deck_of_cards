"""The main controller"""

from typing import List
from models.deck import Deck
from models.player import Player

from views.base import View

from controllers.evaluate import CheckerRankAndSuitIndex


class Controller:
    def __init__(
        self, deck: "Deck", view: "View", checker_strategy: "CheckerRankAndSuitIndex"
    ):
        # models
        self.players: List[Player] = []
        self.deck = deck

        # view
        self.view = view

        self.checker_strategy = checker_strategy

    def get_players(self):
        while len(self.players) < 2:
            name = self.view.prompt_for_player()
            if not name:
                return None
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def rebuild_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)

        self.deck.shuffle()

    def evaluate_game(self):
        """Evaluate the score between gamers and print the winner"""
        return self.checker_strategy.check(self.players)

    def run(self):
        self.get_players()

        running = True
        while running:
            self.start_game()
            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)
            self.view.prompt_for_flip_card()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True

                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            self.rebuild_deck()
