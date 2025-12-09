import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "Clue1.txt")

with open(input_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Parse coordinates (Y,X format)
tiles = []
for line in lines:
    y, x = map(int, line.split(","))
    tiles.append((y, x))

# Build list of horizontal and vertical edges of the polygon
h_edges = []  # (y, x1, x2) horizontal edges
v_edges = []  # (x, y1, y2) vertical edges

for i in range(len(tiles)):
    y1, x1 = tiles[i]
    y2, x2 = tiles[(i + 1) % len(tiles)]

    if y1 == y2:  # Horizontal edge
        h_edges.append((y1, min(x1, x2), max(x1, x2)))
    else:  # Vertical edge
        v_edges.append((x1, min(y1, y2), max(y1, y2)))


def point_in_polygon(py, px):
    """Ray casting algorithm - count crossings to the right"""
    crossings = 0
    for x, y1, y2 in v_edges:
        if x > px and y1 <= py <= y2:
            crossings += 1
    return crossings % 2 == 1


def rect_in_polygon(top, bottom, left, right):
    """Check if rectangle is entirely inside polygon"""
    # All four corners must be inside or on boundary
    # And no edge of the polygon can cross through the rectangle interior

    # Check corners are inside
    corners = [(top, left), (top, right), (bottom, left), (bottom, right)]
    for cy, cx in corners:
        if not point_in_polygon(cy, cx):
            # Check if on boundary
            on_boundary = False
            for y, x1, x2 in h_edges:
                if y == cy and x1 <= cx <= x2:
                    on_boundary = True
                    break
            if not on_boundary:
                for x, y1, y2 in v_edges:
                    if x == cx and y1 <= cy <= y2:
                        on_boundary = True
                        break
            if not on_boundary:
                return False

    # Check no vertical edge crosses through the interior horizontally
    for x, y1, y2 in v_edges:
        if left < x < right:  # Edge x is inside rectangle horizontally
            # Check if edge passes through rectangle vertically
            if y1 < bottom and y2 > top:  # Overlaps vertically
                # Edge crosses through interior
                return False

    # Check no horizontal edge crosses through the interior vertically
    for y, x1, x2 in h_edges:
        if top < y < bottom:  # Edge y is inside rectangle vertically
            # Check if edge passes through rectangle horizontally
            if x1 < right and x2 > left:  # Overlaps horizontally
                # Edge crosses through interior
                return False

    return True


# Find largest valid rectangle
max_area = 0

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        y1, x1 = tiles[i]
        y2, x2 = tiles[j]

        top = min(y1, y2)
        bottom = max(y1, y2)
        left = min(x1, x2)
        right = max(x1, x2)

        area = (bottom - top + 1) * (right - left + 1)

        # Skip if can't beat current max
        if area <= max_area:
            continue

        if rect_in_polygon(top, bottom, left, right):
            max_area = area

print(f"Largest valid rectangle area: {max_area}")
