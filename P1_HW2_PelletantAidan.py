# Aidan Pelletant
# September 24, 2026
# P1HW2
# A Python program that calculates travel expenses and remaining budget based on user inputs.

"""
Pseudocode:
1. Print program title/purpose ("This program calculates and displays travel expenses")
2. Prompt user to enter their budget and store as an integer
3. Prompt user to enter their travel destination and store as a string
4. Prompt user to enter amount spent on gas/fuel and store as an integer
5. Prompt user to enter amount spent on accommodation/hotel and store as an integer
6. Prompt user to enter amount spent on food and store as an integer
7. Add gas, accommodation, and food expenses together to find total expenses
8. Subtract total expenses from initial budget to calculate remaining balance
9. Display destination, initial budget, expenses, and remaining balance
"""

print("This program calculates and displays travel expenses\n")

# Prompt user for inputs
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("How much do you think you will spend on accommodation/hotel? "))
food = int(input("How much do you think you will spend on food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results formatted to match assignment requirements
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}\n")
print(f"Remaining Balance: {remaining_balance}")