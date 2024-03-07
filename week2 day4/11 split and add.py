def split_and_add(arr, k):
    for i in range(k):
        x = arr[0]
        for j in range(len(arr) - 1):
            arr[j] = arr[j + 1]
        arr[i] = x

# Sample input
input_array = [1, 5, 7, 12, 5, 8]
position = 3

# Split and add
split_and_add(input_array, position)

# Print the result
print(*input_array)
