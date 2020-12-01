import itertools

with open("puzzles/day1/puzzle_input.txt") as f:
    text = f.read()

data = [int(i) for i in text.split("\n")]


for a, b, c in itertools.combinations(data, 3):
    if a + b + c == 2020:
        print(a, b, c, a*b*c)
        print(f"Puzzle output is {a*b*c}")
        break