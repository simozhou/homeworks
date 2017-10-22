import math
AB, BC = input(), input()
angle = math.degrees(math.atan2(AB,BC))
if abs(math.floor(angle)-angle) >= 0.5:
    print '%d°' % math.ceil(math.degrees(math.atan2(AB,BC)))
else:
    print '%d°' % math.floor(math.degrees(math.atan2(AB,BC)))

    