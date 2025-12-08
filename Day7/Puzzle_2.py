import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.rstrip("\n") for line in f]

# Find the starting position 'S'
start_col = lines[0].index("S")

# Track path counts per column position
path_counts = {start_col: 1}

# Process each row from top to bottom
for row in range(1, len(lines)):
    line = lines[row]
    new_path_counts = {}

    for col, count in path_counts.items():
        if line[col] == "^":
            new_path_counts[col - 1] = new_path_counts.get(col - 1, 0) + count
            new_path_counts[col + 1] = new_path_counts.get(col + 1, 0) + count
        else:
            new_path_counts[col] = new_path_counts.get(col, 0) + count

    path_counts = new_path_counts

print(f"Total different paths: {sum(path_counts.values())}")
