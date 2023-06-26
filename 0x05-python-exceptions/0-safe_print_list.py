#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    try:
        for a in range(x):
            print(my_list[a], end="")
            counter += 1
    except IndexError:
        pass
    finally:
        print()

        return (counter)
