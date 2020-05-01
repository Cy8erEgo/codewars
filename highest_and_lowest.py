#!/usr/bin/env python3


def high_and_low(numbers):
    numbers_list = [int(number) for number in numbers.split()]
    return f"{max(numbers_list)} {min(numbers_list)}"


assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"

print("All tests passed!")
