# Student class
class Student:

    # Class variable
    total_students = 0

    # Constructor
    def __init__(self, name, age):

        self.name = name
        self._age = age

        Student.total_students += 1

    # Property
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, value):

        if value > 0:
            self._age = value

    # String representation
    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}"

    # Class method
    @classmethod
    def total(cls):

        return cls.total_students

    # Static method
    @staticmethod
    def school():

        return "MY School"