x = int(input("Enter value of X: "))
n = int(input("Enter value of N: "))

print("1 = pow\n2 = Add\n3 = Sub\n4 = Mul\n5 = Div")
choice = int(input("Choice: "))

if choice == 1:
    pow_result = x ** n
    print(f"Pow({x}, {n}) = {pow_result}")
elif choice == 2:
    add_result = x + n
    print(f"Add({x}, {n}) = {add_result}")
elif choice == 3:
    sub_result = x - n
    print(f"Sub({x}, {n}) = {sub_result}")
elif choice == 4:
    mul_result = x * n
    print(f"Mul({x}, {n}) = {mul_result}")
elif choice == 5:
    try:
        div_result = x / n
        print(f"Div({x}, {n}) = {div_result}")
    except ZeroDivisionError:
        print("ZeroDivisionError")
else:
    print("Invalid Input...!")
