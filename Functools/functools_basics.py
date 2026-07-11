# reduce() from many values to one

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
print("=======================================")

# partial() pre fill function arguments

from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2) # a function where a is already 2

print(double(5))
print("=======================================")

# lru_cache() remember previous results

from functools import lru_cache

@lru_cache
def calculate(number):

    print("Calculating...")

    return number * 2


print(calculate(5))

print(calculate(5))
print("=======================================")

# wraps() preserve original function information

from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper():

        print("Before Function")

        func()

    return wrapper


@decorator
def hello():

    print("Hello")


hello()
print("=======================================")