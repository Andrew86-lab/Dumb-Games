import math

metric_prefixes = {
    "yotta": 1e24, "zetta": 1e21, "exa": 1e18, "peta": 1e15,
    "tera": 1e12, "giga": 1e9, "mega": 1e6, "kilo": 1e3,
    "hecto": 1e2, "deca": 1e1, "base": 1,
    "deci": 1e-1, "centi": 1e-2, "milli": 1e-3, "micro": 1e-6,
    "nano": 1e-9, "pico": 1e-12, "femto": 1e-15, "atto": 1e-18,
    "zepto": 1e-21, "yocto": 1e-24
}

def convert_metric_with_prefix(value, from_prefix: str, to_prefix: str):
    try:
        base_value = value * metric_prefixes[from_prefix]
        return base_value / metric_prefixes[to_prefix]
    except KeyError:
        raise ValueError(f"Invalid metric prefix: {from_prefix} or {to_prefix}")

imperial_conversion_weight = {
    "kg_to_lb": 2.20462, "lb_to_kg": 1 / 2.20462,
    "g_to_oz": 0.035274, "oz_to_g": 1 / 0.035274,
    "mg_to_grain": 0.0154324, "grain_to_mg": 1 / 0.0154324,
    "g_to_grain": 15.4324, "grain_to_g": 1 / 15.4324,
    "kg_to_stone": 0.157473, "stone_to_kg": 1 / 0.157473,
    "lb_to_oz": 16, "oz_to_lb": 1 / 16,
    "stone_to_lb": 14, "lb_to_stone": 1 / 14,
    "ton_to_lb": 2000, "lb_to_ton": 1 / 2000,
    "kg_to_g": 1000, "g_to_kg": 1 / 1000,
    "g_to_mg": 1000, "mg_to_g": 1 / 1000,
    "kg_to_mg": 1_000_000, "mg_to_kg": 1 / 1_000_000
}

def convert_weight(value, from_unit: str, to_unit: str):
    key = f"{from_unit}_to_{to_unit}"
    reverse_key = f"{to_unit}_to_{from_unit}"
    if key in imperial_conversion_weight:
        return value * imperial_conversion_weight[key]
    elif reverse_key in imperial_conversion_weight:
        return value / imperial_conversion_weight[reverse_key]
    raise ValueError(f"Unsupported weight conversion from '{from_unit}' to '{to_unit}'.")

imperial_conversion_length = {
    "m_to_ft": 3.28084, "ft_to_m": 1 / 3.28084,
    "cm_to_in": 0.393701, "in_to_cm": 1 / 0.393701,
    "km_to_mile": 0.621371, "mile_to_km": 1 / 0.621371,
    "mm_to_in": 0.0393701, "in_to_mm": 1 / 0.0393701,
    "km_to_m": 1000, "m_to_km": 1 / 1000,
    "m_to_cm": 100, "cm_to_m": 1 / 100,
    "cm_to_mm": 10, "mm_to_cm": 1 / 10,
    "m_to_mm": 1000, "mm_to_m": 1 / 1000,
    "mile_to_yd": 1760, "yd_to_mile": 1 / 1760,
    "yd_to_ft": 3, "ft_to_yd": 1 / 3,
    "ft_to_in": 12, "in_to_ft": 1 / 12
}

def convert_length(value, from_unit: str, to_unit: str):
    key = f"{from_unit}_to_{to_unit}"
    reverse_key = f"{to_unit}_to_{from_unit}"
    if key in imperial_conversion_length:
        return value * imperial_conversion_length[key]
    elif reverse_key in imperial_conversion_length:
        return value / imperial_conversion_length[reverse_key]
    raise ValueError(f"Unsupported length conversion from '{from_unit}' to '{to_unit}'.")

imperial_conversion_volume = {
    "l_to_gal": 0.264172, "gal_to_l": 1 / 0.264172,
    "ml_to_floz": 0.033814, "floz_to_ml": 1 / 0.033814,
    "l_to_ml": 1000, "ml_to_l": 1 / 1000,
    "gal_to_qt": 4, "qt_to_gal": 1 / 4,
    "qt_to_pint": 2, "pint_to_qt": 1 / 2,
    "pint_to_cup": 2, "cup_to_pint": 1 / 2,
    "cup_to_floz": 8, "floz_to_cup": 1 / 8
}

imperial_conversion_volume = {
    # Metric ↔ US Imperial
    "l_to_gal": 0.264172, "gal_to_l": 1 / 0.264172,
    "ml_to_floz": 0.033814, "floz_to_ml": 1 / 0.033814,
    "l_to_ml": 1000, "ml_to_l": 1 / 1000,

    # Larger Imperial Conversions
    "gal_to_qt": 4, "qt_to_gal": 1 / 4,
    "qt_to_pint": 2, "pint_to_qt": 1 / 2,
    "pint_to_cup": 2, "cup_to_pint": 1 / 2,
    "cup_to_floz": 8, "floz_to_cup": 1 / 8,

    # Fluid Ounce ↔ Tablespoon ↔ Teaspoon (US)
    "floz_to_tbsp": 2, "tbsp_to_floz": 1 / 2,
    "tbsp_to_tsp": 3, "tsp_to_tbsp": 1 / 3,
    "floz_to_tsp": 6, "tsp_to_floz": 1 / 6,

    # Metric ↔ Teaspoon/Tablespoon (US standard)
    "ml_to_tsp": 0.202884, "tsp_to_ml": 1 / 0.202884,
    "ml_to_tbsp": 0.067628, "tbsp_to_ml": 1 / 0.067628
}

def convert_time(value, from_unit: str, to_unit: str):
    time_conversion = {
        "second_to_minute": 1 / 60, "minute_to_second": 60,
        "minute_to_hour": 1 / 60, "hour_to_minute": 60,
        "hour_to_day": 1 / 24, "day_to_hour": 24,
        "day_to_week": 1 / 7, "week_to_day": 7,
        "week_to_month": 1 / 4.345, "month_to_week": 4.345,
        "month_to_year": 1 / 12, "year_to_month": 12
    }
    key = f"{from_unit}_to_{to_unit}"
    reverse_key = f"{to_unit}_to_{from_unit}"
    if key in time_conversion:
        return value * time_conversion[key]
    elif reverse_key in time_conversion:
        return value / time_conversion[reverse_key]
    raise ValueError(f"Unsupported time conversion from '{from_unit}' to '{to_unit}'.")

def celsius_to_fahrenheit(c): return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f): return (f - 32) * 5 / 9

def celsius_to_kelvin(c): return c + 273.15

def kelvin_to_celsius(k): return k - 273.15

def fahrenheit_to_kelvin(f): return (f - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(k): return (k - 273.15) * 9 / 5 + 32

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
    print("1. Metric Prefix Conversion")
    print("2. Volume Calculation")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        from_prefix = input("Enter the unit you're converting from (e.g., kilo, milli, base): ").strip().lower()
        to_prefix = input("Enter the unit you're converting to (e.g., mega, micro, base): ").strip().lower()
        value = get_float("Enter the value to convert: ")

        try:
            converted = convert_metric_with_prefix(value, from_prefix, to_prefix)
            print(f"{value} {from_prefix} is equal to {converted} {to_prefix}")
        except ValueError as e:
            print(e)
    elif choice == "2":
        calculate_volume()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")