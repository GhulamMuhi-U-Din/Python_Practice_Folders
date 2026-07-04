# regular expression (regex)

# search() (check only first occurance anywhere in the string)
import re # regex module

text = "I love Python programming."

result = re.search("Python", text)

print(result)

# match() (checks only at the begining)

text = "Python is easy."

result = re.match("Python", text)

print(result)

# findall() (checks all occurances)

text = "Python Java Python C++ Python"

result = re.findall("Python", text)

print(result)

# sub() (replaces tex)

text = "I like Java."

new_text = re.sub("Java", "Python", text)

print(new_text)

# re.split() (Splits a string using a regex pattern)

text = "Ali,Ahmed,Usman"

result = re.split(",", text)

print(result)

# ==========================================================
# COMMON REGEX SYMBOLS
# ==========================================================

# .  (Matches ANY single character)

print(re.findall("c.t", "cat cot cut c9t"))

# \d (Matches a SINGLE digit 0-9)

print(re.findall(r"\d", "Age: 25"))

# \d+ (Matches ONE OR MORE digits)

print(re.findall(r"\d+", "Age 25 Roll 101"))

# \D (Matches any NON-DIGIT character)

print(re.findall(r"\D", "Age25"))

# \w (Matches letters, numbers and underscore)

print(re.findall(r"\w", "Ali_123"))

# \W (Matches everything EXCEPT letters, numbers and underscore)

print(re.findall(r"\W", "Ali@123!"))

# \s (Matches whitespace (space, tab, newline))

print(re.findall(r"\s", "Hello Python"))

# \S (Matches NON-WHITESPACE characters)

print(re.findall(r"\S", "Hello Python"))

# ^ (Beginning of the string)

print(re.search(r"^Python", "Python is easy"))

# $ (End of the string)

print(re.search(r"easy$", "Python is easy"))

# * (Zero or more occurrences)

print(re.findall(r"ab*", "a ab abb abbb"))

# + (One or more occurrences)

print(re.findall(r"ab+", "a ab abb abbb"))

# ? (Zero or one occurrence)

print(re.findall(r"colou?r", "color colour"))

# [] (Character Set)

print(re.findall(r"[aeiou]", "Python Programming"))

# [0-9] (Match any digit

print(re.findall(r"[0-9]", "Age25"))

# [A-Z] (Match uppercase letters)

print(re.findall(r"[A-Z]", "Ali PYTHON"))

# [a-z] (Match lowercase letters)

print(re.findall(r"[a-z]", "Ali PYTHON"))

# | (OR operator)

print(re.findall(r"cat|dog", "dog cat bird"))

# () (Grouping)

result = re.search(r"(Python)", "I love Python")

print(result.group())


# ==========================================================
# REAL EXAMPLES
# ==========================================================

# Find Email

text = "Email: ali@gmail.com"

print(re.findall(r"\S+@\S+", text))

# Find Phone Number

text = "03001234567"

print(re.findall(r"\d+", text))

# Find Date

text = "Today's date is 04/07/2026"

print(re.findall(r"\d{2}/\d{2}/\d{4}", text))

# Replace Multiple Spaces

text = "Hello      Python"

print(re.sub(r"\s+", " ", text))

# Validate CNIC Format

cnic = "35202-1234567-1"

print(re.match(r"\d{5}-\d{7}-\d", cnic))