def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lower = 900
upper = 1000

print(f"Prime numbers between {lower} and {upper} are:")
for num in range(lower, upper + 1):
    if is_prime(num):
        print(num)
