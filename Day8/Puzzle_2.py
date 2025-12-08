import os
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Parse junction boxes
boxes = [tuple(map(int, line.split(","))) for line in lines]
n = len(boxes)

# Calculate all pairwise distances and sort
pairs = []
for i in range(n):
    for j in range(i + 1, n):
        dx = boxes[j][0] - boxes[i][0]
        dy = boxes[j][1] - boxes[i][1]
        dz = boxes[j][2] - boxes[i][2]
        dist = math.sqrt(dx * dx + dy * dy + dz * dz)
        pairs.append((dist, i, j))
pairs.sort()

# Union-Find with circuit count tracking
parent = list(range(n))
num_circuits = n


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global num_circuits
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px
        num_circuits -= 1
        return True
    return False


# Process the first 1000 pairs (Puzzle 1)
for dist, i, j in pairs[:1000]:
    union(i, j)

# Continue until all boxes are in one circuit
last_i, last_j = None, None
for dist, i, j in pairs[1000:]:
    if union(i, j):
        last_i, last_j = i, j
        if num_circuits == 1:
            break

print(f"Product of X coordinates: {boxes[last_i][0] * boxes[last_j][0]}")
