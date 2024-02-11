#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()

    first = (tuple_a[0] if len(tuple_a) >= 1 else 0)
    first += (tuple_b[0] if len(tuple_b) >= 1 else 0)
    second = (tuple_a[1] if len(tuple_a) >= 2 else 0)
    second += (tuple_b[1] if len(tuple_b) >= 2 else 0)
    tuple_c = first, second
    return tuple_c
