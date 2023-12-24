from utils import get_ints_from_str
from dataclasses import dataclass
import math

large = True

if large:

    MINX = 200000000000000
    MAXX = 400000000000000
    MINY = MINX
    MAXY = MAXX
    fn = 'day24.txt'
else:
    MINX = 7
    MAXX = 27
    MINY = 7
    MAXY = 27
    fn = 'small.txt'

def same_sign(a, b):
    return (a >= 0) == (b >= 0)

@dataclass
class Equation:
    pts: list
    vel: list
    i: int

    def __init__(self, pts, vel, i):
        self.pts = pts
        self.vel = vel
        self.i = i
        pts2 = [pts[X] + vel[X], pts[Y] + vel[Y]]
        self.a = (pts2[Y] - pts[Y]) / (pts2[X] - pts[X])
        self.b = pts[Y] - self.a * pts[X]

    def __repr__(self):
        return f"{self.a}x + {self.b} = ({self.pts[X]} , {self.pts[Y]}), vx {self.vel[X]}, vy {self.vel[Y]}"

    def __str__(self):
        return self.__repr__()

    def is_after(self, x, y):
        x1 = self.pts[X]; y1 = self.pts[Y]

        tx = (x - x1) / self.vel[X]
        ty = (y - y1) / self.vel[Y]

        print(f"tx {tx} ty {ty}")
        assert(math.isclose(tx, ty, abs_tol=0.0001))

        if tx < 0:
            return False

        return True

    def get_y(self, x):
        return self.a*x + self.b

    def get_intersection(self, other):
        a1 = self.a; b1 = self.b
        a2 = other.a; b2 = other.b
        if a1 == a2:
            #print(f"Parallel linez {self}, {other}")
            assert(b1!=b2)
            return None
        x = (b1-b2) / (a2-a1)
        y = self.get_y(x)
        return x,y

    def intersect(self, other):
        ix = self.get_intersection(other)
        if ix is None:
            return False
        x,y = ix
        print(f"Intersection at {x}, {y}")
        if x < MINX or x > MAXX or y < MINY or y > MAXY:
            return False
        if self.is_after(x,y) and other.is_after(x,y):
            print("good")
            return True
        return False



X = 0
Y = 1
Z = 2


eqs = []

with open(fn, 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        pts, vel = line.split("@")
        pts = get_ints_from_str(pts)
        vel = get_ints_from_str(vel)

        eqs.append(Equation(pts, vel, i))
        print(eqs[-1])




#eqs[0].intersect(eqs[1])

#import sys
#sys.exit(0)

n = len(eqs)
ans = 0
for i, eq1 in enumerate(eqs):
    for j in range(i+1, n):
        eq2 = eqs[j]
        if eq1.pts == eq2.pts:
            print("We are at same point in the beginning")
            ans+=1
            continue
        if eq1.intersect(eq2):
            ans+=1

print(ans)
