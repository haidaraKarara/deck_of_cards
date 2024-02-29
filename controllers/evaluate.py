"""Define the evalution classes."""

from models.card import RANKS, SUITS


class CheckerRankAndSuitIndex:
    """Check rang strategy"""

    def check(self, players):
        """Evaluate the higher card based on the rank/suit"""

        last_player = players[0]
        best_candidate = players[0]

        for player in players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            score = (RANKS.index(player_card.rank), SUITS.index(player_card.suit))
            last_score = (
                RANKS.index(last_player_card.rank),
                SUITS.index(last_player_card.suit),
            )

            if score[0] == last_score[0]:
                if score[1] == last_score[1]:
                    best_candidate = player
            elif score[0] > last_score[0]:
                best_candidate = player

            last_player = player

        return best_candidate.name
