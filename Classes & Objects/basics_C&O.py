<<<<<<< HEAD
=======
# .............
>>>>>>> cac4fcd4870cb47b34c87d4eec4aeb868e6b1e0b
class Student:

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def display(self):
        print(self.Name)
        print(self.Age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

s1 = Student(name, age)
s2 = Student(name, age)

s1.display()
s2.display()

# different way of accessing variables

class Student:

    def __init__(self):
        self.name = "Ali"
        self.age = 20


student1 = Student()

print(student1.name)
print(student1.age)