# ===================================================
# *args takes many arguments in a function
#  you can also use any name but * at the begining
# arguments become a tuple
# ===================================================

def add(*args):

    # Start total from zero
    total = 0

    # Go through every argument
    for number in args:

        # Add number to total
        total += number

    # Return final total
    return total

print("=============================")
print("First sum is: ", add(1, 2))
print("Second sum is: 0", add(1, 2, 3))
print("Third sum is: ", add(10, 20, 30, 40))
print("=============================")

# another function

def show_numbers(*numbers):
    print(numbers)

show_numbers(500, 1000, 1500)
print("=============================")

# ===================================================
# **kwargs takes keyword arguments in a function
# you can also use any name but ** at the begining
# arguments become a dictionary
# ===================================================

def student(**kwargs):
    print(kwargs)

student(name="Ali", age=20, city="Lahore")
print("=============================")

# access values from kwarg

def student(**kwargs):

    print(kwargs["name"])

student(name="Ali", age=20)