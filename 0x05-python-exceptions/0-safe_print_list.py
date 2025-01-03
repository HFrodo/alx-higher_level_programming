#!/usr/bin/python3
'''
Function that prints x elements of a list
'''


def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            printed += 1
        print()
    except (IndexError):
        print()

    return printed
