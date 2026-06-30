# zero division error exception

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# value error exception

try:
    age = int(input("Enter age: "))

except ValueError:
    print("Please enter numbers only.")

print("End")