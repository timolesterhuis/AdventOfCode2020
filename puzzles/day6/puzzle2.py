import string
from collections import Counter


with open("puzzles/day6/puzzle_input.txt") as f:
    data = f.read().split("\n\n")

def counts(group):
    count = Counter([i for i in group])
    lines = 1 + count.get("\n", 0)
    return {k: v for k, v in count.items() if v == lines}

solution = sum([len(counts(d)) for d in data])

print(f"Solution to puzzle is {solution}")