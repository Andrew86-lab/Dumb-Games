import random

rolls = int(input("How mny times do you want to roll? The dice is out of 20: "))

while rolls > 0:
    number = random.randint(1, 20)
    print(f"Your roll was {number} {rolls}")
    rolls -= 1