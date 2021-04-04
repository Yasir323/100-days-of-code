from collections import UserString

d = 12344

# Creating an UserDict
userS = UserString(d)
print(userS.data)
  
  
# Creating an empty UserDict
userS = UserString("")
print(userS.data)


# Creating a Mutable String
class Mystring(UserString):
	  
	# Function to append to
	# string
	def append(self, s):
		self.data += s
		  
	# Function to rmeove from 
	# string
	def remove(self, s):
		self.data = self.data.replace(s, "")
	  
# Driver's code
s1 = Mystring("Dinosaur")
print("Original String:", s1.data)
  
# Appending to string
s1.append("s")
print("String After Appending:", s1.data)
  
# Removing from string
s1.remove("s")
print("String after Removing:", s1.data)
