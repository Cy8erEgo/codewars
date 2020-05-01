#!/usr/bin/env python3

from math import sqrt
from itertools import count, islice


def step(g, m, n):
    for i in range(m, n + 1):
        e = i + g
        if e > n: return

        if all(map(lambda x: x > 1 and all(x % i for i in islice(count(2), int(sqrt(x) - 1))), (i, e))):
            return [i, e]


assert step(2,100,110) == [101, 103]
assert step(4,100,110) == [103, 107]
assert step(2,5,5) == None
assert step(6,100,110) == [101, 107]
assert step(8,300,400) == [359, 367]
assert step(10,300,400) == [307, 317]
assert step(2, 2, 50) == [3, 5]
assert step(6, 100, 110) == [101, 107]

print("All tests passed!")
