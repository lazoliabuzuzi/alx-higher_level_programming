#!/usr/bin/python3
def magic_string(n):
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool"] * (getattr(magic_string, 'count', 0) + 1))
