#!/usr/bin/env python3
import os
from functools import lru_cache

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    """Parse the input file into a graph (adjacency list)."""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line:
                continue
            parts = line.strip().split(':')
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
    graph = parse_input(os.path.join(SCRIPT_DIR, 'Clue1.txt'))

    # Paths from 'svr' to 'out' visiting both 'dac' and 'fft' (in any order)
    # Two cases:
    # 1. svr -> dac -> fft -> out
    # 2. svr -> fft -> dac -> out

    # Case 1: dac before fft
    svr_to_dac = count_paths(graph, 'svr', 'dac')
    dac_to_fft = count_paths(graph, 'dac', 'fft')
    fft_to_out = count_paths(graph, 'fft', 'out')
    case1 = svr_to_dac * dac_to_fft * fft_to_out

    print(f"Case 1 (svr -> dac -> fft -> out):")
    print(f"  svr->dac: {svr_to_dac}, dac->fft: {dac_to_fft}, fft->out: {fft_to_out}")
    print(f"  Total: {case1}")

    # Case 2: fft before dac
    svr_to_fft = count_paths(graph, 'svr', 'fft')
    fft_to_dac = count_paths(graph, 'fft', 'dac')
    dac_to_out = count_paths(graph, 'dac', 'out')
    case2 = svr_to_fft * fft_to_dac * dac_to_out

    print(f"\nCase 2 (svr -> fft -> dac -> out):")
    print(f"  svr->fft: {svr_to_fft}, fft->dac: {fft_to_dac}, dac->out: {dac_to_out}")
    print(f"  Total: {case2}")

    total = case1 + case2
    print(f"\nTotal paths from 'svr' to 'out' visiting both 'dac' and 'fft': {total}")

if __name__ == '__main__':
    main()
