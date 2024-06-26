#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_number = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            printed_number += 1
        except (TypeError, ValueError):
            continue
    print()
    return printed_number
