# printing a basic string
name = "Abdullah"
print(name)

# printing the letter at a specific index
name = "john"
print(name[0])

# printing a letter through negative indexing
name = "sara"
print(name[-1])

# printing multiple letters through a range [start:end] (ending index is excluded)
name = "jackson"
print(name[0:4]) # index 4 is excluded , index 0 to 3 are printed

# ommiting the start
name = "Jackson"
print(name[:4])

# ommiting the ending
name = "Jackson"
print(name[4:])

# changing a string 
fruit = "Apple"
fruit = "Orange"
print(fruit)

# to make a string uppercase
car = "bmw"
print(car.upper())

# to make a string lower case
month = "JANUARY"
print(month.lower())

# to make it a title
name = "dwayne the rock"
print(name.title())

# to remove extra spaces
name = "   john  snow "
print(name.strip())

# replace text in a string
text = "I am going to Canada"
print(text.replace("Canada", "Scotland"))

# to find something in a string
text = "I am watching you"
print(text.find("y"))

# count occurances in a string
fruit = "Apple"
print(fruit.count("p"))

# sting concatenation
first = "Ali"
last = "Khan"

print(first + " " + last)

# repeating strings
name = "John"
print(name * 3)

# membership operators , to know if something exists in a text
text = "My name is Ghulam Muhi U Din"
print("name" in text)

# escape characters
print("Hello\nWorld") # next line

print("Hello\tWorld") # tab

# f-strings (to insert variables easily)
name = "Ali"
age = 20

print(f"My name is {name} and I am {age} years old.")

















