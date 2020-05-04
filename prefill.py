#!/usr/bin/env python3


def prefill(n, v=None):
    try:
        return [v or "undefined"] * int(n)
    except:
        raise TypeError(f"{n} is invalid")


assert prefill(3, 1) == [1, 1, 1]
assert prefill(2, "abc") == ["abc", "abc"]
assert prefill("1", 1) == [1]
assert prefill(3, prefill(2, "2d")) == [["2d", "2d"], ["2d", "2d"], ["2d", "2d"]]
try:
    prefill("xyz", 1)
except TypeError as err:
    assert str(err) == "xyz is invalid"
