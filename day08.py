import re
from math import lcm

instructions = {}

with open("input/day08.txt") as f:
    for line in f:
        if re.search(r"^[RL]+$", line):
            directions = line.strip()
        elif line == "\n":
            continue
        else:
            regex = re.search(
                r"^([A-Z]{3})\s=\s\(([A-Z]{3}),\s([A-Z]{3})\)$", line.strip()
            )
            k = regex.group(1)
            l = regex.group(2)
            r = regex.group(3)
            instructions[k] = {"R": r, "L": l}


def part1(instructions, directions, location="AAA", end=["ZZZ"]):
    steps = 0

    while True:
        for i in directions:
            location = instructions[location][i]
            steps += 1
            if location in end:
                return steps


print(f"Day 8 part 1: {part1(instructions, directions)}")


def part2(instructions, directions):
    possible_starts = []
    possible_ends = []
    for i in instructions:
        if i.endswith("A"):
            possible_starts.append(i)
        elif i.endswith("Z"):
            possible_ends.append(i)

    paths = []
    for start in possible_starts:
        paths.append(part1(instructions, directions, location=start, end=possible_ends))

    return lcm(*paths)


print(f"Day 8 part 2: {part2(instructions, directions)}")
