#!/usr/bin/env python3

def howmuch(m, n):
    if m > n:
        m, n = n, m

    res = []

    for f in range(m, n + 1):
        if f % 9 == 1:
            c = int(f / 9)
        else:
            continue

        if f % 7  == 2:
            b = int(f / 7)
        else:
            continue

        res.append([f"M: {f}", f"B: {b}", f"C: {c}"])

    return res


assert howmuch(1, 100) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
assert howmuch(1000, 1100) == [["M: 1045", "B: 149", "C: 116"]]
assert howmuch(10000, 9950) == [["M: 9991", "B: 1427", "C: 1110"]]
assert howmuch(0, 200) == [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]
assert howmuch(2950, 2950) == []
assert howmuch(20000, 20100) == [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]]

print("All tests passed!")
