# Aidan Pelletant
# September 24, 2026
# P1HW1
# A Python program that calculates exponents and addition and subtraction
print("-----Calculating Exponents-----\n")

# Prompt user for base and exponent
base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))

# Calculate power
result_pow = base ** exponent

# Display output
print()
print(f"{base} raised to the power of {exponent} is {result_pow} !!")

print("-----Addition and Subtraction-----\n")

# Ask user for three integers
starting_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))

# Calculate math
final_result = starting_num + add_num - sub_num

# Display output
print()
print(f"{starting_num} + {add_num} - {sub_num} is equal to {final_result}")