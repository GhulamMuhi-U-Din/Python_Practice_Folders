# ==========================================
# JSON CHEAT SHEET
# ==========================================

import json

# ==========================================
# Example Data (Python Dictionary)
# ==========================================

student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

# ==========================================
# Python Dictionary → JSON String
# json.dumps()
# ==========================================

json_string = json.dumps(student)

print("JSON String:")
print(json_string)

# ==========================================
# JSON String → Python Dictionary
# json.loads()
# ==========================================

python_dict = json.loads(json_string)

print("\nPython Dictionary:")
print(python_dict)

# ==========================================
# Python Dictionary → JSON File
# json.dump()
# ==========================================

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nstudent.json created successfully.")

# ==========================================
# JSON File → Python Dictionary
# json.load()
# ==========================================

with open("student.json", "r") as file:
    data = json.load(file)

print("\nData Read From File:")
print(data)