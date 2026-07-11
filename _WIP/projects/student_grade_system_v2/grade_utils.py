"""Helper functions
Grade calculations and statistics
"""
from Tutorials.Incomplete.v2.student_mgt import Student
from Tutorials.Incomplete.v2.file_handler import save_student

def add_student(students):
    name = input("Enter student name: ")
    
    while True:
        try:
            score = float(input("Enter student score: "))
        except ValueError:
            print("Please enter a valid number")
            continue
            
        if not is_valid_score(score):
            print("""Invalid Score.
              Score must be between 0 and 100""")
            continue
        
        student = Student(name, score)
        return student
    

def is_valid_score(score: float) -> float:
    return 0 <= score <= 100
    
    
def calculate_average(students):
    total = 0
    count = 0
    for student in students:
        count += 1
        total += student.score
    average = total / count if count > 0 else 0
    return average

def highest_score(students):
    highest = students[0]
    
    for student in students:
        if student.score > highest.score:
            highest = student
    print(f"The student with the highest score is: {highest.name} with a score of {highest.score}")
    return highest


def lowest_score(students):
    lowest = students[0]
    
    for student in students:
        if student.score < lowest.score:
            lowest = student
    print(f"The student with the lowest score is: {lowest.name} with a score of {lowest.score}")
    return lowest

# Future Considerations
# pass_rate()
# class_average()
# median_average()




# def calculate_average(students):
#     total = 0
#     count = 0
#     for student in students:
#         count += 1
#         total = sum(students.score)
#         return count/total
    
