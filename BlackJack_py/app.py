from random import shuffle
from Card import Card, Ascii_card

suits = ['Spade', 'Heart ', 'Diamond', 'Club']
ranks = [str(_) for _ in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']

def new_deck():
    """Returns the deck <list> in which every card
        is an instance of "Card" class."""
    return [Card(rank, suit) for rank in ranks for suit in suits]

# get new a deck of cards, and randomly shuffle it
deck = new_deck()
shuffle(deck)

player_flag = True

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

def hand_value(hand):
    """Returns the integer value of a set of cards."""

    # Sum up all cards in the hand, and then count "Aces".
    hand_sum = sum(card.points for card in hand)
    aces_counter = len([_ for _ in hand if _.rank == 'Ace'])

    while aces_counter > 0:
        if hand_sum > 21 and 'Ace' in ranks:
            hand_sum -= 10
            aces_counter -= 1
        else:
            break

    # Return a string and an integer representing the value of the hand.
    if hand_sum < 21:
        return [str(hand_sum), hand_sum]
    elif hand_sum == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]
