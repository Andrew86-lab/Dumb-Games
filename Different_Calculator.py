import math

def metric_conversion_prompt():
    base_units = ["meter", "liter", "gram"]
    while True:
        base_unit = input("Enter the base unit type (Meter, Liter, Gram): ").strip().lower()
        if base_unit in base_units:
            break
        print("Invalid base unit. Please enter 'Meter', 'Liter', or 'Gram'.")
    
    conversion_type = input("Enter conversion type (metric or imperial): ").strip().lower()
    
    metric_conversion = {
        "yotta": 1e24, "zetta": 1e21, "exa": 1e18, "peta": 1e15, "tera": 1e12, "giga": 1e9, "mega": 1e6, "kilo": 1e3, "hecto": 1e2, "deca": 1e1, "base": 1,
        "deci": 1e-1, "centi": 1e-2, "milli": 1e-3, "micro": 1e-6, "nano": 1e-9, "pico": 1e-12, "femto": 1e-15, "atto": 1e-18, "zepto": 1e-21, "yocto": 1e-24
    }
    
    imperial_conversion = {
        "kg_to_lb": 2.20462, "lb_to_kg": 1 / 2.20462, "g_to_oz": 0.035274, "oz_to_g": 1 / 0.035274,
        "m_to_ft": 3.28084, "ft_to_m": 1 / 3.28084, "cm_to_in": 0.393701, "in_to_cm": 1 / 0.393701,
        "l_to_gal": 0.264172, "gal_to_l": 1 / 0.264172, "ml_to_floz": 0.033814, "floz_to_ml": 1 / 0.033814
    }
    
    if conversion_type == "metric":
        from_prefix = input("Enter the unit you're converting from (e.g., Kilo, Mega, Micro, Milli, Base): ").strip().lower()
        to_prefix = input("Enter the unit you're converting to (e.g., Giga, Centi, Nano, Base): ").strip().lower()
        value = float(input("Enter the value to convert: "))
        
        if from_prefix in metric_conversion and to_prefix in metric_conversion:
            base_value = value * metric_conversion[from_prefix]
            converted_value = base_value / metric_conversion[to_prefix]
            print(f"{value} {from_prefix.capitalize()}{base_unit} is equal to {converted_value} {to_prefix.capitalize()}{base_unit}")
        else:
            print("Invalid unit entered. Please enter a valid metric prefix.")
    
    elif conversion_type == "imperial":
        from_unit = input("Enter the unit you're converting from (e.g., kg, lb, m, ft, cm, in, l, gal): ").strip().lower()
        to_unit = input("Enter the unit you're converting to (e.g., lb, kg, ft, m, in, cm, gal, l): ").strip().lower()
        value = float(input("Enter the value to convert: "))
        
        key = f"{from_unit}_to_{to_unit}"
        if key in imperial_conversion:
            converted_value = value * imperial_conversion[key]
            print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
        else:
            print("Invalid imperial conversion.")
    else:
        print("Invalid conversion type. Please enter 'metric' or 'imperial'.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_volume():
    shapes = {
        "cube", "sphere", "cone", "tetrahedron", "triangular pyramid", "triangular prism", "cuboid", 
        "cylinder", "octahedron", "rectangular pyramid", "ellipsoid", "dodecahedron", "icosahedron", 
        "frustum of a cone", "frustum of a pyramid", "pyramid"
    }
    
    user_shape = input("Enter the 3D shape you want to calculate the volume for: ").strip().lower()
    
    if user_shape not in shapes:
        print("Shape not recognized.")
        return
    
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
    
    print(f"The volume of the {user_shape} is {volume}")

while True:
    print("\nChoose an option:")
    print("1. Metric Unit Conversion")
    print("2. Volume Calculation")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        metric_conversion_prompt()
    elif choice == "2":
        calculate_volume()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")