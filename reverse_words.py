#!/usr/bin/env python3

def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])


assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
assert reverse_words('apple') == 'elppa'
assert reverse_words('a b c d') == 'a b c d'
assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'
