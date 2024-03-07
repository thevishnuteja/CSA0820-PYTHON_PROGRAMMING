def print_reverse_list(lst):
    i = len(lst) - 1
    while i >= 0:
        print(lst[i], end=" ")
        i -= 1

# Sample input
input_list = [2, 3, 5, 6, 7, 8, 9]

# Print the elements in reverse order
print_reverse_list(input_list)
