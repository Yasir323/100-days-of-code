from collections import namedtuple
from rich import print as rprint

student = namedtuple('Student', ['name', 'age', 'dob'])

s = student('Luffy', 19, '12312312')

li = ['Zoro', 21, '12435675']

di = {'name': 'Nami', 'age': 20, 'dob': '23546787'}

# _make() :- This function is used to return a 
# namedtuple() from the iterable passed as argument.
rprint(student._make(li))

# _asdict() :- This function returns the OrderedDict() 
# as constructed from the mapped values of namedtuple().
rprint(type(s._asdict()), s._asdict())

# using “**” (double star) operator :- This function 
# is used to convert a dictionary into the namedtuple().
rprint(student(**di))
