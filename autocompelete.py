#!/usr/bin/env python3

import re


def autocomplete(input_, dictionary):
    pattern = re.compile(r"[a-zA-Z]+(?:(?:\-|\s)[a-zA-Z]+)?|$")
    input_ = re.findall(pattern, input_)[0].lower()
    res = []

    for i in dictionary:
        i = re.findall(pattern, i)[0]

        if i.lower().startswith(input_): 
            res.append(i)

            if len(res) == 5: 
                break

    return res


if __name__ == "__main__":
    import timeit

    dictionary = [
        "abnormal",
        "arm-wrestling",
        "absolute",
        "airplane",
        "airport",
        "amazing",
        "apple",
        "ball",
    ]

    assert autocomplete("ai", dictionary) == ["airplane", "airport"]
    assert autocomplete("a", dictionary) == [
        "abnormal",
        "arm-wrestling",
        "absolute",
        "airplane",
        "airport",
    ]

    print("All tests passed!")

    test_dict = [f"cat_{i}" for i in range(1, 1000)]
    t = timeit.Timer("autocomplete('cat_', test_dict)", globals=globals())

    print("10:", t.timeit(number=10))
    print("100:", t.timeit(number=100))
    print("1000:", t.timeit(number=1000))
