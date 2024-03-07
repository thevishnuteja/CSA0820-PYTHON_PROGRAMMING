def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_composite_numbers(arr):
    count = 0
    for num in arr:
        if num > 1 and not is_prime(num):
            count += 1
    return count

# Sample input
array_of_elements = [16, 18, 27, 16, 23, 21, 19]

# Calculate the number of composite numbers
composite_count = count_composite_numbers(array_of_elements)

print(f"Number of Composite Numbers = {composite_count}")
