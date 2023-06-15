#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in delete_keys:
        del a_dictionary[key]
    return a_dictionary
