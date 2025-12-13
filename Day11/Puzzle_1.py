#!/usr/bin/env python3
import os
from functools import lru_cache

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    """Parse the input file into a graph (adjacency list)."""
    graph = {}
    with open(filename, "r") as f:
        for line in f:
            # Format: "device: target1 target2 ..."
            if ":" not in line:
                continue
            parts = line.strip().split(":")
            device = parts[0].strip()
            targets = parts[1].strip().split() if parts[1].strip() else []
            graph[device] = targets
    return graph


def count_paths(graph, start, end):
    """Count all paths from start to end using memoization."""

    @lru_cache(maxsize=None)
    def dfs(node):
        if node == end:
            return 1
        if node not in graph:
            return 0

        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor)
        return total

    return dfs(start)


def main():
    graph = parse_input(os.path.join(SCRIPT_DIR, "Clue1.txt"))

    print(f"Total devices: {len(graph)}")
    print(f"'you' connects to: {graph.get('you', [])}")

    path_count = count_paths(graph, "you", "out")
    print(f"\nTotal paths from 'you' to 'out': {path_count}")


if __name__ == "__main__":
    main()
