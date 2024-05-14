#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element_index in range(len(row)):
            print("{:d}".format(row[element_index]), end="")
            if element_index != len(row) - 1:
                print(" ", end="")
        print()
