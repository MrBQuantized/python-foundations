"""
Practice script for Python.

Topic: CSV Module

CSV stands for "Comma-Separated Values." A CSV file stores tabular data
as plain text, with each line representing a row and commas separating
the individual values (fields) within that row.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / "sample_names_20.csv"

# =================================================
# Example 1: Reading CSV Files
# =================================================

# Opening a file and creating a reader doesn't read any data yet —
# csv_reader is just an iterator object sitting in memory.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)    # Prints only an object in memory

# Iterating over the reader yields each row as a list of strings.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)  # Prints all the rows

# Each row is a list of strings: first_name, last_name, email.
# The header row lists these field names, and each value in a data row
# can be accessed by its column index, e.g. line[index].

# A fresh reader is needed here since the previous one has already been
# fully consumed by the loop above.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])  # Prints all the emails

# We can skip the header row by calling next() once before the loop.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # Skip the header row

    for line in csv_reader:
        print(line[2])

# =================================================
# Example 2: Writing to CSV Files
# =================================================
# Let's try saving the same values to a new file, using a different
# delimiter this time.

# Open the original file for reading
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open a new file for writing
    with open(BASE_DIR / 'new_names.csv', 'w', newline="") as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')  # Second argument sets the delimiter to "-"

        # Write out each row from the original file to the new file
        for line in csv_reader:
            csv_writer.writerow(line)

# The CSV module distinguishes hyphenated values from delimiters by
# quoting the value. For example:
#   William-Smith-"william-smith6@example.com"
#   "Benjamin-Smith"-benjamin.smith7@example.com

# Another common delimiter is tab (\t)
with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open a new file for writing
    with open(BASE_DIR / 'new_names_2.csv', 'w', newline="") as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

# =================================================
# Example 3: Reading CSV Files with a Specific Delimiter
# =================================================
# When reading a CSV file with a delimiter other than a comma, we need
# to specify it via the delimiter argument in reader(); otherwise, each
# row is printed as a single, undivided value.

with open(BASE_DIR / 'new_names_2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # No delimiter specified

    for line in csv_reader:
        print(line)

with open(BASE_DIR / 'new_names_2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")  # Delimiter specified

    for line in csv_reader:
        print(line)
print()

# =================================================
# Example 4: Dictionary Reader — DictReader()
# =================================================
# With DictReader, each row is returned as an OrderedDict, with the
# header row's field names used as keys.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)

# We can access values by field name instead of by index.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])

# =================================================
# Example 5: Dictionary Writer — DictWriter()
# =================================================
# With DictWriter, we need to pass in the field names.
with open(FILE, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(BASE_DIR / 'new_names_3.csv', 'w', newline="") as new_file:
        # Provide the field names
        fieldnames = ['first_name', 'last_name', 'email']

        # Set up the writer with the field names
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # Write out the header row
        csv_writer.writeheader()  # Optional

        # Write out each row from the original file to the new file
        for line in csv_reader:
            csv_writer.writerow(line)

# To write out only a subset of fields, list just the field names we
# want and delete the remaining key(s) from each row before writing.

with open(FILE, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(BASE_DIR / 'new_names_4.csv', 'w', newline="") as new_file:
        # Select only the field names we need
        fieldnames = ['first_name', 'last_name']

        # Set up the writer with the field names
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # Write out the header row
        csv_writer.writeheader()  # Optional

        # Write out each row from the original file to the new file
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)