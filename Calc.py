user_input = input("Which conversion would you like to perform? (Area, Length, Mass, Energy, Frenquency, Plane Angle, Pressure, Speed, Temperature, Time, Volume): ").lower()

if user_input not in ["area", "length", "mass", "energy", "frenquency", "plane angle", "pressure", "speed", "temperature", "time", "volume"]:
    print("Please enter one of the conversions given to you.")

elif user_input == "area":
    print("Sorry this feature isn't available yet.")

elif user_input == "length":
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

elif user_input == "mass":
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

elif user_input == "energy":
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

elif user_input == "frenquency":
    print("Sorry this feature isn't available yet.")

elif user_input == "plane angle":
    print("Sorry this feature isn't available yet.")

elif user_input == "pressure":
    print("Sorry this feature isn't available yet.")

elif user_input == "speed":
    print("Sorry this feature isn't available yet.")

elif user_input == "temperature":
    print("Sorry this feature isn't available yet.")

elif user_input == "time":
    print("Sorry this feature isn't available yet.")

elif user_input == "volume":
    print("Sorry this feature isn't available yet.")
    
    # imperial_conversion_volume = {
    #     "gal_to_qt": 4, "qt_to_gal": 1 / 4,
    #     "gal_to_pt": 8, "pt_to_gal": 1 / 8,
    #     "gal_to_c": 15.773, "c_to_gal": 1 / 15.773,
    #     "gal_to_oz": 128, "oz_to_gal": 1 / 128,
    #     "gal_to_tbsp": 256, "tbsp_to_gal": 1 / 256,
    #     "gal_to_tsp": 768, "tsp_to_gal": 1 / 768,
    #     "gal_to_cubic_meter": 1 / 264.2, "cubic_meter_to_gal": 264.2,
    #     "gal_to_l": 3.785, "l_to_gal": 1 / 3.785,
    #     "gal_to_ml": 3785, "ml_to_gal": 1 / 3785,
    #     "gal_to_imperial_gal": 1 / 1.201, "imperial_gal_to_gal": 1.201,
    #     "gal_to_imperial_qt": 3.331, "imperial_qt_to_gal": 1 / 3.331,
    #     "gal_to_imperial_pt": 6.661, "imperial_pt_to_gal": 1 / 6.661,
    #     "gal_to_imperial_c": 13.323, "imperial_c_to_gal": 1 / 13.323,
    #     "gal_to_imperial_oz": 133.2, "imperial_oz_to_gal": 1 / 133.2,
    #     "gal_to_imperial_tbsp": 213.2, "imperial_tbsp_to_gal": 1 / 213.2,
    #     "gal_to_imperial_tsp": 639.5, "imperial_tsp_to_gal": 1 / 639.5,
    #     "gal_to_cubic_foot": 1 / 7.48, "cubic_foot_to_gal": 1 / 7.48,
    #     "gal_to_cubic_inch": 231, "cubic_inch_to_gal": 1 / 231,

    #     "qt_to_pt": , "pt_to_qt": ,
    #     "qt_to_c": , "c_to_qt": ,
    #     "qt_to_oz": , "oz_to_qt": ,
    #     "qt_to_tbsp": , "tbsp_to_qt": ,
    #     "qt_to_tsp": , "tsp_to_qt": ,
    #     "qt_to_cubic_meter": , "cubic_meter_to_qt": ,
    #     "qt_to_l": , "l_to_qt": ,
    #     "qt_to_ml": , "ml_to_qt": ,
    #     "qt_to_imperial_gal": , "imperial_gal_to_qt": ,
    #     "qt_to_imperial_qt": , "imperial_qt_to_qt": ,
    #     "qt_to_imperial_pt": , "imperial_pt_to_qt": ,
    #     "qt_to_imperial_c": , "imperial_c_to_qt": ,
    #     "qt_to_imperial_oz": , "imperial_oz_to_qt": ,
    #     "qt_to_imperial_tbsp": , "imperial_tbsp_to_qt": ,
    #     "qt_to_imperial_tsp": , "imperial_tsp_to_qt": ,
    #     "qt_to_cubic_foot": , "cubic_foot_to_qt": ,
    #     "qt_to_cubic_inch": , "cubic_inch_to_qt": ,

    #     "pt_to_c": , "c_to_pt": ,
    #     "pt_to_oz": , "oz_to_pt": ,
    #     "pt_to_tbsp": , "tbsp_to_pt": ,
    #     "pt_to_tsp": , "tsp_to_pt": ,
    #     "pt_to_cubic_meter": , "cubic_meter_to_pt": ,
    #     "pt_to_l": , "l_to_pt": ,
    #     "pt_to_ml": , "ml_to_pt": ,
    #     "pt_to_imperial_gal": , "imperial_gal_to_pt": ,
    #     "pt_to_imperial_qt": , "imperial_qt_to_pt": ,
    #     "pt_to_imperial_pt": , "imperial_pt_to_pt": ,
    #     "pt_to_imperial_c": , "imperial_c_to_pt": ,
    #     "pt_to_imperial_oz": , "imperial_oz_to_pt": ,
    #     "pt_to_imperial_tbsp": , "imperial_tbsp_to_pt": ,
    #     "pt_to_imperial_tsp": , "imperial_tsp_to_pt": ,
    #     "pt_to_cubic_foot": , "cubic_foot_to_pt": ,
    #     "pt_to_cubic_inch": , "cubic_inch_to_pt": ,

    #     "c_to_oz": , "oz_to_c": , 
    #     "c_to_tbsp": , "tbsp_to_c": , 
    #     "c_to_tsp": , "tsp_to_c": , 
    #     "c_to_cubic_meter": , "cubic_meter_to_c": , 
    #     "c_to_l": , "l_to_c": , 
    #     "c_to_ml": , "ml_to_c": , 
    #     "c_to_imperial_gal": , "imperial_gal_to_c": , 
    #     "c_to_imperial_qt": , "imperial_qt_to_c": , 
    #     "c_to_imperial_pt": , "imperial_pt_to_c": , 
    #     "c_to_imperial_c": , "imperial_c_to_c": , 
    #     "c_to_imperial_oz": , "imperial_oz_to_c": , 
    #     "c_to_imperial_tbsp": , "imperial_tbsp_to_c": , 
    #     "c_to_imperial_tsp": , "imperial_tsp_to_c": , 
    #     "c_to_cubic_foot": , "cubic_foot_to_c": , 
    #     "c_to_cubic_inch": , "cubic_inch_to_c": , 

    #     "oz_to_tbsp": , "tbsp_to_oz": , 
    #     "oz_to_tsp": , "tsp_to_oz": , 
    #     "oz_to_cubic_meter": , "cubic_meter_to_oz": , 
    #     "oz_to_l": , "l_to_oz": , 
    #     "oz_to_ml": , "ml_to_oz": , 
    #     "oz_to_imperial_gal": , "imperial_gal_to_oz": , 
    #     "oz_to_imperial_qt": , "imperial_qt_to_oz": , 
    #     "oz_to_imperial_pt": , "imperial_pt_to_oz": , 
    #     "oz_to_imperial_c": , "imperial_c_to_oz": , 
    #     "oz_to_imperial_oz": , "imperial_oz_to_oz": , 
    #     "oz_to_imperial_tbsp": , "imperial_tbsp_to_oz": , 
    #     "oz_to_imperial_tsp": , "imperial_tsp_to_oz": , 
    #     "oz_to_cubic_foot": , "cubic_foot_to_oz": , 
    #     "oz_to_cubic_inch": , "cubic_inch_to_oz": , 

    #     "tbsp_to_tsp": , "tsp_to_tbsp": , 
    #     "tbsp_to_cubic_meter": , "cubic_meter_to_tbsp": , 
    #     "tbsp_to_l": , "l_to_tbsp": , 
    #     "tbsp_to_ml": , "ml_to_tbsp": , 
    #     "tbsp_to_imperial_gal": , "imperial_gal_to_tbsp": , 
    #     "tbsp_to_imperial_qt": , "imperial_qt_to_tbsp": , 
    #     "tbsp_to_imperial_pt": , "imperial_pt_to_tbsp": , 
    #     "tbsp_to_imperial_c": , "imperial_c_to_tbsp": , 
    #     "tbsp_to_imperial_oz": , "imperial_oz_to_tbsp": , 
    #     "tbsp_to_imperial_tbsp": , "imperial_tbsp_to_tbsp": , 
    #     "tbsp_to_imperial_tsp": , "imperial_tsp_to_tbsp": , 
    #     "tbsp_to_cubic_foot": , "cubic_foot_to_tbsp": , 
    #     "tbsp_to_cubic_inch": , "cubic_inch_to_tbsp": , 

    #     "tsp_to_cubic_meter": , "cubic_meter_to_tsp": , 
    #     "tsp_to_l": , "l_to_tsp": , 
    #     "tsp_to_ml": , "ml_to_tsp": , 
    #     "tsp_to_imperial_gal": , "imperial_gal_to_tsp": , 
    #     "tsp_to_imperial_qt": , "imperial_qt_to_tsp": , 
    #     "tsp_to_imperial_pt": , "imperial_pt_to_tsp": , 
    #     "tsp_to_imperial_c": , "imperial_c_to_tsp": , 
    #     "tsp_to_imperial_oz": , "imperial_oz_to_tsp": , 
    #     "tsp_to_imperial_tbsp": , "imperial_tbsp_to_tsp": , 
    #     "tsp_to_imperial_tsp": , "imperial_tsp_to_tsp": , 
    #     "tsp_to_cubic_foot": , "cubic_foot_to_tsp": , 
    #     "tsp_to_cubic_inch": , "cubic_inch_to_tsp": , 

    #     "cubic_meter_to_l": , "l_to_cubic_meter": , 
    #     "cubic_meter_to_ml": , "ml_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_gal": , "imperial_gal_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_qt": , "imperial_qt_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_pt": , "imperial_pt_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_c": , "imperial_c_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_oz": , "imperial_oz_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_tbsp": , "imperial_tbsp_to_cubic_meter": , 
    #     "cubic_meter_to_imperial_tsp": , "imperial_tsp_to_cubic_meter": , 
    #     "cubic_meter_to_cubic_foot": , "cubic_foot_to_cubic_meter": , 
    #     "cubic_meter_to_cubic_inch": , "cubic_inch_to_cubic_meter": , 

    #     "l_to_ml": , "ml_to_l": , 
    #     "l_to_imperial_gal": , "imperial_gal_to_l": , 
    #     "l_to_imperial_qt": , "imperial_qt_to_l": , 
    #     "l_to_imperial_pt": , "imperial_pt_to_l": , 
    #     "l_to_imperial_c": , "imperial_c_to_l": , 
    #     "l_to_imperial_oz": , "imperial_oz_to_l": , 
    #     "l_to_imperial_tbsp": , "imperial_tbsp_to_l": , 
    #     "l_to_imperial_tsp": , "imperial_tsp_to_l": , 
    #     "l_to_cubic_foot": , "cubic_foot_to_l": , 
    #     "l_to_cubic_inch": , "cubic_inch_to_l": , 

    #     "ml_to_imperial_gal": , "imperial_gal_to_ml": , 
    #     "ml_to_imperial_qt": , "imperial_qt_to_ml": , 
    #     "ml_to_imperial_pt": , "imperial_pt_to_ml": , 
    #     "ml_to_imperial_c": , "imperial_c_to_ml": , 
    #     "ml_to_imperial_oz": , "imperial_oz_to_ml": , 
    #     "ml_to_imperial_tbsp": , "imperial_tbsp_to_ml": , 
    #     "ml_to_imperial_tsp": , "imperial_tsp_to_ml": , 
    #     "ml_to_cubic_foot": , "cubic_foot_to_ml": , 
    #     "ml_to_cubic_inch": , "cubic_inch_to_ml": , 

    #     "Imperial_gal_to_imperial_qt": , "imperial_qt_to_Imperial_gal": , 
    #     "Imperial_gal_to_imperial_pt": , "imperial_pt_to_Imperial_gal": , 
    #     "Imperial_gal_to_imperial_c": , "imperial_c_to_Imperial_gal": , 
    #     "Imperial_gal_to_imperial_oz": , "imperial_oz_to_Imperial_gal": , 
    #     "Imperial_gal_to_imperial_tbsp": , "imperial_tbsp_to_Imperial_gal": , 
    #     "Imperial_gal_to_imperial_tsp": , "imperial_tsp_to_Imperial_gal": , 
    #     "Imperial_gal_to_cubic_foot": , "cubic_foot_to_Imperial_gal": , 
    #     "Imperial_gal_to_cubic_inch": , "cubic_inch_to_Imperial_gal": , 

    #     "Imperial_qt_to_imperial_pt": , "imperial_pt_to_Imperial_qt": , 
    #     "Imperial_qt_to_imperial_c": , "imperial_c_to_Imperial_qt": , 
    #     "Imperial_qt_to_imperial_oz": , "imperial_oz_to_Imperial_qt": , 
    #     "Imperial_qt_to_imperial_tbsp": , "imperial_tbsp_to_Imperial_qt": , 
    #     "Imperial_qt_to_imperial_tsp": , "imperial_tsp_to_Imperial_qt": , 
    #     "Imperial_qt_to_cubic_foot": , "cubic_foot_to_Imperial_qt": , 
    #     "Imperial_qt_to_cubic_inch": , "cubic_inch_to_Imperial_qt": , 

    #     "Imperial_pt_to_imperial_c": , "imperial_c_to_Imperial_pt": , 
    #     "Imperial_pt_to_imperial_oz": , "imperial_oz_to_Imperial_pt": , 
    #     "Imperial_pt_to_imperial_tbsp": , "imperial_tbsp_to_Imperial_pt": , 
    #     "Imperial_pt_to_imperial_tsp": , "imperial_tsp_to_Imperial_pt": , 
    #     "Imperial_pt_to_cubic_foot": , "cubic_foot_to_Imperial_pt": , 
    #     "Imperial_pt_to_cubic_inch": , "cubic_inch_to_Imperial_pt": , 

    #     "Imperial_c_to_imperial_oz": , "imperial_oz_to_Imperial_c": , 
    #     "Imperial_c_to_imperial_tbsp": , "imperial_tbsp_to_Imperial_c": , 
    #     "Imperial_c_to_imperial_tsp": , "imperial_tsp_to_Imperial_c": , 
    #     "Imperial_c_to_cubic_foot": , "cubic_foot_to_Imperial_c": , 
    #     "Imperial_c_to_cubic_inch": , "cubic_inch_to_Imperial_c": , 

    #     "Imperial_oz_to_imperial_tbsp": , "imperial_tbsp_to_Imperial_oz": , 
    #     "Imperial_oz_to_imperial_tsp": , "imperial_tsp_to_Imperial_oz": , 
    #     "Imperial_oz_to_cubic_foot": , "cubic_foot_to_Imperial_oz": , 
    #     "Imperial_oz_to_cubic_inch": , "cubic_inch_to_Imperial_oz": , 

    #     "Imperial_tbsp_to_imperial_tsp": , "imperial_tsp_to_Imperial_tbsp": , 
    #     "Imperial_tbsp_to_cubic_foot": , "cubic_foot_to_Imperial_tbsp": , 
    #     "Imperial_tbsp_to_cubic_inch": , "cubic_inch_to_Imperial_tbsp": , 

    #     "Imperial_tsp_to_cubic_foot": , "cubic_foot_to_Imperial_tsp": , 
    #     "Imperial_tsp_to_cubic_inch": , "cubic_inch_to_Imperial_tsp": , 

    #     "cubic_foot_to_cubic_inch": , "cubic_inch_to_cubic_foot": , 
    # }
