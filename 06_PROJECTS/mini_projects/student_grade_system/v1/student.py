class Student:
    """Initialize Student with name and score"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def calculate_grade(self):
        """Calculate the students grade"""
        if self.score >= 70:
            return "A"
        if self.score >= 60:
            return "B"
        if self.score >= 50:
            return "C"
        if self.score >= 45: 
            return "D"
        else:
            return "F"
    
    def display(self):
        """Display all student's details"""
        print("Evaluating Student's Performance...\n")
        print("✅  Evaluation Complete!\n")
        print("🖨️  Printing results...\n")
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.calculate_grade()}")
        