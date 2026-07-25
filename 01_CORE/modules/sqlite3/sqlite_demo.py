"""
Python script on sqlite

Sqlite is a python module from the standard library that provides database functionality in cases where we don't want to make use of full-fledged databases like Postgresql and Mysql.
It is used for working with small and medium-sized applications with databases that live on the disk and it can be used for testing and prototyping out an application.
This database can then be ported over when the need for a larger databse arises.


Let's assume we want a database that we can add and delete employees as well as retreive employee information

The data types of Sqlite are as follows:
    NULL        :  The value is NULL value
    INTEGER     :  The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the smagnitude of the value
    REAL        :  The value is a floating point value, stored as an 8_byte IEEE floating point number
    TEXT        :  The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE)
    BLOB        :  The value is blob of data, stored exactly as it was input
"""

# ======================================================
# Creating a Database, a Table and Inserting values
# ======================================================
import sqlite3

from pathlib import Path

# Let's ensure that the object to be created is in our cwd
BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / 'employee.db'

# Connect object representing our database
conn = sqlite3.connect(FILE) 

# We can also set the connection to memory
# conn = sqlite3.connect(':memory:')  
# This makes the database to start afresh and thus, preventing errors when rerunning create statement multiple times
# You also won't insert multiple values as well


# Creating a cursor
c = conn.cursor()

# Create employees table with colummns/field names first, last and pay:
# c.execute("""CREATE TABLE employees (
#           first TEXT,
#           last TEXT,
#           pay INTEGER
#           );""")           # docstrings used for multiline strings

# conn.commit()  #  commit the connection
# conn.close()   # closes the database

# Insert a value into the table
# c.execute("INSERT INTO employees VALUES ('Blessing', 'Onoh', 160000)")   # single quotes works fine for 
# conn.commit()

# Retrieve data using SELECT and WHERE statements
# c.execute("SELECT * FROM employees WHERE last='Onoh'")
# print(c.fetchone())
# conn.commit()
# conn.close()

# Iteration methods
# c.fetchone()   # returns the next row as a in our result and none if no rows remain afterwards
# c.fetchmany()  # returns the number of rows in the argument as a list in our result and an empty list if no rows remain afterwards
# # c.fetchall()   # returns the remaining rows left as a list in our result and an empty list if no rows remain afterwards
# print(c.fetchmany(2))

# conn.commit()  #  commit the connection
# conn.close()   # closes the database

# ======================================================
# Insering multiple values using SQL syntax
# ======================================================
# Let's insert more employees
# c.execute("""INSERT INTO employees (first, last, pay)
# VALUES ('Chika', 'Onoh', 200000),
#        ('Excel', 'Onoh', 150000),
#        ('Kesandu', 'Onoh', 220000),
#        ('Richard', 'Benson', 40000),
#        ('Kalu', 'Jonathan', 150000),
#        ('Emphraim', 'Alanwoko', 130000)
# """)  
# conn.commit()
# conn.close()


# c.execute("SELECT * FROM employees WHERE last='Onoh'")  # Selecting all the columns/ field names and column with last = Onoh
# print(c.fetchmany(3))
# conn.commit()

# print(c.fetchone())           # returns the next row as a in our result and none if no rows remain afterwards
# print(c.fetchmany(5))         # returns the number of rows in the argument as a list in our result and an empty list if no rows remain 
# print(c.fetchall())           # returns the remaining rows left as a list in our result and an empty list if no rows remain afterwards

# conn.commit()  #  commit the connection
# conn.close()   # closes the database

# ======================================================
# Inserting values from Python variables into our query
# ======================================================
# We will import our Employee class

from emp_demo import Employee

# # Create instances of the class
emp_1 = Employee('John', 'Doe', 150000)
emp_2= Employee('Stanley', 'Dimples', 20000)

print(emp_1.first)
print(emp_1.last) 

print(emp_1.pay)


# # Placeholders using tuple of question marks ?
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()
# Placeholders using dicionary of keys
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
{'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
conn.commit()
# c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
# print(c.fetchall())
# c.execute("SELECT * FROM employees WHERE last=?", ('Onoh',))
# print(c.fetchall())
# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Benson'})  
# print(c.fetchall())

# conn.commit()  # commit the connection
# conn.close()   # closes the database


# ======================================================
# Application: Insert, select, update, delete
# ======================================================
# Let's create some functions and make them more pythonic by using context managers with the `with statement`.

# def insert_emp(emp):
#     with conn:      # context manager
#         c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

# def get_emps_by_name(lastname):
#      # No context manager needed here
#      c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
#      # Select all employees with the lastname
#      return c.fetchall()


# def update_pay(emp, pay):
#     with conn:
#         c.execute("""UPDATE employees SET pay = :pay
#                   WHERE first = :first AND last = :last""",
#                   {'first': emp.first, 'last': emp.last, 'pay': pay})

# def remove_emp(emp):
#     with conn:
#         c.execute("""DELETE from employees WHERE first = :first AND last = :last""",
#                   {'first': emp.first, 'last': emp.last})

# # Now we can use these custom functions to perform query operations

# # Create new emloyees
# emp_3 = Employee('Grace', 'Alakija', 150_000)
# emp_4 = Employee('Yetunde', 'Alakija', 210_000)
# emp_5 = Employee('Daniel', 'Uche', 120_000)

# # Insert new employees
# insert_emp(emp_3)
# insert_emp(emp_4)
# insert_emp(emp_5)

# # Get employees(s) with a specific last name
# emp = get_emps_by_name('Alakija')
# print(emp)

# # Update the pay of an employee
# update_pay(emp_5, 200_000)
# remove_emp(emp_4)
# remove_emp(emp_2)

# # Retrieve the employee after the update and deletion
# emp = get_emps_by_name('Alakija')
# print(emp)

# # close connection
# conn.close()