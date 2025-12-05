import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    content = f.read()

# Split by blank line
sections = content.strip().split("\n\n")
range_lines = sections[0].strip().split("\n")
ingredient_lines = sections[1].strip().split("\n")

# Parse the fresh ranges
fresh_ranges = []
for line in range_lines:
    start, end = map(int, line.split("-"))
    fresh_ranges.append((start, end))

# Count fresh ingredients
fresh_count = 0
for line in ingredient_lines:
    ingredient_id = int(line.strip())
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            fresh_count += 1
            break

print(f"Fresh ingredients: {fresh_count}")
