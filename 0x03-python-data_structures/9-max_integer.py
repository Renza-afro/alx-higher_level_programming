#!/usr/bin/python3
def max_integer(my_list=[]):
    def max_integer(my_list=[]):
        if len(my_list) == 0:
            return None
        big = my_list[0]
        for small in my_list:
            if small > big:
                big = small
                return big
