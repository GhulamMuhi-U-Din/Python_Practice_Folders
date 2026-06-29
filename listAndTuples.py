 # empty list bakery = []
# empty list bakery = list[]
bakery = ["milk", "bread", "eggs"]
bakery[2] = "butter" # changed eggs to butter
print("========== LIST ==========")
print(bakery)
print(len(bakery)) # length of list

fruits = ["Apple", "Banana"]
fruits.append("Orange") # add orange after banana
print(fruits)

numbers = [10, 20, 40]
numbers.insert(2, 30) # insert at index 2
print(numbers)
numbers.pop() # removes last element
print(numbers)

digits = [50, 10, 40, 20]
digits.sort()
print(digits)
digits.sort(reverse = "true")
print(digits)
print("**************************")

numbers = (10, 20, 30, 40, 50, 10) # tuple , cannot change data
student = "Ali", 20, 49.9 # unpackd tuple

print("========== TUPLES ==========")
print(numbers)
print(len(numbers)) # length of tuple
print(numbers.count(10)) # count something in a tuple
print(numbers.index(30)) # prints the index of 30
print(type(numbers)) # tuple
print(type(student)) # tuple
print("**************************")
