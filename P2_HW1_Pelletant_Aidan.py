# Aidan Pelletant
# 10-23-26
# P2HW1
# This program calculates and shows travel expenses with formatted outputs and aligned columns.

# Prompt user to enter budget and expenses
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# Display travel expenses summary
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${hotel:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining_balance:.2f}")