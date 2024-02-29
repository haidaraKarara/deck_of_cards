"""The main module"""

from controllers.base import Controller
from controllers.base import CheckerRankAndSuitIndex

from views.base import View
from views.player import PlayerView
from views.internet import InternetStreamingView
from views.broadcast import BroadcastView

from models.deck import Deck


def main():
    """The main method"""

    deck = Deck()
    active_view = PlayerView()

    views = (active_view, InternetStreamingView(), BroadcastView())
    view = View(active_view, views)

    checker_strategy = CheckerRankAndSuitIndex()
    game = Controller(deck, view, checker_strategy)
    game.run()


if __name__ == "__main__":
    main()
