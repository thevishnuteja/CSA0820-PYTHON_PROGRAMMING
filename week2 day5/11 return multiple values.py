def return_multiple_vals(list2):
    MAX = max(list2)
    MIN = min(list2)
    Sorted_list = sorted(list2, reverse = False)

    return MAX ,MIN, Sorted_list


list1 = [2,5,6,9,1,3,7,9,5,10]

MAX1 , MIN1, sorted1 = return_multiple_vals(list1)

print("maximum = ", MAX1)
print("minimum = ", MIN1)
print("Sorted list = ", sorted1)

    
