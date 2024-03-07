def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)

num = 7  
print(f"The factorial of {num} is {recur_factorial(num)}")
