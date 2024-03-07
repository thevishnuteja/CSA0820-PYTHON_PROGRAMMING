#Add operation
my_set = {1, 2, 3}
my_set.add(4)
print("add operation",my_set)

#update operation
my_set = {1, 2, 3}
my_set.update([3, 4, 5])
print("update :", my_set)  # Output: {1, 2, 3, 4, 5}

#copy operation
original_set = {10, 20, 30}
new_set = original_set.copy()
print("copy :", new_set)  # Output: {10, 20, 30}

# pop operation
my_set = {10, 20, 30}
removed_element = my_set.pop()
print("poped element:", removed_element)
print("Updated set:", my_set)

#remove operation
my_set = {10, 20, 30}
my_set.remove(20)
print("remove :", my_set)  # Output: {10, 30}

#discard
my_set = {10, 20, 30}
my_set.discard(10)  # No error
print("discard ",my_set)

#clear operation
my_set = {1, 2, 3}
my_set.clear()
print("clear ",my_set)  # Output: set()

#union opeation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("union :", union_set)  # Output: {1, 2, 3, 4, 5}

#intersection operation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print("intersection :",intersection_set)  # Output: {3}

#difference operation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("difference  : ", difference_set)  # Output: {1, 2}



