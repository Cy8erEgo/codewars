#!/usr/bin/env python3


def is_regular_1(n):
    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

def is_regular_2(n):
    return True if not list(filter(lambda x: not n % x, range(2, n))) else False


assert is_regular_2(100) == False
assert is_regular_2(101) == True
assert is_regular_2(137) == True
assert is_regular_2(140) == False
assert is_regular_2(199) == True

print("All tests passed!")
