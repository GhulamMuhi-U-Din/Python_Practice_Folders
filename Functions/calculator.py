import math

def calculator(num1, num2):
    print(f"Addition of {num1} and {num2} is: {num1 + num2}")
    print(f"Subtraction of {num1} and {num2} is: {num1 - num2}")
    print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    print(f"Division of {num1} and {num2} is: {num1 / num2}")

def advancedCalculator(wholeNum):
    print(f"Cube of {wholeNum} is: {wholeNum * wholeNum * wholeNum}")
    print(f"Sqaure root of {wholeNum} is: {math.sqrt(wholeNum)}")
   
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
wholeNum = int(input("Enter a whole number to get its cube and square root: "))
print("=========================================")

calculator(num1, num2)
print("=========================================")
advancedCalculator(wholeNum)

# new updation start .......