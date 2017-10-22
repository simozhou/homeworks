N = input()
A = set(map(int, raw_input().split()))
n = input()

for _ in xrange(n):
    func, m = raw_input().split()
    B = set(map(int, raw_input().split()))
    if func == 'update':
        A |= B
    elif func == 'intersection_update':
        A &= B
    elif func == 'difference_update':
        A -= B
    elif func == 'symmetric_difference_update':
        A ^= B
        
print sum(A)