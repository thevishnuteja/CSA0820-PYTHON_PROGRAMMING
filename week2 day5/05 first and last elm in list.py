def first_last(numbers):

    if len(numbers) < 2:
        return False
    else:
        return numbers[0] == numbers[-1]


my_list = [10, 20, 30, 40, 10]
result = first_last(my_list)
print(f"Result: {result}")
