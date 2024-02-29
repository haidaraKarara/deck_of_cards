"""The base view."""

from views.player import PlayerView
from models.player import Hand

class View:
    """The base view"""
    
    def __init__(self, active_view: "PlayerView", views:list):
        """Init the active view and the passives views"""
        self.active_view = active_view
        self.views = views
    
    def prompt_for_player(self):
        """Call the active view."""
        return self.active_view.prompt_for_player()
    
    def prompt_for_flip_card(self):
        """Call the active view."""
        return self.active_view.prompt_for_flip_card()
    
    def prompt_for_new_game(self):
        """Call the active view."""
        self.active_view.prompt_for_new_game()

    
    def show_player_hand(self, name:str, hand: "Hand"):
        """Call the passives views."""
        for view in self.views:
            view.show_player_hand(name, hand)
    
    
    def show_winner(self, name:str):
        """Call the passives views."""
        for view in self.views:
            view.show_winner(name)
        
    
        