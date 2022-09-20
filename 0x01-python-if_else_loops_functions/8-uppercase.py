#!/usr/bin/python3
def uppercase(str):
    for x in str:
        print('{:s}'.format(chr(ord(x) - 32) if ord(x) > 96 and ord(x) < 123
                            else x), end='')
        print('')
