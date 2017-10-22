from itertools import combinations
s, k = raw_input().split(); k = int(k); s = sorted(list(s))
for j in range(1, k+1):
     for i in sorted(combinations(s,j)):
            print ''.join(i)