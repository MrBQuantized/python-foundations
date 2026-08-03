import itertools
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / 'logfile.txt'

with open(FILE, 'r') as f:
    header = itertools.islice(f, 3)             # files are also iterables

    for line in header:
        print(line, end='')