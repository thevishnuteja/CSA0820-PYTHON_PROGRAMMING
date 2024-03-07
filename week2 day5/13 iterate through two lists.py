def iterate_lists(list1, list2):

    if len(list1) != len(list2):
        print("Error: Lists must have the same length.")
        return

    for item1, item2 in zip(list1, reversed(list2)):
        print(f"List1: {item1} | List2 (reversed): {item2}")

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

iterate_lists(list1, list2)
