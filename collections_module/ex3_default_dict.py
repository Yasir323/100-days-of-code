"""
A DefaultDict is also a sub-class to dictionary.
It provides a default value for the key that does 
not exists. and never raises a KeyError.

Syntax:

'class collections.defaultdict(default_factory)'

default_factory is a function that provides the 
default value for the dictionary created. If this 
parameter is absent then the KeyError is raised.
"""
from collections import defaultdict
from rich import print as rprint
dd = defaultdict(int)

l = [*range(1, 10)]

for i in l:
	# The default value is 0 so there is not need
	# to enter the key first
	dd[i - 1] = i

rprint('Defaultdict:', dd)

d = {i: i + 1 for i in range(9)}
rprint('Regular Dictionary:', d)
