# Create Student class
class Student:

    # Initialize object
    def __init__(self, age):

        # Store age
        self._age = age # _age because age is already our property name

    # Make age() behave like an attribute
    @property
    def age(self):

        # Return stored age
        return self._age


# Create Student object
student = Student(20)

print(student.age) # we wrote student.age rather than student.age()