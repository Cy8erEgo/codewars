#!/usr/bin/env python3

def namelist(names):
    names = ", ".join([d["name"] for d in names])
    return names[::-1].replace(" ,", " & ", 1)[::-1]


if __name__ == "__main__":
    assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == "Bart, Lisa & Maggie"
    print("All tests passed!")
