"""
Student creation and management
"""
import pandas as pd

class Student:
    """Initialize Student with name and score"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.status = None
        
    def calculate_grade(self):
        """Calculate the students grade"""
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 45:
            return "D"
        else:
            return "F"

    def get_status(self):
        if self.score >= 45:
            self.status = "Pass"
        else:
            self.status = "Fail"
        return self.status


    def display(self):
        """Display all student's details"""
        print("""
====================
Student Details
====================""")
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Status: {self.get_status()}")
        print("====================")

    def to_dict(self):
        return {
            "Name": self.name,
            "Score": self.score,
            "Grade": self.calculate_grade(),
            "Status": self.get_status()
        }
        

def display_students(students):
    print("""
========================================
       📑 Students Result Sheet
========================================
    """)
    df = pd.DataFrame([student.to_dict() for student in students])
    print(df)