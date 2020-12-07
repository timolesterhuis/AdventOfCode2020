
with open("puzzles/day7/puzzle_input.txt") as f:
    data = f.read().splitlines()



rules = dict()
for row in data:
    bag, contents = row.split(" contain ")
    contents = contents.rstrip(".").split(", ")
    if not isinstance(contents, list):
        contents = [contents]
    rules[bag] = contents

count = 0
to_check = ["shiny gold bags"]
already_checked = []
can_contain = []

while to_check:
    current = to_check.pop(0).rstrip("s")
    print(f"currently searching '{current}', count is {count}")
    for k, v in rules.items():
        if any([current in vv for vv in v]):
            count += 1
            can_contain.append(k)
            to_check.append(k)
    already_checked.append(current)

print(len(list(set(can_contain))))