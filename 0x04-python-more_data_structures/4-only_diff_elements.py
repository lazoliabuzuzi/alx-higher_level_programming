#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_nums = set()
    for num in set_1:
        if num not in set_2:
            diff_nums.add(num)

    for num in set_2:
        if num not in set_1:
            diff_nums.add(num)

    return diff_nums
