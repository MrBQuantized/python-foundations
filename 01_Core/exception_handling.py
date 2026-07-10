# How to handle errors and exceptions in python

# To understand this concept let's try an open a file

f = open('testfile.txt')  

try:
    pass
except Exception:
    pass

    """We insert portions of our codes that we expect to return an 
    error into the exception handling by placing it under the 'try' statement
    """

try:
    f = open('text.txt')
except Exception:
    print("Sorry. This file does not exist")

try:
    f = open('test_file.txt')
except Exception:
    print("Sorry. This file does not exist")


try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print("Something went wrong")


try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e) 
