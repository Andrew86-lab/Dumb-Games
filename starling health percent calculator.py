import math
import time
print("""This is the Health Calculator.
Enter numbers only unless instructed otherwise.
""")
time.sleep(0.75)

base_max = int(input("Input your character's BASE max health: "))
base_weight = float(input("Input your character's BASE weight in pounds: "))

current_max = base_max
current_weight = base_weight

def percent_finder(weight_change):
    global current_max
    global current_weight
    weight_percent = round(((weight_change + current_weight) / current_weight), 2)
    print(weight_percent)
    current_max = current_max * weight_percent
    current_weight += weight_change
    return current_max
ender = input("How much are you adding to the weight in pounds (negative when subtracting, 'end' when done): ").lower().strip()
print(f"Your base max health is {round(base_max)}.")
print(f"Your base weight is {base_weight} pounds.")
while ender != "end":
    percent_finder(float(ender))
    print(f"Your current max health is now {round(current_max)}.")
    print(f"Your current weight is now {current_weight} pounds.")
    ender = input("How much are you adding to the weight in pounds (negative when subtracting, 'end' when done): ").lower().strip()
