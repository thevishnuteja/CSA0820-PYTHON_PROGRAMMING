def lowercase_remove(input_string):
    # Remove spaces
    input_string = input_string.replace(" ", "")
    # Convert to lowercase
    lowercase_string = input_string.lower()
    return lowercase_string

# Get input from the user
user_input = input("Enter a string: ")

# Process the input
result = lowercase_remove(user_input)

# Display the result
print("Result:", result)
