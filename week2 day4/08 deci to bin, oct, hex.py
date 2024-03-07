decimal = int(input("Please Enter the Decimal Number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"{decimal} Decimal = {binary} Binary Value")
print(f"{decimal} Decimal = {octal} Octal Value")
print(f"{decimal} Decimal = {hexadecimal} Hexadecimal Value")
