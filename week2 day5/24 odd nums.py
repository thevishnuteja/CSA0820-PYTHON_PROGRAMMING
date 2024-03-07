
for num in range(21):
    if num % 2 != 0:
        print(num, end=" ")


odd_numbers = [num for num in range(21) if num % 2 != 0]
print("\nOdd numbers using list comprehension:", *odd_numbers)
