"""
Grabbing json data from public API.

The API below a yahoo finance api that converts  USD into other currencies.
We will pull down the data, convert the json to a python object and parse out some information 
"""
import json
from urllib.request import urlopen, Request   # built-in module that allows us to make requests to the web api.

url = "https://api.frankfurter.dev/v1/latest?from=USD" 


# CAUTION: Some servers may reject requests made with urllib's default
# User-Agent header, since it can look like it's coming from a script
# rather than a browser. If you get a 403 Forbidden error using only
# the default headers, this could be the reason — try setting a custom
# User-Agent before assuming the API itself is blocking you.


req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

# Let the url be the response
with urlopen(req) as response:
    # assign a source variable to read the response using the .read() method
    source = response.read()
print(source)


# loading the into a python object
data = json.loads(source)



# Dumping with a string
print(json.dumps(data, indent=2, sort_keys=True))
