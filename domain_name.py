#!/usr/bin/env python3

import re


def domain_name(url):
    matches = re.findall(r"[a-zA-Z0-9\-]+(?=\.)", url)
    for match in matches:
        if match != "www": return match


assert domain_name("http://google.com") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://google.co.jp") == "google"

print("All tests passed!")
