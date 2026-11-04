# CTI-110
# P4LAB2 - Multiplication Table
# Aidan Pelletant
# November 4, 2026
# Description: This program uses a while loop and a for loop together to print 
# multiplication tables for positive integers, handles negative inputs, and 
# allows the user to repeat the program until they type 'no'.

# Pseudocode:
# 1. Initialize run_again variable to "yes" to start the while loop.
# 2. Start a while loop that runs as long as run_again does not equal "no".
# 3. Prompt the user to enter an integer.
# 4. If the integer is >= 0, use a for loop with range(1, 13) to print the multiplication table.
# 5. If the integer is negative (< 0), display an error message.
# 6. Ask the user if they would like to run the program again and update run_again.
# 7. Print an ending message once the loop breaks.

# Initialize run_again variable to start the loop
run_again = "yes"

# While loop to control whether the program runs again
while run_again != "no":
    
    # Get an integer from the user
    user_num = int(input("Enter an integer: "))
    
    # Determine if the integer is positive or negative
    if user_num >= 0:
        # Display multiplication table for that value from 1 to 12
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")
        
    # Ask user if they wish to run the program again
    run_again = input("Would you like to run the program again? ")

# The loop has broken (user entered 'no')
print("Program is ending")
