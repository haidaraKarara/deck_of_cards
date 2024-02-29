SUITS = (
    "diamonds",
    "coeurs",
    "piques",
    "carreaux",
)
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return str(self)
