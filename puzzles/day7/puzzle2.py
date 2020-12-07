
with open("puzzles/day7/puzzle_input.txt") as f:
    data = f.read().splitlines()

rules = dict()
for row in data:
    bag, contents = row.split(" contain ")
    contents = contents.rstrip(".").split(", ")
    if not isinstance(contents, list):
        contents = [contents]
    rules[bag] = contents

bag_count = 0
to_check = [("shiny gold bags", 1)]
already_checked = []
can_contain = []

while to_check:
    current, multiplier = to_check.pop(0)
    #print(f"currently searching '{current}', count is {count}")
    for bag in rules[current]:
        if bag == "no other bags":
            print("end reached")
            break
        count, new_bag = bag.split(" ", 1)
        count = int(count)
        if not new_bag.endswith("s"):
            new_bag += "s"
        bag_count += (multiplier * count)
        to_check.append((new_bag, multiplier * count))

print(bag_count)