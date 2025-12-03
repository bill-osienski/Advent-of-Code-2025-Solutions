import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

total = 0

with open(input_file, "r") as f:
    for line in f:
        bank = line.strip()
        if not bank:
            continue

        # Find the first occurrence of the largest digit (excluding the last position)
        max_digit = max(bank[:-1])
        tens_pos = bank.index(max_digit)

        # Find the largest digit after that position
        remaining = bank[tens_pos + 1 :]
        ones_digit = max(remaining)

        # Form the double-digit number
        number = int(max_digit + ones_digit)
        total += number

print(f"Sum of all double-digit numbers: {total}")
