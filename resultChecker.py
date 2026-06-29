import math
import os

def grade(name, s1, s2, s3, TotalMarks):
    totalObtained = s1 + s2 + s3

    if totalObtained >= 120:
        stuGrade = "A"
        #print(f"You got A Grade")

    elif totalObtained >= 90:
        stuGrade = "B"
        #print(f"You got B grade")

    elif totalObtained >= 70:
        stuGrade = "C"
        #print(f"You got C grade")

    else:
        stuGrade = "F"
        #print(f"You got F grade")

    print(f"====================================================")
    print(f"Showing resut for: {name}")
    print(f"====================================================")
    print(f"Total marks Obatined are {totalObtained} out of {totalMarks}")
    print(f"You got {stuGrade} Grade")


name = input("Enter student's name: ")
totalMarks = 150
print(f"====================================================")
s1 = float(input("Enter marks obtained in English: "))
s2 = float(input("Enter marks obtained in Urdu: "))
s3 = float(input("Enter marks obtained in Maths: "))
print(f"====================================================")
os.system("cls")
grade(name, s1, s2, s3, totalMarks)
