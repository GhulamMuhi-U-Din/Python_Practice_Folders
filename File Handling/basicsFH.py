# to check if file exists
import os

print(os.path.exists("students.txt"))

# to create a file

file = open("students.txt", "w")
file.close()

# write in a file

file = open("students.txt", "w")
file.write("Ali")
file.close()

# read in a file

file = open("students.txt", "r")
print(file.read()) # reads only frist line
file.close()

# append to a file

file = open("students.txt", "a")
file.write("\nAbdullah")
file.close()

# with open() function (no need for file.close())

with open("students.txt", "r") as file:
    print(file.read())

# reading in a file line by line

with open("students.txt", "r") as file:

    for line in file:
        print(line)