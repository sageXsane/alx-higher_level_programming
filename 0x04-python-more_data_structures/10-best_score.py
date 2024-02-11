#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is not None):
        if not a_dictionary:
            return None
        score = 0
        best = ""
        for key, value in a_dictionary.items():
            if value > score:
                score = value
                best = key
        return best
    else:
        return None
