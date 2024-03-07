def sum_of_squares_iterative(N):
    total = 0
    for i in range(1, N + 1):
        total += i ** 2
    return total

N = int(input("Enter a positive integer N: "))
result = sum_of_squares_iterative(N)
print(f"Sum of squares of first {N} natural numbers is: {result}")
