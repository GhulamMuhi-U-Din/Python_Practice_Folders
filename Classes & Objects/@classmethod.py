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

######### change data of class

class Student:

    school = "Old School"

    @classmethod
    def change_school(cls, new_school):

        cls.school = new_school


Student.change_school("New School")

print(Student.school)