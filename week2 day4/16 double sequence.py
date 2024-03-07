def generate_doubling_sequence(n):
    sequence = [2]  # Start with 1 (the first term)
    for i in range(n - 1):
        next_term = sequence[i] * 2
        sequence.append(next_term)
    return sequence

# Input: Number of terms in the sequence
num_terms = 6

# Generate the doubling sequence
doubling_sequence = generate_doubling_sequence(num_terms)

# Print the sequence
print("Doubling Sequence:")
print(*doubling_sequence)
