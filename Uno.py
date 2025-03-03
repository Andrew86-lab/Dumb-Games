# Created by Andrewlab-86, 2/28/25

print("We are going to play a game of UNO ready.")

# there are 108 cards in a deck of UNO cards
# red: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# yellow: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# green: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# blue: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, ,2 , 3, 4, 5, 6, 7, 8, 9, 2 of each for skip, reverse, draw two
# there are 4 of each for wild cards and draw 4 wild cards
# rules: first person to get rid of there cards first wins

uno_cards = {
    "red": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "yellow": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "green": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "blue": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "wild": {"wild": 4, "wild_draw_four": 4},
}