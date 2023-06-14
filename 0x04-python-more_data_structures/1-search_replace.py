#!/usr/bin/python3
def search_replace(my_list, search, replace):
    changed_list = []
    for item in my_list:
        if item == search:
            changed_list.append(replace)
        else:
            changed_list.append(item)

    return (changed_list)
