# dataclass

from dataclasses import dataclass

# Tell Python that this is a dataclass

@dataclass
class Student:
    name: str
    age: int

# Main Program

name = input("Enter Student Name: ")

age = int(input("Enter Student Age: "))

#object

student1 = Student(name, age)

print("\nStudent Object:")
print(student1)

print("\nAccessing Individual Values")
print("Name :", student1.name)
print("Age  :", student1.age)