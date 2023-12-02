import re
from collections import defaultdict

data = defaultdict(list)
with open("input/day02.txt") as f:
    for line in f:
        game = int(re.search(r"^Game (\d+):", line).group(1))
        line2 = re.sub(r"^Game (\d+): ", "", line.strip())
        contents = re.findall(r":?([\da-z\s,]+)", line2)
        data[game] = contents

max_cubes = {"red": 12, "green": 13, "blue": 14}
all_games = list(data.keys())


def compare_max_val(colour, data, game, max_cubes, all_games):
    for item in data[game]:
        occ = re.search(r"(\d+) " + colour, item)
        if occ:
            num = int(occ.group(1))
            if num > max_cubes[colour]:
                try:
                    all_games.remove(game)
                except Exception:
                    break
                break

    return all_games


for game_id in data.keys():
    for colour in max_cubes.keys():
        all_games = compare_max_val(colour, data, game_id, max_cubes, all_games)

print(f"Answer Day 2 part 1: {sum(all_games)}")


def find_min_val(colour, old_val, item):
    occ = re.search(r"(\d+) " + colour, item)
    if occ:
        num = int(occ.group(1))
        if num > old_val:
            return num
        else:
            return old_val
    else:
        return old_val


def calc_power(data, game):
    r = 0
    b = 0
    g = 0
    for item in data[game]:
        r = find_min_val("red", r, item)
        b = find_min_val("blue", b, item)
        g = find_min_val("green", g, item)

    return r * b * g


powers = []
for game_id in data.keys():
    powers.append(calc_power(data, game_id))

print(f"Answer Day 2 part 2: {sum(powers)}")
