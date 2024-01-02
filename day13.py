import numpy as np
from copy import deepcopy


def find_horizontal_reflection(pattern, horizontal, original_ans=None):
    for idx in range(len(pattern) - 1):
        if np.array_equal(pattern[idx], pattern[idx + 1]):
            if is_complete_reflection(idx, pattern):
                if original_ans is None:
                    return idx + 1
                else:
                    if idx + 1 == original_ans[1] and horizontal == original_ans[0]:
                        continue
                    else:
                        return idx + 1

    return None


def is_complete_reflection(line, pattern):
    for bottom, top in zip(range(line, -1, -1), range(line + 1, len(pattern))):
        if np.array_equal(pattern[top], pattern[bottom]):
            continue
        else:
            return False

    if bottom == 0 or top == len(pattern) - 1:
        return True
    else:
        return False


def try_all_smudges(pattern, original_ans):
    for row in range(len(pattern)):
        for item in range(len(pattern[row])):
            temp = deepcopy(pattern)
            if temp[row][item] == "#":
                temp[row][item] = "."
            else:
                temp[row][item] = "#"

            horizontal = True
            ans = find_horizontal_reflection(temp, horizontal, original_ans)
            if ans is not None and (horizontal, ans) != original_ans:
                return ans * 100 if horizontal else ans

            else:
                horizontal = False
                ans = find_horizontal_reflection(temp.T, horizontal, original_ans)

            if ans is not None and (horizontal, ans) != original_ans:
                return ans * 100 if horizontal else ans


def part1(data):
    total = 0
    for v in data.values():
        ans = find_horizontal_reflection(v, horizontal=True)
        if ans is None:
            ans = find_horizontal_reflection(v.T, horizontal=False)
            total += ans
        else:
            total += 100 * ans

    return total


def part2(data):
    total = 0
    for k, v in data.items():
        horizontal = True
        ans = find_horizontal_reflection(v, horizontal)
        if ans is None:
            horizontal = False
            ans = find_horizontal_reflection(v.T, horizontal)
        original_ans = (horizontal, ans)
        total += try_all_smudges(v, original_ans)

    return total


data = {}

idx = 0
with open("input/day13.txt") as f:
    temp = []
    for line in f:
        if not line == "\n":
            temp.append(list(line.strip()))
        elif line == "\n":
            data[idx] = np.array(temp)
            idx += 1
            temp = []
    data[idx] = np.array(temp)


print(f"Day 13 part 1: {part1(data)}")
print(f"Day 13 Part 2: {part2(data)}")
