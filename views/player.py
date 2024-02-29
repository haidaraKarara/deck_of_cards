"""The Player view."""


from models.player import Hand


class PlayerView:
    """Player view."""

    def prompt_for_player(self):
        name = input("Tapez le nom du joueur : ")
        if not name:
            return None
        return name

    def show_player_hand(self, name: str, hand: "Hand"):
        """Show the player hand"""
        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")

    def prompt_for_flip_card(self):
        print()
        input("Prêt à retourner les cartes ?")
        return True

    def show_winner(self, name: str):
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        print("Souhaitez-vous refaire une autre partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False

        return True
