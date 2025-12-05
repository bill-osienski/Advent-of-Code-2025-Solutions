import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    content = f.read()

# Split by blank line
sections = content.strip().split("\n\n")
range_lines = sections[0].strip().split("\n")

# Parse the fresh ranges
fresh_ranges = []
for line in range_lines:
    start, end = map(int, line.split("-"))
    fresh_ranges.append((start, end))

# Sort ranges by start
fresh_ranges.sort()

# Merge overlapping ranges and count total IDs
merged = []
for start, end in fresh_ranges:
    if merged and start <= merged[-1][1] + 1:
        # Overlapping or adjacent, extend the previous range
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

# Count total unique IDs
total_ids = 0
for start, end in merged:
    total_ids += end - start + 1

print(f"Total fresh ingredient IDs in ranges: {total_ids}")
