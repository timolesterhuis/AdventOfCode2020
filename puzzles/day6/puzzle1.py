import string
from collections import Counter


with open("puzzles/day6/puzzle_input.txt") as f:
    data = f.read().split("\n\n")

def counts(group):
    return Counter([i for i in group if i in string.ascii_lowercase])

solution = sum([len(counts(d)) for d in data])

print(f"Solution to puzzle is {solution}")