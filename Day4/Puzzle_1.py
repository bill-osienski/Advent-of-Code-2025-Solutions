import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

# Read the grid
with open(input_file, "r") as f:
    grid = [line.rstrip("\n") for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# 8 adjacent directions: top, bottom, left, right, and 4 corners
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

movable_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            # Count adjacent rolls of paper
            adjacent_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Positions outside grid count as blank
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        adjacent_rolls += 1
            # Can be moved if fewer than 4 adjacent rolls
            if adjacent_rolls < 4:
                movable_count += 1

print(f"Rolls of paper that can be moved: {movable_count}")
