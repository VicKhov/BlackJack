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

is_playing = True

p_hand = [deck.pop(), deck.pop()]
# let's shuffle again to achieve
shuffle(deck)
d_hand = [deck.pop(), deck.pop()]

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

while is_playing:
    hand_str = '''\nYou are currently at %s\nwith the hand %s\n'''
    current_score = hand_str\
        % (hand_value(p_hand)[0], [_.get_name() for _ in p_hand])

    print(current_score)
    if hand_value(p_hand)[1] == 100:
        break

    if is_playing:
        response = int(input('You gonna hit (=> 1) or stay (=> 0) ?'))
        if response:
            is_playing = True
            new_player_card = deck.pop()
            p_hand.append(new_player_card)
            print('You draw %s' % new_player_card.get_name())
        else:
            is_playing = False

p_score_str, p_score = hand_value(p_hand)
d_score_str, d_score = hand_value(d_hand)

if p_score <= 21:
    print('''\nDealer is at %s\nwith the hand %s\n'''\
        % (d_score_str, [_.get_name() for _ in d_hand]))
else:
    print("Dealer wins.")

while hand_value(d_hand)[1] < 17:
    # let's shuffle the deck one more time!
    shuffle(deck)
    new_dealer_card = deck.pop()
    d_hand.append(new_dealer_card)
    print('Dealer draws %s' % new_dealer_card.get_name())

d_score_str, d_score = hand_value(d_hand)

if p_score < 100 and d_score == 100:
    print('You beat the dealer!')
elif p_score > d_score:
    print('You beat the dealer!')
elif p_score == d_score:
    print('You tied the dealer, nobody wins.')
elif p_score < d_score:
    print('Dealer wins!')
