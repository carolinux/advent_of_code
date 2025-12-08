
import sys
import re

fn = sys.argv[1]

if fn == "small.txt":
    ro = 7
    co = 11
    n = 12
else:
    ro = 103
    co = 101
    n = 500

class Robot:
    def __init__(self, x, y, vx, vy, ro, co):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ro = ro
        self.co = co

    def move(self):
        self.x = (self.x + self.vx) % self.co
        self.y = (self.y + self.vy) % self.ro

    def __str__(self):
        return f"Robot(x={self.x}, y={self.y}, vx={self.vx}, vy={self.vy})"

    def __repr__(self):
        return self.__str__()


robots = []

for _ in range(n):
    s = input().strip()
    # parse the regex for p=0,4 v=3,-3
    x,y, vx, vy = map(int, re.findall(r"(-?\d+)", s))
    robots.append(Robot(x, y, vx, vy, ro, co))

def detect(grid):
    for i in range(ro//2):
        mid = co//2
        if grid[i][mid+i] < 1 or grid[i][mid-i] <1:
            return False
    return True

def print_grid(robots):
    grid = [[0 for _ in range(co)] for _ in range(ro)]
    for r in robots:
        grid[r.y][r.x]+=1
    for row in grid:
        print("".join(map(str, row)))
    print()
    return grid

for i in range(7073701):
    print(f"i={i}")
    #grid = print_grid(robots)
    #if detect(grid):
    #    raise Exception("found")
    for r in robots:
        r.move()
    if i > 7073690:
        print_grid(robots)



q1 = 0
q2 = 0
q3 = 0
q4 = 0
for r in robots:
    # find in which quadrant it is, ignoring the center
    if r.x < co//2 and r.y < ro//2:
        q1+=1
    elif r.x > co//2 and r.y < ro//2:
        q2+=1
    elif r.x < co//2 and r.y > ro//2:
        q3+=1
    elif r.x > co//2 and r.y > ro//2:
        q4+=1

print(q1*q2*q3*q4)




