#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary[key]
        print(key + ":", value)
