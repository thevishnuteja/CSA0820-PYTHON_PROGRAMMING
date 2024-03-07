def calculate_overtime_pay(hours_worked):
    regular_hours = 40
    overtime_rate = 12.00

    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
        return overtime_pay
    else:
        return 0.0


num_employees = 10

for employee in range(1, num_employees + 1):
    hours_worked = float(input(f"Enter hours worked for Employee {employee}: "))
    total_pay = calculate_overtime_pay(hours_worked)
    print(f"Employee {employee} Overtime Pay: Rs. {total_pay:.2f}")


