#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        length = 0
        for char in sentence:
            length += 1
        return (length, sentence[0])
