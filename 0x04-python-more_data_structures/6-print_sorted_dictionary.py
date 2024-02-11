#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_list = sorted(a_dictionary)
    for i in range(0, len(a_dictionary)):
        print("{}: {}".format(sort_list[i], a_dictionary[sort_list[i]]))
