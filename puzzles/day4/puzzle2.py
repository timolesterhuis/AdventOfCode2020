import re


with open("puzzles/day4/puzzle_input.txt") as f:
    data = f.read().split("\n\n")

regex = re.compile("([a-z]{3}):([^ ^\n]+)")

def validate_passport(passport):
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    fields = regex.findall(passport)
    keys = [i[0] for i in fields]
    if all([expected in keys for expected in expected_fields]):
        return validate_fields(**dict(fields))
    else:
        return False

def val_byr(byr):
    return 1920 <= int(byr) <= 2002

def val_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def val_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def val_hgt(hgt):
    m = re.search("(\d+)(cm|in)", hgt)
    if m:
        val, typ = m.groups()
        if typ == "cm":
            return 150 <= int(val) <= 193
        elif typ == "in":
            return 59 <= int(val) <= 76
    return False

def val_hcl(hcl):
    return bool(re.search("#[0-9a-f]{6}", hcl))

def val_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def val_pid(pid):
    return bool(re.search("^\d{9}$", pid))

def validate_fields(**fields):
    return all([
        val_byr(fields["byr"]),
        val_iyr(fields["iyr"]),
        val_eyr(fields["eyr"]),
        val_hgt(fields["hgt"]),
        val_hcl(fields["hcl"]),
        val_ecl(fields["ecl"]),
        val_pid(fields["pid"]),
    ])  

count = 0
for p in data:
    if validate_passport(p):
        count += 1

print(f"Solution to the puzzle is {count}")

