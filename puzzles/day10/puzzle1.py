from collections import Counter


with open("puzzles/day10/puzzle_input.txt") as f:
    data = f.read().splitlines()


adapters = sorted([int(d) for d in data] + [0])
differences = [b - a for a, b in zip(adapters[:-1], adapters[1:]) ]

count = Counter(differences)
count[3] += 1

print(f"Solution is {count[1]*count[3]}")