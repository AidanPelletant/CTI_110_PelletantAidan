# Aidan Pelletant  
# 10-24-26
# P3LAB
# This program takes a floating-point money value, converts it into an integer of cents, and calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed.

# Prompt user for a money value as a float
amount = float(input("Enter an amount of money (e.g., 12.41): "))

# Handle the case where the amount is 0 or negative
if amount <= 0:
    print("No change needed.")
else:
    # Convert the amount to total cents to avoid floating-point math precision errors
    total_cents = int(round(amount * 100))

    # Calculate dollars and remaining cents
    dollars = total_cents // 100
    total_cents %= 100

    # Calculate quarters
    quarters = total_cents // 25
    total_cents %= 25

    # Calculate dimes
    dimes = total_cents // 10
    total_cents %= 10

    # Calculate nickels
    nickels = total_cents // 5
    total_cents %= 5

    # Remaining cents are pennies
    pennies = total_cents

    # Display dollars (only if greater than 0, using singular/plural logic)
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} dollar")
        else:
            print(f"{dollars} dollars")

    # Display quarters (only if greater than 0, using singular/plural logic)
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} quarter")
        else:
            print(f"{quarters} quarters")

    # Display dimes (only if greater than 0, using singular/plural logic)
    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} dime")
        else:
            print(f"{dimes} dimes")

    # Display nickels (only if greater than 0, using singular/plural logic)
    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} nickel")
        else:
            print(f"{nickels} nickels")

    # Display pennies (only if greater than 0, using singular/plural logic)
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} penny")
        else:
            print(f"{pennies} pennies")