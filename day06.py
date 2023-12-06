import re
import math
import numpy as np


with open("input/day06.txt") as f:
    for line in f:
        if "Time" in line:
            times = [int(i) for i in re.findall(r"(\d+)", line)]
        elif "Distance" in line:
            dists = [int(i) for i in re.findall(r"(\d+)", line)]

# Math context
# total_time = time_button + time_travel
# distance = time_button * time_travel
# distance = (time_total - time_travel) * time_travel
# distance = -time_travel^2 + time_travel
# time_travel^2 - time_travel + (record_distance + 1) = 0
# also known as
# x^2 - x + constant = 0
# a     b       c
# => discriminant = b^2 - 4ac


def calc(travel_time, record_dist):
    # D = b^2 -4ac
    D = travel_time**2 - 4 * 1 * (record_dist + 1)
    #  x = (-b +- sqrt(D)) / 2a
    travel1 = math.floor((travel_time + math.sqrt(D)) / 2 * 1)
    travel2 = math.ceil((travel_time - math.sqrt(D)) / 2 * 1)

    return travel1 - travel2 + 1


num_win_options = []
for t, d in zip(times, dists):
    num_win_options.append(calc(t, d))

print(f"Day 6 part 1: {np.prod(num_win_options)}")

time2 = int("".join([str(i) for i in times]))
dist2 = int("".join([str(i) for i in dists]))

print(f"Day 6 part 2: {calc(time2, dist2)}")
