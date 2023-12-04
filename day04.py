import re
from collections import defaultdict

data = defaultdict(dict)
with open("input/day04.txt") as f:
    for line in f:
        card_id = int(re.search(r"^Card\s+(\d+):", line).group(1))
        winners = re.findall(r"(\d+)", line.split("|")[0])[1:]
        numbers = re.findall(r"(\d+)", line.split("|")[1])
        winners = [int(i) for i in winners]
        numbers = [int(i) for i in numbers]
        data[card_id] = {"winners": winners, "numbers": numbers}


def calc_score(data):
    for k, v in data.items():
        common = set(v["winners"]) & set(v["numbers"])
        if len(common) > 0:
            data[k]["score"] = 2 ** (len(common) - 1)
        else:
            data[k]["score"] = 0

    return data


def sum_results(data, field):
    total = 0
    for i in data.values():
        total += i[field]

    return total


data = calc_score(data)
print(f"Answer day 4 part 1: {sum_results(data, 'score')}")


def calc_num_cards(data):
    for k in data:
        data[k]["num_cards"] = 1
    for k, v in data.items():
        for _ in range(v["num_cards"]):
            num_common = len(set(v["winners"]) & set(v["numbers"]))
            if num_common > 0:
                for x in range(1, num_common + 1):
                    data[k + x]["num_cards"] += 1
    return data


data = calc_num_cards(data)
print(f"Answer day 4 part 2: {sum_results(data, 'num_cards')}")
