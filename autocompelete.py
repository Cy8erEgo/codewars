#!/usr/bin/env python3

import re


def autocomplete(input_, dictionary):
    input_ = "".join(re.findall(r"[a-zA-Z\-]", input_))
    res = []

    for i in dictionary:
        if i.startswith(input_.lower()): 
            res.append(i)

        if len(res) == 5: 
            break

    return res


if __name__ == "__main__":
    import timeit

    dictionary = ['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport', 'amazing', 'apple', 'ball' ]

    assert autocomplete("ai", dictionary) == ['airplane','airport']
    assert autocomplete("a", dictionary) == ['abnormal','arm-wrestling','absolute','airplane','airport']
    # assert autocomplete("_a$", dictionary) == ['airplane', 'apple', 'air', 'avenue', 'airport'] 

    print("All tests passed!")

    test_dict = [f"cat_{i}" for i in range(1, 1000)]
    t = timeit.Timer("autocomplete('cat_', test_dict)", globals=globals())

    print("10:", t.timeit(number=10))
    print("100:", t.timeit(number=100))
    print("1000:", t.timeit(number=1000))
