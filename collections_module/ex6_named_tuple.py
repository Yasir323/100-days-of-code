"""
Like dictionaries they contain keys that are hashed 
to a particular value. But on contrary, it supports 
both access from key value and iteration, the 
functionality that dictionaries lack.
"""
from collections import namedtuple
from rich import print as rprint

student = namedtuple('Student', ['name', 'age', 'dob'])

s = student('Luffy', 19, '12312312')

rprint(s)

# Access by key
rprint(s.name)
# Access by index
rprint(s[1])
# Access by key like dictionary gives error
# rprint(s['dob']) ## Typeerror: Key must be integer

# Access using getattr
rprint(getattr(s, 'dob'))