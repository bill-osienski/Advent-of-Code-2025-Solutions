import os
import re
from itertools import combinations

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]


def parse_line(line):
    # Extract target pattern from []
    target_match = re.search(r"\[([.#]+)\]", line)
    target_str = target_match.group(1)
    target = [1 if c == "#" else 0 for c in target_str]

    # Extract buttons from ()
    buttons = []
    for match in re.finditer(r"\(([0-9,]+)\)", line):
        indices = list(map(int, match.group(1).split(",")))
        buttons.append(indices)

    return target, buttons


def min_presses(target, buttons):
    n_lights = len(target)
    n_buttons = len(buttons)

    # Convert buttons to bitmasks for faster operations
    button_masks = []
    for btn in buttons:
        mask = 0
        for idx in btn:
            mask |= 1 << idx
        button_masks.append(mask)

    target_mask = 0
    for i, v in enumerate(target):
        if v:
            target_mask |= 1 << i

    # Try all combinations of buttons (2^n_buttons possibilities)
    # Since each button only needs to be pressed 0 or 1 times
    min_presses_needed = float("inf")

    for num_pressed in range(n_buttons + 1):
        if num_pressed >= min_presses_needed:
            break
        for combo in combinations(range(n_buttons), num_pressed):
            result = 0
            for btn_idx in combo:
                result ^= button_masks[btn_idx]
            if result == target_mask:
                min_presses_needed = num_pressed
                break

    return min_presses_needed if min_presses_needed != float("inf") else 0


total = 0
for line in lines:
    target, buttons = parse_line(line)
    presses = min_presses(target, buttons)
    total += presses

print(f"Total minimum presses: {total}")
