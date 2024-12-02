import numpy as np
from collections import defaultdict


input = np.genfromtxt("d1/input.txt", delimiter="   ")

left_list = input[:, 0]
right_list = input[:, 1]

left_list = np.sort(left_list)
# print(left_list[:5])
right_list = np.sort(right_list)
# print(right_list[:5])

abs_diff = np.absolute(left_list - right_list)
# print(abs_diff[:5])

abs_diff_sum = np.sum(abs_diff)

print(abs_diff_sum)

# Part 2
counts = defaultdict(int)

for elem in right_list:
    counts[elem] += 1

sim_score = 0
for elem in left_list:
    count = counts.get(elem)
    if count:
        sim_score += elem * count

print(sim_score)
