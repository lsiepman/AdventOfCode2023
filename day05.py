import re
from collections import defaultdict

sts = defaultdict(list)
stf = defaultdict(list)
ftw = defaultdict(list)
wtl = defaultdict(list)
ltt = defaultdict(list)
tth = defaultdict(list)
htl = defaultdict(list)
indicator = None


def collect_nums(d, line):
    temp = [int(i) for i in re.findall(r"(\d+)", line.strip())]
    d["dest"].append(temp[0])
    d["source"].append(temp[1])
    d["range"].append(temp[2])

    return d


with open("input/day05.txt") as f:
    for line in f:
        # check if numbers should be collected
        if line == "\n":
            indicator = None
            continue

        elif "seeds" in line:
            seeds = [int(i) for i in re.findall(r"(\d+)", line.strip())]
            continue

        elif "seed-to-soil" in line:
            indicator = "sts"
            continue

        elif "soil-to-fertilizer" in line:
            indicator = "stf"
            continue

        elif "fertilizer-to-water" in line:
            indicator = "ftw"
            continue

        elif "water-to-light" in line:
            indicator = "wtl"
            continue

        elif "light-to-temperature" in line:
            indicator = "ltt"
            continue

        elif "temperature-to-humidity" in line:
            indicator = "tth"
            continue

        elif "humidity-to-location" in line:
            indicator = "htl"
            continue

        # Make dicts
        if indicator == "sts":
            sts = collect_nums(sts, line)

        elif indicator == "stf":
            stf = collect_nums(stf, line)

        elif indicator == "ftw":
            ftw = collect_nums(ftw, line)

        elif indicator == "wtl":
            wtl = collect_nums(wtl, line)

        elif indicator == "ltt":
            ltt = collect_nums(ltt, line)

        elif indicator == "tth":
            tth = collect_nums(tth, line)

        elif indicator == "htl":
            htl = collect_nums(htl, line)

all_maps = [sts, stf, ftw, wtl, ltt, tth, htl]


def calc_next_val(cur_val, d):
    for i, j, k in zip(d["source"], d["dest"], d["range"]):
        if cur_val >= i and cur_val <= (i + k):
            diff = cur_val - i
            new_val = j + diff
            break
        else:
            new_val = cur_val

    return new_val


values = []
for i in seeds:
    val = i
    for j in all_maps:
        val = calc_next_val(val, j)
    values.append(val)

print(f"Answer day 5 part 1: {min(values)}")
