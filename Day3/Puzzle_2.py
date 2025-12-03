import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

total = 0

with open(input_file, "r") as f:
    for line in f:
        bank = line.strip()
        if not bank:
            continue

        result = ""
        pos = 0

        for digits_needed in range(12, 0, -1):
            # Find the largest digit from current position that leaves enough digits after
            max_digit = "0"
            max_pos = pos
            for i in range(pos, len(bank) - digits_needed + 1):
                if bank[i] > max_digit:
                    max_digit = bank[i]
                    max_pos = i

            result += max_digit
            pos = max_pos + 1

        total += int(result)

print(f"Sum of all 12-digit numbers: {total}")
