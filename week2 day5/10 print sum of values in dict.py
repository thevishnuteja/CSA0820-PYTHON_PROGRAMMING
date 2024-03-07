def values_Sum(myDict):
    values_list = list(myDict.values())
    return sum(values_list)

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'x': 25, 'y': 18, 'z': 45}
print("Sum of 1st dictionary values ", values_Sum(dict1))
print("Sum of 2nd dictionary values = ", values_Sum(dict2))


'''

def returnSum(dict):
    total_sum = 0
    for value in dict.values():
        total_sum += value
    return total_sum

dict1 = {'a': 100, 'b': 200, 'c': 300}
print("Sum:", returnSum(dict1))  # Output: 600


def returnSum(dict):
    return sum(dict.values())

dict1 = {'a': 100, 'b': 200, 'c': 300}
print("Sum:", returnSum(dict1))  # Output: 600

'''
