#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        le = 1
        for col in row:
            if le == len(row):
                print('{:d}'.format(col), end='')
            else:
                print('{:d}'.format(col), end=' ')
            le += 1
            print()
