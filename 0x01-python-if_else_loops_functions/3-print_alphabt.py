#!/usr/bin/python3
x = 0
while x < 26:
    if x != 4 and x != 16:
        print('{:c}'.format(x + 97), end='')
    x = x + 1
