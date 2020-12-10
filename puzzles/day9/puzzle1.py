from typing import List
import itertools


PREAMBLE_LENGTH = 25
with open("puzzles/day9/puzzle_input.txt") as f:
    data = f.read().splitlines()

numbers = [int(d) for d in data]


def validate_number(preamble: List[int], number: int, length: int = PREAMBLE_LENGTH) -> bool:
    assert len(preamble) == length
    if number >= (2*max(preamble)):
        return False
    if number <= (2*min(preamble)):
        return False
    valid = False
    for a, b in itertools.combinations(preamble, 2):
        if a + b == number:
            valid = True
            break
    return valid


for i in range(PREAMBLE_LENGTH, len(numbers)):
    preamble = numbers[i-PREAMBLE_LENGTH:i]
    number = numbers[i]
    check = validate_number(preamble, number)
    if not check:
        print(i, number)