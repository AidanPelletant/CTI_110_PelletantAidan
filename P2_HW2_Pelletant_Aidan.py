# Aidan Pelletant
# 10-24-26
# P2HW2
# This program prompts the user for 6 module grades, stores them in a list, calculates the lowest, highest, sum, and average, and displays the results.


# Step 2: Prompt user to enter test grades for each module using separate input statements
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 3: Store all six entered grades in a descriptive list
module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 4: Calculate required results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
total_sum = sum(module_grades)
average_grade = total_sum / len(module_grades)

# Step 5: Format and display results matching standard output format
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade}")
print(f"{'Highest Grade:':<20} {highest_grade}")
print(f"{'Sum of Grades:':<20} {total_sum}")
print(f"{'Average:':<20} {average_grade:.2f}")
print("--------------------------------")