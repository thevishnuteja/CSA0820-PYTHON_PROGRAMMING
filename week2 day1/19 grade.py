subject_1 = float(input("Enter marks for subject 1: "))
subject_2 = float(input("Enter marks for subject 2: "))
subject_3 = float(input("Enter marks for subject 3: "))
subject_4 = float(input("Enter marks for subject 4: "))
subject_5 = float(input("Enter marks for subject 5: "))

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

average = total / 5.0

percentage = (total / 500.0) * 100

if percentage >= 450:
    grade = 'S'
elif 400 <= percentage < 450:
    grade = 'A'
elif 350 <= percentage < 400:
    grade = 'B'
elif 300 <= percentage < 350:
    grade = 'C'
else:
    grade = 'D'

print("\nThe Total marks is:", total, "/ 500.00")
print("The Average marks is:", average)
print("The Percentage is:", percentage, "%")
print("The Grade is:", grade)
