import re
from collections import Counter

with open("puzzles/day2/puzzle_input.txt") as f:
    text = f.read()


data = [row.split(":") for row in text.split("\n")]

def checksum(check: str, password: str) -> bool:
    m = re.search("(\d+)-(\d+) ([a-z])", check)
    id1, id2, char = m.groups()
    # because of the space character before password, we can use "index zero"
    return  (password[int(id1)] == char) ^ (password[int(id2)] == char)

solution = [checksum(check, password) for check, password in data]
print(f"answer of puzzle 2 is:", Counter(solution).get(True))
