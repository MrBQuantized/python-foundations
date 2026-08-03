"""
Counters

Counters are containers that stores the elements as dictionary keys and their counts as dictionary values.
    
E.g. characters: string = 'abbccc'
     counts: a=1, b=2, c=3
    
    output format
    -------------
    
    {'key': value}
    {'character': count}
"""

from collections import Counter

a : str = "aaaaaabbbbcccccdddd"
my_counter = Counter(a)

# We can now view the full dictionary, items and key and values separately
# print(my_counter)      
# print(my_counter.items())  
# print(my_counter.keys())  
# print(my_counter.values())  

# We can also view the most common items
# print(my_counter.most_common(3))       # displays a list of 3 tuples
# print(my_counter.most_common(3)[0])    # displays the tuple at index 0
print(my_counter.most_common(3)[0][0])   # displays the element at index 0 of the tuple at index 0


# We can also have a list of all the elements
print(list(my_counter.elements()))