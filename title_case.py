#!/usr/bin/env python3


def title_case(title, minor_words=""):
    title = title.capitalize()
    minor_words = minor_words.lower().split()
    words = [word if word in minor_words else word.capitalize() for word in title.split()]
    return " ".join(words)


assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
assert title_case('the quick brown fox') == 'The Quick Brown Fox'
assert title_case('First a of in', 'an often into') == 'First A Of In'

print("All tests passed")
