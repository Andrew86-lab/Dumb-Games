# Created by Andrewlab-86, 2/28/25

# Class Definitions for UNOGame and Player go here

import random
import time

class UNOGame:
    def __init__(self, num_players=2):
        self.uno_cards = { 
            "red": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
            "yellow": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
            "green": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
            "blue": {0: 1, **dict.fromkeys(range(1, 10), 2), "skip": 2, "reverse": 2, "draw_two": 2},
            "wild": {"wild": 4, "wild_draw_four": 4},
        }
        
        self.deck = []
        self.discard_pile = []
        self.players = [Player(self, i) for i in range(num_players)]
        self.current_card = None

        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        """Create the deck from the card dictionary."""
        for color, cards in self.uno_cards.items():
            for card, count in cards.items():
                self.deck.extend([(color, card)] * count)

    def shuffle_deck(self):
        """Shuffle the deck and set the first card."""
        random.shuffle(self.deck)
        self.current_card = self.deck.pop()
        self.discard_pile.append(self.current_card)

    def draw_card(self, player):
        """Draw a card for a player."""
        if not self.deck:  # If deck is empty, shuffle discard pile into deck
            print("Deck is empty! Shuffling discard pile back into the deck...")
            top_card = self.discard_pile[-1]  # Keep the top card from the discard pile
            self.deck.extend(self.discard_pile[:-1])  # Add all but the top card
            random.shuffle(self.deck)
            self.discard_pile.clear()  # Clear the discard pile
            self.discard_pile.append(top_card)  # Keep the top card
            print(f"Top card from discard pile is now: {top_card}")
        
        card = self.deck.pop()
        player.hand.append(card)
        print(f"{player.name} drew a card: {card}")
        return card

    def is_valid_play(self, card):
        """Check if a card can be played based on the current card."""
        return card[0] == self.current_card[0] or card[1] == self.current_card[1] or card[0] == "wild"

    def play_turn(self, player):
        """Handle a player's turn."""
        print(f"\n{player.name}'s Turn...")
        print(f"Current card: {self.current_card}")
        print(f"Your hand: {player.hand}")

        valid_choices = [card for card in player.hand if self.is_valid_play(card)]

        if valid_choices:
            card_to_play = player.choose_card(valid_choices)
            player.hand.remove(card_to_play)
            self.current_card = card_to_play
            self.discard_pile.append(card_to_play)
            print(f"{player.name} played: {card_to_play}")

            # Handle special cards (Skip, Reverse, Draw Two, Wild)
            self.handle_special_cards(player, card_to_play)
        else:
            print(f"No valid cards! {player.name} draws a card...")
            self.draw_card(player)

    def handle_special_cards(self, player, card):
        """Handle the effects of special cards."""
        if card[1] == "skip":
            print(f"{player.name} played a Skip! Skipping next player.")
        elif card[1] == "reverse":
            print(f"{player.name} played a Reverse!")
        elif card[1] == "draw_two":
            print(f"{player.name} played Draw Two! The next player draws 2 cards.")
        elif card[1] == "wild":
            chosen_color = player.choose_color()
            self.current_card = (chosen_color, "wild")
            print(f"{player.name} played a Wild card! Chose color {chosen_color}.")
        elif card[1] == "wild_draw_four":
            chosen_color = player.choose_color()
            self.current_card = (chosen_color, "wild_draw_four")
            print(f"{player.name} played Wild Draw Four! Chose color {chosen_color}.")
            # Next player draws 4 cards
            self.draw_card(self.players[(player.id + 1) % len(self.players)])
            self.draw_card(self.players[(player.id + 1) % len(self.players)])

    def play_game(self):
        """Run the game loop."""
        turn = 0
        while True:
            current_player = self.players[turn % len(self.players)]
            self.play_turn(current_player)

            # Check for winner (if any player has no cards left)
            if len(current_player.hand) == 0:
                print(f"\n{current_player.name} has won the game!")
                break

            turn += 1


class Player:
    def __init__(self, game, player_id):
        self.game = game
        self.id = player_id
        self.name = f"Player {player_id + 1}" if player_id == 0 else f"AI {player_id + 1}"
        self.hand = [self.game.draw_card(self) for _ in range(7)]

    def choose_card(self, valid_choices):
        """Choose a card to play (AI or player)."""
        if self.name.startswith("Player"):
            while True:
                try:
                    choice = int(input(f"Choose a card to play (1-{len(valid_choices)}): ")) - 1
                    if 0 <= choice < len(valid_choices):
                        return valid_choices[choice]
                    else:
                        print("Invalid choice. Please choose a valid card.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            # AI chooses a card randomly for now
            return random.choice(valid_choices)

    def choose_color(self):
        """Choose a color for wild cards."""
        while True:
            chosen_color = input("Choose a color (red, yellow, green, blue): ").strip().lower()
            if chosen_color in ["red", "yellow", "green", "blue"]:
                return chosen_color
            print("Invalid color. Please choose a valid color.")


# Start the game
game = UNOGame(num_players=2)  # 2 players (can be increased for more)
game.play_game()
