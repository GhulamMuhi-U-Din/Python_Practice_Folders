# =======================================
# *args and **kwargs
# =======================================

# the wrapper() in basic decorator deos not take arguments, so we use *args and **kwargs

def decorator(func):

    # Create a wrapper function.
    def wrapper(*args, **kwargs):

        # Run before the original function.
        print("Before Function")

        # Call the original function.
        func(*args, **kwargs) # now the function takes arguments

        # Run after the original function.
        print("After Function")

    # Return the wrapper function itself.
    return wrapper

# Apply the decorator to greet().
@decorator
def greet(name):
    print("Hello", name)

# Call the decorated function.
greet("Ali")

# =======================================
# with @wraps,it store functions metadata
# =======================================

from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Before")

        # Call original function
        # add(5, 3) returns 8
        # Store 8 in result
        result = func(*args, **kwargs)

        # Print the returned result
        print(result)

        print("After")

        # Return result
        return result

    return wrapper

@decorator
def add(a, b):

    # Calculate and return addition
    return a + b


# Call decorated function
answer = add(5, 3)

# =======================================
# @repeat() for repeated function
# =======================================

def repeat(times):

    def decorator(func):

        def wrapper():

            for i in range(times):

                func()

        return wrapper

    return decorator

@repeat(3)
def hello():

    print("Hello")

hello()

# =======================================
# multiple decorators
# =======================================

def stars(func):

    def wrapper():

        print("*****")

        func()

        print("*****")

    return wrapper

def lines(func):

    def wrapper():

        print("-----")

        func()

        print("-----")

    return wrapper

@stars
@lines
def hello():

    print("Hello")

hello()