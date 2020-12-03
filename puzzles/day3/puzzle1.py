

with open("puzzles/day3/puzzle_input.txt") as f:
    data = f.read().splitlines()

length = len(data[0])

pos = 0
count = 0
for row in data:
    if row[pos] == "#":
        count += 1
    pos = (pos + 3) % 31

print(f"answer of puzzle 1 is {count}")