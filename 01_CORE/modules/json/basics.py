"""
Json - JavaScript Object Notation

A widely used data format for storing information.
It was initially inspired by Javascript, but it's now independent of any programming language.
Its applications includes fetching data from online APIs, configuration files and different kinds of data that can besaved on your local machine forms
"""

import json

# ============================================
# loading a Json string into a python object
# ============================================
# This is python string that is a valid json. It has a key called people which is an array of 2 more objects. Each objects contains items that are key-value pairs — similar to a dictionary
people_string = """
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
"""
# We can load the data using .loads() method
data = json.loads(people_string)
print(data)

# Json data is decoded and translated to pythlon following a conversion table.
# So a json object gets converted to a dict in python, array to list, string to string and so on..
print(type(data))  # It converts to a dictionary
print(type(data["people"]))

# We can loop through the data

for person in data["people"]:
    print(person["name"])

print()
# ============================================
# Dumping a python object into a json string
# ============================================
# We can dump a python object into a json string using the  json.dumps() method
# Suppose we want to remove the phone numbers and convert it back to a json string

for person in data["people"]:
    del person["phone"]  # deletes the phone key and values from each person

# We now dump the python object back to json string
new_string = json.dumps(data)
print(new_string)
print()  # prints a new json string with no phone number item


# ============================================
# Cleaning up the json string
# ============================================
# --- 1. Indentation ---
# We can indent levels for better readability of the result
new_string = json.dumps(data, indent=2)  # Each level gets indented twice
print(new_string)

# --- 2. Sorting ---
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
