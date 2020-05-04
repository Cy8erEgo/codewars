#!/usr/bin/env python3


def iq_test(numbers):
    nn = [int(number) % 2 == 0 for number in numbers.split()]

    return nn.index(True) + 1 if nn.count(True) == 1 else nn.index(False) + 1


def iq_test_2(numbers):
    numbers = numbers.split()
    even = []
    odd = []

    for i in numbers:
        even.append(i) if int(i) % 2 else odd.append(i)
        l1, l2 = len(even), len(odd)

        if l1 and l2 and (l1 > 1 or l2 > 1):
            index = odd[0] if l1 > l2 else even[0]
            return numbers.index(index) + 1


if __name__ == "__main__":
    import timeit

    def speed_test(func_name):
        print(
            f"{func_name}:",
            timeit.timeit(
                f"{func_name}(' '.join(['33' for _ in range(1000)] + ['34', '35']))",
                f"from __main__ import {func_name}",
                number=100,
            ),
        )

    assert iq_test("2 4 7 8 10") == 3
    assert iq_test("1 2 2") == 1

    print("All tests passed!")

    speed_test("iq_test")
    speed_test("iq_test_2")
