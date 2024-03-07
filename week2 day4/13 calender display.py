import calendar

# Input: Year and Month
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# Display the calendar
print(calendar.month(yy, mm))
print(calendar.calendar(yy))
