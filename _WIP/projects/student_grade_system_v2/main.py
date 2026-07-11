"""
Controls the application's flow
"""

# Import modules
from Tutorials.Incomplete.v2.student_mgt import Student, display_students

from Tutorials.Incomplete.v2.grade_utils import (
    add_student,
    calculate_average, 
    highest_score,
    lowest_score
)
from Tutorials.Incomplete.v2.file_handler import (
    save_student,
    load_students,
    delete_student_file,
)

def main():
    print("""
==================================================
    📑 Students Grade Management System
==================================================

    1. Add Student
    2. Calculate Grades
    3. Highest Score
    4. Lowest Score
    5. Display Students
    6. Display Students dataframe
    7. Exit
    
    """)
    
    students = load_students()
    
    while True:
        
        try:
            choice = int(input("Enter choice number: "))
        except ValueError:
            print("Enter a valid choice number")
            continue

    
        if choice == 1:
            student = add_student()
            students.append(student)
            save_student
        elif choice == 2:
            for student in students:
                calculate_grade(student)
        elif choice == 3:
            highest_score(students)
        elif choice == 4:
            lowest_score(students)
        elif choice == 5:
            for student in students:
                student.display()
        elif choice == 6:
            display_students(students)
        elif choice == 7:
            print("Goodbye!")
        else:
            print("Invalid choice")
            break

    return

        







    # while True:
    #     choice = input("Enter choice: ")
        
    #     try:
    #         choice = int(input("Enter student score: "))
    #     except ValueError:
    #         print("Please enter a valid number")
    #         continue
            
    #     if not is_valid_score(score):
    #         print("""Invalid Score.
    #           Score must be between 0 and 100""")
    #         continue
        
    #     student = Student(name, score)
    #     students.append(student)
    #     save_student(student)
        
    #     grade = student.calculate_grade()
    #     print(f"Grade: {grade}")
    #     student.display()
    
    #     choice = input("Do you want to add another student? (y/n): ")
        
    #     if choice.lower() != 'y':
    #         break
        
        
if __name__ == "__main__":
    main()