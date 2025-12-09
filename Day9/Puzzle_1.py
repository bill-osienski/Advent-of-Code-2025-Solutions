import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Parse coordinates (Y,X format)
tiles = []
for line in lines:
    y, x = map(int, line.split(","))
    tiles.append((y, x))

# Find the two tiles that form the largest rectangle
max_area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        y1, x1 = tiles[i]
        y2, x2 = tiles[j]
        height = abs(y2 - y1) + 1
        width = abs(x2 - x1) + 1
        area = height * width
        if area > max_area:
            max_area = area

print(f"Largest rectangle area: {max_area}")
