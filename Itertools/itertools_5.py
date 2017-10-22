from itertools import groupby
S = list(raw_input().strip())
for c, k in groupby(S):
    print '(%d, %d)' % (len(list(k)), int(c)),