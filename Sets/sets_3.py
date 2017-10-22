n, m = map(int, raw_input().split())
arr, aSet, bSet = map(int, raw_input().split()), set(map(int, raw_input().split())), set(map(int, raw_input().split()))

happiness = 0

for i in arr:
    if i in aSet:
        happiness += 1
    elif i in bSet:
        happiness -= 1

print happiness