#!/usr/bin/env python3

import timeit


def how_much(m, n):
    if m > n:
        m, n = n, m

    res = []

    for f in range(m, n + 1):
        if f % 9 == 1:
            c = int(f / 9)
        else:
            continue

        if f % 7 == 2:
            b = int(f / 7)
        else:
            continue

        res.append([f"M: {f}", f"B: {b}", f"C: {c}"])

    return res


def how_much_2(m, n):
    if m > n:
        m, n = n, m
    return [
        ["M: %d" % f, "B: %d" % (f / 7), "C: %d" % (f / 9)]
        for f in range(m, n + 1)
        if f % 9 == 1 and f % 7 == 2
    ]


def how_much_3(m, n):
    if m > n:
        m, n = n, m
    x = filter(lambda x: x % 7 == 2 and x % 9 == 1, range(m, n + 1))
    return [[f"M: {f}", f"B: {int(f / 7)}", f"C: {int(f / 9)}"] for f in x]


assert how_much_3(1, 100) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
assert how_much_3(1000, 1100) == [["M: 1045", "B: 149", "C: 116"]]
assert how_much_3(10000, 9950) == [["M: 9991", "B: 1427", "C: 1110"]]
assert how_much_3(0, 200) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]
assert how_much_3(2950, 2950) == []
assert how_much_3(20000, 20100) == [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]]

print("All tests passed!")

t1 = timeit.Timer("how_much(1, 10000)", globals=globals())
print("how_much\t", t1.timeit(number=1000))

t2 = timeit.Timer("how_much_2(1, 10000)", globals=globals())
print("how_much_2\t", t2.timeit(number=1000))

t3 = timeit.Timer("how_much_3(1, 10000)", globals=globals())
print("how_much_3\t", t3.timeit(number=1000))
