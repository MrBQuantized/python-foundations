"""
Shutil is a Python module foor advanced file handling
"""
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

print(BASE_DIR)

SOURCE_DIR = BASE_DIR / 'source_dir'
NEW_DIR = BASE_DIR / 'new_dir'
SAMPLE_DIR = BASE_DIR / 'sample_files'
VIDEOS_DIR = BASE_DIR / 'sample_videos'
DESTINATION = BASE_DIR / 'destination'
print(NEW_DIR)

 
# ===================================== 
# Copying Files & Directories
# =====================================
# You can make a copy of a file or directory
# For file
# shutil.copy(BASE_DIR / 'first.txt', BASE_DIR / 'second.txt')

# shutil.copytree(SOURCE_DIR, NEW_DIR)

# Ignoring specific files while copying a directory
# We define a function that can perform this filtering
def ignore_specific_files(directory, files):
    return [f for f in files if f.endswith('.txt') or 'invoice' in f]
    
# we can exclude either patterns or individual files



# shutil.copytree(SAMPLE_DIR, DESTINATION, ignore=ignore_specific_files)

 
# ===================================== 
# Moving Files & Directories
# =====================================
# Moving a file
# shutil.move(SAMPLE_DIR /'invoice-2023-08-01.pdf', DESTINATION)

# ===================================== 
# Removing a Directory
# =====================================
# shutil.rmtree(SOURCE_DIR)

# ===================================== 
# Getting Information 
# =====================================

# total, used, free = shutil.disk_usage('/')
# print(total, used, free)
def output_format(information: tuple):
    SECTION_LINE =  "=" * 60
    FOOTER_LINE = '-' * 60
    print(SECTION_LINE)
    print(f"STORAGE INFO\n{SECTION_LINE}")
    
    for name, value in zip(disk._fields, disk):
        total = disk.total
        pct = value / total 
        print(f"{name.capitalize()} Space: {value:,} bytes;  {pct:.2%}")
    print(FOOTER_LINE)


disk = shutil.disk_usage('/')

# output_format(disk)

# ===================================== 
# Copying Metadata
# =====================================
# shutil.copystat(NEW_DIR / "first.txt", NEW_DIR / 'second.txt') # metdata of first.txt gets copied to second.txt

# ===================================== 
# Changing File Ownership
# =====================================

# shutil.chown(BASE_DIR, user='OnohLabs') # Requires admin priviledges to make such changes
# But still executable in terminal using:
#   sudo python 3 script_name.py

# ===================================== 
# Finding Excutables location
# =====================================
# Finding Python: use either python or python3
# python_path = shutil.which('python')
# executable = (python_path.split())[-1].lower()
# print(executable)

# ===================================== 
# Unpacking and Creating Archives
# =====================================
# Create archive 'myarchive'
# shutil.make_archive('myarchive', 'zip', NEW_DIR)

# Unpacking the archive
# shutil.unpack_archive(NEW_DIR / 'myarchive.zip')
print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())