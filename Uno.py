# Created by Andrewlab-86, 2/28/25

import random

# The UNO card dictionary
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

random.shuffle(deck)

def remove_from_dict(card):
    color, card_type = card
    if uno_cards[color][card_type] > 1:
        uno_cards[color][card_type] -= 1
    else:
        del uno_cards[color][card_type]

def is_valid_play(card, current_card):
    return card[0] == current_card[0] or card[1] == current_card[1] or card[0] == "wild"

def draw_card(hand):
    if deck:
        card = deck.pop()
        remove_from_dict(card)
        hand.append(card)
        return card
    return None

player_hand = [draw_card([]) for _ in range(7)]
ai_hand = [draw_card([]) for _ in range(7)]

while True:
    current_card = deck.pop()
    if current_card[0] != "wild":  
        remove_from_dict(current_card)
        break
    else:
        deck.insert(0, current_card)  

def choose_color():
    colors = ["red", "yellow", "green", "blue"]
    while True:
        chosen = input("Choose a color (red, yellow, green, blue): ").strip().lower()
        if chosen in colors:
            return chosen
        print("Invalid choice! Pick a valid color.")

def player_turn():
    global current_card
    print("\nCurrent Card:", current_card)
    print("Your Hand:")
    for i, card in enumerate(player_hand):
        print(f"{i + 1}: {card}")

    valid_choices = [card for card in player_hand if is_valid_play(card, current_card)]

    if not valid_choices:
        print("No valid cards! Drawing...")
        drawn_card = draw_card(player_hand)
        print(f"You drew: {drawn_card}")
        if is_valid_play(drawn_card, current_card):
            print(f"Playing drawn card: {drawn_card}")
            player_hand.remove(drawn_card)
            current_card = drawn_card
        return True  

    while True:
        try:
            choice = int(input("Choose a card to play: ")) - 1
            if 0 <= choice < len(player_hand) and is_valid_play(player_hand[choice], current_card):
                played_card = player_hand.pop(choice)
                current_card = played_card
                print(f"You played: {current_card}")
                
                # Handle special cards
                if current_card[1] == "skip":
                    print("AI's turn is skipped!")
                    return False  
                elif current_card[1] == "reverse":
                    print("Reverse played! (No effect in 2-player game)")
                elif current_card[1] == "draw_two":
                    print("AI draws 2 cards and skips turn!")
                    for _ in range(2):
                        draw_card(ai_hand)
                    return False  
                elif current_card[1] == "wild":
                    current_card = (choose_color(), "wild")
                elif current_card[1] == "wild_draw_four":
                    print("AI draws 4 cards and skips turn!")
                    for _ in range(4):
                        draw_card(ai_hand)
                    current_card = (choose_color(), "wild_draw_four")
                    return False  
                return True  
            else:
                print("Invalid choice! Pick a valid card.")
        except ValueError:
            print("Enter a valid number.")

def ai_turn():
    global current_card
    print("\nAI's Turn...")

    valid_choices = [card for card in ai_hand if is_valid_play(card, current_card)]

    if valid_choices:
        special_cards = [card for card in valid_choices if isinstance(card[1], str)]
        normal_cards = [card for card in valid_choices if isinstance(card[1], int)]
        ai_choice = special_cards[0] if special_cards else normal_cards[0]
        
        ai_hand.remove(ai_choice)
        current_card = ai_choice
        print(f"AI played: {current_card}")

        if current_card[1] == "skip":
            print("Your turn is skipped!")
            return False  
        elif current_card[1] == "reverse":
            print("Reverse played! (No effect in 2-player game)")
        elif current_card[1] == "draw_two":
            print("You draw 2 cards and skip your turn!")
            for _ in range(2):
                draw_card(player_hand)
            return False  
        elif current_card[1] == "wild":
            chosen_color = random.choice(["red", "yellow", "green", "blue"])
            current_card = (chosen_color, "wild")
            print(f"AI changed color to {chosen_color}")
        elif current_card[1] == "wild_draw_four":
            print("You draw 4 cards and skip your turn!")
            for _ in range(4):
                draw_card(player_hand)
            chosen_color = random.choice(["red", "yellow", "green", "blue"])
            current_card = (chosen_color, "wild_draw_four")
            print(f"AI changed color to {chosen_color}")
            return False  
        return True  

    else:
        drawn_card = draw_card(ai_hand)
        print("AI had no valid cards and drew a card.")
        return True  

while True:
    if player_turn():
        if not player_hand:
            print("\n🎉 You win! 🎉")
            break
    else:
        continue  

    if ai_turn():
        if not ai_hand:
            print("\n🤖 AI wins! 🤖")
            break