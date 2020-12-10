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
        #print(i, number)
        break

false_idx = i
false_number = number

for i, n in enumerate(numbers):
    contiguous_length = 2
    while sum(numbers[i:i+contiguous_length]) < false_number:
        contiguous_length += 1
    if sum(numbers[i:i+contiguous_length]) == false_number:
        contiguous_set = numbers[i:i+contiguous_length]
        solution = min(contiguous_set) + max(contiguous_set)
    else:
        pass

print(f"Solution is {solution}")