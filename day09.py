import re
import numpy as np
from copy import deepcopy

data = []
with open("input/day09.txt") as f:
    for line in f:
        data.append([int(i) for i in re.findall(r"[\d\-]+", line)])


def calc_diff(li):
    return np.diff(li).tolist()


def store_diffs(li):
    diffs = [li]
    while sum(li) != 0:
        x = calc_diff(li)
        diffs.append(x)
        li = x

    return diffs


def calc_next_val(li):
    diffs = store_diffs(li)
    diffs.reverse()
    val = 0
    for idx, lst in enumerate(diffs):
        if idx + 1 == len(diffs):
            return val

        val = diffs[idx + 1][-1] + lst[-1]
        diffs[idx + 1].append(val)


def part1(data):
    prediction = []
    for history in data:
        prediction.append(calc_next_val(history))

    return sum(prediction)


print(f"Day 9 Part 1: {part1(deepcopy(data))}")


def calc_prev_val(li):
    diffs = store_diffs(li)
    diffs.reverse()
    [i.reverse() for i in diffs]
    val = 0
    for idx, lst in enumerate(diffs):
        if idx + 1 == len(diffs):
            return val

        val = diffs[idx + 1][-1] - lst[-1]
        diffs[idx + 1].append(val)


def part2(data):
    previous = []
    for history in data:
        previous.append(calc_prev_val(history))

    return sum(previous)


print(f"Day 9 part 2: {part2(data)}")
