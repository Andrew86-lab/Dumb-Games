import time
print("""This is the Health Calculator.
Enter numbers only unless instructed otherwise.
""")
time.sleep(0.75)

base_max_hp = int(input("Input your character's BASE max health: ").strip())
base_weight = float(input("Input your character's BASE weight in pounds: ").strip())
base_current_hp = int(input("Input your character's current health points: ").strip())

current_max_hp = base_max_hp
current_weight = base_weight
current_hp = base_current_hp

def percent_finder(weight_change):
    global current_max_hp
    global current_weight
    global current_hp
    weight_percent = round(((weight_change + current_weight) / current_weight), 2)
    print(weight_percent)
    current_max_hp = current_max_hp * weight_percent
    current_weight += weight_change
    current_hp = current_hp * weight_percent
    return current_max_hp, current_hp, current_weight
ender = input("How much are you adding to the weight in pounds (negative when subtracting, 'end' when done): ").lower().strip()
print(f"Your base max health is {round(base_max_hp)}.")
print(f"Your base weight is {base_weight} pounds.")
while ender != "end":
    percent_finder(float(ender))
    print(f"Your current max health is now {round(current_max_hp)}.")
    print(f"Your current healh is now {round(current_hp)}.")
    print(f"Your current weight is now {current_weight} pounds.")
    current_hp = int(input("What is your current hp: ").strip())
    ender = input("How much are you adding to the weight in pounds (negative when subtracting, 'end' when done): ").lower().strip()
