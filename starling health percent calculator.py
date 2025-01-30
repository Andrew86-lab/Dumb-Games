import math
print("this is the health calculator")
base_max = int(input("input your characters BASE max health "))
base_weight = float(input("input your characters BASE weight in pounds (only type numbers) "))

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
ender = input("how much are you adding to the weight in pounds (only type numbers input a negative when subtracting  ...  input end when done) ")
while ender != "end":
    percent_finder(float(ender))
    print("your base max health is ", base_max )
    print("your base weight is ", base_weight)
    print("your current max health is now", current_max)
    print("your current weight is now ", current_weight)
    ender = input("how much are you adding to the weight in pounds (only type numbers input a negative when subtracting  ...  input end when done) ")
