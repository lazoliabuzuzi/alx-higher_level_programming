#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(first_num + 1, 10):
        if first_num == 8 and second_num == 9:
            print("{:d}{:d}".format(first_num, second_num), end="")
        else:
            print("{:d}{:d}".format(first_num, second_num), end=", ")
        if first_num < 9 and not (first_num == 8 and second_num == 9):
            print("", end="")
