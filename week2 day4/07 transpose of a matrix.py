import numpy as np

# Original matrix
original_matrix = np.matrix([[1, 2, 3], [4, 5, 6]])

# Transposed matrix
transposed_matrix = original_matrix.transpose()

print("Original Matrix:")
print(original_matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)


'''
# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
'''
