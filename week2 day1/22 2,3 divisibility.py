def check_divisibility(number):
    if number % 2 == 0 and number % 3 == 0:
        print(f"The number {number} is divisible by both 2 and 3.")
    else:
        print(f"The number {number} is not divisible by both 2 and 3.")

# Get input from the user
try:
    user_input = int(input("Enter a number: "))
    check_divisibility(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
