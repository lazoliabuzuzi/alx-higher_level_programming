#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(first_num + 1, 10):
        print("{:d}{:d}".format(first_num, second_num), end=", ")
    print()
