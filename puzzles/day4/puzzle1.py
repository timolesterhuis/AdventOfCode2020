import re


with open("puzzles/day4/puzzle_input.txt") as f:
    data = f.read().split("\n\n")

regex = re.compile("([a-z]{3}):([^ ^\n]+)")

def validate_passport(passport):
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    fields = regex.findall(passport)
    keys = [i[0] for i in fields]
    return all([expected in keys for expected in expected_fields])

count = 0
for p in data:
    if validate_passport(p):
        count += 1

print(f"Solution to the puzzle is {count}")

