# Input: Take a number from the user
number = int(input("Enter a number: "))

# Check divisibility by 3 and 6
if number % 3 == 0 and number % 6 == 0:
    print(f"The number {number} is divisible by both 3 and 6.")
else:
    print(f"The number {number} is not divisible by both 3 and 6.")
