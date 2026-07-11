# count() keeps counting

from itertools import count

for number in count(1):
    print(number)

    if number == 5:
        break

print("================================================")

# cycle() repeat forever

from itertools import cycle

colors = ["Red", "Green", "Blue"]

counter = 0

for color in cycle(colors):
    print(color)

    counter += 1

    if counter == 6:
        break

print("================================================")

# repeat() repeat one value

from itertools import repeat

for word in repeat("Python", 3):
    print(word)

print("================================================")

# permutations() all possible orders (order matters)

from itertools import permutations

letters = ["A", "B", "C"]

result = permutations(letters)

for item in result:
    print(item)

print("================================================")

# combinations() possible groups (order does not matter)

from itertools import combinations

students = ["Ali", "Ahmed", "Usman"]

result = combinations(students, 2)

for group in result:
    print(group)

print("================================================")

# product() all possible pairings

from itertools import product

colors = ["Red", "Blue"]
sizes = ["Small", "Large"]

result = product(colors, sizes)

for item in result:
    print(item)

print("================================================")

# accumulate() running total (adds all previous values)

from itertools import accumulate

numbers = [10, 20, 30, 40]

result = accumulate(numbers)

print(list(result))

print("================================================")

# chain() join iterables

from itertools import chain

list1 = [1, 2, 3]

list2 = [4, 5, 6]

result = chain(list1, list2)

print(list(result))

print("================================================")