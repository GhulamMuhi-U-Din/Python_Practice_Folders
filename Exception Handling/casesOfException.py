# case 1: exception does not occurs (use else)

try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)

# case 2: whether exception occurs or not (use finally)

# (without error)

try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Program Finished")

# (with error)

try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Program Finished")

# case 3: index error

numbers = [10, 20]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist.")


# case 4: key error (in case of dictionaries)

student = {"name": "Ali"}

try:
    print(student["age"])

except KeyError:
    print("Key not found.")

# case 5: if you want to generate an exception

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")