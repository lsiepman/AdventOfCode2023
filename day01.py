import re

nums = []
with open("input/day01.txt") as f:
    for line in f:
        first = re.search(r"^[a-z]*([0-9])", line).group(1)
        last = re.search(r".*([0-9])[a-z]*$", line.strip()).group(1)
        nums.append(int(f"{first}{last}"))

print(f"Answer day 1 part 1: {sum(nums)}")

num_dct = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

nums2 = []
with open("input/day01.txt") as f:
    for line in f:
        first = re.search(r"([0-9]|" + "|".join(num_dct.keys()) + r").*$", line).group(
            1
        )
        last = re.search(
            r"^.*([0-9]|" + "|".join(num_dct.keys()) + r").*$", line.strip()
        ).group(1)

        if first in num_dct.keys():
            first = num_dct[first]

        if last in num_dct.keys():
            last = num_dct[last]

        nums2.append(int(f"{first}{last}"))

print(f"Answer day 1 part 2: {sum(nums2)}")
