from collections import deque
testcase = int(input())
for _ in range(testcase):
    n = input()
    d = deque(map(int, input().split()))
    #from biggest to smallest value
    for s in sorted(d, reverse = True):
        if d[0] == s:
            d.popleft()
        elif d[-1] == s:
            d.pop()
        else: 
            print("No")
            break
    else:
        print("Yes")
               