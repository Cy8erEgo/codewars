#!/usr/bin/env python3

import timeit


def speed_test(func):
    def wrapper(*args):
        stmt = f"{func.__name__}({', '.join([str(a) for a in args])})"
        t = timeit.Timer(stmt, globals=globals())
        time = t.timeit(number=1)

    return wrapper


if __name__ == "__main__":

    @speed_test
    def foo(n):
        return n + 2

    foo(2)
