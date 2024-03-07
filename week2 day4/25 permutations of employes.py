import itertools

# Input: Take a number from the user
N = 123
digits_list = list(str(N))

# Generate all permutations
permutations = list(itertools.permutations(digits_list))

# Print the permutations
for perm in permutations:
    print(int(''.join(perm)), end=" ")
