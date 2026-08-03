"""
Default dictionary

The default dictionary (defaultdict) is a subclass of the built-in dictionary class (dict) that
has the same methods and operations as that of the dictionary class, with the only difference
being that it never raises a KeyError, as a normal dictionary would. defaultdict is a convenient
way to initialize dictionaries:

    d = defaultdict(def_value)
"""

from collections import defaultdict

d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a'])
# print(d['b'])

# # returns a default value of 0 for non-existing keys
# print(d['c'])


# default = defaultdict(float)
# default['a'] = 2
# default['b'] = 4
# print(default['a'])
# print(default['b'])
# print(default['c'])


dd = defaultdict(int)

for word in str.split('data python data data structure data python'):
    dd[word] += 1
print(dd)