class Teacher:

    def __init__(self, name):

        self.name = name


class Department:

    def __init__(self, teacher):

        self.teacher = teacher


teacher = Teacher("John")

department = Department(teacher)

print(department.teacher.name)