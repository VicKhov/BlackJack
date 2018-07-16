from random import shuffle

suits = ['Spade', 'Heart ', 'Diamond', 'Club']
ranks = [x for x in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']

def new_deck():
    """Return a new deck of cards."""

    return [[rank, suit] for rank in ranks for suit in suits]

# get new a deck of cards, and randomly shuffle it
deck = new_deck()
shuffle(deck)

player_in = True

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]
