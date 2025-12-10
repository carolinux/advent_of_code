from matplotlib import pyplot as plt


pts = []
n = 0
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        a,b = line.strip().split(',')
        pts.append((int(a),int(b)))

fig, ax = plt.subplots()

for i in range(len(pts)):
    p1 = pts[i]
    p2 = pts[(i + 1) % len(pts)]  # Wrap around to first point
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b-', alpha=0.6)

# Plot the points themselves
x_coords = [p[0] for p in pts]
y_coords = [p[1] for p in pts]
ax.scatter(x_coords, y_coords, c='red', s=10    )

# Add index labels to each point
for i, (x, y) in enumerate(pts):
    ax.text(x, y, str(i), fontsize=8, ha='right', va='bottom')

# the solution found in sol2.py
lines = [((5921, 67692), (94901, 50265))]

j = 0
for pt1,pt2 in lines:

    rect_x = [pt1[0], pt2[0], pt2[0], pt1[0], pt1[0]]
    rect_y = [pt1[1], pt1[1], pt2[1], pt2[1], pt1[1]]

    ax.plot(rect_x, rect_y, linewidth=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Lines between consecutive points')
ax.grid(True, alpha=0.3)
ax.axis('equal')
ax.legend()
plt.show()
j+=1

