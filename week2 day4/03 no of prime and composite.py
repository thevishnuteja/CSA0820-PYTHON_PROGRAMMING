def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_and_composite():
    num_count = int(input("Enter the total number of values: "))
    prime_count = 0
    composite_count = 0

    for i in range(num_count):
        num = int(input("Enter a number: "))
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1

    print(f"Composite number: {composite_count} Prime number: {prime_count}")

# Example usage:
count_prime_and_composite()
