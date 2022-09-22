#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv)
    if x == 1:
        print('0 arguments.')
    elif x == 2:
        print('{:d} argument:'.format(x - 1))
    else:
        print('{:d} arguments:'.format(x - 1))
    for y in range(1, x):
        print('{:d}: {:s}'.format(y, sys.argv[y]))
