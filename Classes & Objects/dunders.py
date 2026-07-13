# Create Student class
class Student:

    # __init__ runs when a new object is created
    def __init__(self, name, age):


        self.name = name
        self.age = age

        print(name, ",", age)


# Create a Student object. Python automatically calls __init__(student, "Ali", 20)
s1 = Student("Ali", 20)