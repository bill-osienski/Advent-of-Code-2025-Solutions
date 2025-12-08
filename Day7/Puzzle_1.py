import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.rstrip("\n") for line in f]

# Find the starting position 'S'
start_col = lines[0].index("S")

# Track active beam positions (set of columns)
beams = {start_col}
split_count = 0

# Process each row from top to bottom
for row in range(1, len(lines)):
    line = lines[row]
    new_beams = set()

    for col in beams:
        if line[col] == "^":
            split_count += 1
            new_beams.add(col - 1)
            new_beams.add(col + 1)
        else:
            new_beams.add(col)

    beams = new_beams

print(f"Total splits: {split_count}")
