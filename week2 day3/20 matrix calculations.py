'''def calculate_sums(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Initialize lists to store row and column sums
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(num_rows)) for j in range(num_cols)]

    # Calculate diagonal sum (main diagonal)
    diag_sum = sum(matrix[i][i] for i in range(min(num_rows, num_cols)))

    return row_sums, col_sums, diag_sum

# Given matrix
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate sums
row_sums, col_sums, diag_sum = calculate_sums(a)

# Print results
for i, row_sum in enumerate(row_sums, start=1):
    print(f"Sum of {i} row: {row_sum}")

for j, col_sum in enumerate(col_sums, start=1):
    print(f"Sum of {j} column: {col_sum}")

print(f"Diagonal sum: {diag_sum}")
'''

import numpy as np

def matrix_sum(matrix):
    rows, cols = np.shape(matrix)
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    diagonal_sum1 = np.trace(matrix)
    diagonal_sum2 = np.trace(np.fliplr(matrix))
    
    print("Sum of rows:")
    for i in range(rows):
        print(f"Sum of {i+1} row: {row_sums[i]}")
    print("\nSum of columns:")
    for j in range(cols):
        print(f"Sum of {j+1} column: {col_sums[j]}")
    print("\nDiagonal sum:")
    print("Diagonal 1:", diagonal_sum1)
    print("Diagonal 2:", diagonal_sum2)

# Given matrix
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate and print sums
matrix_sum(a)
