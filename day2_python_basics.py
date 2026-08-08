# 1. Variables and Data Types
name = "Nageswari"
age = 20
marks = 85.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Student:", is_student)

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))


# 2. Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 3. If-Else
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# 4. For Loop
print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)


# 5. While Loop
count = 1

while count <= 5:
    print(count)
    count += 1


# 6. Function
def square(number):
    return number * number

print("Square:", square(5))


# 7. Student Grade Calculator
student_name = input("Enter student name: ")
student_marks = float(input("Enter marks: "))

if student_marks >= 90:
    grade = "A"
elif student_marks >= 75:
    grade = "B"
elif student_marks >= 60:
    grade = "C"
elif student_marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Student:", student_name)
print("Marks:", student_marks)
print("Grade:", grade)