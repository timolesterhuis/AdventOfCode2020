

with open("puzzles/day8/puzzle_input.txt") as f:
    data = f.read().splitlines()

instructions = [d.split(" ", 1) for d in data]


def run_program(instructions, raise_error=False):
    idx = 0
    accumulator = 0
    history = []
    while idx < len(instructions):
        ins, val = instructions[idx]
        print(idx, ins, val, accumulator)

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



with open("puzzles/day8/puzzle_input.txt") as f:
    data = f.read().splitlines()

instructions = [d.split(" ", 1) for d in data]


def run_program(instructions, raise_error=False):
    idx = 0
    accumulator = 0
    history = []
    while idx < len(instructions):
        ins, val = instructions[idx]
        print(idx, ins, val, accumulator)

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

print(f"solution to puzzle is {run_program(instructions)[0]}")