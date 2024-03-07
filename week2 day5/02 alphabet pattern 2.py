
rows = int(input("enter a number: "))


current_char = ord('A')
for i in range(1, rows + 1):
        for j in range(i):
            print(chr(current_char), end=" ")
            current_char += 1
        print()
