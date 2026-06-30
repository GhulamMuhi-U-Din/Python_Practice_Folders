# an empty set 
student = set()

# creating a set
numbers = {10, 20, 30, 40}
print(numbers)

# set removes duplicates
numbers = {10, 20, 30, 40, 20, 50, 30, 20}
print(numbers)

# add to set
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# add multiple values
numbers = {10, 20}
numbers.update([30, 40, 50])
print(numbers)

# remove element
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

# discard element
numbers = {10, 20, 30}
numbers.discard(30)
print(numbers)

# remove everything
numbers = {10, 20, 30}
numbers.clear()
print(numbers)

# create copy
numbers = {10, 20, 30}
numbers2 = numbers.copy()
print(numbers2)


# membership operators
numbers = {100, 200, 300, 400}
print(200 in numbers) # true
print(500 in numbers) # false

# loop in sets
numbers = {10, 20, 30}
for number in numbers:
    print(number)

# union of sets
n1 = {1, 2, 3, 4, 5}
n2 = {3, 4, 5, 6, 7}
print(n1 | n2) # method 1
print(n1.union(n2)) # method 2

# intersection of sets
print(n1 & n2) # method 1
print(n1.intersection(n2)) # method 2

# difference of sets (elements in first set but not in second)
print(n1 - n2) # method 1
print(n1.difference(n2)) # method 2

# elements that are not in both sets
print(n1 ^ n2) # method 1
print(n1.symmetric_difference(n2)) # method 2