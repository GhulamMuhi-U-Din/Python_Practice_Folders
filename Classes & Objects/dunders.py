# =====================================
# __init__()
# =====================================

# Create Student class
class Student:

    # __init__ runs when a new object is created
    def __init__(self, name, age):


        self.name = name
        self.age = age

# Create a Student object. Python automatically calls __init__(student, "Ali", 20)
s1 = Student("Ali", 20)
print(s1)

# =====================================
# __str__() , to get proper output
# =====================================

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def __str__(self):

        return f"Student: {self.name}, Age: {self.age}"

student = Student("Ali", 20)

print(student)

# =====================================
# __len__() , to get length of object
# =====================================

class Classroom:

    def __init__(self, students):

        self.students = students

    def __len__(self):

        return len(self.students)


classroom = Classroom(
    ["Ali", "Ahmed", "Sara"]
)

print(len(classroom))

# ==========================================
# __eq__() , to check if equal using "and"
# ==========================================

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def __eq__(self, other):

        return (
            self.name == other.name
            and
            self.age == other.age
        )

student1 = Student("Ali", 20)

student2 = Student("Ali", 20)

print(student1 == student2)

# =======================================
# __add__() , to add two objects using +
# =======================================

class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value

number1 = Number(10)

number2 = Number(20)

print(number1 + number2)