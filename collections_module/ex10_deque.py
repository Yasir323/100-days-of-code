from collections import deque
from rich import print as rprint
import numpy as np 
from array import array
import time

li = [*range(100000)]
arr = array('i', [*range(100000)])
nparr = np.array([*range(100000)])
queue = deque([*range(100000)])

t_li = 0
t_arr = 0
t_nparr = 0
t_queue = 0

start_time = time.time()
for i in range(100000):
	li.pop(0)
stop_time = time.time()
t_li = stop_time - start_time
rprint("[yellow]Time taken to remove all the elements of a list of size 100000 is:", t_li)

start_time = time.time()
for i in range(100000):
	arr.pop(0)
stop_time = time.time()
t_arr = stop_time - start_time
rprint("[yellow]Time taken to remove all the elements of a array of size 100000 is:", t_arr)


start_time = time.time()
for i in range(100000):
	np.delete(nparr, 0)
stop_time = time.time()
t_nparr = stop_time - start_time
rprint("[yellow]Time taken to remove all the elements of a NumPy Array of size 100000 is:", t_nparr)


start_time = time.time()
for i in range(100000):
	queue.popleft()
stop_time = time.time()
t_queue = stop_time - start_time
rprint("[yellow]Time taken to remove all the elements of a deque of size 100000 is:", t_queue)

# So as we can see, popping elements from either side of the 
# deque takes equal time. If we only want to pop the last element
# list is the fastest but if we want to pop from bith sides
# deque is better. Same goes for append.
# Array is slower than list and Numpy arrays are really slow in these
# situations.