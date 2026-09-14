"""
Practice script for Python.

More exercises on csv module

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / "sample_names_20.csv"

# =================================================
# Example 1: Writing and Reading to a CSV file 
# =================================================

# Method 1. Use  `w+` and `seek(0)` — Open once for both read/write
# This opens the new file, writes to it, then rewinds and reads it back.

with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
   
    # w+ = create/write + read. truncates file if it exists
    # with open(BASE_DIR / 'new_names_2.csv', 'w+', newline="") as new_file:
        # csv_writer = csv.writer(new_file, delimiter='\t')

        # # 1. WRITE
        # for line in csv_reader:
        #     csv_writer.writerow(line)

        # # 2. REWIND to the sbeginning so we can read what we just wrote
        # new_file.seek(0)

        # # 3. READ what we just wrote
        # print(f"\n--- Reading back the new file immediately ---\n")
        # csv_reader2 = csv.reader(new_file, delimiter='\t')
        # for row in csv_reader2:
        #     print(row)

# Method 2. Write to list first, then write + print
# It simpler if the file isn't huge. No 2nd open needed

# with open(FILE, 'r', newline="") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     all_rows = list(csv_reader)  # load everything to memory

#     with open(BASE_DIR / 'new_names_2', 'w', newline="") as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for line in all_rows:
#             csv_writer.writerow(line)
#             print(line)

# Method 2. Use  `r+` method:  Read + Write without closing
# r+ = open existing file for both reading and writing. File must already exist
# `flush()` and `seek(0)` — Open once for both read/write
# This opens the new file, writes to it, then rewinds and reads it back.

NEW_FILE = BASE_DIR / "new_file.csv"

# Make the sure that the file exists
NEW_FILE.touch()

with open(NEW_FILE, 'r+', newline="") as file:          # r+ = read + write
    csv_reader = csv.reader(file, delimiter='\t')
    csv_writer = csv.writer(file, delimiter='\t')

    # 1. WRITE: write all data
    with open(FILE, 'r', newline="") as csv_file:  
        csv_reader_orig = csv.reader(csv_file)
        for line in csv_reader_orig:
            csv_writer.writerow(line)

    # 2. IMPORTANT: flush buffer + rewind cursor to start
    file.flush()       # make sure all writes hit disk
    file.seek(0)       # move cursor back to line 1

    # 3. READ: read back what we just wrote
    print(f"\n--- Reading back with r+ ---\n")
    for row in csv_reader:
        print(row)