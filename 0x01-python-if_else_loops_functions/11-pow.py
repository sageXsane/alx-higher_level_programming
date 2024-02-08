#!/usr/bin/python3

def pow(a, b):
    ans = 1
    if (b < 0):
        a = (1/a)
        b = abs(b)
    while (b != 0):
        ans *= a
        b -= 1
    return (ans)
