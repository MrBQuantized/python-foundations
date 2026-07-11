# Python Foundations

A structured repository documenting my journey from Python fundamentals to advanced software engineering concepts, automation, and real-world projects.

This repository serves as both a personal knowledge base and a portfolio of hands-on Python practice. Rather than simply completing tutorials, I organize concepts, experiments, notebooks, and projects in a way that allows me to revisit, improve, and build upon them over time.

## Repository Structure

```text
python-foundations/
├── .gitignore
├── README.md
├── 01_CORE/
│   ├── data_types/
│   ├── control_flow/
│   ├── functions/
│   └── modules/
├── 02_OOP_AND_INTERMEDIATE/
│   ├── oop/
│   ├── exceptions/
│   ├── file_handling/
│   ├── comprehensions/
│   ├── regular_expressions/
│   ├── itertools/
│   └── collections/
├── 03_ADVANCED/
│   ├── decorators/
│   ├── generators/
│   ├── iterators/
│   ├── context_managers/
│   ├── concurrency/
│   ├── type_hints/
│   ├── dataclasses/
│   └── unit_testing/
├── 04_SOFTWARE_ENGINEERING/
│   ├── git/
│   ├── github/
│   ├── virtual_environments/
│   ├── pip/
│   ├── pipenv/
│   ├── poetry/
│   ├── conda/
│   ├── environment_variables/
│   ├── setting_path/
│   ├── switching_python_versions/
│   ├── packaging/
│   └── ci_cd/
├── 05_EXERCISES/
│   ├── dsa/
│   └── ... (topic-based practice sets, WIP until finished)
├── 06_PROJECTS/
│   ├── mini_projects/
│   ├── api_projects/
│   ├── csv_to_html/
│   ├── file_organizer/
│   ├── excel_automation/
│   └── pdf_automation/
├── _WIP/                  (in-progress project work, local reference only)
└── Tutorials/              (downloaded course videos, local reference only)
```

## Topics Covered

### 01 — Core

* Data types: strings, integers/floats, lists/tuples/sets, dictionaries
* Control flow: conditionals, loops, iteration
* Functions
* Standard library modules: `os`, `pathlib`, `datetime`, `csv`, `json`, `sqlite3`, `subprocess`

### 02 — OOP and Intermediate

* Classes and objects, inheritance, encapsulation, abstraction, polymorphism
* Instance vs. class/static methods and attributes
* Exception handling and file handling
* Comprehensions, regular expressions, itertools, collections

### 03 — Advanced

* Decorators, generators, iterators, context managers
* Concurrency (threading, asyncio)
* Type hints, dataclasses
* Unit testing (`unittest`, `pytest`)

### 04 — Software Engineering

* Git and GitHub
* Virtual environments (venv, pipenv, poetry, conda)
* Environment variables, PATH configuration, switching Python versions
* Packaging and CI/CD fundamentals

### 05 — Exercises

* Topic-based practice sets (conditionals/loops, dictionaries, functions, file handling, OOP)
* Data Structures & Algorithms notebooks
* Kept as work-in-progress until each set is complete, then tracked in git

### 06 — Projects

* Mini projects: bank account system, student grade system
* API projects: working with `requests` and REST APIs
* Automation projects: CSV-to-HTML, file organizer, Excel automation, PDF automation

## Repository Goals

This repository is intended to:

* Build a strong foundation in Python
* Practice writing clean and maintainable code
* Explore Python's standard library
* Develop software engineering best practices
* Create progressively more complex projects
* Serve as a long-term reference for future AI, automation, and backend development

## Technologies

* Python 3
* Jupyter Notebook
* Git
* GitHub

## Notes

Most folders contain both notebooks used for learning and standalone Python scripts used for experimentation and implementation. `_WIP/` holds project work that's genuinely in progress and is excluded from version control entirely — once a project is finished, it moves into its proper home under `06_PROJECTS/` and becomes visible in the repo for the first time. `Tutorials/` holds downloaded course videos for personal reference only and is likewise excluded from version control entirely.

As I continue learning, existing code will be refactored and improved to reflect better design practices and cleaner architecture.

---

*This repository is actively maintained as part of my software engineering and AI learning journey.*