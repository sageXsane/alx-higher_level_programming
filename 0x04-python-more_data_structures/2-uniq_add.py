#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    uq_list = list(set(my_list))
    if len(uq_list) > 0:
        for i in range(0, len(uq_list)):
            res += uq_list[i]
    return res
