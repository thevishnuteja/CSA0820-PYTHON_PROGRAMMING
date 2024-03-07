def get_multiple_values(dictionary, keys):
    return [dictionary.get(key) for key in keys]

# Sample dictionary
my_dict = {'answer': 42, 'greeting': 'hello', 'numbers': [1, 2, 3]}

# Specify keys to retrieve values
keys_to_get = ['answer', 'greeting', 'numbers']

# Get multiple values
result = get_multiple_values(my_dict, keys_to_get)

# Print the result
print(*result)
