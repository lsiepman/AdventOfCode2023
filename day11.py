import numpy as np
from copy import deepcopy

data = []
with open("input/day11.txt") as f:
    for line in f:
        data.append(list(line.strip()))

arr = np.array(data)


def expand(a):
    rows = []
    for idx in range(0, a.shape[0]):
        row = a[idx, :]
        if "#" not in row:
            rows.append(idx)

    cols = []
    for idx in range(0, a.shape[1]):
        col = a[:, idx]
        if "#" not in col:
            cols.append(idx)

    row_inserts = 0
    for i in rows:
        a = np.insert(a, i + row_inserts, np.repeat(".", a.shape[1]), axis=0)
        row_inserts += 1

    col_inserts = 0
    for i in cols:
        a = np.insert(a, i + col_inserts, np.repeat(".", a.shape[0]), axis=1)
        col_inserts += 1

    return a


def find_galaxy(a, symbol="#"):
    return list(zip(*np.where(a == symbol)))


def shortest_paths(locs):
    distances = 0
    while len(locs) > 0:
        cur = locs.pop()
        for i in locs:
            distances += np.abs(cur[0] - i[0]) + np.abs(cur[1] - i[1])

    return distances


arr_big = expand(arr)
locations = find_galaxy(arr_big)
print(f"Day 11, Part 1: {shortest_paths(deepcopy(locations))}")


def calc_offset(loc_init, loc_part1):
    offsets = []
    for i, j in zip(loc_init, loc_part1):
        y_offset = j[0] - i[0]
        x_offset = j[1] - i[1]
        offsets.append((y_offset, x_offset))

    return offsets


def calc_galaxy(loc_init, offsets, m=999999):
    locations = []
    for i, j in zip(loc_init, offsets):
        y_new = i[0] + m * j[0]
        x_new = i[1] + m * j[1]
        locations.append((y_new, x_new))

    return locations


initial_locations = find_galaxy(arr)
offsets = calc_offset(initial_locations, locations)
locations2 = calc_galaxy(initial_locations, offsets)
print(f"Day 11, Part 2: {shortest_paths(locations2)}")
