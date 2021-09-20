#4A robot moves in a plane starting from the original point (0,0).
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(round(math.sqrt(pos[1]**2+pos[0]**2)))
