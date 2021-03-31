from collections import defaultdict
from rich import print as rprint
import time

rprint('-' * 20, 'Speed Test', '-' * 20)
dd = defaultdict(int)
l = [*range(1, 1000000)]

for i in l:
	# The default value is 0 so there is not need
	# to enter the key first
	dd[i - 1] = i

d = {i: i + 1 for i in range(999999)}

rprint('[yellow]Dictionary')
for _, val in d.items():
	val
stop_time = time.time()
td = stop_time - start_time
rprint('[green]Total time taken to access the elements:', td)
print('-'*40)
rprint('[yellow]Defaultdict')
start_time = time.time()
for _, val in dd.items():
	val
stop_time = time.time()
tdd = stop_time - start_time
rprint('[green]Total time taken to access the elements:', tdd)