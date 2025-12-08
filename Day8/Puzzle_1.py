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

# Union-Find
parent = list(range(n))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px


# Process the 1000 closest pairs
for dist, i, j in pairs[:1000]:
    union(i, j)

# Count circuit sizes
circuit_sizes = {}
for i in range(n):
    root = find(i)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

# Get the three largest circuits
sizes = sorted(circuit_sizes.values(), reverse=True)
while len(sizes) < 3:
    sizes.append(1)

print(f"Product: {sizes[0] * sizes[1] * sizes[2]}")
