#part one
#student's name along with the average of the grades:

# Create an empty array to store student information
students = []

# Get the student's name
student_name = input("Enter student's name: ")

# Store the student's name in the list
students.append(student_name)

# Get the grades
grades = []
for i in range(3):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

# Calculate the average of the grades
average = sum(grades) / len(grades)

# Print the student's name and average grade
print(f"\nStudent Name: {student_name}")
print(f"Average Grade: {average:.2f}")
