# A record of students in Physics Deptarment
import pandas as pd

students = {
    "Name": ['Onoh Blessing', 'Samuel Duke', 'Williams Cynthia', 'Okala Thompson', 'Chigozie Adaeze',  'Olajide Tayo', 
    'Okeke Princewill', 'Piriye Tonye-Luke'],
    "Age": [26, 21, 23, 27, 20, 21, 23, 24],
    "Department":'Phyiscs',
    "Gender": ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male']
}

df = pd.DataFrame(students)

print("\n===🧾Student's Record ===")
print("-" * 30)
print(students)

print("\n ")
print(students.keys())
print("-" * 30)
print(students.values())
print("-" * 30)

print("===🧾✒️ Students Record ===")
print(df.head())