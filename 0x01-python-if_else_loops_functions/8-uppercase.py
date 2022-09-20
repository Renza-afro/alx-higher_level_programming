#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(c) >= 97 and ord(c) <= 123:
            x = chr(ord(x) - 32)
            print('{}'.format(x), end='')
            print('')
