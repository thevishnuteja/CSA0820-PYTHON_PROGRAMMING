def shuffle(l1, l2):
    result = []
    min_len = min(len(l1), len(l2))
    
    for i in range(min_len):
        result.append(l1[i])
        result.append(l2[i])
    
    # Append remaining elements from the longer list
    if len(l1) > len(l2):
        result.extend(l1[min_len:])
    else:
        result.extend(l2[min_len:])
    
    return result

# Sample input
n1 = int(input("Enter the number of elements of l1: "))
l1 = [int(input("Enter the element: ")) for _ in range(n1)]

n2 = int(input("Enter the number of elements of l2: "))
l2 = [int(input("Enter the element: ")) for _ in range(n2)]

# Get the shuffled list
shuffled_list = shuffle(l1, l2)

# Print the result
print(f"Shuffled list={shuffled_list}")
