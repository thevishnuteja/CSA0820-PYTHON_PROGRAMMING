# Create a dictionary representing a person's information
person_info = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "city": "New York"
}

# Calculate the length of the dictionary
dictionary_length = len(person_info)

# Print the dictionary and its length
print("Person Information:")
for key, value in person_info.items():
    print(f"{key}: {value}")

print(f"\nLength of the Dictionary: {dictionary_length}")
