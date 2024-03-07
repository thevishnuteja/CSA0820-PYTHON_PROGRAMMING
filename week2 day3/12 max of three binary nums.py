def max_binary(binary_list):
    max_num = binary_list[0]
    for binary in binary_list[1:]:
        for i in range(len(binary)):
            if binary[i] > max_num[i]:
                max_num = binary
                break
            elif binary[i] < max_num[i]:
                break
    return max_num

# Sample input
binary_numbers = ["1101", "1011", "1001"]
max_number = max_binary(binary_numbers)
print("Maximum Number:", max_number)
