from pathlib import Path


def create_folders():
    here = Path(".")

    for i in range(1, 26):
        folder = here / f"day{i}"
        folder.mkdir()
        p1 = folder / f"puzzle1.py"
        p2 = folder / f"puzzle2.py"
        inp = folder / f"puzzle_input.txt"
        p1.touch()
        p2.touch()
        inp.touch()
