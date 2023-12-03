import re
import numpy as np
from collections import defaultdict

# read data, find all possible symbols
data = []
possible_symbols = set()
with open("input/day03.txt") as f:
    for line in f:
        data.append(list(line.strip()))
        symbols = re.findall(r"[^\d\.]", line.strip())
        possible_symbols.update(symbols)

mat = np.array(data)

# symbol locations
symbol_locs = []
for i in list(possible_symbols):
    symbol_locs.extend(list(zip(*np.where(mat == i))))


# find all adjacent locations to the symbols
def check_valid(arr, pos):
    i = pos[0]
    j = pos[1]
    n = len(arr) - 1
    m = len(arr[0]) - 1
    if i < 0 or j < 0 or i > n or j > m:
        return False
    return pos


def adjacent_positions(i, j):
    positions = [
        # topleft
        (i - 1, j - 1),
        # top
        (i - 1, j),
        # topright
        (i - 1, j + 1),
        # left
        (i, j - 1),
        # right
        (i, j + 1),
        # bottomleft
        (i + 1, j - 1),
        # bottom
        (i + 1, j),
        # bottomright
        (i + 1, j + 1),
    ]
    return positions


adjacent_locs = set()
for i, j in symbol_locs:
    positions = adjacent_positions(i, j)
    valid_positions = [check_valid(mat, x) for x in positions]
    adjacent_locs.update(valid_positions)

# number locations
num_locations = []
for i in list("1234567890"):
    num_locations.extend(list(zip(*np.where(mat == i))))

# create numbers
num_locations = sorted(num_locations)
a, b = (0, 0)
nums_and_locs = []
for i, j in num_locations:
    if a == 0 and b == 0:
        a = i
        b = j
        temp_num = mat[a, b]
        temp_loc = [(a, b)]
    elif i == a and j == b + 1:
        a = i
        b = j
        temp_num += mat[a, b]
        temp_loc.append((a, b))
    else:
        nums_and_locs.append((int(temp_num), temp_loc))
        a = i
        b = j
        temp_num = mat[a, b]
        temp_loc = [(a, b)]
nums_and_locs.append((int(temp_num), temp_loc))

# find relevant numbers
relevant_nums = []
for i, j in nums_and_locs:
    if len(set(j) & adjacent_locs) > 0:
        relevant_nums.append(i)

print(f"Answer day 3 part 1: {sum(relevant_nums)}")

# part 2
# all gear locations
gear_locs = list(zip(*np.where(mat == "*")))
gear_adjacents = defaultdict(list)
for i, j in gear_locs:
    positions = adjacent_positions(i, j)
    valid_positions = [check_valid(mat, x) for x in positions]
    gear_adjacents[(i, j)] = valid_positions

# all adjacent numbers for gears
gear_dict = defaultdict(list)
for i, j in nums_and_locs:
    for x in gear_adjacents:
        if len(set(j) & set(gear_adjacents[x])) > 0:
            gear_dict[x].append(i)

# find all gears with exactly 2 neighbours
double_neigh = []
for i in gear_dict.values():
    if len(i) == 2:
        double_neigh.append(np.prod(i))

print(f"Answer day 3 part 1: {sum(double_neigh)}")
