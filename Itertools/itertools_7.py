from itertools import product
K, M = map(int, raw_input().split())
L = list()
for _ in xrange(K):
    L.append(map(lambda x: int(x)**2, raw_input().split()[1:]))
    
magic_trio = max(product(*L), key = lambda x: sum(x)%M)
print sum(magic_trio)%M 