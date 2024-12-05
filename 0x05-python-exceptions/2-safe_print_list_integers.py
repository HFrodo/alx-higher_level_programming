#!/usr/bin/python3
'''
Function that prints the first x elements of a list and only integers.
'''


def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            pass
    print()
    return printed
