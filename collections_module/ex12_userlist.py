from collections import UserList

li = [*range(10)]

# Creating an empty UserList
custom_dict = UserList()
print(custom_dict.data)

custom_dict = UserList(li)
print(custom_dict.data)

# Creating a custom dictionary where deletion is not allowed
class MyList(UserList):

	def pop(self, s=None):
		raise RuntimeError("Deletion not allowed")

	def remove(self, s=None):
		raise RuntimeError("Deletion not allowed")


nl = MyList(li)
print("Original dictionary:", li)
li.pop()
print("Original dictionary after deleting one element:", li)
print("Custom dictionary:", nl)
nl.pop()
print("Custom dictionary after deleting one element:", nl)
