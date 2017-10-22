K, rooms = input(), map(int, raw_input().split())
roomKeys = map(lambda x: x*K,set(rooms))
print (sum(roomKeys)-sum(rooms))//(K-1)