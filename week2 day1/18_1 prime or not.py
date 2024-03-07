def is_prime_recursive(n, checkpoint=2):
    if n <= 1:
        return False
    elif checkpoint >= n:
        return True
    elif n % checkpoint == 0:
        return False
    else:
        return is_prime_recursive(n, checkpoint + 1)

number = int(input("Enter a positive integer: "))

if is_prime_recursive(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
