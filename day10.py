import numpy as np
from math import floor
from shapely.geometry import Point, Polygon

data = []
with open("input/day10.txt") as f:
    for line in f:
        data.append(list(line.strip()))

arr = np.array(data)
start_loc = tuple(zip(*np.where(arr == "S")))[0]


def move(cur_loc, pipe, seen):
    if pipe == "|":
        if (cur_loc[0] - 1, cur_loc[1]) not in seen:
            return (cur_loc[0] - 1, cur_loc[1])
        elif (cur_loc[0] + 1, cur_loc[1]) not in seen:
            return (cur_loc[0] + 1, cur_loc[1])

    elif pipe == "-":
        if (cur_loc[0], cur_loc[1] - 1) not in seen:
            return (cur_loc[0], cur_loc[1] - 1)
        elif (cur_loc[0], cur_loc[1] + 1) not in seen:
            return (cur_loc[0], cur_loc[1] + 1)

    elif pipe == "L":
        if (cur_loc[0] - 1, cur_loc[1]) not in seen:
            return (cur_loc[0] - 1, cur_loc[1])
        elif (cur_loc[0], cur_loc[1] + 1) not in seen:
            return (cur_loc[0], cur_loc[1] + 1)

    elif pipe == "J":
        if (cur_loc[0] - 1, cur_loc[1]) not in seen:
            return (cur_loc[0] - 1, cur_loc[1])
        elif (cur_loc[0], cur_loc[1] - 1) not in seen:
            return (cur_loc[0], cur_loc[1] - 1)

    elif pipe == "7":
        if (cur_loc[0], cur_loc[1] - 1) not in seen:
            return (cur_loc[0], cur_loc[1] - 1)
        elif (cur_loc[0] + 1, cur_loc[1]) not in seen:
            return (cur_loc[0] + 1, cur_loc[1])

    elif pipe == "F":
        if (cur_loc[0], cur_loc[1] + 1) not in seen:
            return (cur_loc[0], cur_loc[1] + 1)
        elif (cur_loc[0] + 1, cur_loc[1]) not in seen:
            return (cur_loc[0] + 1, cur_loc[1])

    else:
        return False


def part1(arr, start_loc):
    possible_pipes = ["|", "-", "L", "J", "7", "F"]
    for p in possible_pipes:
        cur_loc = start_loc
        seen = []

        while True:
            if arr[cur_loc] == "S":
                pipe = p
            else:
                pipe = arr[cur_loc]

            cur_loc = move(cur_loc, pipe, seen)

            if not cur_loc:
                break

            seen.append(cur_loc)

            if arr[cur_loc] == "S":
                return seen


loop = part1(arr, start_loc)
print(f"Day 10 Part 1: {floor((len(loop) + 1)/2)}")

poly = Polygon(loop)
inside_loop = []
for i in np.ndindex(arr.shape):
    p = Point(i)
    if p.within(poly):
        inside_loop.append(p)

print(f"Day 10 Part 2: {len(inside_loop)}")
