#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set()
    for num in my_list:
        if num not in unique_num:
            unique_num.add(num)

    total_sum = sum(unique_num)

    return total_sum
