# USERDICT
"""
Python supports a dictionary like a container called 
UserDict present in the collections module. This 
class acts as a wrapper class around the dictionary 
objects. This class is useful when one wants to 
create a dictionary of their own with some modified 
functionality or with some new functionality. It 
can be considered as a way of adding new behaviors 
for the dictionary. This class takes a dictionary 
instance as an argument and simulates a dictionary 
that is kept in a regular dictionary. The dictionary 
is accessible by the data attribute of this class.
"""

from collections import UserDict

d = {
	'a': 1,
	'b': 2,
	'c': 3
}

# Creating an empty UserDict
custom_dict = UserDict()
print(custom_dict.data)

custom_dict = UserDict(d)
print(custom_dict.data)

# Creating a custom dictionary where deletion is not allowed
class MyDict(UserDict):
	# pass
	def __del__(self):
		raise RuntimeError("Deletion not allowed")

	def pop(self, s=None):
		raise RuntimeError("Deletion not allowed")

	def popitem(self, s=None):
		raise RuntimeError("Deletion not allowed")


nd = MyDict(d)
print("Original dictionary:", d)
d.popitem()
print("Original dictionary after deleting one element:", d)
print("Custom dictionary:", nd)
nd.popitem()
print("Custom dictionary after deleting one element:", nd)
