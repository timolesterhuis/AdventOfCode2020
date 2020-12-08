
with open("puzzles/day8/puzzle_input.txt") as f:
    data = f.read().splitlines()

instructions = [d.split(" ", 1) for d in data]


def run_program(instructions, raise_error=False):
    idx = 0
    accumulator = 0
    history = []
    while idx < len(instructions):
        ins, val = instructions[idx]
        #print(idx, ins, val, accumulator)

        if idx in history:
            if raise_error:
                raise ValueError
            else:
                break
        else:
            history.append(idx)

        if ins == "jmp":
            idx += int(val)
            continue

        if ins == "nop":
            pass

        if ins == "acc":
            accumulator += int(val)

        idx += 1
    return accumulator, history

solution_puzzle_1, history = run_program(instructions)

#print(f"solution to puzzle is {run_program(instructions)[0]}")

for h in reversed(history):
    if instructions[h][0] == "acc":
        continue
    test_instructions = deepcopy(instructions)
    ins, val = instructions[h]

    if ins == "nop":
        new_ins = "jmp"
    elif ins == "jmp":
        new_ins = "nop"
    else:
        raise ValueError

    test_instructions[h] = (new_ins, val)
    try:
        solution, history = run_program(test_instructions, raise_error=True)
        break
    except ValueError:
        pass


print(f"solution to puzzle is {solution}")