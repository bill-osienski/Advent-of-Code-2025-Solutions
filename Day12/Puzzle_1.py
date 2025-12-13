#!/usr/bin/env python3
"""
Day 12: Polyomino Packing

Count regions where total cells needed <= cells available.
With large slack, packing always succeeds if space exists.
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    shape_sizes = {}
    current_shape_id = None
    current_cell_count = 0
    count = 0

    with open(os.path.join(SCRIPT_DIR, 'Clue1.txt'), 'r') as f:
        for line in f:
            line = line.strip()

            if not line:
                # End of shape definition
                if current_shape_id is not None:
                    shape_sizes[current_shape_id] = current_cell_count
                    current_shape_id = None
                    current_cell_count = 0
                continue

            if 'x' in line and ':' in line:
                # Region definition
                dims, counts_str = line.split(':')
                width, height = map(int, dims.split('x'))
                shape_counts = list(map(int, counts_str.split()))

                cells_available = width * height
                cells_needed = sum(shape_sizes[i] * c for i, c in enumerate(shape_counts))

                if cells_needed <= cells_available:
                    count += 1

            elif ':' in line:
                # Shape header (e.g., "0:")
                if current_shape_id is not None:
                    shape_sizes[current_shape_id] = current_cell_count
                current_shape_id = int(line.split(':')[0])
                current_cell_count = 0

            elif '#' in line or '.' in line:
                # Shape row - count # characters
                current_cell_count += line.count('#')

    print(count)


if __name__ == '__main__':
    main()
