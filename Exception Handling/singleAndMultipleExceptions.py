# single exception case

print("Start")

try:
    print(10 / 0)

except:
    print("An error occurred.")

print("End")

# multiple exception case

try:
    number = int(input("Enter number: "))

    print(100 / number)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("End")