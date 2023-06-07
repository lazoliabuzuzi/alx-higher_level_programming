#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(first_num + 1, 10):
        if first_num == 8 and second_num == 9:
            print("{:02d}".format(first_num * 10 + second_num), end=" ")
        else:
            print("{:02d}".format(first_num * 10 + second_num), end=", ")
        if first_num < 8:
            print("", end="")
