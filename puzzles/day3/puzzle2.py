import functools

with open("puzzles/day3/puzzle_input.txt") as f:
    data = f.read().splitlines()

length = len(data[0])

increments = [1, 3, 5, 7, 1]
steepnes = [1, 1, 1, 1, 2]
positions = [0, 0, 0, 0, 0]
counts = [0, 0, 0, 0, 0]

for step, row in enumerate(data):
    for idx, (inc, stp) in enumerate(zip(increments, steepnes)):
        if stp == 2 and step % 2 == 1:
            continue
        if row[positions[idx]] == "#":
            counts[idx] += 1
        positions[idx] = (positions[idx] + inc) % length

solution = functools.reduce(lambda a,b: a*b, counts)
print(f"answer of puzzle 1 is {solution}")