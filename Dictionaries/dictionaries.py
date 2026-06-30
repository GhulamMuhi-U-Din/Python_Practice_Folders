# creates empty dictionary 
# student = {}

# creates empy dictioanary
# student = dict()

student = {
    "name" : "Ali", # key:value
    "age" : 20,
    "city" : "Lahore"
}

print(student["name"]) # accessing a key of dictionary student

# adding a key to dictionary
student["degree"] = "BSCS"
print(student)

# updating a key
student["age"] = 22
print(student)

# getting keys
print(student.keys())

# getting values
print(student.values())

# getting value of a key
print(student.get("city"))

# toget the pairs in form of key-value
print(student.items())

# update multiple values
student.update({
    "age" : 19,
    "city" : "Karachi"
})

print(student)

# remove a key
student.pop("city")
print(student)

# to remove last inserted key-value pair
student.popitem()
print(student)

# clear everyhing
student.clear()
print(student)

# copy dictionary
student2 = student.copy()
print(student2)