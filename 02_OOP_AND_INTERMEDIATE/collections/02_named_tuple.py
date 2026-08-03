"""
namedtuple

The namedtuple of collections provides an extension of the built-in tuple data type. 
namedtuple objects are immutable, similar to standard tuples. Thus, we can’t add new fields 
or modify existing ones after the namedtuple instance is created. They contain keys that are 
mapped to a particular value, and we can iterate through named tuples either by index or key. 
The namedtuple function is mainly useful when several tuples are used in an application and it 
is important to keep track of each of the tuples in terms of what they represent. 
In this situation, namedtuple presents a more readable and self-documenting method. 
The syntax is as follows:
    
    nt = namedtuple(typename , field_names)
"""

from collections import namedtuple

# Class creation
Point = namedtuple('Point', 'x, y')

# Create an instance
pt = Point(1, -4)

# Access the fields
print(pt.x, pt.y)