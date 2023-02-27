#queue (double ended queue)
from collections import deque

queue = deque()

queue.append(1)
queue.append(1)
print(queue)

queue.popleft() #constant time unlikely like stacks
print(queue)

##add values in the left
queue.appendleft(3)
print(queue)

#pop right
queue.pop()
print(queue)