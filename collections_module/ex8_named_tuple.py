from collections import namedtuple
from rich import print as rprint

student = namedtuple('Student', ['name', 'age', 'dob'])

s = student('Luffy', 19, '12312312')

# _fields :- This function is used to return all the 
# keynames of the namespace declared.
rprint(s._fields)

# _replace() :- This function is used to change 
# the values mapped with the passed keyname.
rprint(s._replace(dob='344567'))