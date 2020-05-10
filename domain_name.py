#!/usr/bin/env python3

import re
import timeit


def domain_name(url):
    matches = re.findall(r"[a-zA-Z0-9\-]+(?=\.)", url)
    for match in matches:
        if match != "www": return match                                                                              


def domain_name_2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


assert domain_name("http://google.com") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("icann.org") == "icann"

print("All tests passed!")

print(1, timeit.Timer("domain_name('http://google.com')", globals=globals()).timeit(number=1000))
print(2, timeit.Timer("domain_name_2('http://google.com')", globals=globals()).timeit(number=1000))
