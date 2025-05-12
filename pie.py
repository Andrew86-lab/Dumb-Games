from mpmath import mp

# Set precision to 50 decimal places
mp.dps = 50
pi_str = str(mp.pi)[2:]  # Skip "3."

# Convert first 50 digits of π (after "3.") into a list of integers
pi_digits = [int(d) for d in pi_str[:50]]

# Apply the user's carry-based rule with starting digit 3
results = []
carry = 0
current = 3  # Starting digit

for i, target in enumerate(pi_digits):
    # Try possible values of delta from -9 to 9
    found = False
    for delta in range(-9, 10):
        next_val = (current + delta + carry) % 10
        next_carry = (current + delta + carry) // 10
        if next_val == target:
            results.append((i + 1, target, f"{current} + ({delta}) + carry({carry}) = {current + delta + carry} → {next_val}, carry = {next_carry}"))
            carry = next_carry
            current = next_val
            found = True
            break
    if not found:
        results.append((i + 1, target, f"Could not match digit {target} from {current} with carry {carry}"))
        break

results
