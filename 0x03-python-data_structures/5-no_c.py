#!/usr/bin/python3
def no_c(my_string):
    cp_string = [x for x in my_string if x.lower() != 'c']
    return (''.join(cp_string))
