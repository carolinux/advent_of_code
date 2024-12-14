
import sys
import re
import math
import copy
from PIL import Image

fn = sys.argv[1]

if fn == "small.txt":
    ro = 7
    co = 11
    n = 12
    targrows = 3 # for 9
else:
    ro = 103
    co = 101
    n = 500
    targrows = 22 # for 484

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

xys = set()

for _ in range(n):
    s = input().strip()
    # parse the regex for p=0,4 v=3,-3
    x,y, vx, vy = map(int, re.findall(r"(-?\d+)", s))
    xys.add((x, y))
    robots.append(Robot(x, y, vx, vy, ro, co))

def top(i, j, rows, grid):
    for row in range(rows):
        st = j - row
        end = j + row + 1
        currr = i + row


        for col in range(st, end, 1):
            if col<0 or currr<0 or col>=len(grid[0]) or currr>=len(grid):

                return False
    return True

def detect(grid, iter):
    for i in range(ro):
        for j in range(co):
            if grid[i][j] > 0:
                # see if we are a top of the tree
                good = top(i, j, 3, grid)
                if good:
                    return True
                #if stacked > 1:
                #    raise Exception(f"found partial tree at {iter} from {i, j}, stacked={stacked}")
    return False

def create_pixel_image(grid, output_file):
    """
    Creates a pixel image from a grid and writes it to a file.

    Cells with value > 1 are black, and the rest are white.

    Args:
        grid (list of lists): 2D grid of numeric values.
        output_file (str): Output file path (e.g., "output.png").
    """
    # Get grid dimensions
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    # Create a new image (mode "1" for 1-bit pixels: black and white)
    img = Image.new("1", (width, height))

    # Populate the image
    for y in range(height):
        for x in range(width):
            # Set pixel: 0 (black) if grid[y][x] > 1, else 1 (white)
            img.putpixel((x, y), 0 if grid[y][x] >= 1 else 1)

    # Save the image
    img.save(output_file)
    print(f"Image saved to {output_file}")

def print_grid(robots, out=True):
    grid = [[0 for _ in range(co)] for _ in range(ro)]
    for i,r in enumerate(robots):
        grid[r.y][r.x] = 1
    if out:

        if isinstance(out, str):
            create_pixel_image(grid, out)
        else:
            for row in grid:
                print("".join(map(str, row)))
            print()
    return grid

grid = print_grid(robots, out=True)
for i in range(ro*co):

    for r in robots:
        r.move()
    print_grid(robots, out=f"seqs/{i+1}.png")


sys.exit(0)


for i, r in enumerate(robots):
    visited = []
    visited.append((r.y, r.x))
    visset = set()
    visset.add((r.y, r.x))

    while True:
        r.move()
        if (r.y, r.x) in visset:
            break

        visited.append((r.y, r.x))

        visset.add((r.y, r.x))

    print(f"Robot {i} has cycle {len(visited)} vs {ro*co}")








