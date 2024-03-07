def create_student_dictionary():

    num_students = int(input("Enter the number of students: "))
    student_dict = {}

    for i in range(num_students):
        roll_no = int(input("Enter Roll No: "))
        student_name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))
        student_dict[student_name] = marks

    return student_dict

def display_student_marks(student_dict):

    student_name = input("Enter Student Name to get marks: ")
    if student_name in student_dict:
        print(f"{student_name}'s Marks: {student_dict[student_name]}")
    else:
        print(f"{student_name} not found in the dictionary.")

student_marks_dict = create_student_dictionary()

# Display student marks based on input student name
display_student_marks(student_marks_dict)
