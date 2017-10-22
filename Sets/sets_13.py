A = set(map(int, raw_input().split()))
n = input()
L = []
for i in xrange(n):
    B = set(map(int, raw_input().split()))
    L.append(A.issuperset(B))
    
print False not in L