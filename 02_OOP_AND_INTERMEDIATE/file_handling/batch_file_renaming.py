"""
Practice script for Python.

Topic: Automating File Renaming

Demonstrates using pathlib and os to locate files in a directory,
parse their names and extensions, and progressively build up a
renaming pattern from the parsed parts.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

from pathlib import Path
import os

# =================================================
# Example 1: Locating and Listing Files
# =================================================

# Change directory to the one containing the files
BASE_DIR = Path(__file__).resolve().parents[2]
print(BASE_DIR)

FILE_PATH = BASE_DIR / '02_OOP_AND_INTERMEDIATE' / 'file_handling' / 'sample_videos'
print(FILE_PATH)

os.chdir(FILE_PATH)
print(os.getcwd())  # Confirm the current working directory

# Print out all files in the directory
for f in os.listdir():
    print(f)

# =================================================
# Example 2: Splitting Filename and Extension
# =================================================
# os.path.splitext() separates the filename from its extension,
# returning a tuple: ('filename', 'extension').

for f in os.listdir():
    print(os.path.splitext(f))

# We can unpack that tuple into two variables.
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name, end='')  # Prints the filename only
    print()

# =================================================
# Example 3: Splitting the Filename on a Delimiter
# =================================================
# Let's go further by splitting each filename on its underscore
# delimiter.

# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     print(file_name.split('_'), end='')  # Returns a list of substrings
#     print()

# =================================================
# Example 4: Extracting and Formatting the Parts
# =================================================
# We can unpack the list of substrings into individual variables.

# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     f_title, f_course_head, f_course_tail, f_num = file_name.split('_')
#     # Combine course head and tail into one variable
#     f_course = f'{f_course_head} {f_course_tail}'
#
#     # Print the files in the format we want
#     print(f'{f_num}-{f_title}-{f_course}{file_ext}')

# =================================================
# Example 5: Zero-Padding and Renaming the Files
# =================================================
# We can refine f_num further by slicing off the leading "#" symbol
# and zero-padding single-digit numbers so they line up consistently.

# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#
#     f_title, f_course_head, f_course_tail, f_num = file_name.split('_')
#     f_course = f'{f_course_head} {f_course_tail}'
#
#     # Strip any stray whitespace
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num = f_num.strip()[1:].zfill(2)  # zfill(2) pads to 2 digits wide; "10" is already 2 digits, so it's unchanged.
#
#     # Rename the files using the format we want
#     new_name = f'{f_num}-{f_course}{file_ext}'
#
#     os.rename(f, new_name)

# Confirm the changes
# for f in os.listdir():
#     print(f)