from collections import deque
from rich import print as rprint

"""
Deque (Doubly Ended Queue) in Python is 
implemented using the module “collections“. 
Deque is preferred over list in the cases where 
we need quicker append and pop operations from 
both the ends of container, as deque provides an 
O(1) time complexity for append and pop operations 
as compared to list which provides O(n) time 
complexity.
"""

queue = deque(['Luffy', 'Zoro', 'Nami', 'Ussop', 'Sanji'])
rprint("Queue:", queue)

# Append at the end
queue.append('Chopper')
rprint("After adding element to the right:", queue)

# Append at the start
queue.appendleft('Garp')
rprint("After adding element to the left:", queue)

# Remove from the end
queue.pop()
rprint("After removing an element from the right:", queue)

# Remove from the start
queue.popleft()
rprint("After removing an element from the left:", queue)

# Search an element
queue = deque([1, 2, 3, 3, 4, 2, 4])
print("Searching for an element 4:", queue.index(4, 2, 5))
"""
This function returns the first index of the value 
mentioned in arguments, starting searching from beg 
till end index.
"""

# Inserting an element
queue.insert(4, 3)
print("After inserting an element 3 at position 4:", queue)

# Removing an element
queue.remove(3)
# Removes the first occurrence of 3
print("After removing the first occurrence of 3:", queue)

# Count the number of occurrences of an element
print("Counting the number of occurrences of 3:", queue.count(3))

# Add elements from an iterable
ls = [89, 98, 78, 87]
queue.extend(ls)
queue.extendleft(ls) # Appends the list in reversed order
rprint("After extending from the right and left:", queue)

# Rotate
queue.rotate(1) # Rotates to the right
# Provide a negative value to rotate left
rprint("After rotating right:", queue)

# Reversing the list
queue.reverse()
rprint("After reversing:", queue)

# Clearing  the list
queue.clear()
print("After clearing the list:", queue)