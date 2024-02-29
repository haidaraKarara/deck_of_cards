"""Define the InternetStreaming view."""

from models.player import Hand


class InternetStreamingView:
    """Stream on internet."""

    def show_player_hand(self, name:str, hand: "Hand"):
        """Show the player hand"""
        card = hand[0]
        card = card if card.is_face_up else "carte face cachée."
        print(f"[Internet] {name} -> {card}")

    def show_winner(self, name):
        """Print the winner"""
        print(f"[Internet] {name} a gagné !")
