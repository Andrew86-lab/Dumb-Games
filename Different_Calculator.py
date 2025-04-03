import math

metric_conversion = {
    "Kilo" : .001,
    "Hecto" : .01,
    "Deca" : .1,
    "Base" : 1,
    "Deci" : 10,
    "Centi" : 100,
    "Milli" : 1000
}

base_unit = input("Enter the base unit (e.g., Meter, Liter, Gram): ").split().lower()

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

shapes = {
    "cube", "sphere", "cone", "tetrahedron", "triangular pyramid", "triangular prism", "cuboid", 
    "cylinder", "octahedron", "rectangular pyramid", "ellipsoid", "dodecahedron", "icosahedron", 
    "frustum of a cone", "frustum of a pyramid", "pyramid"
}

user_shape = input("Enter the 3D shape you want to calculate the volume for: ").strip().lower()

if user_shape not in shapes:
    print("Shape not recognized.")
    exit()

if user_shape == "cube":
    side = get_float("Enter the length of a side: ")
    volume = side ** 3
elif user_shape == "sphere":
    radius = get_float("Enter the radius: ")
    volume = (4/3) * math.pi * radius ** 3
elif user_shape == "cone":
    radius = get_float("Enter the radius: ")
    height = get_float("Enter the height: ")
    volume = (1/3) * math.pi * radius ** 2 * height
elif user_shape == "tetrahedron":
    side = get_float("Enter the length of a side: ")
    volume = (side ** 3) / (6 * math.sqrt(2))
elif user_shape in {"triangular pyramid", "rectangular pyramid", "pyramid"}:
    base_area = get_float("Enter the area of the base: ")
    height = get_float("Enter the height: ")
    volume = (1/3) * base_area * height
elif user_shape == "triangular prism":
    base_area = get_float("Enter the area of the base: ")
    height = get_float("Enter the height: ")
    volume = base_area * height
elif user_shape == "cuboid":
    length = get_float("Enter the length: ")
    width = get_float("Enter the width: ")
    height = get_float("Enter the height: ")
    volume = length * width * height
elif user_shape == "cylinder":
    radius = get_float("Enter the radius: ")
    height = get_float("Enter the height: ")
    volume = math.pi * radius ** 2 * height
elif user_shape == "octahedron":
    side = get_float("Enter the length of a side: ")
    volume = (math.sqrt(2) / 3) * side ** 3
elif user_shape == "ellipsoid":
    a = get_float("Enter the semi-major axis (a): ")
    b = get_float("Enter the first semi-minor axis (b): ")
    c = get_float("Enter the second semi-minor axis (c): ")
    volume = (4/3) * math.pi * a * b * c
elif user_shape == "dodecahedron":
    side = get_float("Enter the length of a side: ")
    volume = ((15 + 7 * math.sqrt(5)) / 4) * side ** 3
elif user_shape == "icosahedron":
    side = get_float("Enter the length of a side: ")
    volume = (5 * (3 + math.sqrt(5)) / 12) * side ** 3
elif user_shape == "frustum of a cone":
    radius1 = get_float("Enter the radius of the bottom base: ")
    radius2 = get_float("Enter the radius of the top base: ")
    height = get_float("Enter the height: ")
    volume = (1/3) * math.pi * height * (radius1 ** 2 + radius1 * radius2 + radius2 ** 2)
elif user_shape == "frustum of a pyramid":
    base_area1 = get_float("Enter the area of the bottom base: ")
    base_area2 = get_float("Enter the area of the top base: ")
    height = get_float("Enter the height: ")
    volume = (1/3) * height * (base_area1 + base_area2 + math.sqrt(base_area1 * base_area2))

print(f"The volume of the {user_shape} is {volume}")
