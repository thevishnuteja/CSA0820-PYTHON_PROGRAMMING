A = int(input("Enter the first integer (A): "))
B = int(input("Enter the second integer (B): "))

AND = A & B
OR = A | B
XOR = A ^ B
LEFT_SHIFT = A << 2
RIGHT_SHIFT = B >> 1

print(f"Bitwise AND (A & B): {bin(AND)}")
print(f"Bitwise OR (A | B): {bin(OR)}")
print(f"Bitwise XOR (A ^ B): {bin(XOR)}")
print(f"binary value of A : {bin(A)}")
print(f"Left Shift (A << 1): {bin(LEFT_SHIFT)}")
print(f"binary value of B : {bin(B)}")
print(f"Right Shift (B >> 1): {bin(RIGHT_SHIFT)}")

