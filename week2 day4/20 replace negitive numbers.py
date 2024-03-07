def replace_negatives_with_average(arr):
    # Calculate the average of non-negative elements
    non_negative_sum = sum(num for num in arr if num >= 0)
    non_negative_count = len([num for num in arr if num >= 0])
    average = non_negative_sum / non_negative_count if non_negative_count > 0 else 0

    # Replace negative numbers with the average
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = average

    # Sort the modified array
    arr.sort()

# Sample input
input_array = [9, 0, -4, 5, -6]

# Replace negatives with average and sort
replace_negatives_with_average(input_array)

# Print the output
print(input_array)
