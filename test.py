metric_conversion = {
    "kilo": 0.001,
    "hecto": 0.01,
    "deca": 0.1,
    "base": 1,  # Base stands for meters, grams, or liters
    "deci": 10,
    "centi": 100,
    "milli": 1000
}

# Recognized base units
base_units = ["meter", "liter", "gram"]

def parse_input(unit_input, base):
    """Extracts the prefix and ensures it matches the chosen base unit."""
    unit_input = unit_input.lower().strip()
    
    if unit_input == base:
        return "base", base  # User entered the base unit directly
    
    for prefix in metric_conversion:
        if unit_input == prefix + base:
            return prefix, base  # User entered a prefixed unit (e.g., kilometer)
    
    return None, None  # Invalid input

# Ask for the base unit type
while True:
    base_unit = input("Enter the base unit type (Meter, Liter, Gram): ").strip().lower()
    if base_unit in base_units:
        break
    print("Invalid base unit. Please enter 'Meter', 'Liter', or 'Gram'.")

# Get user inputs for conversion
from_unit_input = input(f"Enter the unit you're converting from (e.g., Kilo{base_unit}, Milli{base_unit}): ").strip()
to_unit_input = input(f"Enter the unit you're converting to (e.g., {base_unit}, Centi{base_unit}): ").strip()
value = float(input("Enter the value to convert: "))

# Parse user input
from_prefix, from_base = parse_input(from_unit_input, base_unit)
to_prefix, to_base = parse_input(to_unit_input, base_unit)

# Check validity
if from_prefix and to_prefix and from_base == to_base:
    # Convert value to base unit
    base_value = value / metric_conversion[from_prefix]
    # Convert from base to target unit
    converted_value = base_value * metric_conversion[to_prefix]
    
    print(f"{value} {from_unit_input} is equal to {converted_value} {to_unit_input}")
else:
    print(f"Invalid conversion. Please use metric units related to {base_unit}.")
