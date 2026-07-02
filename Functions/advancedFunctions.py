# lambda function (single time , short function)
add = lambda a, b: a + b
print(add(10, 20))

# lambda for squaring values
square = lambda x: x * x
print(square(5))

# map function
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))

# map for uppercase letters
names = ["ali", "ahmed", "akbar"]
result = map(str.upper, names)
print(list(result))

# filter function (returns a filtered object)
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

# numbers greater than 50 using filter
numbers = [10, 20, 60, 80, 100, 200]
result = filter(lambda x: x > 50, numbers)
print(list(result))

# zip function (combines iterables)
names = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

result = zip(names, marks)
print(list(result))

# three iterables using zip function
names = ["Ali", "Ahmed"]
marks = [80, 90]
cities = ["Lahore", "Karachi"]

result = zip(names, marks, cities)
print(list(result))

# unequal lengths of iterables (stops for next incomplete value)
names = ["Ali", "Ahmed", "Sara"]
marks = [80, 90]
print(list(zip(names, marks)))

# enumerate function (provides indexes)
names = ["Ali", "Ahmed", "Sara"]

for i, name in enumerate(names):
    print(i, name)