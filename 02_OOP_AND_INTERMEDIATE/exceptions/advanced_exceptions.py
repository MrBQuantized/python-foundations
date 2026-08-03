"""
Exercises on Advanced exceptions
"""


# try: 
#     print(10/0)
# except Exception:
#     print("Error occured! Division failed")


# # ignoring an exception
values = [10, 5, 6, 0, 9, 8, 2]

# for value in values:
#     try:
#         print(10 / value)
#     except:
#         pass    # this will ignore the exception.

# =================================== 
# Best Practices
# =================================== 
# Be explicit:  Exceptions should be explicitly stated.
# for value in values:
#     try:
#         print(10 / value)
#         print(int('Hello'))
#     except ZeroDivisionError as e:      # ZeroDivision is an explicit exception
#         print(str(e))  
#     except ValueError as v:
#         print(v)

# If we include the general/broad exception clause just in case we get unexpected errors, we should log it.
import logging

values = [10, 5, 6, 0, 9, 8, "Hello", 2]

for value in values:
    try:
        print(10 / int(value))
    except ValueError as e:
        print("Value error")
    except ZeroDivisionError as e:    # ZeroDivision is an explicit exception
        print("Zero division error")     
    except Exception as e:
        logging.exception(e)

print()

# We can combine exceptions if we handle them the same way

for value in values:
    try:
        print(10 / int(value))
    # Handle ValueError and ZeroDivision error the same way
    except (ValueError, ZeroDivisionError) as e:
        pass
    except AttributeError as e:
        print("Hello World!")
    except Exception as e:
        logging.exception(e)

print()

# You could do something before an exception crashes a program.

# for value in values:
#     try:
#         print(10 / int(value))
#     except ZeroDivisionError as e:
#         pass
#     except ValueError as e:
#         # do something before your program crashes.
#         print("Hello Everyone!")
#         raise
print()

# =================================== 
# Finally and Else statements
# =================================== 
# The keyword 'finally' allows the execution of anything that 
# follows under it regradless of whether an exception happens or not.

# for value in values:
#     try:
#         print(10 / int(value))
#     except ZeroDivisionError as e:
#         pass
#     except ValueError as e:
#         print("Value error")
#         raise
#     finally:
#         print("Execute no matter what")

# # The opposite of finally is else.
# else means "If there is no exception run the code"
for value in values:
    try:
        print(10 / int(value))
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        print("Value error")
        raise
    else:
        print("No exception")