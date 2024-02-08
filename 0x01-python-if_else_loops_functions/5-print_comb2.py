#!/bin/usr/python3

for i in range(0, 100):
    if (i < 10):
        print("0", end="")
    if (i == 99):
        print(i)
    else:
        print(i, end=", ")
