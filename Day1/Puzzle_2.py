import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, 'Clue1.txt')

position = 50
count = 0

with open(input_file, 'r') as f:
    for line in f:
        instruction = line.strip()
        if not instruction:
            continue

        direction = instruction[0]
        number = int(instruction[1:])

        # Calculate steps until dial first points at 0
        first_zero = (100 - position) % 100 if direction == 'R' else position
        if first_zero == 0:
            first_zero = 100

        # Count how many times dial points at 0 during this move
        if first_zero <= number:
            count += 1 + (number - first_zero) // 100

        # Update position
        position = (position + number if direction == 'R' else position - number) % 100

print(f'Times pointing at 0: {count}')
