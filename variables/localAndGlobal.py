# local variable

def greet():

    name = "John"

    print(name)

greet()

# global variable

name = "John" # global

def greet():

    print(name)

greet()

print(name)

# to modify the global variable elsewhere use global keyword

count = 10

def change():

    # Tell Python to use the GLOBAL variable.
    global count

    # Modify the global variable.
    count = 20

change()

print(count)

# scope of local variable is inside the function

x = 100

def test():

    # Local variable
    x = 50

    print(x)

test()

print(x)