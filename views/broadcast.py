"""Define the Broadcast view."""

from models.player import Hand


class BroadcastView:
    """Broadcast on TV."""

    def show_player_hand(self, name, hand: "Hand"):
        """Show the player hand"""
        card = hand[0]
        card = card if card.is_face_up else "carte face cachée."
        print(f"[TV] {name} -> {card}")

    def show_winner(self, name):
        """Print the winner"""
        print(f"[TV] {name} a gagné !")
