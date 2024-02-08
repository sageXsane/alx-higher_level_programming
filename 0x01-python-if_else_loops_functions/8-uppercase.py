#!/usr/bin/python3
def uppercase(string):
    for i in string:
        code = int(i)
        if ((ord(code) >= 97) and (ord(code) < 123)):
            code = ord(code) + 32
        print(chr(code), end="")
