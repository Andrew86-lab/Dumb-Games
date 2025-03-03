# Created by Andrewlab-86, 2/28/25

import random
import time

# The UNO card dictionary
uno_cards = { 
    "red": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "yellow": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "green": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "blue": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
    "wild": {"wild": 4, "wild_draw_four": 4},
}

deck = []
discard_pile = []  # This will store cards that have been played

# Create the deck
for color, cards in uno_cards.items():
    for card, count in cards.items():
        deck.extend([(color, card)] * count)

random.shuffle(deck)

# Function to remove a card from the card dictionary
def remove_from_dict(card):
    color, card_type = card
    if uno_cards[color][card_type] > 1:
        uno_cards[color][card_type] -= 1
    else:
        del uno_cards[color][card_type]

# Function to check if a card is valid to play
def is_valid_play(card, current_card):
    return card[0] == current_card[0] or card[1] == current_card[1] or card[0] == "wild"

# Function to draw a card
def draw_card(hand):
    if not deck:  # If deck is empty, shuffle the discard pile back into the deck
        print("Deck is empty! Shuffling discard pile back into the deck...")
        top_card = discard_pile[-1]  # Keep the top card from the discard pile to continue the game
        deck.extend(discard_pile[:-1])  # Add all but the top card to the deck
        random.shuffle(deck)
        discard_pile.clear()  # Clear the discard pile
        discard_pile.append(top_card)  # Put the top card back to be the current card
        print(f"Top card from discard pile is now: {top_card}")

    if deck:
        card = deck.pop()
        remove_from_dict(card)
        hand.append(card)
        return card
    return None

player_hand = [draw_card([]) for _ in range(7)]
ai_hand = [draw_card([]) for _ in range(7)]

# Start the game
current_card = deck.pop()  # Get the first card from the deck
discard_pile.append(current_card)
remove_from_dict(current_card)

def choose_color():
    colors = ["red", "yellow", "green", "blue"]
    while True:
        chosen = input("Choose a color (red, yellow, green, blue): ").strip().lower()
        if chosen in colors:
            return chosen
        print("Invalid choice! Pick a valid color.")

# Player turn logic
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
                    time.sleep(1)  # Adding a delay for smoother gameplay
                    return False  
                elif current_card[1] == "reverse":
                    print("Reverse played! (No effect in 2-player game)")
                elif current_card[1] == "draw_two":
                    print("AI draws 2 cards and skips turn!")
                    for _ in range(2):
                        draw_card(ai_hand)
                    time.sleep(1)
                    return False  
                elif current_card[1] == "wild":
                    current_card = (choose_color(), "wild")
                elif current_card[1] == "wild_draw_four":
                    print("AI draws 4 cards and skips turn!")
                    for _ in range(4):
                        draw_card(ai_hand)
                    current_card = (choose_color(), "wild_draw_four")
                    time.sleep(1)
                    return False  
                return True  
            else:
                print("Invalid choice! Pick a valid card.")
        except ValueError:
            print("Enter a valid number.")

# AI turn logic
def ai_turn(ai_number):
    global current_card
    print(f"\nAI {ai_number}'s Turn...")

    valid_choices = [card for card in ai_hand if is_valid_play(card, current_card)]

    if valid_choices:
        # AI prioritizes special cards first, then plays the lowest-value card.
        special_cards = [card for card in valid_choices if isinstance(card[1], str)]
        normal_cards = [card for card in valid_choices if isinstance(card[1], int)]
        
        ai_choice = None
        
        # Priority 1: Play Draw Two or Wild Draw Four if it's a good time
        if any(card[1] in ["draw_two", "wild_draw_four"] for card in special_cards):
            ai_choice = next(card for card in special_cards if card[1] in ["draw_two", "wild_draw_four"])
        
        # Priority 2: Play Skip or Reverse strategically
        elif any(card[1] in ["skip", "reverse"] for card in special_cards):
            ai_choice = next(card for card in special_cards if card[1] in ["skip", "reverse"])
        
        # Priority 3: Play the lowest number card (excluding Wilds)
        elif normal_cards:
            ai_choice = min(normal_cards, key=lambda card: card[1])
        
        # Priority 4: If no better choice, use Wild card to change color or save it for later
        if not ai_choice and special_cards:
            ai_choice = special_cards[0]  # Use a Wild card if needed

        ai_hand.remove(ai_choice)
        current_card = ai_choice
        print(f"AI {ai_number} played: {current_card}")

        # Handle special cards
        if current_card[1] == "skip":
            print("Next player's turn is skipped!")
            time.sleep(1)
            return False  
        elif current_card[1] == "reverse":
            print("Reverse played! (No effect in 2-player game)")
        elif current_card[1] == "draw_two":
            print("Next player draws 2 cards and skips turn!")
            for _ in range(2):
                draw_card(player_hand)
            time.sleep(1)
            return False  
        elif current_card[1] == "wild":
            chosen_color = random.choice(["red", "yellow", "green", "blue"])
            current_card = (chosen_color, "wild")
            print(f"AI {ai_number} changed color to {chosen_color}")
        elif current_card[1] == "wild_draw_four":
            print("Next player draws 4 cards and skips turn!")
            for _ in range(4):
                draw_card(player_hand)
            chosen_color = random.choice(["red", "yellow", "green", "blue"])
            current_card = (chosen_color, "wild_draw_four")
            print(f"AI {ai_number} changed color to {chosen_color}")
            time.sleep(1)
            return False  
        return True  
    else:
        drawn_card = draw_card(ai_hand)
        print(f"AI {ai_number} had no valid cards and drew a card.")
        time.sleep(1)
        return True

# Game loop
while True:
    # Player turn
    if player_turn():
        # AI turn
        if not ai_turn(1):
            break

    if not player_hand:  # Check if the player has won
        print("You win!")
        break

    if not ai_hand:  # Check if AI has won
        print("AI wins!")
        break
