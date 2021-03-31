"""
An OrderedDict is also a sub-class of dictionary
but unlike dictionary, it remembers the order in
which the keys were inserted. 
As of Python 3.7, a new improvement to the dict
built-in is:

    The insertion-order preservation nature of 
    dict objects has been declared to be an official
    part of the Python language spec.

This means there is no real need for OrderedDict 
anymore. They are almost the same.
"""

from collections import OrderedDict
from rich import print as rprint

d = {'b': 1, 'a': 2}
od = OrderedDict([('b', 1), ('a', 2)])

# they are equal with content and order
assert d == od, "They are not equal"
assert list(d.items()) == list(od.items()), "The items are not same"
assert repr(dict(od)) == repr(d), "The raw representation is not same"