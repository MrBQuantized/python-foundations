"""
Exercise with StackOverflow
"""

import requests
import json

# Define a variable as the response to our requests
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response)          # returns a status code: 200 OK
# print(response.json())   # returns the data in json format 

# We can also extract key-values from the json file
# print(response.json()['items'])   # returns the values of the the key 'items' which is a list

# # or even index the the keys which list of dictionaries
# print(response.json()['items'][0])   

# We can iterate over the reponse
# for data in response.json()['items']:
#     print(data['title'])    # displays the titles
#     print(data['link'])     # displays the links
#     print()                 # separate the each title cand link from the others

# We could set a conditions
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])    
        print(data['link'])      
    else:
        print('skipped')
        print()