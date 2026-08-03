"""
Exercise on Json

Loading json files into python objects and 
writing them back into python 

load() and loads() methods have different functions

  load()  : loads a file into a python object
  loads() : loads a string
"""

# ============================================
# Loading json files into python objects
# ============================================
import json
import os
from pathlib import Path

PATH = Path(__file__).resolve().parents[0]
os.chdir(PATH)
# print("Current working directory: ", os.getcwd())
JSON_FILE = PATH / 'states.json'

# Load the json file 
with open(JSON_FILE) as f:
    data = json.load(f)

# Looping through the state key
for state in data['states']:
    # print(state)
    print(state['name'], state['abbreviation'])


# ============================================ 
# Writing back into python 
# ============================================
for state in data['states']:
    # Suppose we don't want the area codes
    del state['area_codes']

NEW_FILE = PATH / 'new_state.json'
# Open the file we want to write to 
with open(NEW_FILE, 'w') as file:
    json.dump(data, file, indent=2)