import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "clue1.txt")

position = 50
zero_count = 0

with open(input_file, "r") as f:
    for line in f:
        instruction = line.strip()
        if not instruction:
            continue

        direction = instruction[0]  # 'L' or 'R'
        number = int(instruction[1:])  # The number after L or R

        if direction == "R":
            position = (position + number) % 100
        elif direction == "L":
            position = (position - number) % 100

        if position == 0:
            zero_count += 1

print(f"Times landing exactly on 0: {zero_count}")
