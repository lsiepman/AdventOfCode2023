from collections import defaultdict
import re

data = []
with open("input/day15.txt") as f:
    for line in f:
        data.extend(line.strip().split(","))


def calc(val, char):
    asc = ord(char)
    val += asc
    val *= 17
    val = val % 256

    return val


def part1(inp, init=0):
    store = []
    for i in inp:
        val = init
        for j in i:
            val = calc(val, j)
        store.append(val)

    return sum(store)


def calc_focal(boxes):
    total = 0
    for k, v in boxes.items():
        box_score = 1 + k
        lens_score = []
        for idx, item in enumerate(v):
            lens_score.append(box_score * (idx + 1) * item[1])
        total += sum(lens_score)

    return total


def part2(inp):
    boxes = defaultdict(list)
    for i in inp:
        regex = re.search(r"^([a-zA-Z]+)([\-=])(\d)*", i)
        label = regex.group(1)
        action = regex.group(2)
        box = 0
        for j in label:
            box = calc(box, j)

        temp = [b[0] for b in boxes[box]]
        idx = temp.index(label) if label in temp else None
        if action == "=":
            focal = int(regex.group(3))
            if label in temp:
                boxes[box][idx] = (label, focal)
            else:
                boxes[box].append((label, focal))
        elif action == "-":
            if idx is not None:
                boxes[box].pop(idx)

    return calc_focal(boxes)


print(f"Day 15 Part 1: {part1(data, 0)}")
print(f"Day 15 Part 2: {part2(data)}")
