def calculate_library_fine(days_late):
    if days_late <= 0:
        return 0  # No fine if returned on or before the expected return date
    elif days_late <= 5:
        return days_late * 0.50  # Fine of 50 paise per day
    elif days_late <= 10:
        return 5.00  # Fine of 1 rupee per day for 6 to 10 days
    else:
        return 30.00  # Fixed fine of 5 rupees for more than 10 days (membership cancellation)


days_late = int(input("Enter the number of days late: "))
fine_amount = calculate_library_fine(days_late)

if fine_amount == 0:
    print("No fine. Thank you for returning the book on time!")
else:
    print(f"Fine amount: Rs. {fine_amount:.2f}")

