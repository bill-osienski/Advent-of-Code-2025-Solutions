import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.rstrip("\n") for line in f]

# Find the maximum line length
max_len = max(len(line) for line in lines)

# Pad all lines to the same length
lines = [line.ljust(max_len) for line in lines]

# The last line contains the operations
ops_line = lines[-1]
number_lines = lines[:-1]

# Find column boundaries by looking for columns that are all spaces in number lines
# and finding where problems are separated
problems = []
current_problem_start = None

col = 0
while col < max_len:
    # Check if this column is all spaces (separator)
    is_separator = all(line[col] == " " if col < len(line) else True for line in number_lines)

    if is_separator:
        if current_problem_start is not None:
            # End of a problem
            problems.append((current_problem_start, col))
            current_problem_start = None
    else:
        if current_problem_start is None:
            # Start of a new problem
            current_problem_start = col
    col += 1

# Don't forget the last problem if it extends to the end
if current_problem_start is not None:
    problems.append((current_problem_start, max_len))

# Now extract numbers and operations for each problem
grand_total = 0

for start, end in problems:
    numbers = []
    operation = None

    # Extract numbers from each row
    for line in number_lines:
        segment = line[start:end].strip()
        if segment and segment not in ["+", "*"]:
            # Could be a number
            try:
                numbers.append(int(segment))
            except ValueError:
                pass

    # Extract operation from the last line
    op_segment = ops_line[start:end].strip()
    if op_segment in ["+", "*"]:
        operation = op_segment

    # Calculate the result
    if numbers and operation:
        if operation == "+":
            result = sum(numbers)
        else:  # operation == "*"
            result = 1
            for n in numbers:
                result *= n
        grand_total += result

print(f"Grand total: {grand_total}")
