from collections import ChainMap
from rich import print as rprint

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)
rprint(c)
"""
As we can see a ChainMap encapsulates multiple dictionaries
into one unit. Ordering is done in case there are same 
keys in multiple dictionaries.
"""

# Lets check the value mapped to 'b'
print(c['b'])
# Print the keys
rprint(list(c.keys()))

# Print the values
rprint(list(c.values()))

# Print all the data
rprint(c.maps)

# Adding more dictionaries to the ChainMap
d4 = {'c': '7'}
c = c.new_child(d4)
rprint(c.maps)