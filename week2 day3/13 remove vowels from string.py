def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

# Input from user
input_string = input("Enter a string: ")

# Remove vowels
result_string = remove_vowels(input_string)

# Display result
print("The string without vowels is:", result_string)
