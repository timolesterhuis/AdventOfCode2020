import re
from collections import Counter

with open("puzzles/day2/puzzle_input.txt") as f:
    text = f.read()


data = [row.split(":") for row in text.split("\n")]


def checksum(check, password):
    m = re.search("(\d+)-(\d+) ([a-z])", check)
    lower, higher, char = m.groups()
    count = Counter(password).get(char, 0)
    return count >= int(lower) and count <= int(higher)

solution = [checksum(check, password) for check, password in data]
print(f"answer of puzzle 1 is:", Counter(solution).get(True))
