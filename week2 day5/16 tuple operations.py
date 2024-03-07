#length

my_tuple = (10, 20, 30, 40)
length = len(my_tuple)
print("Length of the tuple:", length)  # Output: Length of the tuple: 4

#count
my_tuple = (1, 2, 3, 2, 1, 4, 2)
count_of_2 = my_tuple.count(2)
print("Count of 2 in the tuple:", count_of_2)  # Output: Count of 2 in the tuple: 3

#index
my_tuple = (10, 20, 30, 20, 40)
index_of_20 = my_tuple.index(20)
print("Index of 20 in the tuple:", index_of_20)  # Output: Index of 20 in the tuple: 1

# sorted
unsorted_tuple = (5, 2, 8, 1, 3)
sorted_list = sorted(unsorted_tuple)
print("Sorted list:", sorted_list)  # Output: Sorted list: [1, 2, 3, 5, 8]

#min and max

my_tuple = (10, 5, 20, 15)
min_value = min(my_tuple)
max_value = max(my_tuple)
print("Minimum value:", min_value)  # Output: Minimum value: 5
print("Maximum value:", max_value)  # Output: Maximum value: 20


#reversed

my_tuple = (1, 2, 3, 4)
reversed_tuple = tuple(reversed(my_tuple))
print("Reversed tuple:", reversed_tuple)  # Output: Reversed tuple: (4, 3, 2, 1)
