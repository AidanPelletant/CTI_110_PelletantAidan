# Aidan Pelletant
# 10-25-26
# P3HW1
# This program takes six module grades, determines the lowest, highest, sum, and average, and then displays the average and its corresponding letter grade.

# Enter grades for six modules (converted to floats so math functions work properly)
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list (fixed missing commas and variable names)
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Display results summary block
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {low}")
print(f"{'Highest Grade:':<20} {high}")
print(f"{'Sum of Grades:':<20} {total_sum}")
print(f"{'Average:':<20} {avg:.2f}")
print("--------------------------------")

# Determine letter grade for average using a proper if-elif-else structure
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')