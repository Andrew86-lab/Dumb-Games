imperial_conversion_mass = {
    "kg_to_g": 1000, "g_to_kg": 1 / 1000,
    "kg_to_mg": 1e6, "mg_to_kg": 1 / 1e6,
    "kg_to_tonne": 1 / 1000, "tonne_to_kg": 1000,
    "kg_to_microgram": 1e9, "microgram_to_kg": 1 / 1e9,
    "kg_to_imperial_ton": 1 / 1016, "imperial_ton_to_kg": 1016,
    "kg_to_ton": 1 / 907.18474, "ton_to_kg": 907.18474,
    "kg_to_stone": 1 / 6.35029, "stone_to_kg": 6.35029,
    "kg_to_lb": 2.20462, "lb_to_kg": 1 / 2.20462,
    "kg_to_oz": 35.274, "oz_to_kg": 1 / 35.274,

    "g_to_tonne": 1 / 1e6, "tonne_to_g": 1e6,
    "g_to_mg": 1000, "mg_to_g": 1 / 1000,
    "g_to_microgram": 1e6, "microgram_to_g": 1 / 1e6,
    "g_to_imperial_ton": 1 / 1.016e6, "imperial_ton_to_g": 1.016e6,
    "g_to_ton": 1 / 907184.74, "ton_to_g": 907184.74,
    "g_to_stone": 1 / 6350.29, "stone_to_g": 6350.29,
    "g_to_lb": 1 / 453.592, "lb_to_g": 453.592,
    "g_to_oz": 1 / 28.3495, "oz_to_g": 28.3495,

    "mg_to_tonne": 1 / 1e9, "tonne_to_mg": 1e9,
    "mg_to_microgram": 1000, "microgram_to_mg": 1 / 1000,
    "mg_to_imperial_ton": 1 / 1.016e9, "imperial_ton_to_mg": 1.016e9,
    "mg_to_ton": 1 / 9.0718474e8, "ton_to_mg": 9.0718474e8,
    "mg_to_stone": 1 / 6.35029e6, "stone_to_mg": 6.35029e6,
    "mg_to_lb": 1 / 453592, "lb_to_mg": 453592,
    "mg_to_oz": 1 / 28349.5, "oz_to_mg": 28349.5,

    "microgram_to_tonne": 1 / 1e12, "tonne_to_microgram": 1e12,
    "microgram_to_imperial_ton": 1 / 1.016e12, "imperial_ton_to_microgram": 1.016e12,
    "microgram_to_ton": 1 / 9.0718474e11, "ton_to_microgram": 9.0718474e11,
    "microgram_to_stone": 1 / 6.35029e9, "stone_to_microgram": 6.35029e9,
    "microgram_to_lb": 1 / 4.53592e8, "lb_to_microgram": 4.53592e8,
    "microgram_to_oz": 1 / 2.83495e7, "oz_to_microgram": 2.83495e7,

    "imperial_ton_to_tonne": 1.016, "tonne_to_imperial_ton": 1 / 1.016,
    "imperial_ton_to_ton": 1.12, "ton_to_imperial_ton": 1 / 1.12,
    "imperial_ton_to_stone": 160, "stone_to_imperial_ton": 1 / 160,
    "imperial_ton_to_lb": 2240, "lb_to_imperial_ton": 1 / 2240,
    "imperial_ton_to_oz": 35840, "oz_to_imperial_ton": 1 / 35840,

    "ton_to_tonne": 0.90718474, "tonne_to_ton": 1 / 0.90718474,
    "ton_to_stone": 142.857, "stone_to_ton": 1 / 142.857,
    "ton_to_lb": 2000, "lb_to_ton": 1 / 2000,
    "ton_to_oz": 32000, "oz_to_ton": 1 / 32000,

    "stone_to_tonne": 1 / 157.473, "tonne_to_stone": 157.473,
    "stone_to_lb": 14, "lb_to_stone": 1 / 14,
    "stone_to_oz": 224, "oz_to_stone": 1 / 224,

    "lb_to_tonne": 1 / 2204.62, "tonne_to_lb": 2204.62,
    "lb_to_oz": 16, "oz_to_lb": 1 / 16,

    "oz_to_tonne": 1 / 35274, "tonne_to_oz": 35274
}

unit_aliases = {
    "grams": "g", "gram": "g", "g": "g",
    "kilograms": "kg", "kilogram": "kg", "kgs": "kg", "kg": "kg",
    "milligrams": "mg", "milligram": "mg", "mg": "mg",
    "micrograms": "microgram", "microgram": "microgram",
    "tonnes": "tonne", "tonne": "tonne",
    "tons": "ton", "ton": "ton",
    "imperial_tons": "imperial_ton", "imperial_ton": "imperial_ton",
    "stones": "stone", "stone": "stone",
    "pounds": "lb", "pound": "lb", "lbs": "lb", "lb": "lb",
    "ounces": "oz", "ounce": "oz", "oz": "oz"
}

while True:
    try:
        units = input("Enter the units to convert from and to (e.g., 'kg g' or 'kilograms to grams'): ").strip().lower().split()
        if len(units) != 2:
            raise ValueError("Please enter exactly two units separated by a space (e.g., 'kg g').")
        
        from_unit_raw, to_unit_raw = units

        from_unit = unit_aliases.get(from_unit_raw)
        to_unit = unit_aliases.get(to_unit_raw)

        if not from_unit or not to_unit:
            raise KeyError(f"Could not recognize unit(s): '{from_unit_raw}' or '{to_unit_raw}'.")

        conversion_key = f"{from_unit}_to_{to_unit}"

        if conversion_key not in imperial_conversion_mass:
            raise KeyError(f"Conversion '{conversion_key}' not found.")

        user_number_input = float(input(f"Enter the number of {from_unit_raw} to convert: ").strip())
        if user_number_input <= 0:
            raise ValueError("Number must be greater than zero.")

        conversion = user_number_input * imperial_conversion_mass[conversion_key]
        print(f"{user_number_input} {from_unit_raw} = {conversion} {to_unit_raw}")

        again = input("Would you like to convert another value? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for using the converter! Goodbye.")
            break

    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except KeyError as ke:
        print(f"Conversion error: {ke}")

imperial_conversion_length = {
    "km_to_m": 1000, "m_to_km": 1 / 1000,
    "km_to_cm": 100000, "cm_to_km": 1 / 100000,
    "km_to_mm": 1e6, "mm_to_km": 1 / 1e6,
    "km_to_micrometer": 1e9, "micrometer_to_km": 1 / 1e9,
    "km_to_nanometer": 1e12, "nanometer_to_km": 1 / 1e12,
    "km_to_mi": 1 / 1.609, "mi_to_km": 1.609,
    "km_to_yd": 1094, "yd_to_km": 1 / 1094,
    "km_to_ft": 3281, "ft_to_km": 1 / 3281,
    "km_to_in": 39370, "in_to_km": 1 / 39370,
    "km_to_nautical_mile": 1 / 1.852, "nautical_mile_to_km": 1.852,

    "m_to_cm": 100, "cm_to_m": 1 / 100,
    "m_to_mm": 1000, "mm_to_m": 1 / 1000,
    "m_to_micrometer": 1e6, "micrometer_to_m": 1 / 1e6,
    "m_to_nanometer": 1e9, "nanometer_to_m": 1 / 1e9,
    "m_to_mi": 1 / 1609.34, "mi_to_m": 1609.34,
    "m_to_yd": 1.094, "yd_to_m": 1 / 1.094,
    "m_to_ft": 3.281, "ft_to_m": 1 / 3.281,
    "m_to_in": 39.37, "in_to_m": 1 / 39.37,
    "m_to_nautical_mile": 1 / 1852, "nautical_meter_to_m": 1852,

    "cm_to_mm": 10, "mm_to_cm": 1 / 10,
    "cm_to_micrometer": 1e4, "micrometer_to_cm": 1 / 1e4,
    "cm_to_nanometer": 1e7, "nanometer_to_cm": 1 / 1e7,
    "cm_to_mi": 1 / 160934, "mi_to_cm": 160934,
    "cm_to_yd": 1 / 91.44, "yd_to_cm": 91.44,
    "cm_to_ft": 1 / 30.48, "ft_to_cm": 30.48,
    "cm_to_in": 1 / 2.54, "in_to_cm": 2.54,
    "cm_to_nautical_mile": 1 / 185200, "nautical_mile_to_cm": 185200,

    "mm_to_micrometer": 1000, "micrometer_to_mm": 1 / 1000,
    "mm_to_nanometer": 1e6, "nanometer_to_mm": 1 / 1e6,
    "mm_to_mi": 1 / 1.609e6, "mi_to_mm": 1.609e6,
    "mm_to_yd": 1 / 914.4, "yd_to_mm": 914.4,
    "mm_to_ft": 1 / 304.8, "ft_to_mm": 304.8,
    "mm_to_in": 1 / 25.4, "in_to_mm": 25.4,
    "mm_to_nautical_mile": 1 / 1.852e6, "nautical_mile_to_mm": 1.852e6,

    "micrometer_to_nanometer": 1000, "nanometer_to_micrometer": 1 / 1000,
    "micrometer_to_mi": 1 / 1.609e9, "mi_to_micrometer": 1.609e9,
    "micrometer_to_yd": 1 / 9.144e5, "yd_to_micrometer": 9.144e5,
    "micrometer_to_ft": 1 / 3.048e5, "ft_to_micrometer": 3.048e5,
    "micrometer_to_in": 1 / 25400, "in_to_micrometer": 25400,
    "micrometer_to_nautical_mile": 1 / 1.852e9, "nautical_mile_to_micrometer": 1.852e9,

    "nanometer_to_mi": 1 / 1.609e12, "mi_to_nanometer": 1.609e12,
    "nanometer_to_yd": 1 / 9.144e8, "yd_to_nanometer": 9.144e8,
    "nanometer_to_ft": 1 / 3.048e8, "ft_to_nanometer": 3.048e8,
    "nanometer_to_in": 1 / 2.54e7, "in_to_nanometer": 2.54e7,
    "nanometer_to_nautical_mile": 1 / 1.852e12, "nautical_mile_to_nanometer": 1.852e12,

    "mi_to_yd": 1760, "yd_to_mi": 1 / 1760,
    "mi_to_ft": 5280, "ft_to_mi": 1 / 5280,
    "mi_to_in": 63360, "in_to_mi": 1 / 63360,
    "mi_to_nautical_mile": 1.15078, "nautical_mile_to_mi": 1 / 1.15078,

    "yd_to_ft": 3, "ft_to_yd": 1 / 3,
    "yd_to_in": 36, "in_to_yd": 1 / 36,
    "yd_to_nautical_mile": 1 / 2025.37, "nautical_mile_to_yd": 2025.37,

    "ft_to_in": 12, "in_to_ft": 1 / 12,
    "ft_to_nautical_mile": 1 / 6076.12, "nautical_mile_to_ft": 6076.12,

    "in_to_nautical_mile": 1 / 72913.4, "nautical_mile_to_in": 72913.4,
}

unit_aliases = {
    "kilometers": "km", "kilometer": "km", "km": "km",
    "meters": "m", "meter": "m", "m": "m",
    "centimeters": "cm", "centimeter": "cm", "cm": "cm",
    "millimeters": "mm", "millimeter": "mm", "mm": "mm",
    "micrometers": "micrometer", "micrometer": "micrometer",
    "nanometers": "nanometer", "nanometer": "nanometer",
    "miles": "mi", "mile": "mi", "mi": "mi",
    "yards": "yd", "yard": "yd", "yd": "yd",
    "feet": "ft", "foot": "ft", "ft": "ft",
    "inches": "in", "inch": "in", "in": "in",
    "nautical miles": "nautical_mile", "nautical mile": "nautical_mile", "nautical_mile": "nautical_mile"
}

while True:
    try:
        units = input("Enter the units to convert from and to (e.g., 'km m' or 'kilometers to meters'): ").strip().lower().split()
        if len(units) != 2:
            raise ValueError("Please enter exactly two units separated by a space (e.g., 'km m').")
        
        from_unit_raw, to_unit_raw = units
        
        from_unit = unit_aliases.get(from_unit_raw)
        to_unit = unit_aliases.get(to_unit_raw)

        if not from_unit or not to_unit:
            raise KeyError(f"Could not recognize unit(s): '{from_unit_raw}' or '{to_unit_raw}'.")
        
        conversion_key = f"{from_unit}_to_{to_unit}"

        if conversion_key not in imperial_conversion_length:
            raise KeyError(f"Conversion '{conversion_key}' not found.")
        
        user_number_input = float(input(f"Enter the number of {from_unit_raw} to convert: ").strip())
        if user_number_input <= 0:
            raise ValueError("Number must be greater than zero.")
        
        conversion = user_number_input * imperial_conversion_length[conversion_key]

        print(f"{user_number_input} {from_unit_raw} = {conversion} {to_unit_raw}")

        again = input("Would you like to convert another value? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thanks for using the converter! Goodbye.")
            break

    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except KeyError as ke:
        print(f"Conversion error: {ke}")

imperial_conversion_volume = {
        "gal_to_qt": 4, "qt_to_gal": 1 / 4,
    "gal_to_pt": 8, "pt_to_gal": 1 / 8,
    "gal_to_c": 16, "c_to_gal": 1 / 16,
    "gal_to_oz": 128, "oz_to_gal": 1 / 128,
    "gal_to_tbsp": 256, "tbsp_to_gal": 1 / 256,
    "gal_to_tsp": 768, "tsp_to_gal": 1 / 768,
    "gal_to_cubic_meter": 0.00378541, "cubic_meter_to_gal": 264.172,
    "gal_to_l": 3.78541, "l_to_gal": 1 / 3.78541,
    "gal_to_ml": 3785.41, "ml_to_gal": 1 / 3785.41,
    "gal_to_imperial_gal": 0.832674, "imperial_gal_to_gal": 1 / 0.832674,
    "gal_to_imperial_qt": 3.3307, "imperial_qt_to_gal": 1 / 3.3307,
    "gal_to_imperial_pt": 6.6614, "imperial_pt_to_gal": 1 / 6.6614,
    "gal_to_imperial_c": 13.3228, "imperial_c_to_gal": 1 / 13.3228,
    "gal_to_imperial_oz": 133.228, "imperial_oz_to_gal": 1 / 133.228,
    "gal_to_imperial_tbsp": 213.165, "imperial_tbsp_to_gal": 1 / 213.165,
    "gal_to_imperial_tsp": 639.494, "imperial_tsp_to_gal": 1 / 639.494,
    "gal_to_cubic_foot": 0.133681, "cubic_foot_to_gal": 7.48052,
    "gal_to_cubic_inch": 231, "cubic_inch_to_gal": 1 / 231,

    "qt_to_pt": 2, "pt_to_qt": 1 / 2,
    "qt_to_c": 4, "c_to_qt": 1 / 4,
    "qt_to_oz": 32, "oz_to_qt": 1 / 32,
    "qt_to_tbsp": 64, "tbsp_to_qt": 1 / 64,
    "qt_to_tsp": 192, "tsp_to_qt": 1 / 192,
    "qt_to_cubic_meter": 0.000946353, "cubic_meter_to_qt": 1056.69,
    "qt_to_l": 0.946353, "l_to_qt": 1 / 0.946353,
    "qt_to_ml": 946.353, "ml_to_qt": 1 / 946.353,
    "qt_to_imperial_gal": 0.208169, "imperial_gal_to_qt": 1 / 0.208169,
    "qt_to_imperial_qt": 0.832674, "imperial_qt_to_qt": 1 / 0.832674,
    "qt_to_imperial_pt": 1.66535, "imperial_pt_to_qt": 1 / 1.66535,
    "qt_to_imperial_c": 3.3307, "imperial_c_to_qt": 1 / 3.3307,
    "qt_to_imperial_oz": 33.307, "imperial_oz_to_qt": 1 / 33.307,
    "qt_to_imperial_tbsp": 53.2913, "imperial_tbsp_to_qt": 1 / 53.2913,
    "qt_to_imperial_tsp": 159.874, "imperial_tsp_to_qt": 1 / 159.874,
    "qt_to_cubic_foot": 0.0334201, "cubic_foot_to_qt": 29.9221,
    "qt_to_cubic_inch": 57.75, "cubic_inch_to_qt": 1 / 57.75,

    "pt_to_c": 2, "c_to_pt": 1 / 2,
    "pt_to_oz": 16, "oz_to_pt": 1 / 16,
    "pt_to_tbsp": 32, "tbsp_to_pt": 1 / 32,
    "pt_to_tsp": 96, "tsp_to_pt": 1 / 96,
    "pt_to_cubic_meter": 0.000473176, "cubic_meter_to_pt": 2113.38,
    "pt_to_l": 0.473176, "l_to_pt": 1 / 0.473176,
    "pt_to_ml": 473.176, "ml_to_pt": 1 / 473.176,
    "pt_to_imperial_gal": 0.104084, "imperial_gal_to_pt": 1 / 0.104084,
    "pt_to_imperial_qt": 0.416337, "imperial_qt_to_pt": 1 / 0.416337,
    "pt_to_imperial_pt": 0.832674, "imperial_pt_to_pt": 1 / 0.832674,
    "pt_to_imperial_c": 1.66535, "imperial_c_to_pt": 1 / 1.66535,
    "pt_to_imperial_oz": 16.6535, "imperial_oz_to_pt": 1 / 16.6535,
    "pt_to_imperial_tbsp": 26.6457, "imperial_tbsp_to_pt": 1 / 26.6457,
    "pt_to_imperial_tsp": 79.937, "imperial_tsp_to_pt": 1 / 79.937,
    "pt_to_cubic_foot": 0.0167101, "cubic_foot_to_pt": 59.8442,
    "pt_to_cubic_inch": 28.875, "cubic_inch_to_pt": 1 / 28.875,

    "pt_to_imperial_tbsp": 21.317, "imperial_tbsp_to_pt": 1 / 21.317,
    "pt_to_imperial_tsp": 63.952, "imperial_tsp_to_pt": 1 / 63.952,
    "pt_to_cubic_foot": 0.00835506, "cubic_foot_to_pt": 119.688,
    "pt_to_cubic_inch": 14.4375, "cubic_inch_to_pt": 1 / 14.4375,

    "c_to_oz": 8, "oz_to_c": 1 / 8,
    "c_to_tbsp": 16, "tbsp_to_c": 1 / 16,
    "c_to_tsp": 48, "tsp_to_c": 1 / 48,
    "c_to_cubic_meter": 0.000236588, "cubic_meter_to_c": 4226.75,
    "c_to_l": 0.236588, "l_to_c": 1 / 0.236588,
    "c_to_ml": 236.588, "ml_to_c": 1 / 236.588,
    "c_to_imperial_gal": 0.052042, "imperial_gal_to_c": 1 / 0.052042,
    "c_to_imperial_qt": 0.208169, "imperial_qt_to_c": 1 / 0.208169,
    "c_to_imperial_pt": 0.416337, "imperial_pt_to_c": 1 / 0.416337,
    "c_to_imperial_oz": 4.1706, "imperial_oz_to_c": 1 / 4.1706,
    "c_to_imperial_tbsp": 6.6453, "imperial_tbsp_to_c": 1 / 6.6453,
    "c_to_imperial_tsp": 19.9359, "imperial_tsp_to_c": 1 / 19.9359,
    "c_to_cubic_foot": 0.00417952, "cubic_foot_to_c": 238.479,
    "c_to_cubic_inch": 7.875, "cubic_inch_to_c": 1 / 7.875,

    "oz_to_tbsp": 2, "tbsp_to_oz": 1 / 2,
    "oz_to_tsp": 6, "tsp_to_oz": 1 / 6,
    "oz_to_cubic_meter": 2.95735e-5, "cubic_meter_to_oz": 33814.02,
    "oz_to_l": 0.0295735, "l_to_oz": 1 / 0.0295735,
    "oz_to_ml": 29.5735, "ml_to_oz": 1 / 29.5735,
    "oz_to_imperial_gal": 0.006417, "imperial_gal_to_oz": 1 / 0.006417,
    "oz_to_imperial_qt": 0.025668, "imperial_qt_to_oz": 1 / 0.025668,
    "oz_to_imperial_pt": 0.051337, "imperial_pt_to_oz": 1 / 0.051337,
    "oz_to_imperial_c": 0.20669, "imperial_c_to_oz": 1 / 0.20669,
    "oz_to_imperial_tbsp": 1.33333, "imperial_tbsp_to_oz": 1 / 1.33333,
    "oz_to_imperial_tsp": 4, "imperial_tsp_to_oz": 1 / 4,
    "oz_to_cubic_foot": 1.044e-4, "cubic_foot_to_oz": 957.506,
    "oz_to_cubic_inch": 1.80469, "cubic_inch_to_oz": 1 / 1.80469,

    "tbsp_to_tsp": 3, "tsp_to_tbsp": 1 / 3,
    "tbsp_to_cubic_meter": 1.47868e-6, "cubic_meter_to_tbsp": 67628.045,
    "tbsp_to_l": 0.0147868, "l_to_tbsp": 1 / 0.0147868,
    "tbsp_to_ml": 14.7868, "ml_to_tbsp": 1 / 14.7868,
    "tbsp_to_imperial_gal": 0.002553, "imperial_gal_to_tbsp": 1 / 0.002553,
    "tbsp_to_imperial_qt": 0.010212, "imperial_qt_to_tbsp": 1 / 0.010212,
    "tbsp_to_imperial_pt": 0.020425, "imperial_pt_to_tbsp": 1 / 0.020425,
    "tbsp_to_imperial_c": 0.081701, "imperial_c_to_tbsp": 1 / 0.081701,
    "tbsp_to_imperial_oz": 0.851071, "imperial_oz_to_tbsp": 1 / 0.851071,
    "tbsp_to_imperial_tsp": 2.55321, "imperial_tsp_to_tbsp": 1 / 2.55321,
    "tbsp_to_cubic_foot": 1.057e-5, "cubic_foot_to_tbsp": 9463.53,
    "tbsp_to_cubic_inch": 0.919, "cubic_inch_to_tbsp": 1 / 0.919,

    "tsp_to_cubic_meter": 4.92892e-7, "cubic_meter_to_tsp": 202884.1,
    "tsp_to_l": 0.00492892, "l_to_tsp": 1 / 0.00492892,
    "tsp_to_ml": 4.92892, "ml_to_tsp": 1 / 4.92892,
    "tsp_to_imperial_gal": 0.000851, "imperial_gal_to_tsp": 1 / 0.000851,
    "tsp_to_imperial_qt": 0.003404, "imperial_qt_to_tsp": 1 / 0.003404,
    "tsp_to_imperial_pt": 0.006808, "imperial_pt_to_tsp": 1 / 0.006808,
    "tsp_to_imperial_c": 0.027234, "imperial_c_to_tsp": 1 / 0.027234,
    "tsp_to_imperial_oz": 0.2836, "imperial_oz_to_tsp": 1 / 0.2836,
    "tsp_to_imperial_tbsp": 0.851071, "imperial_tbsp_to_tsp": 1 / 0.851071,
    "tsp_to_cubic_foot": 3.515e-6, "cubic_foot_to_tsp": 28406.4,
    "tsp_to_cubic_inch": 0.3075, "cubic_inch_to_tsp": 1 / 0.3075,

    "cubic_meter_to_l": 1000, "l_to_cubic_meter": 1 / 1000,
    "cubic_meter_to_ml": 1e6, "ml_to_cubic_meter": 1 / 1e6,
    "cubic_meter_to_imperial_gal": 219.969, "imperial_gal_to_cubic_meter": 1 / 219.969,
    "cubic_meter_to_imperial_qt": 879.875, "imperial_qt_to_cubic_meter": 1 / 879.875,
    "cubic_meter_to_imperial_pt": 1759.75, "imperial_pt_to_cubic_meter": 1 / 1759.75,
    "cubic_meter_to_imperial_c": 7039, "imperial_c_to_cubic_meter": 1 / 7039,
    "cubic_meter_to_imperial_oz": 70394.3, "imperial_oz_to_cubic_meter": 1 / 70394.3,
    "cubic_meter_to_imperial_tbsp": 112631, "imperial_tbsp_to_cubic_meter": 1 / 112631,
    "cubic_meter_to_imperial_tsp": 337892, "imperial_tsp_to_cubic_meter": 1 / 337892,
    "cubic_meter_to_cubic_foot": 35.3147, "cubic_foot_to_cubic_meter": 1 / 35.3147,
    "cubic_meter_to_cubic_inch": 61023.7, "cubic_inch_to_cubic_meter": 1 / 61023.7,

    "l_to_ml": 1000, "ml_to_l": 1 / 1000,
    "l_to_imperial_gal": 0.219969, "imperial_gal_to_l": 1 / 0.219969,
    "l_to_imperial_qt": 0.879875, "imperial_qt_to_l": 1 / 0.879875,
    "l_to_imperial_pt": 1.75975, "imperial_pt_to_l": 1 / 1.75975,
    "l_to_imperial_c": 7.039, "imperial_c_to_l": 1 / 7.039,
    "l_to_imperial_oz": 70.393, "imperial_oz_to_l": 1 / 70.393,
    "l_to_imperial_tbsp": 112.631, "imperial_tbsp_to_l": 1 / 112.631,
    "l_to_imperial_tsp": 337.892, "imperial_tsp_to_l": 1 / 337.892,
    "l_to_cubic_foot": 0.0353147, "cubic_foot_to_l": 1 / 0.0353147,
    "l_to_cubic_inch": 61.0237, "cubic_inch_to_l": 1 / 61.0237,

    "ml_to_imperial_gal": 2.19969e-5, "imperial_gal_to_ml": 1 / 2.19969e-5,
    "ml_to_imperial_qt": 8.7987e-5, "imperial_qt_to_ml": 1 / 8.7987e-5,
    "ml_to_imperial_pt": 0.000175975, "imperial_pt_to_ml": 1 / 0.000175975,
    "ml_to_imperial_c": 0.0007039, "imperial_c_to_ml": 1 / 0.0007039,
    "ml_to_imperial_oz": 0.007039, "imperial_oz_to_ml": 1 / 0.007039,
    "ml_to_imperial_tbsp": 0.0112631, "imperial_tbsp_to_ml": 1 / 0.0112631,
    "ml_to_imperial_tsp": 0.0337892, "imperial_tsp_to_ml": 1 / 0.0337892,
    "ml_to_cubic_foot": 3.5315e-6, "cubic_foot_to_ml": 1 / 3.5315e-6,
    "ml_to_cubic_inch": 0.0610237, "cubic_inch_to_ml": 1 / 0.0610237,

      "Imperial_gal_to_imperial_qt": 4, "imperial_qt_to_Imperial_gal": 0.25,
  "Imperial_gal_to_imperial_pt": 8, "imperial_pt_to_Imperial_gal": 0.125,
  "Imperial_gal_to_imperial_c": 16, "imperial_c_to_Imperial_gal": 0.0625,
  "Imperial_gal_to_imperial_oz": 160, "imperial_oz_to_Imperial_gal": 0.00625,
  "Imperial_gal_to_imperial_tbsp": 256, "imperial_tbsp_to_Imperial_gal": 0.00390625,
  "Imperial_gal_to_imperial_tsp": 768, "imperial_tsp_to_Imperial_gal": 0.0013020833,
  "Imperial_gal_to_cubic_foot": 0.160544, "cubic_foot_to_Imperial_gal": 6.22884,
  "Imperial_gal_to_cubic_inch": 277.419, "cubic_inch_to_Imperial_gal": 0.00360465,

  "Imperial_qt_to_imperial_pt": 2, "imperial_pt_to_Imperial_qt": 0.5,
  "Imperial_qt_to_imperial_c": 4, "imperial_c_to_Imperial_qt": 0.25,
  "Imperial_qt_to_imperial_oz": 40, "imperial_oz_to_Imperial_qt": 0.025,
  "Imperial_qt_to_imperial_tbsp": 64, "imperial_tbsp_to_Imperial_qt": 0.015625,
  "Imperial_qt_to_imperial_tsp": 192, "imperial_tsp_to_Imperial_qt": 0.005208333,
  "Imperial_qt_to_cubic_foot": 0.040136, "cubic_foot_to_Imperial_qt": 24.9153,
  "Imperial_qt_to_cubic_inch": 69.3549, "cubic_inch_to_Imperial_qt": 0.0144185,

  "Imperial_pt_to_imperial_c": 2, "imperial_c_to_Imperial_pt": 0.5,
  "Imperial_pt_to_imperial_oz": 20, "imperial_oz_to_Imperial_pt": 0.05,
  "Imperial_pt_to_imperial_tbsp": 32, "imperial_tbsp_to_Imperial_pt": 0.03125,
  "Imperial_pt_to_imperial_tsp": 96, "imperial_tsp_to_Imperial_pt": 0.0104167,
  "Imperial_pt_to_cubic_foot": 0.020068, "cubic_foot_to_Imperial_pt": 49.8307,
  "Imperial_pt_to_cubic_inch": 34.6774, "cubic_inch_to_Imperial_pt": 0.028837,

  "Imperial_c_to_imperial_oz": 10, "imperial_oz_to_Imperial_c": 0.1,
  "Imperial_c_to_imperial_tbsp": 16, "imperial_tbsp_to_Imperial_c": 0.0625,
  "Imperial_c_to_imperial_tsp": 48, "imperial_tsp_to_Imperial_c": 0.0208333,
  "Imperial_c_to_cubic_foot": 0.010034, "cubic_foot_to_Imperial_c": 99.6613,
  "Imperial_c_to_cubic_inch": 17.3387, "cubic_inch_to_Imperial_c": 0.057674,

  "Imperial_oz_to_imperial_tbsp": 1.6, "imperial_tbsp_to_Imperial_oz": 0.625,
  "Imperial_oz_to_imperial_tsp": 4.8, "imperial_tsp_to_Imperial_oz": 0.208333,
  "Imperial_oz_to_cubic_foot": 0.0010034, "cubic_foot_to_Imperial_oz": 996.613,
  "Imperial_oz_to_cubic_inch": 1.73387, "cubic_inch_to_Imperial_oz": 0.576744,

  "Imperial_tbsp_to_imperial_tsp": 3, "imperial_tsp_to_Imperial_tbsp": 0.333333,
  "Imperial_tbsp_to_cubic_foot": 0.0006271, "cubic_foot_to_Imperial_tbsp": 1594.58,
  "Imperial_tbsp_to_cubic_inch": 1.08367, "cubic_inch_to_Imperial_tbsp": 0.922225,

  "Imperial_tsp_to_cubic_foot": 0.0002090, "cubic_foot_to_Imperial_tsp": 4783.75,
  "Imperial_tsp_to_cubic_inch": 0.361224, "cubic_inch_to_Imperial_tsp": 2.76832,

  "cubic_foot_to_cubic_inch": 1728, "cubic_inch_to_cubic_foot": 0.000578704
}

conversion_energy = {
    "j_to_kj": 1 / 1000, "kj_to_j": 1000, 
    "j_to_cal": 1 / 4.184, "cal": 4.184, 
    "j_to_kcal": 1 / 4184, "kcal_to_j": 4184, 
    "j_to_wh": 1 / 3600, "wh_to_j": 3600, 
    "j_to_kwh": 1 / 3.6e+6, "kwh_to_j": 3.6e+6, 
    "j_to_ev": 6.242e+18, "ev_to_j": 1 / 6.242e+18, 
    "j_to_btu": 1 / 1055, "btu_to_j": 1055, 
    "j_to_thm": 1 / 1.055e+8, "thm_to_j": 1.055e+8, 
    "j_to_ftlb": 1 / 1.356, "ftlb_to_j": 1.356, 
    
    "kj_to_cal": 239, "cal_to_kj": 1 / 239, 
    "kj_to_kcal": 1 / 4.184, "kcal_to_kj": 4.184, 
    "kj_to_wh": 1 / 3.6, "wh_to_kj": 3.6, 
    "kj_to_kwh": 1 / 3600, "kwh_to_kj": 3600, 
    "kj_to_ev": 6.242e+21, "ev_to_kj": 1 / 6.242e+21, 
    "kj_to_btu": 1 / 1.055, "btu_to_kj": 1.055, 
    "kj_to_thm": 1 / 105500, "thm_to_kj": 105500,
    "kj_to_ftlb": 737.6, "ftlb_to_kj": 1 / 737.6, 
    
    "cal_to_kcal": 1 / 1000, "kcal_to_cal": 1000, 
    "cal_to_wh": 1 / 860.4, "wh_to_cal": 860.4, 
    "cal_to_kwh": 1 / 860400, "kwh_to_cal": 860400, 
    "cal_to_ev": 2.611e+19, "ev_to_cal": 1 / 2.611e+19, 
    "cal_to_btu": 1 / 252.2, "btu_to_cal": 252.2, 
    "cal_to_thm": 1 / 2.521e+7, "thm_to_cal": 2.521e+7, 
    "cal_to_ftlb": 3.086, "ftlb_to_cal": 1 / 3.086, 

    "kcal_to_wh": 1.162, "wh_to_kcal": 1 / 1.162, 
    "kcal_to_kwh": 1 / 860.4, "kwh_to_kcal": 1 / 860.4, 
    "kcal_to_ev": 2.611e+22, "ev_to_kcal": 1 / 2.611e+22, 
    "kcal_to_btu": 3.966, "btu_to_kcal": 1 / 3.966, 
    "kcal_to_thm": 1 / 25210, "thm_to_kcal": 25210, 
    "kcal_to_ftlb": 3086, "ftlb_to_kcal": 1 / 3086, 
    
    "wh_to_kwh": 1 / 1000, "kwh_to_wh": 1000, 
    "wh_to_ev": 2.247e+22, "ev_to_wh": 1 / 2.247e+22, 
    "wh_to_btu": 3.412, "btu_to_wh": 1 / 3.412, 
    "wh_to_thm": 1 / 29300, "thm_to_wh": 29300, 
    "wh_to_ftlb": 2655, "ftlb_to_wh": 1 / 2655, 
    
    "kwh_to_ev": 2.247e+25, "ev_to_kwh": 1 / 2.247e+25, 
    "kwh_to_btu": 3412, "btu_to_kwh": 1 / 3412, 
    "kwh_to_thm": 1 / 29.3, "thm_to_kwh": 29.3, 
    "kwh_to_ftlb": 2.655e+6, "ftlb_to_kwh": 1 / 2.655e+6, 
    
    "ev_to_btu": 1 / 6.585e+21, "btu_to_ev": 6.585e+21, 
    "ev_to_thm": 1 / 6.584e+26, "thm_to_ev": 6.584e+26, 
    "ev_to_ftlb": 1 / 8.462e+18, "ftlb_to_ev": 8.462e+18, 
    
    "btu_to_thm": 1 / 99980, "thm_to_btu": 99980, 
    "btu_to_ftlb": 778.2, "ftlb_to_btu": 1 / 778.2, 
    
    "thm_to_ftlb": 7.78e+7, "ftlb_to_thm": 1 / 7.78e+7, 
     
}

unit_aliases = {
    "joules": "j", "joule": "j", "j": "j",
    "kilojoules": "kj", "kilojoule": "kj", "kj": "kj",
    "gram calories": "cal", "gram calorie": "cal", "calories": "cal", "calorie": "cal", "cal": "cal",
    "kilocalories": "kcal", "kilocalorie": "kcal", "food calories": "kcal", "food calorie": "kcal", "kcal": "kcal",
    "watt hours": "wh", "watt hour": "wh", "wh": "wh",
    "kilowatt hours": "kwh", "kilowatt hour": "kwh", "kwh": "kwh",
    "electronvolts": "ev", "electronvolt": "ev", "electron volts": "ev", "electron volt": "ev", "ev": "ev",
    "british thermal units": "btu", "british thermal unit": "btu", "btu": "btu",
    "us therm units": "thm", "us therm unit": "thm", "us thermal units": "thm", "us thermal unit": "thm", "thm": "thm",
    "foot pounds": "ftlb", "foot pound": "ftlb", "foot-pounds": "ftlb", "foot-pounds": "ftlb", "ftlbs": "ftlb", "ftlb": "ftlb",
}

while True:
    try:
        units = input("Enter the units to convert from and to (e.g., 'J kJ' or 'Joules to Kilojoules'): ").strip().lower().split()
        if len(units) != 2:
            raise ValueError("Please enter exactly two units separated by a space (e.g., 'J kJ).")
        
        from_unit_raw, to_unit_raw = units

        from_unit = unit_aliases.get(from_unit_raw)
        to_unit = unit_aliases.get(to_unit_raw)

        if not from_unit or not to_unit:
            raise KeyError(f"Could not recognize unit(s): '{from_unit_raw}' or '{to_unit_raw}'.")

        conversion_key = f"{from_unit}_to_{to_unit}"

        if conversion_key not in conversion_energy:
            raise KeyError(f"Conversion '{conversion_key}' not found.")

        user_number_input = float(input(f"Enter the number of {from_unit_raw} to convert: ").strip())
        if user_number_input <= 0:
            raise ValueError("Number must be greater than zero.")

        conversion = user_number_input * conversion_energy[conversion_key]
        print(f"{user_number_input} {from_unit_raw} = {conversion} {to_unit_raw}")

        again = input("Would you like to convert another value? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for using the converter! Goodbye.")
            break

    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except KeyError as ke:
        print(f"Conversion error: {ke}")