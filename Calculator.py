import math

def get_user_input():
    while True:
        try:
            user_input = int(input("What do you want? 1 for Multiply, 2 for Divide, 3 for Add and Subtract, 4 for Square, 5 for Square Root, or 6 for Exponentiate? "))
            if user_input in range(1, 7):
                return user_input
            else:
                print("Please enter a number between 1 and 6")
        except ValueError:
            print("Please enter a number instead of a letter or word, please make it a whole number.")
        
user_input = get_user_input()

def mutliply(user_input):
    if user_input == 1:
        while True:
            try:     
                num1 = input("Enter the numbers you want to multiply: ").split()
                if not num1:
                    print("Please enter a number.")
                    continue
                
                num1 = list(map(float, num1))
                result = (math.prod(num1))
                print(f"The answer is {result}")
                break
            except ValueError:
                print("Please enter a number instead of a letter or a word.")

mutliply(user_input)

def divide(user_input):
    if user_input == 2:
        while True:
            try:
                num1 = input("Enter the numbers you want to divide: ").split()
                if not num1:
                    print("Please enter a number.")
                    continue
                
                num1 = list(map(float, num1))
                first_number = num1.pop(0)
                for x in num1:
                    if x == 0:
                        print("You cannot divide by zero.")
                        break
                    first_number /=  x
                else:
                    print(f"The answer is {first_number}")
                    break
            except ValueError:
                print("Please enter a number instead of a letter or a word.")

divide(user_input)

def add_subtract(user_input):
    if user_input == 3:
        while True:
            try:
                num1 = input("Enter the numbers you want to add or subract: ").split()
                if not num1:
                    print("Please enter a number.")
                    continue
                
                num1 = list(map(float, num1))
                result = sum(num1)
                print(f"The answer is {result}")
                break
            except ValueError:
                print("Please enter a number instead of a letter or a word.")

add_subtract(user_input)

def square(user_input):
    if user_input == 4:
        while True:
            try:
                num1 = input("Enter the number you want to square: ")
                if not num1:
                    print("Please enter a number.")
                    continue
                
                sqrt = input("Do you want to squiare by? ")
                if not sqrt:
                    print("Please enter a number.")
                    continue
                
                num1 = float(num1)
                sqrt = float(sqrt)
                result = num1 ** sqrt
                print(f"The answer is {result}")
                break
            except ValueError:
                print("Please enter a number instead of a letter or word.")

square(user_input)