def print_pattern_G(n):
    for i in range(n):
        for j in range(n):
            if ((j == 1 and i != 0 and i != n - 1) or
                ((i == 0 or i == n - 1) and j > 1 and j < n - 2) or
                (i == (n - 1) // 2 and j > n - 5 and j < n - 1) or
                (j == n - 2 and i != 0 and i != n - 1 and i >= (n - 1) // 2)):
                print("*", end="")
            else:
                print(" ", end=" ")
        print()

# Example usage:
line = 7
print_pattern_G(line)
