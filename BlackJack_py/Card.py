CARD_FRONT = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

CARD_BACK = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""

class Card:
    rank_points = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.rank_points[rank]

    def get_name(self):
        return ' '.join([self.rank, 'of', self.suit])

    # def __del__(self):
    #     print(' '.join([self.rank, 'of', self.suit]), ' was removed.')

class Ascii_card(Card):
    def __gen_card_front(self):
        suit_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
        }

        # 10 is the only card with a 2-char rank abbreviation
        rank = self.rank if self.rank == '10' else self.rank[0]
        # add the individual card on a line by line basis
        return CARD_FRONT.format(rank=rank, suit=suit_to_symbol[self.suit])

    def __init__(self, suit, rank):
        Card.__init__(self, suit, rank)
        self.front = self.__gen_card_front()
        self.back = CARD_BACK

    def print_front(self):
        print(self.front)

    def print_back(self):
        print(self.back)
