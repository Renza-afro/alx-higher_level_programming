#!/usr/bin/python3
for x in range(99):
    print('{:02d}'.format(x), ', ' if x < 99 else '\n', sep='', end='')
