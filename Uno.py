# Created by Andrewlab-86, 2/28/25

import random

print("We are going to play a game of UNO ready. Note this is a test so your only going agaisnt 1 AI.")

# there are 108 cards in a deck of UNO cards
# red: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# yellow: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# green: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# blue: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# there are 4 of each for wild cards and draw 4 wild cards
# rules: first person to get rid of all there cards first wins, when game starts each player gets seven cards, if you don't have a card to play you must draw a card from the deck and play it if playable,
# if you don't have any matching cards to play you must draw a card from the deck, if playable play it.

uno_cards = {
    "red": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "yellow": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "green": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "blue": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "wild": {"wild": 4, "wild_draw_four": 4},
}

deck = []
for color, cards in uno_cards.items():
    for card, count in cards.items():
        deck.extend([(color, card)] * count)

def remove_from_dict(card):
    color, card_type = card
    if uno_cards[color][card_type] > 1:
        uno_cards[color][card_type] -= 1
    else:
        del uno_cards[color][card_type]

random.shuffle(deck)

player_hand = [deck.pop() for _ in range(7)]
ai_hand = [deck.pop() for _ in range(7)]

for card in player_hand + ai_hand:
    remove_from_dict(card)

print("Your Hand:")
for card in player_hand:
    print(card)

print("\nAI's Hand: (Hidden)")
print("[Hidden]" for _ in range(7))

print("\nRemaining Cards in UNO Dictionary:")
print(uno_cards)