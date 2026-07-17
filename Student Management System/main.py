from student import Student
from config import APP_NAME, VERSION

print(APP_NAME)
print(VERSION)

student1 = Student("Ali", 20)
student2 = Student("Ahmed", 22)

print(student1)
print(student2)

student1.age = 25

print(student1)

print(Student.school())

print(Student.total())