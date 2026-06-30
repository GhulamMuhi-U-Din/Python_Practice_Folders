# to create a new list by changing the elements of previous list
numbers = [1, 2, 3, 4]
result = [number * 2 for number in numbers]
print(result)

# to get square of element in a new list
squares = [number ** 2 for number in numbers]
print(squares)

# to get all the letters as upppercase use .upper() function
names = ["ali", "abdullah", "akbar"]
upper_names = [name.upper() for name in names]
print(upper_names)

# range function 
numbers = [i for i in range(1, 11)]
print(numbers)

# for even numbers
numbers = [i for i in range(1,11) if i % 2 == 0]
print(numbers)

# for odd numbers
numbers = [i for i in range(1, 12) if i % 2 != 0]
print(numbers)