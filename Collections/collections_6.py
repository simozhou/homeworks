from __future__ import print_function
from collections import deque
d, n = deque(), input()
for _ in xrange(n):
    cmd = raw_input().split()
    if cmd[0] == 'append':
        d.append(cmd[1])
    elif cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        d.pop()
    else:
        d.popleft()

print(*d, sep =' ', end='\n')