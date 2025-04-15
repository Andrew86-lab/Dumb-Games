imperial_conversion_mass = {
    "kg_g": 1000, "g_kg": 1 / 1000, 
    "kg_mg": 1e+6, "mg_kg": 1 / 1e-6, 
    "kg_tonne": 1 / .001, "tonne_kg": 1000, 
    "Kg_microgram": 1e+9, "microgram_kg": 1 / 1e-9, 
    "kg_imperial ton": 1 / 1016, "imperial ton_kg": 1016, 
    "kg_ton": 1 / 907.2, "ton_kg": 907.2, 
    "kg_stone": 1 / 6.35, "stone_kg": 6.35, 
    "kg_lb": 2.205, "lb_kg": 1 / 2.205, 
    "Kg_oz": 35.274, "oz_kg": 1 / 35.274, 
    "g_tonne": 1 / 1e-6, "tonne_g": 1e+6, 
    "g_mg": 1000, "mg_g": 1 / 1000, 
    "g_microgram": 1e+6, "microgrm_g": 1 / 1e-6, 
    "g_imperial ton": 1 / 1.016e+6, "imperial ton_g": 1.016e+6, 
    "g_ton": 1 / 907200, "ton_g": 907200, 
    "g_stone": 1 / 6350, "stone_g": 6350, 
    "g_lb": 1 / 453.6, "lb_g": 453.6, 
    "g_oz": 1 / 28.35, "oz_g": 28.35, 
    "mg_tonne": 1 / 1e+9, "tonne_mg": 1e+9, 
    "mg_microgram": , "microgram_mg": , 
    "mg_imperial ton": , "imperial ton_mg": , 
    "mg_ton": , "ton_mg": , 
    "mg_stone": , "stone_mg": , 
    "mg_lb": , "lb_mg": , 
    "mg_oz": , "oz_mg": ,
}

def convert_mass(value, from_unit: str, to_unit: str):
    key = f"{from_unit}_to_{to_unit}"
    reverse_key = f"{to_unit}_to_{from_unit}"
    if key in imperial_conversion_mass:
        return value * imperial_conversion_mass[key]
    elif reverse_key in imperial_conversion_mass:
        return value / imperial_conversion_mass[reverse_key]
    else:
        raise ValueError(f"Unsupported mass conversion from '{from_unit}' to '{to_unit}'.")