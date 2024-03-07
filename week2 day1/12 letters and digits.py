def count_digits_and_letters(input_string):
    num_digits = 0
    num_letters = 0

    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1

    return num_digits, num_letters


user_input = input("Enter a string: ")


digits, letters = count_digits_and_letters(user_input)


print(f"Letters {letters}")
print(f"Digits {digits}")
