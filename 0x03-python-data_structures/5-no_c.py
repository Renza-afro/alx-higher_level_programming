#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for x in range(len(my_string)):
        if my_string[x] != 'c' and my_string[x] != 'C':
            n_str += my_string[x]
            return n_str
