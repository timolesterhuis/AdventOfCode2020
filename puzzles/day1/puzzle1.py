import itertools

with open("puzzles/day1/puzzle_input.txt") as f:
    text = f.read()

data = [int(i) for i in text.split("\n")]


for a, b in itertools.combinations(data, 2):
    if a + b == 2020:
        print(a, b, a*b)
        print(f"Puzzle output is {a*b}")
        break