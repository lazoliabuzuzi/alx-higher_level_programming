#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    try:
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                counter += 1
    except (ValueError, TypeError):
        pass
    finally:
        print()

    return counter
