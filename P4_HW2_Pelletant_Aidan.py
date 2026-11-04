# Aidan Pelletant
# 11/4/2026
# P4HW2
# salary calculator with loops

# request employee info
name = input("enter employee's name or 'done' to finish: ")

# create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    
    # add employee count plus one
    employee_count += 1
    
    # ask for employee info
    hours = float(input(f"How many hours did {name} work this week? "))
    rate = float(input(f"What is {name}'s hourly pay rate? "))
    
    # evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
    else:
        overtime_pay = 0
        regular_pay = hours * rate
        
    gross_pay = regular_pay + overtime_pay
    
    # accumulate totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay
    
    # display employee info and pay breakdown
    print("-" * 35)
    print(f"Employee name: {name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<12}")
    print("-" * 70)
    print(f"{hours:<15.1f}{rate:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<12.2f}")
    print("-" * 35)
    
    # ask for next employee name to continue or terminate loop
    name = input("enter employee's name or 'done' to finish: ")

# display final grand totals after loop terminates
print("\n")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${overtimepay_total:,.2f}")
print(f"Total amount paid for regular time: ${regularpay_total:,.2f}")
print(f"Total amount paid in gross: ${grosspay_total:,.2f}")