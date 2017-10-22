n = input()
s = set(map(int, raw_input().split())) 
N = input()
for i in xrange(N):
    func = raw_input().split()
    if 'pop' in func:
        s.pop()
    elif 'discard' in func:
        s.discard(int(func[1]))
    elif 'remove' in func:
        s.remove(int(func[1]))
print sum(s)