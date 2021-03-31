"""
A counter is a sub-class of the dictionary.
It is used to keep the count of the elements
in an iterable in the form of an unordered
dictionary where the key represents the element
in the iterable and value represents the count
of that element in the iterable.
"""

from collections import Counter
from rich import print as rprint

# With sequence of items
rprint(Counter(['B', 'B', 'A', 'B','C','A','B',
               'B','A','C']))

# With dictionary
rprint(Counter({'A': 3, 'B': 5, 'C': 2}))

# With kwargs
rprint(Counter(A=3, B=5, C=2))