from functools import cache

data = []
with open("input/day12.txt") as f:
    for line in f:
        springs, instructions = line.strip().split()
        inst = tuple(map(int, instructions.split(",")))
        data.append((tuple(springs), inst))


@cache
def count_options(inst, springs):
    if not springs:
        return 0 if "#" in inst else 1
    if not inst:
        return 1 if not springs else 0

    num_options = 0

    if inst[0] in ".?":
        num_options += count_options(inst[1:], springs)
    if inst[0] in "#?":
        if (
            springs[0] <= len(inst)
            and "." not in inst[: springs[0]]
            and (springs[0] == len(inst) or inst[springs[0]] != "#")
        ):
            num_options += count_options(inst[springs[0] + 1 :], springs[1:])

    return num_options


def part1(data):
    result = 0
    for i, j in data:
        result += count_options(i, j)

    return result


def part2(data):
    new_data = []
    for i, j in data:
        a = list(i)
        a.append("?")
        a = a * 5
        a.pop()
        a = tuple(a)
        b = tuple(list(j) * 5)
        new_data.append((a, b))

    result = part1(new_data)
    return result


print(f"Day 12 Part 1: {part1(data)}")
print(f"Day 12 Part 2: {part2(data)}")
