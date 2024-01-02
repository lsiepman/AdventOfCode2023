import numpy as np


data = []
with open("input/day14.txt") as f:
    for line in f:
        data.append(list(line.strip()))

arr = np.array(data)


def roll(data, direction):
    if direction in ["N", "W"]:
        for y in range(data.shape[0]):
            for x in range(data.shape[1]):
                cur_val = data[y][x]
                if cur_val == "O":
                    new_y, new_x = move_direction(data, y, x, cur_val, direction)
                    data[y][x] = "."
                    data[new_y][new_x] = "O"
    elif direction in ["S", "E"]:
        for y in range(data.shape[0] - 1, -1, -1):
            for x in range(data.shape[1] - 1, -1, -1):
                cur_val = data[y][x]
                if cur_val == "O":
                    new_y, new_x = move_direction(data, y, x, cur_val, direction)
                    data[y][x] = "."
                    data[new_y][new_x] = "O"

    return data


def move_direction(data, y, x, value, direction):
    new_y = y
    new_x = x

    if direction == "N":
        while new_y > 0:
            if data[new_y - 1][new_x] == ".":
                new_y -= 1
            else:
                break
    elif direction == "E":
        while new_x < data.shape[1] - 1:
            if data[new_y][new_x + 1] == ".":
                new_x += 1
            else:
                break

    elif direction == "S":
        while new_y < data.shape[0] - 1:
            if data[new_y + 1][new_x] == ".":
                new_y += 1
            else:
                break

    elif direction == "W":
        while new_x > 0:
            if data[new_y][new_x - 1] == ".":
                new_x -= 1
            else:
                break

    return new_y, new_x


def calc_load(data, direction):
    total = 0
    if direction == "N":
        for val, row in zip(range(data.shape[0], -1, -1), data):
            rocks = np.count_nonzero(row == "O")
            total += rocks * val
    return total


def cycle(data):
    dirs = ["N", "W", "S", "E"]
    for d in dirs:
        data = roll(data, d)

    return data


def part1(arr):
    arr = roll(arr, "N")
    return calc_load(arr, "N")


def part2(arr, n):
    seen = {tuple(map(tuple, arr))}
    seen_list = [tuple(map(tuple, arr))]
    for i in range(n):
        arr = cycle(arr)
        if tuple(map(tuple, arr)) not in seen:
            seen.add(tuple(map(tuple, arr)))
            seen_list.append(tuple(map(tuple, arr)))
        else:
            break

    idx = seen_list.index(tuple(map(tuple, arr)))
    final = seen_list[(n - idx) % (i + 1 - idx) + idx]
    return calc_load(np.array(final), "N")


print(f"Day 14 Part 1: {part1(arr)}")
print(f"Day 14 Part 2: {part2(np.array(data), 1000000000)}")
