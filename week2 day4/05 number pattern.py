def print_pattern(start, max_lines):
    current_number = start
    for line in range(1, max_lines + 1):
        for _ in range(line):
            print(f"{current_number:.1f}", end=" ")
            current_number += 0.1
        print()

start_number = float(input("Enter the starting number: "))
max_lines_to_print = int(input("Max number of lines to be printed: "))

print_pattern(start_number, max_lines_to_print)
