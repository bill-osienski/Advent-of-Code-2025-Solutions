import os
import re
from scipy.optimize import linprog, milp, Bounds, LinearConstraint
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]


def parse_line(line):
    # Extract buttons from ()
    buttons = []
    for match in re.finditer(r"\(([0-9,]+)\)", line):
        indices = list(map(int, match.group(1).split(",")))
        buttons.append(indices)

    # Extract joltage requirements from {}
    joltage_match = re.search(r"\{([0-9,]+)\}", line)
    joltage = list(map(int, joltage_match.group(1).split(",")))

    return buttons, joltage


def min_presses_joltage(buttons, joltage):
    n_buttons = len(buttons)
    n_counters = len(joltage)

    # Build constraint matrix A where A[i][j] = 1 if button j affects counter i
    A = np.zeros((n_counters, n_buttons))
    for j, btn in enumerate(buttons):
        for idx in btn:
            if idx < n_counters:
                A[idx][j] = 1

    b = np.array(joltage)

    # Objective: minimize sum of all button presses
    c = np.ones(n_buttons)

    # Use MILP (Mixed Integer Linear Programming) for integer solutions
    # All variables must be non-negative integers
    integrality = np.ones(n_buttons)  # 1 = integer
    bounds = Bounds(lb=0, ub=np.inf)

    # Equality constraints: A @ x == b
    constraints = LinearConstraint(A, b, b)

    result = milp(c, integrality=integrality, bounds=bounds, constraints=constraints)

    if result.success:
        return int(round(result.fun))
    else:
        return 0


total = 0
for i, line in enumerate(lines):
    buttons, joltage = parse_line(line)
    presses = min_presses_joltage(buttons, joltage)
    total += presses

print(f"Total minimum presses: {total}")
