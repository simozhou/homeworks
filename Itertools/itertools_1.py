from itertools import product
A, B = map(int, raw_input().split()), map(int, raw_input().split())
for i in sorted(product(A,B)):
    print i,