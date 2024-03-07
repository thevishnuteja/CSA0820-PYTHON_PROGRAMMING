number = int(input("Enter any number: "))


count = 0

while number > 0:
    number //= 10
    count += 1

print(f"Number of digits: {count}")

a = len(number)

print(a)
