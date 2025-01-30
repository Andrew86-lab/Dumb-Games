#Created by Kai Reinhold (kaireinhold on GitHub)

import math

lbs_weight = float(input("Enter your character's weight in pounds (NUMBERS ONLY): "))

volume = lbs_weight * 0.00045
mass = lbs_weight * 0.453592  # This turns it into pounds from Kilograms, you already made sure the enterd there weight in pounds.
density = math.ceil(mass / volume)
print("V:", volume, "m^3")
print("M:", mass, "kg")
print("D:", density, "kg/m^3")
