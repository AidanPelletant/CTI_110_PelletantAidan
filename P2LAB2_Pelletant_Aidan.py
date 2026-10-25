# Aidan Pelletant
# 10-23-26
# P2LAB2
# This program stores vehicle MPG values in a dictionary, displays the available vehicle keys, prompts the user to select a vehicle and miles driven, and then calculates and displays the required gallons of gas rounded to two decimal places.

# 1. Create the dictionary with vehicle keys and MPG values
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# 2. Create a variable that holds all the keys in the dictionary and print them
keys = vehicles.keys()
print(keys)

# 3. Prompt the user to enter one of the vehicles from the dictionary
chosen_vehicle = input("\nEnter a vehicle to see its MPG: ")

# 4. Display the MPG for the chosen vehicle
mpg = vehicles[chosen_vehicle]
print(f"The {chosen_vehicle} gets {mpg} mpg.")

# 5. Prompt the user to enter the number of miles they will drive
miles = float(input(f"How many miles will you drive the {chosen_vehicle}? "))

# 6. Calculate gallons of gas needed (Miles driven divided by MPG)
gallons_needed = miles / mpg

# 7. Display the gallons of gas needed, rounded to two decimal places using an f-string
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {chosen_vehicle} {miles} miles.")