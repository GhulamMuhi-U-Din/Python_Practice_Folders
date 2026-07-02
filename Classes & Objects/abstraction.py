# abstraction in classes ....

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        super().display()
        print("Age :", self.age)


student = Student("Ali", 20)

student.display()