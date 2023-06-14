#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_dict = sorted(a_dictionary.items())

    for key, value in ordered_dict:
        print(key + ":", value)
