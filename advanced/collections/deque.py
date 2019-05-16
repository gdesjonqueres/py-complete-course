# it is similar to list
# it is thread safe

from collections import deque


friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)
