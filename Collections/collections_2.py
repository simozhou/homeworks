from __future__ import print_function
from collections import defaultdict
n, m = map(int,raw_input().split())
A = defaultdict(list)
B = defaultdict(list)
for i in xrange(1, n+1):
    A[raw_input()].append(i)
for i in xrange(1, m+1):
    key = raw_input()
    if key in A.keys():
        print(*A[key], sep = ' ', end = '\n')
    else:
        print(-1)