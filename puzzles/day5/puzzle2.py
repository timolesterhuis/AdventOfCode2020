import re

with open("puzzles/day5/puzzle_input.txt") as f:
    data = f.read().splitlines()


regex = re.compile("([BF]{7})([LR]{3})")

def read_bsp(code: str) -> (int, int):
    row, col = regex.search(code).groups()
    
    exponent = len(row) - 1
    value_row = 0
    for  r in row:
        if r == "B":
            value_row += 2**exponent
        exponent -= 1

    exponent = len(col) - 1
    value_col = 0
    for  c in col:
        if c == "R":
            value_col += 2**exponent
        exponent -= 1

    return value_row, value_col

numerical = [read_bsp(code) for code in data]
seat_id = [(r*8) + c for r, c in numerical]
empty_seat = list(set(seat_id) ^ set([*range(min(seat_id), max(seat_id)+1)]))[0]

print(f"Solution to puzzle 2 is {empty_seat}")