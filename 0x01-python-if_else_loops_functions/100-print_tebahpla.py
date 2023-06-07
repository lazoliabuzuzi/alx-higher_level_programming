#!/usr/bin/python3
for reverse_char in range(ord('z'), ord('A') - 1, -1):
    if reverse_char % 2 == 0:
        print(chr(reverse_char), end="")
    else:
        print(chr(reverse_char).upper(), end="")

