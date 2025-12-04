import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

# Read the grid
with open(input_file, "r") as f:
    grid = [list(line.rstrip("\n")) for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# 8 adjacent directions: top, bottom, left, right, and 4 corners
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

total_removed = 0

while True:
    # Find all rolls that can be moved this iteration
    to_remove = []

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
                    to_remove.append((r, c))

    # If no rolls can be removed, we're done
    if not to_remove:
        break

    # Remove all movable rolls
    for r, c in to_remove:
        grid[r][c] = "."

    total_removed += len(to_remove)

print(f"Total rolls of paper removed: {total_removed}")
