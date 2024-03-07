previous_num = 0
for i in range(10):
    current_sum = previous_num + i
    print(f"Current Number {i} + Previous Number {previous_num} = {current_sum}")
    previous_num = i
