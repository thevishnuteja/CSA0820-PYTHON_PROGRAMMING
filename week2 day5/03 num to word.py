from num2words import num2words

print(num2words(36))

print(num2words(36, to = 'ordinal'))
print(num2words(36, to = 'ordinal_num'))
print(num2words(36, to = 'year'))
print(num2words(36, to = 'currency'))

print(num2words(36, lang ='es'))

'''
def number_to_words(n):
    # Define a list of English words for digits 0 to 9
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # Check if the input is a valid single-digit number
    if 0 <= n <= 9:
        print(f"The English word for {n} is: {words[n]}")
    else:
        print("Please enter a valid single-digit number.")

# Get input from the user
try:
    num = int(input("Enter a single-digit number: "))
    number_to_words(num)
except ValueError:
    print("Invalid input. Please enter an integer between 0 and 9.")
'''