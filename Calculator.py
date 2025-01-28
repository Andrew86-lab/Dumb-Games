import math

while True:
    def get_user_input():
        while True:
            try:
                user_input = int(input("What do you want? 1 for Multiply, 2 for Divide, 3 for Add and Subtract, 4 for exponentiate, 5 for Square Root: "))
                if 1 <= user_input <= 5:
                    return user_input
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")

    def get_numbers(prompt):
        while True:
            try:
                numbers = input(prompt).split()
                if not numbers:
                    print("Please enter at least one number.")
                    continue
                return list(map(float, numbers))
            except ValueError:
                print("Please enter valid numbers.")

    def multiply():
        numbers = get_numbers("Enter the numbers you want to multiply: ")
        result = math.prod(numbers)
        print(f"The answer is {result}")

    def divide():
        numbers = get_numbers("Enter the numbers you want to divide: ")
        first_number = numbers.pop(0)
        try:
            for x in numbers:
                if x == 0:
                    raise ValueError("Cannot divide by zero.")
                first_number /= x
            print(f"The answer is {first_number}")
        except ValueError as e:
            print(e)

    def add_subtract():
        numbers = get_numbers("Enter the numbers you want to add or subtract: ")
        result = sum(numbers)
        print(f"The answer is {result}")

    def exponentiate():
        while True:
            try:
                num1 = float(input("Enter the number you want to square: "))
                exponent = float(input("Enter the exponent (default is 2 for squaring): ") or 2)
                result = num1 ** exponent
                print(f"The answer is {result}")
                break
            except ValueError:
                print("Please enter valid numbers.")

    def square_root():
        while True:
            try:
                num1 = float(input("Enter the number you want to square root: "))
                result = math.sqrt(num1)
                print(f"The answer is {result}")
                break
            except ValueError:
                print("Please enter a valid number.")

    def main():
        user_input = get_user_input()

        if user_input == 1:
            multiply()
        elif user_input == 2:
            divide()
        elif user_input == 3:
            add_subtract()
        elif user_input == 4:
            exponentiate()
        elif user_input == 5:
            square_root()

    if __name__ == "__main__":
        main()
