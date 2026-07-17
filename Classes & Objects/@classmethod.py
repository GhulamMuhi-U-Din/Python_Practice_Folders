# Create Student class
class Student:

    # Class variable
    school = "My School"

    # Create a class method
    @classmethod
    def show_school(cls):

        # cls refers to the Student class
        print(cls.school)


# Call class method using the class
Student.show_school()