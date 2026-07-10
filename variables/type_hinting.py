# Type Hinting

from typing import Optional, Union, Any

# Variable Type Hints

# String
name: str = "Ali"

# Integer
age: int = 20

# Float
salary: float = 75000.50

# Boolean
is_student: bool = True

# Collection Type Hints

# List of integers
numbers: list[int] = [10, 20, 30]

# List of strings
cities: list[str] = ["Lahore", "Karachi", "Islamabad"]

# Dictionary
# Key   -> String
# Value -> Integer
students: dict[str, int] = {
    "Ali": 20,
    "Ahmed": 22
}

# Tuple
coordinates: tuple[int, int] = (25, 50)

# Set
unique_numbers: set[int] = {1, 2, 3, 4}

# Function Type Hints

# Function parameters are integers. Function returns an integer
def add(a: int, b: int) -> int:

    return a + b

# Function parameters are strings. Function returns a string
def greet(name: str) -> str:

    return f"Hello {name}"


# Optional

# Variable can contain either a string OR None
city: Optional[str] = None

# Union

# Variable can contain either an integer OR a string
data: Union[int, str]

data = 100

data = "Python"

# Any
# Variable can contain ANY datatype
value: Any

value = 10

value = "Ali"

value = [1, 2, 3]

value = {"Name": "Ali"}

# Main Program

print("Name :", name)
print("Age :", age)
print("Salary :", salary)
print("Student :", is_student)

print()

print("Numbers :", numbers)
print("Cities :", cities)
print("Students :", students)
print("Coordinates :", coordinates)
print("Unique Numbers :", unique_numbers)

print()

print("Addition :", add(5, 3))
print(greet("Kamran"))

print()

print("City :", city)
print("Data :", data)
print("Value :", value)