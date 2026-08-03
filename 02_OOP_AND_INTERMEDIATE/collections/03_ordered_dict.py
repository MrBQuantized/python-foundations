"""
OrderedDict

An ordered dictionary is a dictionary that preserves the order of the keys that are inserted. 
If the key order is important for any application, then OrderedDict can be used:
    
    od = OrderedDict([items])
"""

from collections import OrderedDict

# The dictionary follows the order in which the elements where inserted
ordered_dict = OrderedDict()
ordered_dict['e'] = 5     
ordered_dict['b'] = 2    
ordered_dict['c'] = 3    
ordered_dict['d'] = 4    
ordered_dict['a'] = 4

print(ordered_dict)
