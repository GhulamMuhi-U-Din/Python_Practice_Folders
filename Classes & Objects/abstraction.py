<<<<<<< HEAD
# abstraction in classes 
=======
# abstraction in classes ....
>>>>>>> cac4fcd4870cb47b34c87d4eec4aeb868e6b1e0b

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