"""
File operations
"""
from Tutorials.Incomplete.v2.student_mgt import Student
import os
from pathlib import Path

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "students.txt")

def save_student(student):
    "Save student information"
    with open(FILE_PATH, "a") as file:
        file.write(f"{student.name}, {student.score}")


def load_students():
  
    students = []

    with open(FILE_PATH, "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            student = Student(name, float(score))
            students.append(student)

    return students


    


# students = load_students()

# print(students)
# print(type(students))

def delete_student_file():
    pass



