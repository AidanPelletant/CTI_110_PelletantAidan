# Aidan Pelletant
# 10-25-26
# P3HW2
# This program calculates gross pay for an employee, handling overtime hours and regular pay using if/else logic
"""
Pseudocode:
1. Prompt the user to enter the employee's name.
2. Prompt the user to enter the number of hours worked.
3. Prompt the user to enter the hourly pay rate.
4. Check if hours worked are greater than 40 using an if/else statement:
   - If True (Overtime):
     - Calculate overtime hours (hours worked - 40).
     - Set regular hours to 40.
     - Calculate overtime pay (overtime hours * pay rate * 1.5).
     - Calculate regular pay (40 * pay rate).
   - If False (No Overtime):
     - Set overtime hours to 0.
     - Set regular hours equal to hours worked.
     - Set overtime pay to 0.0.
     - Calculate regular pay (hours worked * pay rate).
5. Calculate gross pay (regular pay + overtime pay).
6. Display the results formatted neatly with column headers.
"""

# Prompt user for inputs
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize variables
if hours_worked > 40:
    # Overtime calculations
    overtime_hours = hours_worked - 40
    regular_hours = 40
    reg_hour_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    # No overtime calculations
    overtime_hours = 0.0
    regular_hours = hours_worked
    reg_hour_pay = regular_hours * pay_rate
    overtime_pay = 0.0

# Calculate gross pay
gross_pay = reg_hour_pay + overtime_pay

# Display results in structured table format
print("\n--------------------------------------------------------------------------")
print(f"{'Employee name:':<15} {employee_name}")
print("--------------------------------------------------------------------------")
print(f"{'Hours Worked':<14} {'Pay Rate':<10} {'Overtime':<10} {'Overtime Pay':<14} {'RegHour Pay':<14} {'Gross Pay'}")
print("--------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f} {pay_rate:<10.1f} {overtime_hours:<10.1f} {overtime_pay:<14.2f} {reg_hour_pay:<14.2f} {gross_pay:<.2f}")
print("--------------------------------------------------------------------------")