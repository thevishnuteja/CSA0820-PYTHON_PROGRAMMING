def create_new_list(list1, list2):
    
    new_list = []
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

list1 = [2, 5, 8, 12, 4, 6, 87, 32, 65]
list2 = [1, 6, 3, 90, 4, 5, 32, 4]
result = create_new_list(list1, list2)
print(f"New list: {result}")
