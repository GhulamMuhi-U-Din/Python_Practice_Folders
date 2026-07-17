# we use @staticmethod because we do not need any object or class data for add()

class Calculator:

    @staticmethod
    def add(a, b):

        return a + b


print(Calculator.add(5, 3))

### complete example (instance method, class method, static method)

# Create Student class
class Student:

    # Class variable
    school = "My School"


    # Constructor
    def __init__(self, name):

        # Store the object's name
        self.name = name


    # Instance method
    def show_name(self):

        # Print object's name
        print(self.name)


    # Class method
    @classmethod
    def show_school(cls):

        # Print class variable
        print(cls.school)


    # Static method
    @staticmethod
    def say_hello():

        print("Hello")


# Create object
student = Student("John")


# Call instance method
student.show_name()


# Call class method
Student.show_school()


# Call static method
Student.say_hello()