#!/usr/bin/env python3

from collections import Counter


def highest_rank(arr):
    counter = Counter(arr)
    return max(filter(lambda x: x[1] == max(counter.values()), counter.items()))[0]


assert highest_rank([3, 3, 5, 5, 3, 5]) == 5
assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]) == 10

print("All tests passed")
