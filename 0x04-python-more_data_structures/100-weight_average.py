#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    s_fx = sum(map(lambda i: i[0] * i[1], my_list))
    s_f = sum(map(lambda j: j[1], my_list))
    return s_fx / s_f
