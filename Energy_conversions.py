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

# while True:
#     try:
#         units = input("Enter the units to convert from and to (e.g., 'J kJ' or 'Joules to Kilojoules'): ").strip().lower().split()
#         if len(units) != 2:
#             raise ValueError("Please enter exactly two units separated by a space (e.g., 'J kJ).")
        
#         from_unit_raw, to_unit_raw = units

#         from_unit = unit_aliases.get(from_unit_raw)
#         to_unit = unit_aliases.get(to_unit_raw)

#         if not from_unit or not to_unit:
#             raise KeyError(f"Could not recognize unit(s): '{from_unit_raw}' or '{to_unit_raw}'.")

#         conversion_key = f"{from_unit}_to_{to_unit}"

#         if conversion_key not in conversion_energy:
#             raise KeyError(f"Conversion '{conversion_key}' not found.")

#         user_number_input = float(input(f"Enter the number of {from_unit_raw} to convert: ").strip())
#         if user_number_input <= 0:
#             raise ValueError("Number must be greater than zero.")

#         conversion = user_number_input * conversion_energy[conversion_key]
#         print(f"{user_number_input} {from_unit_raw} = {conversion} {to_unit_raw}")

#         again = input("Would you like to convert another value? (y/n): ").strip().lower()
#         if again != 'y':
#             print("Thanks for using the converter! Goodbye.")
#             break

#     except ValueError as ve:
#         print(f"Invalid input: {ve}")

#     except KeyError as ke:
#         print(f"Conversion error: {ke}")