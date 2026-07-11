
from student import Student
from grade_utils import is_valid_score


def main():
    print("""
================================ 
🧮 Student Grade Calculator 
================================ 
\n""")
    
    students = []
    
    while True:
        
        name = str(input("Enter student name: "))
        
        try:
            score = int(input("Enter student score: "))
        except ValueError:
            print("Please enter a valid number")
            continue
            
        if not is_valid_score(score):
            print("""Invalid Score.
              Score must be between 0 and 100""")
            continue
        
        student = Student(name, score)
        students.append(student)
        
        grade = student.calculate_grade()
        print(f"Grade: {grade}")
        student.display()
    
        choice = input("\nDo you want to add another student? (y/n): ")
        
        if choice.lower() != 'y':
            break
        
        
if __name__ == "__main__":
    main()