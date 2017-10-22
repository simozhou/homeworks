from itertools import combinations_with_replacement
s, k = raw_input().split(); k = int(k); s = sorted(list(s))
for i in sorted(combinations_with_replacement(s,k)):
    print ''.join(i)