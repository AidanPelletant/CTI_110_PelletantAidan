# Aidan Pelletant
# November 1, 2026
# P4LAB2
# Description: This program asks the user for an integer, checks if it is 
#              negative or positive/zero, displays a multiplication table 
#              from 1 to 12 using a for loop if valid, and uses a while loop 
#              to repeat the program based on user input.
#
# Pseudocode:
# 1. Initialize a control variable (run_program = "yes") to start the while loop.
# 2. WHILE run_program equals "yes":
#    a. Prompt the user to enter an integer.
#    b. IF the integer is greater than or equal to 0:
#       - Use a FOR loop from 1 to 12 to calculate and display the multiplication product.
#    c. ELSE (if the integer is less than 0):
#       - Display an error message stating negative numbers are not accepted.
#    d. Ask the user if they want to run the program again ("yes" or "no").
#    e. Update the control variable with the user's response.
# 3. END program when the user types "no".

def main():
    # While loop to control repeating the program
    run_program = "yes"
    
    while run_program == "yes":
        # Input step
        user_num = int(input("Enter an integer: "))
        
        # Decision for positive vs. negative integer
        if user_num >= 0:
            # Multiplication table logic using a for loop (1 to 12)
            print(f"\nMultiplication table for {user_num}:")
            for i in range(1, 13):
                product = user_num * i
                print(f"{user_num} * {i} = {product}")
        else:
            # Error message for negative values
            print("\nError: You entered a negative integer. Negative values are not accepted.")
            
        # Repeat/run-again logic
        print("-" * 30)
        run_program = input("Would you like to run the program again? (yes/no): ").strip().lower()
        print("-" * 30)

    print("Exiting program. Goodbye!")

if __name__ == "__main__":
    main()