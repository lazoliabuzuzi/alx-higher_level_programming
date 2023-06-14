#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiplied_list = []

    for num in my_list:
        multiplied_num = num * number
        multiplied_list.append(multiplied_num)

    return multiplied_list
