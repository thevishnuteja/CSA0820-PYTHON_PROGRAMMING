def swap_positions(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst

# Sample input (same as above)
my_list = [4, 6, 12, 50, 67, 55]
position1, position2 = 1, 4

# Swap the elements
result_list = swap_positions(my_list, position1, position2)
print(result_list)
'''

def swap_positions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Sample input
my_list = [4, 6, 12, 50, 67, 55]
position1, position2 = 1, 4

# Swap the elements
result_list = swap_positions(my_list, position1, position2)

print(result_list)
'''
