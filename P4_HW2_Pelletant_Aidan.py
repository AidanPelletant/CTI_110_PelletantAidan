# Aidan Pelletant
# November 1, 2026
# P4HW2
# Description: This program calculates gross pay for multiple employees, 
#              handling regular hours, overtime hours and pay, and tracking 
#              cumulative totals for overtime, regular pay, and gross pay until 
#              the user enters "Done" to terminate the loop.
#
# Pseudocode:
# 1. Make total employee counter and total pay to zero.
# 2. Prompt the user to enter an employee's name or "Done" to stop.
# 3. WHILE name is not equal to "Done":
#    a. Ask for hours worked and pay rate.
#    b. IF hours worked > 40:
#       - Calculate regular pay (40 hours * pay rate).
#       - Calculate overtime hours (hours - 40) and overtime pay (ot_hours * pay rate * 1.5).
#    c. ELSE:
#       - Calculate regular pay (hours * pay rate) and set overtime pay to 0.0.
#    d. Calculate gross pay (regular pay + overtime pay).
#    e. Add individual pay metrics to cumulative totals and increment employee count.
#    f. Display individual employee summary table.
#    g. Prompt for next employee name or "Done" to terminate.
# 4. Display final totals (total employees, total overtime pay, total regular pay, total gross pay).
# -----------------------------------------------------------------------------

def main():
    # Initialize accumulators
    total_employees = 0
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0

    # Prime the sentinel loop
    emp_name = input("Enter employee's name or \"Done\" to terminate: ")

    while emp_name.lower() != "done":
        # Input employee details
        hours_worked = float(input(f"How many hours did {emp_name} work? "))
        pay_rate = float(input(f"What is {emp_name}'s pay rate? "))
        print()

        # Calculate pay details
        if hours_worked > 40:
            reg_hours = 40.0
            ot_hours = hours_worked - 40.0
            reg_pay = reg_hours * pay_rate
            ot_pay = ot_hours * pay_rate * 1.5
        else:
            reg_hours = hours_worked
            ot_hours = 0.0
            reg_pay = reg_hours * pay_rate
            ot_pay = 0.0

        gross_pay = reg_pay + ot_pay

        # Update cumulative totals
        total_employees += 1
        total_overtime_pay += ot_pay
        total_regular_pay += reg_pay
        total_gross_pay += gross_pay

        # Display individual employee report matching the output format
        print(f"Employee name:   {emp_name}")
        print()
        print(f"{'Hours Worked':<14} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<14} {'RegHour Pay':<14} {'Gross Pay'}")
        print("-" * 88)
        print(f"{hours_worked:<14.1f} {pay_rate:<10.2f} {ot_hours:<10.1f} {ot_pay:<14.2f} ${reg_pay:<13.2f} ${gross_pay:.2f}")
        print()
        print("-" * 88)
        print()

        # Prompt for next employee
        emp_name = input("Enter employee's name or \"Done\" to terminate: ")

    # Display final totals after loop terminates
    print()
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
    print(f"Total amount paid for gross pay: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()