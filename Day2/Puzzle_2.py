import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")


def is_invalid(n):
    s = str(n)
    # Invalid if starts with 0
    if s[0] == "0":
        return True
    # Invalid if it's a pattern repeated 2 or more times
    length = len(s)
    # Check all possible pattern lengths (1 to length//2)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    return False


total = 0

with open(input_file, "r") as f:
    data = f.read().strip()

for r in data.split(","):
    start, end = map(int, r.split("-"))
    for n in range(start, end + 1):
        if is_invalid(n):
            total += n

print(f"Sum of invalid IDs: {total}")
