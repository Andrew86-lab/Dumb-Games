#Created by Kai Reinhold (kaireinhold on GitHub)

import math

lbs_weight = float(input("Enter your character's weight in pounds (NUMBERS ONLY): "))

volume = round(lbs_weight * 0.00045, 4)
mass = round(lbs_weight / 2.205, 2)
density = round(mass / volume, 4)
print("V:", volume, "m^3")
print("M:", mass, "kg")
print("D:", density, "kg/m^3")
