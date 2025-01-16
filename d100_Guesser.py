#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import sys
import math

play = False

def roll(di=None):

    if di == None:
        dice_chosen = input("What dice would you like to roll? (d[number] ")
    else:
        dice_chosen = di
    dice_list = dice_chosen.lower().split()
    an_list = [11, 18,]
    for x in dice_list:
        if "d" not in x:
            raise ValueError("Value must have a 'd' in front to specify that it is a dice")
        roll_num = int(x[1:len(x)])
        roll_output = random.randint(1,roll_num)
        output_str = str(roll_output)
        return rolls.append(roll_output)

while True:
    rolls = []
    start = input("Start? (y/n) ").lower().strip()
    if start == "y":
        version = input("""Which version do you want to play?
(1) Roll until 1 is rolled
(2) Roll until 1 or a duplicate is rolled
""")
        player_1 = int(input("How many rolls do you think there will be, Player 1? "))
        player_2 = int(input("How many rolls do you think there will be, Player 2? "))
        dice_to_roll = input("What type of dice would you like to roll for this game? (ex: d100, d20, d6) ")
        if version == "2":
            duplicates = input("How many duplicates do you want to allow? (Greater than 1) ")
        play = True
    else:
        play = False
        sys.exit()
    
    while play == True:
            roll(dice_to_roll)
            if version == "1":
                if rolls[-1] == 1:
                    if math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_1, len(rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    elif math.isclose(player_2, len(rolls), abs_tol = 10) == True and math.isclose(player_1, len(rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    elif math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_2, len(rolls), abs_tol = 10) == True:
                        print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    else:
                        if abs(player_1 - len(rolls)) < abs(player_2 - len(rolls)):
                            print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif abs(player_2 - len(rolls)) < abs(player_1 - len(rolls)):
                            print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif abs(player_1 - len(rolls)) == abs(player_2 - len(rolls)):
                            print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                    break
            elif version == "2":
                if rolls[-1] == 1:
                    if math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_2, len(rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    elif math.isclose(player_2, len(rolls), abs_tol = 10) == True and math.isclose(player_1, len(rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    elif math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_2, len(rolls), abs_tol = 10) == True:
                        print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                        print(rolls)
                    else:
                        if abs(player_1 - len(rolls)) < abs(player_2 - len(rolls)):
                            print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif abs(player_2 - len(rolls)) < abs(player_1 - len(rolls)):
                            print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif abs(player_1 - len(rolls)) == abs(player_2 - len(rolls)):
                            print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                    break
                elif rolls[-1] in rolls[0:-1]:
                    if rolls.count(rolls[-1]) >= int(duplicates):
                        if math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_2, len(rolls), abs_tol = 10) == False:
                            print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif math.isclose(player_2, len(rolls), abs_tol = 10) == True and math.isclose(player_1, len(rolls), abs_tol = 10) == False:
                            print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        elif math.isclose(player_1, len(rolls), abs_tol = 10) == True and math.isclose(player_2, len(rolls), abs_tol = 10) == True:
                            print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                            print(rolls)
                        else:
                            if abs(player_1 - len(rolls)) < abs(player_2 - len(rolls)):
                                print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                                print(rolls)
                            elif abs(player_1 - len(rolls)) < abs(player_1 - len(rolls)):
                                print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                                print(rolls)
                            elif abs(player_1 - len(rolls)) == abs(player_2 - len(rolls)):
                                print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(rolls)}!")
                                print(rolls)
                    else:
                        continue
                    break
