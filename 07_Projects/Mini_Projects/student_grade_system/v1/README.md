# Student Grade Management System (CLI)

---

## Description

> **A Python command-line application for managing student grades.**

---

## Features

- Add student
- Calculate grade
- Display student information
  
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

Utilities are helper functions. Instead of putting calculations inside `main.py` you move them here.

**Functions**:

```text
- is_valid_score()
```

**Future considerations**:

```text
- calculate_average()
- highest_score()
- lowest_score()
- pass_rate()
- class_average()
- median_average()
```

___This keeps calculations separate from the rest of the project___

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
   └───────────────────────────────────►  grade_utils.py
                                            |
                                            ▼
                                     Calculations
```

---

## Future Improvements

```text
- File Handling
- GUI
- Database
- Multiple subjects
```