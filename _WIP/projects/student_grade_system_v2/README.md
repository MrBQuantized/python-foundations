# Student Grade Management System (CLI)

---

(![alt text](image.png))

## Description

> **A Python command-line application for managing student grades.**

---

## Features

- Add student
- Calculate grade
- Display student information
- Save student information
- Save student records
- Load saved records

---

## Project Structure

```text
student_grade_system/
|
├── main.py
├── student.py
├── grade_utils.py
├── file_handler.py
├── student.txt
└── README.md
```

---

## Technologies

- Python

---

## Concepts Used

```text
- Functions
- OOP
- File handling
- Modules
- Input Validation
```

---

## File Information

### `main.py`

This is the entry point of the project. Its job is not to do everything. It simply coordinates the program. Think of it as a manager.

**Example responsibilities**:

```text
- Show menu
- Get user
- Call functions
- Create Student objects
- Save data
- Exit
```

It imports everything else

### `student.py`

This file defines the `Student` class. Think of it as the blueprint for every student.

```markdown
- Student Class
- Attributes
  - name
  - score

- Methods:
  - calculate_grade()
  - display()
```


### `grade_utils.py`

**Functions**:

```text
- is_valid_score()
- calculate_average()
- highest_score()
- lowest_score()
```

**Future considerations**:

```text
- pass_rate()
- class_average()
- median_average()
```

___This keeps calculations separate from the rest of the project___

### `file_handler.py`

Responsible for reading and writing files. Nothing else.

**Functions**:

```text
- save_student()
- load_students()
```

**Future Considerations**:

```text
- delete_student()
- update_student()
- export_csv()
```

### `student.txt`

This is your database. Instead of sql, you're storing records inside a text file.

### `requirements.txt`

Remains empty for now, but will be filled with list of packages.

---

## How the project works

```text
User
   |
   ▼
main.py
   |
   ├───────────────────────────────────► student.py
   |                                        |
   |                                        ▼
   |                                 Student object
   |
   |
   ├───────────────────────────────────► grade_utils.py
   |                                         |
   |                                         ▼
   |                                 Calculations
   |
   └───────────────────────────────────► file_handler.py
                                             |  
                                             ▼
                                     students.txt
```

---

## Future Improvements

```text
- GUI
- Database
- Multiple subjects
```