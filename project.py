import math

try:
    user_input = int(input("What do you want? 1 for Multiply, 2 for Divide, Add, 3 for Subtract, 4 for Square, 5 for Square Root, or 6 for Exponentiate? "))
except ValueError:
    print("Please enter a number instead of a letter or word and whole numbers.")
    user_input = int(input("What do you want? 1 for Multiply, 2 for Divide, Add, 3 for Subtract, 4 for Square, 5 for Square Root, or 6 for Exponentiate? "))

if user_input == 1:
    num1 = list(map(int, input("Enter the numbers you want to multiply: ").split()))
    num1 = int(math.prod(num1))
    print(num1)