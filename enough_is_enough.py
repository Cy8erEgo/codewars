#!/usr/bin/env python3

from collections import Counter


def delete_nth(order, max_e):
    order.reverse()

    for i, v in Counter(order).items():
        if v > max_e:
            for _ in range(v - max_e):
                order.remove(i)

    return order[::-1]


def delete_nth_2(order, max_e):
    new_order = []

    for i in order:
        if new_order.count(i) < max_e:
            new_order.append(i)

    return new_order


assert delete_nth_2([20, 37, 20, 21], 1) == [20, 37, 21]
assert delete_nth_2([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
assert delete_nth_2(
    [
        23,
        23,
        18,
        46,
        30,
        46,
        19,
        18,
        46,
        18,
        46,
        19,
        23,
        18,
        23,
        19,
        18,
        23,
        23,
        23,
        19,
        30,
        18,
        23,
        30,
    ],
    1,
) == [23, 18, 46, 30, 19]

print("All tests passed!")
